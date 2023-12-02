import sys
import requests
import pyperclip
from rich import print
from rich.markdown import Markdown
from rich.console import Console

API_URL = "http://localhost:3000/api/v1/prediction/dc866a6c-41bb-49b4-aa0f-e4c0adbecd53" # API pointing to our locally running flowise API

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

def main():
    if len(sys.argv) < 2:
        print("Please provide a question!")
        return

    question = ' '.join(sys.argv[1:])
    output = query({"question": question})

    text = output["text"]
    better_text = Markdown(text)
    print("\n")
    print(better_text)
    print()
    pyperclip.copy(text)
    print("[bold]Raw text copied to clipboard.[/bold]")

if __name__ == "__main__":
    main()
