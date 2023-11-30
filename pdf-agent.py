import sys
import requests
import re
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import Terminal256Formatter

API_URL = "http://localhost:3000/api/v1/prediction/dc866a6c-41bb-49b4-aa0f-e4c0adbecd53"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

def extract_and_highlight_code(text):
    # Regular expression to detect code blocks in Markdown
    code_blocks = re.split(r'(```[^\n]*\n.*?\n```|`[^`\n]+`)', text, flags=re.DOTALL)

    for part in code_blocks:
        if part.startswith("`"):
            # Single backtick code block found, process and highlight inline
            code_block = part.strip('`')
            highlighted_code = highlight(code_block, get_lexer_by_name('python'), Terminal256Formatter(style='default'))
            print(highlighted_code, end="")
        else:
            # Double backtick code block or non-code text, print as it is
            print(part, end="")

def main():
    if len(sys.argv) < 2:
        print("Please provide a question!")
        return

    question = ' '.join(sys.argv[1:])
    output = query({"question": question})

    text = output["text"]

    # Call function to extract and highlight code blocks
    extract_and_highlight_code(text)

if __name__ == "__main__":
    main()
