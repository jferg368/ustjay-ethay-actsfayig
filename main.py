import os

import requests
from flask import Flask, send_file, Response, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():
    response = requests.get("http://unkno.com")
    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")
    return (facts[0].getText().strip())


def pig_latinize(fact):
    response = requests.post(
        "https://hidden-journey-62459.herokuapp.com/piglatinize/",
        {'input_text': fact}
    )
    return response.url


@app.route('/')
def home():
    url = pig_latinize(get_fact())
    return render_template('homepage.jinja2', url=url)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

