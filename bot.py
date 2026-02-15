import telebot
from bot_logic import gen_pass
import random

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
    
@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
def on_user_joins(message):
    name = message.new_chat_participant.first_name
    if hasattr(message.new_chat_participant, 'last_name') and message.new_chat_participant.last_name is not None:
        name += u" {}".format(message.new_chat_participant.last_name)

    if hasattr(message.new_chat_participant, 'username') and message.new_chat_participant.username is not None:
        name += u" (@{})".format(message.new_chat_participant.username)

    bot.reply_to(message, 'добро пожаловать'+ name)
    
    
@bot.message_handler(func=lambda message: True)
def filter(message):
    if 'ла' in message.text: 
        bot.reply_to(message, 'лалала')    
    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)



bot.polling()