
import telebot
from pars import parse
from pars_kg import parser
from telebot import types

bot = telebot.TeleBot('1168831413:AAG-__pUqDOI0fA5cmjK5zMOP8uBjz1nS3I')


def update():
    parse()
    parser()



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBGTpfHDBZceywfUTIkSREFCQvGvYfRAACzgEAAladvQqto5rs5p76TBoE')
    name = message.from_user
    botz = bot.get_me()

    bot.send_message(message.chat.id, 
        "Привет 👋  😷, {0.first_name}!\nЯ - <b>{1.first_name}</b> бот, который поможет тебе понять что такое CoVID-19 и как выжить в такое тяжелое время.".format(name, botz),
        parse_mode='html', reply_markup=keyboard())




@bot.message_handler(content_types=['text'])
def stat(message):


    #Статистика
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('В мире🌎')
    button2 = types.KeyboardButton('В Кыргызстане🇰🇬')
    button3 = types.KeyboardButton('<-Назад->')
    keyboard1.add(button1)
    keyboard1.add(button2)
    keyboard1.add(button3)
    if message.chat.type == 'private':
        if message.text == 'Статистика📊':
            update()
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBG8lfHtxSP784YnkWzOuzMbF_onuruAAC8QEAAladvQohKm5i6iYv7hoE', reply_markup=keyboard1)
        if message.text == 'В мире🌎':
            bot.send_message(message.chat.id, 'Статистика распространения коронавируса в Мире на сегодня:')
            with open('stat.txt', 'r') as fils:
                bot.send_message(message.chat.id, fils.read())
        if message.text == 'В Кыргызстане🇰🇬':
            bot.send_message(message.chat.id, 'Статистика распространения коронавируса в Кыргызстане на сегодня:')
            with open('stat_kg.txt', 'r') as fil:
                bot.send_message(message.chat.id, fil.read())


    #Меры предосторожности    a.K.a Кнопка
    if message.text == 'Меры предосторожности😷':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBG8VfHttP1p-ywi4lhenneJ9r4OBlCwAC8wEAAladvQqqJ4iMaCVBjxoE')
        bot.send_message(message.chat.id, meryy, parse_mode='html', reply_markup=keyboard())



    #Куда обращаться?
    keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button21 = types.KeyboardButton('Дневные стационары🏙')
    button22 = types.KeyboardButton('Ночные стационары🌃')
    button23 = types.KeyboardButton('Горячие линии☎️')
    button24 = types.KeyboardButton('<-Назад->')
    keyboard2.add(button21)
    keyboard2.add(button22)
    keyboard2.add(button23)
    keyboard2.add(button24)

    if message.chat.type == 'private':
        if message.text == 'Куда можно обратиться?🚨':
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBG8tfHt0cYTXtP6_6fOj0zZuIyQ6eTgAC4wEAAladvQoPvIMqCGp2lRoE', reply_markup=keyboard2)
        if message.text == 'Дневные стационары🏙':
            bot.send_message(message.chat.id, dnev_stac, parse_mode='html')
        if message.text == 'Ночные стационары🌃':
            bot.send_message(message.chat.id, nochnye)
        if message.text == 'Горячие линии☎️':
            bot.send_message(message.chat.id, linii, parse_mode='html')
        if message.text == '<-Назад->':
            bot.send_message(message.chat.id, 'Всё, что вы пожелаете♥️', reply_markup=keyboard())


        #О коронавирусе
        keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button31 = types.KeyboardButton('Что такое коронавирус?🦠')
        button32 = types.KeyboardButton('Какие симптомы?🤧')
        button33 = types.KeyboardButton('Профилактика коронавирусной инфекции🤒')
        button34 = types.KeyboardButton('<-Назад->')
        button35 = types.KeyboardButton('Как передается?')
        keyboard3.add(button31)
        keyboard3.add(button32, button35)
        keyboard3.add(button33)
        keyboard3.add(button34)

        if message.text == 'О коронавирусе✳':
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBHElfIA_pKcvGmKSeFaAFhGMbGcl-lgAC7QEAAladvQoRSyLWSliKTRoE', reply_markup=keyboard3)
        if message.text == 'Что такое коронавирус?🦠':
            bot.send_message(message.chat.id, virus, parse_mode='html')
        if message.text == 'Какие симптомы?🤧':
            bot.send_message(message.chat.id, simptomy)
        if message.text == 'Профилактика коронавирусной инфекции🤒':
            bot.send_message(message.chat.id, profilaktika)
        if message.text == 'Как передается?':
            bot.send_message(message.chat.id, peredacha, parse_mode='html')


        # ДОПЛНИТЕЛЬНО
        keyboard4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button41 = types.KeyboardButton('Опровержение мифов о коронавирусе🚫')
        button42 = types.KeyboardButton('Кто в группе риска?👨‍👨‍👧‍👦')
        button43 = types.KeyboardButton('История происхождения коронавируса📜')
        button44 = types.KeyboardButton('<-Назад->')
        keyboard4.add(button41)
        keyboard4.add(button42)
        keyboard4.add(button43)
        keyboard4.add(button44)

        if message.text == 'Дополнительно📌':
            bot.send_message(message.chat.id, 'выбирайте', reply_markup=keyboard4)

        if message.text == 'Опровержение мифов о коронавирусе🚫':
            bot.send_sticker(message.chat.id,   'CAACAgIAAxkBAAEBG8dfHtvN0hb1p4qXlG68mF-rC-xPtAAC5wEAAladvQoNeVnL-khcCxoE')
            bot.send_message(message.chat.id, mif, parse_mode='html')

        if message.text == 'Кто в группе риска?👨‍👨‍👧‍👦':
            bot.send_message(message.chat.id, gruppa_riska, parse_mode='html')

        if message.text == 'История происхождения коронавируса📜':
            bot.send_message(message.chat.id, history, parse_mode='html')



