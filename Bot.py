from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from test import *
from ydownload import *
#-------------------------------------------------------------------------------------------------
updater=Updater(token="1993581043:AAHbYI9JKqsefDJyJtZiHoHA2Av4HgLq9BI",use_context = True)

def hello (updater:Update,context:CallbackContext):
	updater.message.reply_text(f"Hello {updater.effective_user.first_name} \nNow send me the Youtube link. ")
def download_url (updater:Update,context: CallbackContext, url: str):
	audio = None
	try:
		audio = YTDOWNLOAD(url,url_only=False)
	except ValueError:
		updater.message.reply_text("Invaled Link")
	try:
		audio.make_audio_stream()
	except file_size_ex:
		updater.message.reply_text("Max size 50MB")
		return
	try:
	   audio.download()
	except erroe_download:
		updater.message.reply_text("Can not download this file")
		return
	context.bot.send_audio(chat_id=updater.message.chat_id,
                               audio=audio.audio_file,
                               title=audio.pafy_obj.title,
                               thumb=audio.TBM,
                               performer=audio.pafy_obj.author,
                               duration=sectime(audio.pafy_obj.duration),
                               timeout=60)

def get_url (updater: Update, context: CallbackContext):
	messege = updater.message.text
	url =get_link_text(messege)
	yt_urls_msg = updater.message.reply_text(pretty_url_string(url), disable_web_page_preview=True)
	download(updater, context, url)
	context.bot.delete_message(message_id=yt_urls_msg.message_id, chat_id=yt_urls_msg.chat_id)

def extract_url_download(update: Update, context: CallbackContext) -> None:
    """Extract youtube urls from the random text send to the bot and starts downloading and sending from url"""
    received_text = update.message.text
    yt_urls = get_link_text(received_text)
    yt_urls_msg = update.message.reply_text(pretty_url_string(yt_urls), disable_web_page_preview=True)
    if len(yt_urls) > 0:
        for url in yt_urls:
            if 'list=' in url:
               print("dshgshj")
				# download_playlist_url(update, context, url)
            else:
                download_url(update, context, url)
        context.bot.delete_message(message_id=yt_urls_msg.message_id, chat_id=yt_urls_msg.chat_id)
def main():
	updater.dispatcher.add_handler(CommandHandler('start', hello, run_async=True))
	updater.dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, extract_url_download, run_async=True))
	updater.start_polling()


