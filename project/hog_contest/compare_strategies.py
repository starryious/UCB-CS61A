import json
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from auth import OAuthSession
from baseline_strategy import baseline_strategy
from final_strategy import final_strategy
from ucb import main

GOAL_SCORE = 300

ENDPOINT = "https://hog-calc.cs61a.org/api/compare_strategies"


def export(strategy):
    out = []
    for i in range(GOAL_SCORE):
        out.append([])
        for j in range(GOAL_SCORE):
            out[-1].append(strategy(i, j))
    return out


def compare(strategy_1, strategy_2, goal0, goal1):
    data = {
        "strat0": json.dumps(export(strategy_1)),
        "strat1": json.dumps(export(strategy_2)),
        "goal0": json.dumps(goal0),
        "goal1": json.dumps(goal1),
        "token": OAuthSession().auth(),
        "use_contest": json.dumps(True),
    }
    request = Request(ENDPOINT, bytes(urlencode(data), "utf-8"))
    try:
        body = json.loads(urlopen(request).read().decode())
        win_rate = body["win_rate"]
        print("Win rate: {}".format(win_rate))
        return win_rate
    except HTTPError as e:
        message = e.read().decode()
        print("Error: {}".format(message))
        raise Exception(message)


@main
def main(goal0=None, goal1=None):
    if not goal0:
        goal0 = int(
            input(
                f"Specify target score for final_strategy: (between 1 and {GOAL_SCORE}): "
            )
        )
    if not goal1:
        goal1 = int(
            input("Specify target score for baseline_strategy: (between 1 and 300): ")
        )
    compare(final_strategy, baseline_strategy, goal0, goal1)
