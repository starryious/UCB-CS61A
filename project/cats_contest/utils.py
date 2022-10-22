from typing import Dict, Set
from collections import Counter
import re

REPLACEMENTS = {
    "’": "'",
    "“": " ",
    "”": " ",
    ".": " ",
}


def replace_all_occurrences(string, replacement_dictionary):
    for original, replacement in replacement_dictionary.items():
        string = string.replace(original, replacement)
    return string


def birkbeck_to_dict(filepath: str) -> Dict[str, Set[str]]:
    """
    Arguments:
        filepath: path to a list of typos in birkbeck format (see readme.md)
    Return Value:
        dictionary where KEY = correct spelling and VALUE = set of typos
    """
    d, current_word = {}, ''
    with open(filepath, 'r', encoding="utf8") as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                break
            elif '#' in line:
                continue
            elif '$' in line:
                correct = line[1:]
                d[correct] = set()
                current_word = correct
            else:
                d[current_word].add(line)
    return d


def dict_to_birkbeck(d: Dict[str, Set[str]]) -> str:
    """
    Arguments:
        dictionary where KEY = correct spelling and VALUE = list of typos
    Return Value:
        A string in Birkbeck format (see readme.md)
    """
    birkbeck_format = ''
    for word, typos in d.items():
        birkbeck_format += "$" + word + "\n" + "\n".join(typos) + "\n"
    return birkbeck_format


def get_common_unique_words_from_corpus(filename: str, n_words: int = None):
    with open(filename, "r", encoding="utf8") as f:
        filtered_words = replace_all_occurrences(f.read().lower(), REPLACEMENTS)
        words = Counter(re.findall(r"[a-z0-9']+", filtered_words), flags=re.ASCII)
        if n_words:
            return words.most_common(n_words)
        return words
