import config
import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, BaseFilter


class FilterAwesome(BaseFilter):
    def filter(self, message: telegram.Message):
        return 'python is ok' in message.text

filter_awesome = FilterAwesome()

updater = Updater(token=config.TOKEN, use_context=True, request_kwargs=config.REQUEST_KWARGS)
# bot = telegram.Bot(token=config.TOKEN)
dispatcher = updater.dispatcher
jobqueue = updater.job_queue


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    print(context.user_data)

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

def filter_callback(update: telegram.Update, context: telegram.ext.CallbackContext):
    update.message.reply_text("Yeah, it's true!!!")

def start1_callback(update, context):
    update.message.reply_text("Welcome to my awesome bot!")


def callback_minute(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id=CHAT_ID,
                             text='KOKOKO')
def callback_30(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id=CHAT_ID,
                             text='A single message with 30s delay')

def callback_increasing(context: telegram.ext.CallbackContext):
    job = context.job
    context.bot.send_message(chat_id=CHAT_ID,
                             text='Sending messages with increasing delay up to 10s, then stops.')
    job.interval += 1.0
    if job.interval > 10.0:
        job.schedule_removal()

def callback_alarm(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id=context.job.context, text='BEEP')

def callback_timer(update: telegram.Update, context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Setting a timer for 1 minute!')

    context.job_queue.run_once(callback_alarm, 10, context=update.message.chat_id)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# ~Filters.command is equal to user input is not a command
# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

timer_hander = CommandHandler('timer', callback_timer)
dispatcher.add_handler(timer_hander)

dispatcher.add_handler(MessageHandler(filter_awesome, filter_callback))

dispatcher.add_handler(CommandHandler('start1', start1_callback))


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)




# job_minute = jobqueue.run_repeating(callback_minute, interval=120, first=0)
# jobqueue.run_once(callback_30,10)
# jobqueue.run_repeating(callback_increasing, 1)



updater.start_polling()

