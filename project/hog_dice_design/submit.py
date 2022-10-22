import json
import urllib
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen, Request

from ucb import main

URL = "https://dice.cs61a.org"
SUBMISSION_ENDPOINT = "/api/submit_designs"


def submit(dice, caption, token, out):
    data = {
        "dice": json.dumps(dice),
        "caption": caption,
        "token": token,
    }
    request = Request(urllib.parse.urljoin(URL, SUBMISSION_ENDPOINT), bytes(urlencode(data), "utf-8"))
    try:
        body = json.loads(urlopen(request).read().decode())
        out("You have submitted in the group: {}".format(body["group"]))
        out("Visit {} to see the gallery and check out other submissions.".format(URL))
        out("Thank you for participating!\n")
    except HTTPError as e:
        message = e.read().decode()
        out("Error: {}".format(message))
        raise Exception(message)


@main
def main():
    print("To submit, please run python3 ok --submit, so your strategy can be validated and backed up!")
