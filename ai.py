import sys
import uuid
import requests
import pyperclip
from rich import print
from rich.markdown import Markdown
from file_util import FileUtil

from session_manager import SessionManager

# API_URL = "http://localhost:3000/api/v1/prediction/dc866a6c-41bb-49b4-aa0f-e4c0adbecd53" # API pointing to our locally running flowise API
API_URL = "http://localhost:3000/api/v1/prediction/fd62cfc9-a1b7-479b-acb4-712ac6a01f3a"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

def main():
    session_manager = SessionManager("logs/conversation_history.json")
    chat_id = str(uuid.uuid4()) 
    history = []

    print("Welcome! Ask me anything. Type 'exit' to quit.")
    while True:
        question = input("Your question: ")
        if question.lower() == 'exit':
            print("Goodbye!")
            break

        output = query({"question": question, "history": history})
        answer = output["text"]

        formatted_answer = Markdown(answer)
        print("\n")
        print(formatted_answer)
        print()
        pyperclip.copy(answer)
        print("[bold]Raw answer copied to clipboard.[/bold]")

        history.append({"type": "userMessage", "message": question})
        history.append({"type": "apiMessage", "message": answer})

        session_manager.create_chat(chat_id, history) 


if __name__ == "__main__":
    main()
