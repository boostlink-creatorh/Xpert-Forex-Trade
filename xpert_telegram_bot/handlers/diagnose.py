from telegram import Update
from telegram.ext import ContextTypes
from supabase import create_client
import os, platform, socket, uuid
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

def get_diagnostics():
    return {
        "hostname": socket.gethostname(),
        "platform": platform.system(),
        "release": platform.release(),
        "uuid": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat()
    }

async def diagnose(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    diagnostics = get_diagnostics()

    supabase.table("diagnostics").insert(diagnostics).execute()

    emoji_map = {
        "Windows": "🪟",
        "Linux": "🐧",
        "Darwin": "🍎"
    }

    reply = (
        f"🧪 Diagnostic Report\n"
        f"Hostname: `{diagnostics['hostname']}`\n"
        f"Platform: {emoji_map.get(diagnostics['platform'], '💻')} `{diagnostics['platform']}`\n"
        f"Release: `{diagnostics['release']}`\n"
        f"Logged at: `{diagnostics['timestamp']}`"
    )

    await context.bot.send_message(chat_id=chat_id, text=reply, parse_mode="Markdown")
