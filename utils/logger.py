import datetime
import os

def log_event(message, level="INFO", to_file=False, file_path="logs/tastytrade.log"):
    timestamp = datetime.datetime.now().isoformat()
    emoji = {
        "INFO": "ℹ️", "ERROR": "❌", "SUCCESS": "✅",
        "DEBUG": "🔍", "WARNING": "⚠️"
    }.get(level, "📝")
    log_line = f"{emoji} [{timestamp}] {level}: {message}"
    print(log_line)
    if to_file:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "a") as f:
            f.write(log_line + "\n")
