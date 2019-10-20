import telebot
import requests
import config
from bs4 import BeautifulSoup
import bs4
bot = telebot.TeleBot('761870984:AAHlqKr_6N3IwBafFufz_gq4e3U8cVW-khw')
print(bot.get_me())
def log(message, answer):
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \nТекст = {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id),message.text))
    print(answer)
user_markup=telebot.types.ReplyKeyboardMarkup(True, False)
user_markup.row('Привет', 'Пока')
@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.from_user.id, u'Привет, меня зовут Newsbot. Я умею искать в Интернете интересные новости.', reply_markup=user_markup)


def getnews():
    z=''
    s=requests.get('http://www.ug.ru/news/archive')
    b=bs4.BeautifulSoup(s.text, "html.parser")
    p=b.select('.news-archive-item')
    for x in p:
        s=(x.getText().strip())
        z=z+s+'\n\n'
    return s
def getanekdot():
    f=''
    m=requests.get('http://anekdotme.ru/random')
    c=bs4.BeautifulSoup(m.text, "html.parser")
    d=c.select('.anekdot_text')
    for v in d:
        m=(v.getText().strip())
        f=f+m+'\n\n'
    return m
@bot.message_handler(content_types=["text"])
def handle_text(message):
    msg=message.text
    msg=msg.lower()
    if (u'новости' in msg):
        try:
            bot.send_message(message.from_user.id, getnews())
        except:
            pass
    elif (u'привет' in msg ):
        bot.send_message(message.chat.id, 'Привет! Рад тебя видеть.')
    elif (u'пока' in msg):
        bot.send_message(message.chat.id, 'Прощай, возвращайся еще!')
    elif (u'анекдот' in msg):
        try:
            bot.send_message(message.from_user.id, getanekdot())
        except:
            pass



bot.polling(none_stop=True, timeout=123)


bot.polling(none_stop=True, interval=0)
