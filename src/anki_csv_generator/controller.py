from anki_csv_generator.model import get_data
from anki_csv_generator.helper import write_to_csv


def generate_csv(words, tags, output_file):
    rows = []
    for word in words:
        info = get_data(word)
        if info:
            word_field = (
                f'<div class="entry-front"><div class="word">{word}</div></div>'
            )
            rows.append([word_field, info, "::".join(tags)])

    write_to_csv(output_file, rows)
