from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from log import *

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
    await update.message.reply_text(f'/hello\n/sum\n/min\n/mult\n/delit\n/help\n')


async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x}, + , {y} , = , {x+y}')


async def min(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg1 = update.message.text
    print(msg1)
    items = msg1.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x}, - , {y} , = , {x-y}')


async def mult(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg2 = update.message.text
    print(msg2)
    items = msg2.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x}, * , {y} , = , {x*y}')


async def delit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg3 = update.message.text
    print(msg3)
    items = msg3.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x}, / , {y} , = , {x/y}')


