import requests
import csv
import sys

if sys.version_info < (3, 8):
    sys.exit("❌ Python 3.8 or higher is required")

words = ["law555"]
tags = ["unit1", "phrasal_verbs"]


def get_data(item):

    try:
        response = requests.get(
            f"https://api.dictionaryapi.dev/api/v2/entries/en/{item}"
        )

        response.raise_for_status()

        json = response.json()[0]

        response = ""
        for meaning in json.get("meanings", []):

            info = ""
            for definition in meaning.get("definitions", []):
                definition_value = definition.get("definition", "")
                example_value = definition.get("example", "")

                if not definition_value or not example_value:
                    continue

                info += f'<li><div class="definition">{definition_value}</div><div class="example">{example_value}</div></li>'

            if info:
                if not response:
                    response += '<div class="entry">'

                response += f'<div class="type">{meaning.get("partOfSpeech", "")}</div><div class="definitions"><ul>{info}</ul></div>'

        if response:
            response += "</div>"

        return response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.ConnectionError:
        print("Network connection error")
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")

    return


file = open(file="anki.csv", mode="w+", newline="")

with file:
    writer = csv.writer(file, delimiter=";", quotechar="'")

    # writer.writerow(["word", "info", "tags"])

    for word in words:
        info = get_data(word)
        if not info:
            continue

        word_field = f'<div class="entry-front"><div class="word">{word}</div></div>'

        writer.writerow([word_field, info, "::".join(tags)])
