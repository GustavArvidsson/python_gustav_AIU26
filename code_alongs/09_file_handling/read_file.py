from pathlib import Path

# --file__ -> absolute path to the current file
# .parent -> parent directory of the current file
# / "data" -> add this directory to the path

DATA_PATH = Path(__file__).parent / "data"

print(DATA_PATH)

with open(DATA_PATH / "quotes.txt", "r") as file:
    print(file.read())

# Kommentera cmd +k + cmd + c
# ta bort kommentar cmd + k + cmd + u