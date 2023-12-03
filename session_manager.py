import json
from typing import Dict, List
from datetime import datetime

class SessionManager:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def create_chat(self, chat_id: str, history: list):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = self._read_file()
        if chat_id not in data:
            data[chat_id] = []
        
        # Add only new conversations
        for msg in history:
            if msg not in data[chat_id]: 
                msg_with_timestamp = {"timestamp": timestamp, **msg}
                data[chat_id].append(msg_with_timestamp)
        
        self._write_file(data)

    def get_chat(self, chat_id: str) -> List[Dict[str, str]]:
        data = self._read_file()
        return data.get(chat_id, [])

    def update_chat(self, chat_id: str, question: str, answer: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = self._read_file()
        if chat_id in data:
            data[chat_id].append({"timestamp": timestamp, "type": "userMessage", "message": question})
            data[chat_id].append({"timestamp": timestamp, "type": "apiMessage", "message": answer})
            self._write_file(data)

    def delete_chat(self, chat_id: str):
        data = self._read_file()
        if chat_id in data:
            del data[chat_id]
            self._write_file(data)

    def _read_file(self) -> Dict[str, List[Dict[str, str]]]:
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _write_file(self, data: Dict[str, List[Dict[str, str]]]):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=2) 
