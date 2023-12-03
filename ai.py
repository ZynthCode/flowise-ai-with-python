import sys
import uuid
import requests
import pyperclip
from rich import print
from rich.markdown import Markdown
from file_util import FileUtil

from session_manager import SessionManager

API_URL = "http://localhost:3000/api/v1/prediction/dc866a6c-41bb-49b4-aa0f-e4c0adbecd53" # API pointing to our locally running flowise API

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

def main():
    if len(sys.argv) < 2:
        print("Please provide a question!")
        return

    question = ' '.join(sys.argv[1:])
    # TODO: Simulate output without just the text
    # output = query({"question": question})
    # answer = output["text"]

    # testing part
    answer = FileUtil.read_file("test/ai_markdown_answer.md")

    better_answer = Markdown(answer)
    print("\n")
    print(better_answer)
    print()
    pyperclip.copy(answer)
    print("[bold]Raw answer copied to clipboard.[/bold]")

    session_manager = SessionManager("logs/conversation_history.json")
    # session_id = str(uuid.uuid4())
    session_id = "36f05135-e259-4a4d-8f7a-afc78bec3c16"
    session_manager.create_session(session_id, question, answer)


if __name__ == "__main__":
    main()
