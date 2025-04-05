from anki_csv_generator.view import App
import sys

if sys.version_info < (3, 8):
    sys.exit("❌ Python 3.8 or higher is required")

if __name__ == "__main__":
    app = App()
    app.run()
