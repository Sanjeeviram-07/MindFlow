import re


def clean_text(text):

    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"\n", " ", text)

    return text.strip()