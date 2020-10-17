import telebot

bot = telebot.TeleBot('1308852014:AAECDOZplMMI26Yyfbt50kvxNCDEOf7tOeY')

@bot.message_handler(commands=['start'])
def start_massage(message):
    bot.send_message(message.chat.id, 'Salam Aleykum!')

@bot.message_handler(content_types = ['text'])
def send_text(message):
    if message.text == 'Salam!':
        bot.send_message(message.chat.id,'Salam my creator!')
    elif message.text == 'Bye':
        bot.send_message(message.chat.id,'Goodbye my creator!')
    elif message.text == 'euuu':
        bot.send_message(message.chat.id,'Ты будешь иметь дело с ним!')
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAMxXxrZxC4g6HmXDeOOfbWb_d3pnucAApYDAAJ8BQcbXjmd2pyEhmgaBA')
    else:
        bot.send_message(message.chat.id,'I do not understand you!')
        
@bot.message_handler(content_types = ['sticker'])
def sticker_id(message):
    print(message)




bot.polling()