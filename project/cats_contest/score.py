from autocorrect import autocorrect
from utils import birkbeck_to_dict

TEST_FILE = "test.birkbeck"


def get_score(test_file: str, print_scores=False, limit=None) -> float:
    """
    Returns score of autocorrect against test_file
    """
    test_dict = birkbeck_to_dict(test_file)

    score = 0
    num_checked = 0
    for correct in test_dict.keys():
        typos = test_dict[correct]
        for_print = f"{correct}\n"
        for typo in typos:
            guess = autocorrect(typo)
            num_checked += 1
            if guess == correct:
                for_print += f"\t+1\tCORRECT\t\t({typo})\n"
                score += 1
            elif guess != typo:
                for_print += f"\t+0\tINCORRECT\t({typo} -> {guess})\n"
            else:
                for_print += f"\t+0.2\tUNCORRECTED\t({typo})\n"
                score += 0.2
        if print_scores:
            print(for_print)
        if limit is not None and num_checked >= limit:
            break
    return round(score / num_checked * 100, 2)


if __name__ == "__main__":
    print(get_score(TEST_FILE, print_scores=True))
