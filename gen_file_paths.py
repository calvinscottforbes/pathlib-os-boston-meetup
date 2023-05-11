import random
from itertools import combinations
from pathlib import Path
import requests

def download_word_list():
    # r = requests.get("https://github.com/dwyl/english-words/blob/master/words_alpha.txt")
    r = requests.get("https://github.com/dwyl/english-words/raw/master/words_alpha.txt")
    Path("words_alpha.txt").write_text()

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