"""
XIT License 2021
Copyright (c) 2021 WKRPrabashwara & Damantha126 
"""
import os
import time
import shutil
import psutil
import pyrogram
import subprocess
from pyrogram import filters
from sys import version as pyver

from bot.helpers.database.access_db import db
from bot.helpers.humanbytes import humanbytes

# Stats Module


async def bot_sys_stats():
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    stats = f"""
💡Sithija's assistant bot

• 💽 Tᴏᴛᴇʟ Dɪsᴋ Sᴘᴀᴄᴇ: {total}
• 💿 Uꜱᴇᴅ Sᴘᴀᴄᴇ: {used}({disk_usage}%)
• 📊 Fʀᴇᴇ Sᴘᴀᴄᴇ: {free}
• 🔋 Cᴘᴜ Usᴀɢᴇ: {cpu_usage}%
• 💾 Rᴀᴍ Usɢᴇ: {ram_usage}%
• ⚡️ Tᴏᴛᴀʟ Usᴇʀs 👀: {total_users}

@Team_Semmy_Bot
"""

    return stats
