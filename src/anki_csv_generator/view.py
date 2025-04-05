import tkinter as tk
from anki_csv_generator.controller import generate_csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Anki CSV generator")

        tk.Label(self.root, text="Word").pack()
        self.word_entry = tk.Entry(self.root)
        self.word_entry.pack()

        self.button = tk.Button(
            self.root, text="Generate CSV", command=self.generate_csv
        )
        self.button.pack()

    def generate_csv(self):
        word = self.word_entry.get().strip()
        print(word)
        generate_csv([word], ["unit1"], ROOT / "anki.csv")

    def run(self):
        self.root.mainloop()
