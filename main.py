import traceback
import telebot

from markups import conv_marcup, inf_val_markup, val_marcup, all_marcup, start_markup
from Constants import TOKEN, STR_VALUES,MANUAL
from extensions import APIException
from extensions import Convertor

global isRunning

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    bot.send_message(message.chat.id, MANUAL, reply_markup = inf_val_markup)


@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    bot.send_message(message.chat.id, STR_VALUES, reply_markup = conv_marcup)

@bot.message_handler(commands=["convert"])
def conv(message: telebot.types.Message):
    isRunning = False
    if not isRunning:
        text = "Выберите валюту, из которой конвертировать"
        msg = bot.send_message(message.chat.id, text, reply_markup = val_marcup)
        bot.register_next_step_handler(msg, base_handler)
        isRunning = True

def base_handler(message: telebot.types.Message):
    base = message.text.strip()
    text = "Выберите валюту, в которую конвертировать"
    bot.send_message(message.chat.id, text, reply_markup = val_marcup )
    bot.register_next_step_handler(message,sym_handler, base)
def sym_handler(message: telebot.types.Message, base):
    sym = message.text.strip()
    text = "Выберите количество конвентируемой валюты"
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message,amount_handler, base,sym)
def amount_handler(message: telebot.types.Message, base, sym ):
    amount = message.text.strip()
    text = "Результат конвертации:"
    try:
        answer = Convertor.get_price(base,sym,amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")

    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.send_message(message.chat.id, text,reply_markup = all_marcup)
        bot.send_message(message.chat.id, answer,reply_to_message_id = all_marcup)
    finally:
        isRunning = False



if __name__ == "__main__":
    bot.polling(none_stop=True)