# ==================VARIABLES=======================


#меры предосторожности
meryy = '''<b><i>🟢Нет рукопожатиям или поцелуям в щеки\n
🟢Маска предназначена для защиты людей вокруг вас.\n
🟢Часто мойте руки.\n
🟢Держите руки подальше от лица.\n
🟢Кашляйте и чихайте правильно.\n
🟢Немедленно выбрасывайте использованные одноразовые носовые платки.\n
🟢Регулярно проветривайте помещения.\n
🟢Держите дистанцию   и избегайте столпотворений.\n</i></b>'''


#Дневные стационары
dnev_stac = '''<b>В Ленинском районе:     🏥</b>

ФОК «Газпром» по улице Токонбаева,
СШ №68, улица Токтогула, 220 (пересекает улицу Уметалиева),
кафе «Арал», улица Дэн Сяопина, 199, (район Кызыл Аскера),
СШ №96, улица Каркыра, 93А («Ак-Ордо»),
СШ №95 в микрорайоне «Джал».

<b>В Свердловском районе:       🏥</b>

ФОК им. Р.Санатбаева (Восток 5),
СШ №94 (ж/м «Дордой»),
УВК №38, улица Аламедин-1, 38/1.

<b>В Октябрьском районе:        🏥</b>

«Бишкекпекарня » в 12 мкр (возле церкви),
школа «Сейтек», улица Анкара, 15.

<b>В Первомайском районе:     🏥</b>

СШ №83, улица Патриса Лумумбы, 9 (рядом с рынком Кудайберген),
Дворец спорта им. К.Кожомкула,
СШ №81, ул. Пр.Зимы, 262 (ж/м «Ак Босого»).'''


nochnye = '''🏥На базе спорткомплекса «ДСК» в 7-м микрорайоне\n
🏥В ресторане «Консул» на пересечении улиц Фрунзе и Орозбекова\n
🏥В ресторане «Салтанат» на улице Бегматова, 67 в жилом массиве «Кара-Жыгач»'''



#Горячие линии
linii = '''<b>Горячая линия районных штабов г.Бишкек</b>\n

Ленинский район: 0312 656-920, 0551 184-328\n

Первомайский район: 0312 661-537, 0702 493-993, 0990 644-410\n

Свердловский район: 0312 360-707, 0703 906-116, 0705 641-833\n

Октябрьский район: 0312 576-550, 0555 401-681, 0709 812-324\n
'''



