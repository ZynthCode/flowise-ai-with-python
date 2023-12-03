import json
from typing import Dict, List
from datetime import datetime

class SessionManager:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def create_session(self, session_id: str, question: str, answer: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = self._read_file()
        if session_id not in data:
            data[session_id] = []
        data[session_id].append({"timestamp": timestamp, "question": question, "answer": answer})
        self._write_file(data)

    def get_session(self, session_id: str) -> List[Dict[str, str]]:
        data = self._read_file()
        return data.get(session_id, [])

    def update_session(self, session_id: str, question: str, answer: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = self._read_file()
        if session_id in data:
            data[session_id].append({"timestamp": timestamp, "question": question, "answer": answer})
            self._write_file(data)

    def delete_session(self, session_id: str):
        data = self._read_file()
        if session_id in data:
            del data[session_id]
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
