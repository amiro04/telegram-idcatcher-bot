from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

import os

BOT_TOKEN = os.environ['BOT_TOKEN']
OWNER_CHAT_ID = int(os.environ['OWNER_CHAT_ID'])

async def catch_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    msg = f"یک نفر پیام داد:\n\nID: {user.id}\nUsername: @{user.username or 'ندارد'}\nName: {user.full_name}"
    await context.bot.send_message(chat_id=OWNER_CHAT_ID, text=msg)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, catch_id))
app.run_polling()
