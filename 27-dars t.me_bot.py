# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 22:57:41 2023

@author: asus
"""


from transliterate import to_cyrillic, to_latin

Matn = input("Matn kiriting:")
import telebot

TOKEN = "6048448915:AAFkx8_z6s1gX_vl43yHaNK3jtpqLkiSzaY"
bot = telebot.TeleBot("TOKEN", parse_mode=None)
Admin = '192444504'


@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalom aleykum, Xush kelibsiz "
    javob = "\nMatn kiriting:"
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    
    bot.reply_to(message, javob(msg))
    

bot.polling()




# print(to_cyrillic(matn))
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))
