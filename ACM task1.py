import re
from datetime import datetime

def transform_text(input_text: str) -> str:

    phone_pattern = r'\b\d{3}[- ]?\d{3}[- ]?\d{4}\b'
    text = re.sub(phone_pattern, "[REDACTED]", input_text)

    date_pattern = r'\b(\d{4})-(\d{2})-(\d{2})\b'
    def format_date(match):
        year, month, day = match.groups()
        date_obj = datetime(int(year), int(month), int(day))
        return date_obj.strftime("%d %B %Y")

    text = re.sub(date_pattern, format_date, text)
    text = text.replace("Python", "🐍")
    text = text.replace("AI", "🤖")
    text = text.replace("ACM", "⭐")
    text = text.replace("research", "🌌")
    return text
sample = "The workshop on AI through Python is being held on 2025-09-03.It will be conducted by research department of ACM"
print(transform_text(sample))