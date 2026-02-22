import telebot
from bot_logic import gen_pass
import random
import os
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь! или Я могу подбрасываю монетку. Напиши '/coin' или /flip")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['passwords'])
def send_password(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['flip', 'coin'])
def flip(message):
    result = random.choice(['Орел', 'Решка'])
    bot.reply_to(message, f"Монетка показывает: {result}")

@bot.message_handler(commands=['mem'])
def mems(message):
    fiels = os.listdir('images')
    fiel = random.choice(fiels)
    with open(f'images/{fiel}','rb') as f:
         bot.send_photo(message.chat.id,f)
    
@bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
def on_user_joins(message):
    for user in message.new_chat_members:
        name = user.first_name
        if hasattr(user, 'last_name') and user.last_name is not None:
            name += u" {}".format(user.last_name)

        if hasattr(user, 'username') and user.username is not None:
            name += u" (@{})".format(user.username)

        bot.reply_to(message, 'добро пожаловать '+ name)
        
    
@bot.message_handler(func=lambda message: True)
def filter(message):
    if 'ла' in message.text: 
        bot.reply_to(message, 'лалала')    
    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()