from telebot import types
from Constants import VALUES

start_markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
start_markup_btn = types.KeyboardButton('/start')
start_markup.add(start_markup_btn)

inf_val_markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
inf_val_markup_bt = types.KeyboardButton('/values')
inf_val_markup.add(inf_val_markup_bt)

conv_marcup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
conv_marcup_bt = types.KeyboardButton('/convert')
conv_marcup.add(conv_marcup_bt)

val_marcup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
buttons = []
for val in VALUES.keys():
    buttons.append(types.KeyboardButton(val.capitalize()))
val_marcup.add(*buttons)

all_marcup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
all_marcup.add(start_markup_btn,inf_val_markup_bt,conv_marcup_bt)