import random
from itertools import combinations
from pathlib import Path

import requests


def download_word_list():
    r = requests.get(
        "https://www.mit.edu/~ecprice/wordlist.10000"
    )  # legit source of words
    path = Path("wordlist.txt")
    path.write_text(r.text)
    return path


def main():
    word_list = download_word_list()
    words = word_list.read_text().splitlines()
    random.shuffle(words)
    combos = combinations(words, 5)
    first_1m = (next(combos) for _ in range(1_000_000))
    base_path = Path("C:\\Users\\calvin\\AppData\\Local\\")
    suffixes = [".txt", ".py", ".yaml", ".json"]
    paths = []
    for combo in first_1m:
        path = base_path.joinpath(*combo).with_suffix(random.choice(suffixes))
        paths.append(str(path))

    Path("file_list.txt").write_text("\n".join(paths))


if __name__ == "__main__":
    main()