#Что такое корона...?
virus = '''<b>Семейство коронавирусов🦠 </b>- это один из возбудителей обычной ОРВИ. \nОни распространены повсеместно. Поражают как животных, так и людей. \nВ зоне умеренного климата пики вспышек коронавирусной инфекции приходятся на зиму, хотя могут наблюдаться весной и осенью. Вероятность заболеть летом существенно ниже.
'''

simptomy = '''◾ Лихорадка в 99 процентов случаев \n
◾️ Слабость, утомляемость в 70 процентов случаев \n
◾️ Сухой кашель в 59 процентов случаев \n
◾️ Потеря аппетита у 40 процентов случаев \n
◾️ Боль в мышцах в 35 процентах случаев \n
◾️ Одышка у 31 процента случаев\n
◾️ Кашель с мокротой в 27 процентов случаев\n '''


profilaktika = '''💦Соблюдение личной гигиены \n
🚪Самоизоляция \n
⚠️Карантин\n 
❗️На сегодняшний день методов специфического лечения и/или профилактики COVID-19 нет.'''


peredacha = '''<i><b>Самые распространенные пути передачи:</b></i> \n\n<b>🍽БЫТОВОЙ</b>--> общая посуда, полотенца, предметы быта\n<b>👥КОНТАКТНЫЙ</b>-->через рукопожатия, близкий контакт\n<b>🗣ВОЗДУШНО-КАПЕЛЬНЫЙ</b>-->  по воздуху от зараженного к здоровому.'''


mif = '''<b><i>☑️Новым коронавирусом могут заразиться (и заражаются) представители всех возрастных групп: и дети, и пожилые, и люди среднего возраста.\n
☑️Антибиотики на вирусы не действуют.\n
☑️Никаких лекарств, эффективных именно при Covid-19, пока не существует.\n
☑️Длительное ношение медицинских масок* в случае их правильного использования НЕ ПРИВОДИТ к интоксикации углекислым газом или кислородной недостаточности.\n
☑️Частое питье горячей воды, которое, как утверждается в рассылке, смоет вирус в желудок,  действительности неспособно предотвратить попадание вируса в дыхательные пути и последующее заражение.\n
☑️Но пить воду при респираторных инфекциях можно и даже нужно, но не для уничтожения вируса, а для предотвращения потерь жидкости.</i></b> 
            '''

gruppa_riska = '''<b><i>▫️Общая смертность держится на уровне 2,3%.\n
▫️Самая высокая — в группе людей старше 80 лет — 14,8%.\n
▫️В группе от 70 до 80 лет — 8%.\n
▫️Ни одного ребенка в возрасте 0–9 лет не умерло.\n
▫️В группе 10–40 лет смертность равна 0,2%.\n
▫️Мужчин умерло больше, чем женщин: 2,8% и 1,7% соответственно.</i></b>'''


history = '''<b>В конце декабря 2019 года китайские власти сообщили о вспышке пневмонии неизвестного происхождения в городе Ухань.</b> \n
Первые заболевшие имели отношение к рынку морепродуктов. 
Эксперты предварительно установили, что возбудителем заболевания стал новый тип коронавируса - 2019-nCoV.
По состоянию на 20 января 2020 года, в общей сложности было зарегистрировано 218 случаев заражения этим заболеванием. 
Четыре человека погибли. Вирус уже распространился за пределы Китая, случаи заражения зафиксированы в Южной Корее, Японии и Таиланде.'''



def keyboard():
    #Основная клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Статистика📊')
    button2 = types.KeyboardButton('Меры предосторожности😷')
    button3 = types.KeyboardButton('Куда можно обратиться?🚨')
    button4 = types.KeyboardButton('Дополнительно📌')
    button6 = types.KeyboardButton('О коронавирусе✳')

    markup.add(button1, button6)
    markup.add(button3, button2)
    markup.add(button4)
    return markup




bot.polling()

