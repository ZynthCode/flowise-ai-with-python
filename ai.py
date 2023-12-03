import sys
import uuid
import requests
import pyperclip
from rich import print
from rich.markdown import Markdown
from file_util import FileUtil
from rich.console import Console
from rich.align import Align
from rich.layout import Layout
from rich.live import Live
from rich.text import Text


from session_manager import SessionManager

API_URL = "http://localhost:3000/api/v1/prediction/fd62cfc9-a1b7-479b-acb4-712ac6a01f3a"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

def main():
    session_manager = SessionManager("logs/conversation_history.json")
    chat_id = str(uuid.uuid4()) 
    history = []

    layout = Layout()
    layout.split_row(
        Layout(name="left", size=30),
        Layout(name="right"),
    )
    layout["left"].update(
        Align.left(
            Text(
                text="Overlord AI Terminal Chat",
                style="bold red on black"
            )
        )
    )
    layout["right"].update(
        Align.left(
            Text(
                text="Please ask me anything. Type 'exit' to quit.",
                
            )
        )
    )
    console = Console()
    console.print(layout)


    print("-----")
    console.print("[bold][underscore][red]AI:[/red][/underscore][/bold] \t\t\tWelcome! Ask me anything. Type 'exit' to quit.", style="bold purple on black")
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
