from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from func import *
from log import *

app = ApplicationBuilder().token("5834850128:AAGo7IXYNtpqH3HoYlF5KZHemQvA4oq9CEY").build()

app.add_handler(CommandHandler("hello", hello))

app.add_handler(CommandHandler("help", help))

app.add_handler(CommandHandler("sum", sum))

app.add_handler(CommandHandler("min", min))

app.add_handler(CommandHandler("mult", mult))

app.add_handler(CommandHandler("mult", delit))

app.run_polling()