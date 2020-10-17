import telebot
import csv
from telebot import types

bot = telebot.TeleBot('1170296404:AAF81f9JVVVPIarZslIIRMjk1nq6HYOBD-4')

def write_csv(data):
    with open('alice.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow((data['yesterday'],data['today'],data['problems']))

yesterday = {}
today = {}
problems = {}


@bot.message_handler(commands=['start'])
def start_massage(message):
    bot.send_message(message.chat.id, 'Что вы сделали?')
    yesterday[message.from_user.first_name] = message.text


@bot.message_handler(content_types=['text'])
def get_ques1(message):
    ques1 = ''
    name = message.text;  
    bot.send_message(message.from_user.id, 'Что вы будете делать?'); 
    yesterday[message.from_user.first_name] = message.text
    bot.register_next_step_handler(message, get_ques2)

@bot.message_handler(content_types=['text'])
def get_ques2(message):
    ques2 = ''
    surname = message.text; 
    bot.send_message(message.from_user.id,'Какие были сложности?')
    today[message.from_user.first_name] = message.text
    bot.register_next_step_handler(message, get_ques3)


@bot.message_handler(content_types=['text'])
def get_ques3(message):
    bot.send_message(message.from_user.id,'Спасибо, что написали отчет')
    problems[message.from_user.first_name] = message.text
    bot.register_next_step_handler(message, callback_worker)

    data = {
        'yesterday':yesterday,
        'today':today,
        'problems':problems
    }

    write_csv(data)

    keyboard = types.InlineKeyboardMarkup(); 
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); 
    keyboard.add(key_yes); 
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no'); 
    keyboard.add(key_no);   
    question = 'Отправить отчет?';  
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.from_user.id,'Ответ на первый вопрос:'+str(yesterday)+',')
        bot.send_message(call.from_user.id,'Ответ на второй вопрос:'+str(today)+',')
        bot.send_message(call.from_user.id,'Ответ на третий вопрос:'+str(problems)+'.')

        # with open("alice.csv","w+") as misc:
        #     f = misc.read()
        #     bot.send_document(call.message.chat.id,f)
    elif call.data == "no":
        bot.send_message(call.from_user.id,'Тогда, до свидания')


bot.polling(none_stop = True)