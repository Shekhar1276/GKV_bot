from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import asyncio
from webscraper import run
from typing import Union, List
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

Telegrambottoken = "" # Enter here telegram bot token
updater = Updater(Telegrambottoken,
                  use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello, Welcome to the GKV Bot.You can get many information related to GKV.This bot is created by Himanshu Shekhar ,CSE, 2020-24 Batch. Please write\
		/help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        "/GetResult  : Manually download your result. "
        "/PreviousYearPaper : Get or upload previous year papers."
    )

def manualresult(update: Update, context: CallbackContext):
    months = ['January', 'February']
    update.message.reply_text(
        "Hello there download your result here. Select the Month of exam",
        reply_markup=ReplyKeyboardMarkup(
            months, one_time_keyboard=True, input_field_placeholder="Chose a month"
        ),
    )
    
def Papers(update: Update, context: CallbackContext):
    update.message.reply_text(
        "You can get Previous year question paper. Type /PYQs and after space write the name of paper you want in the format /PYQs PAPERCODE-YEAR. For Example /PYQs BCE-C11-2020."
        "Or be a gentleman and upload previous year paper and help your juniors. Type /Uploadpaper to upload."
        )

def Prevpaperdownload(update: Update, context: CallbackContext):
    subject  = ' '.join(context.args)
    context.bot.send_document(chat_id=update.effective_chat.id, document=open("./Question/"+subject+".pdf", "rb"))

async def Uploadpaper(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Upload the question paper here. Firstly please rename the document in the given format. Format is Ses1/Ses2/Sem-PAPERCODE-YEAR. For example Ses1-BCE-C514-2022 or Sem-BCE-C514-2022 or Ses2-BCE-C514-2022."
        )
    fileName =  await update.message.document.file_name
    new_file =  await update.message.effective_attachment.get_file()
    await new_file.download_to_drive(fileName)
    
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" %
                              update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" %
                              update.message.text)


def runfeb(update: Update, context: CallbackContext):
    # run(Playwright ,"Feb", "206320061")
    # run()

    global monthnm
    monthnm = Monthselector("Feb")
    global regno
    regno = "206320061"
    asyncio.run(run())


def runjuly(update: Update, context: CallbackContext):
    # run(Playwright ,"July", "206320061")
    # run()

    global monthnm
    monthnm = Monthselector("July")
    global regno
    regno = "206320061"
    asyncio.run(run())
    


def runDecem(update: Update, context: CallbackContext):
    global monthnm
    monthnm = Monthselector("December")
    global regno
    regno = "206320061"
    asyncio.run(run(monthnm, regno))
    context.bot.send_document(chat_id=update.effective_chat.id, document=open("./Result/Report.pdf", "rb"))

def Monthselector(Month):
    if Month == "Feb":
        return "FEB-2022"
    if Month == "July":
        return "JULY-2022"
    if Month == "December":
        return "DEC-2022"



updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('GetResult', manualresult))
updater.dispatcher.add_handler(CommandHandler('PreviousYearPaper', Papers))
updater.dispatcher.add_handler(CommandHandler('UploadPaper', Uploadpaper))
updater.dispatcher.add_handler(CommandHandler('PYQs', Prevpaperdownload))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('February', runfeb))
updater.dispatcher.add_handler(CommandHandler('July', runjuly))
updater.dispatcher.add_handler(CommandHandler('December', runDecem))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
updater.idle()