import telebot
TOKEN=""
bot = telebot.TeleBot(TOKEN)
times = {"пластик":"до 450 лет"}
@bot.message_handler(commands=['times'])
def decay_time(message):
    words = message.text.split()
    if len(words) >1:
        key = words[1]
        if key in times:
            bot.reply_to(message, times[key])
        else:
            bot.reply_to(message, 'обЪект не найден')

@bot.message_handler(commands=['quiz'])
def quiz(message):
    bot.send_poll(message.chat.id,'сколько мусора выбрасывают за час?',['1','2','3'],type='quiz',correct_option_id=1,explanation=("в мире выбрасывают очень много мусора "))
bot.polling()