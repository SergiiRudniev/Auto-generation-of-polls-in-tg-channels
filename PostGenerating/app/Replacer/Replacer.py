import re

def Replace(text: str) -> str:
    escape_chars = r'_*\[\]()~`>#+\-=|{}.!'
    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text).replace("\\`\\`\\`", "```").replace("\\*\\*", "**")