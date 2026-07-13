import telebot
import os

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "Здравствуйте! Я антикоррупционный помощник.\n\n"
        "Я могу помочь разобраться:\n"
        "• куда сообщать о коррупции\n"
        "• какие права есть у граждан\n"
        "• как действовать при вымогательстве"
    )

@bot.message_handler(func=lambda message: True)
def answer(message):
    text = message.text.lower()

    if "взят" in text:
        reply = (
            "Если у вас требуют взятку, не передавайте деньги. "
            "Зафиксируйте информацию и обратитесь в официальные органы."
        )
    elif "жалоб" in text or "сообщ" in text:
        reply = (
            "Для обращения подготовьте описание ситуации, даты, "
            "участников и возможные доказательства."
        )
    else:
        reply = (
            "Я пока обучен отвечать на базовые вопросы. "
            "Опишите ситуацию подробнее."
        )

    bot.reply_to(message, reply)

bot.infinity_polling()