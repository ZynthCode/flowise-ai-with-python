class FileUtil:
    @staticmethod
    def read_file(file_path: str) -> str:
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return ""