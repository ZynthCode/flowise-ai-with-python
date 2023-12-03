import uuid
import requests
import pyperclip
from rich import print
from rich.markdown import Markdown
from rich.console import Console


from session_manager import SessionManager

API_URL = "http://localhost:3000/api/v1/prediction/fd62cfc9-a1b7-479b-acb4-712ac6a01f3a"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

def main():
    session_manager = SessionManager("logs/conversation_history.json")
    chat_id = str(uuid.uuid4()) 
    history = []

    console = Console()
    print()
    console.print("Welcome! Ask me anything. Type 'exit' to quit.\n", style="bold")
    while True:
        console.print("\n\n\nYou\n",  style="bold purple on black")
        question = input("> ")
    
        if question.lower() == "exit" or question.lower() == "clear":
            print("Goodbye!")
            break
        
        console.print("\n\n\nAI\n",  style="bold red on black")
        answer = ""
        with console.status("[bold green]AI is thinking...") as status:
            output = query({"question": question, "history": history})
            answer = output["text"]
    
        formatted_answer = Markdown(answer)
        print(formatted_answer)

        pyperclip.copy(answer)
        print("\n[bold]Raw answer copied to clipboard.[/bold]")

        history.append({"id": str(uuid.uuid4()), "type": "userMessage", "message": question})
        history.append({"id": str(uuid.uuid4()), "type": "apiMessage", "message": answer})

        session_manager.create_chat(chat_id, history) 

if __name__ == "__main__":
    main()
