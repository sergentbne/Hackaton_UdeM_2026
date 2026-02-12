import csv
import tqdm
from collections import Counter
import re

cipher = "aitrem orbeauc urs nu rbrea erchep enaitt ne ons ecb nu romagef"


def compare_word_letters(a: str, b: str):
    """
    Count letters in two words and compare counts.

    - Ignores non-letter characters.
    - Case-insensitive.
    - Returns a tuple: (are_equal, counts_a, counts_b)
      where are_equal is True when the letter counts match.
    """
    # keep only letters and lowercase them
    clean = lambda s: re.sub(r"[^A-Za-z]", "", s).lower()
    ca = Counter(clean(a))
    cb = Counter(clean(b))
    return ca == cb


with open(
    "/Users/louis/prog/Hackaton_UdeM_2026/crypto/French-Dictionary/dictionary/dictionary.csv"
) as c:
    reader = csv.reader(c)
    reader = list(reader)
    reader = [str(x) for inner in reader for x in inner]
    list_of_words = []
    for i in cipher.split(" "):
        a = reader.copy()
        a = [inner for inner in tqdm.tqdm(a) if len(inner) == len(i)]
        a = [inner for inner in a if compare_word_letters(i, inner)]
        print(a)
