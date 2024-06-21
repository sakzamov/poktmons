import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, 'Покемоны (pokemon – «карманный монстр») родились из фантазий Сатоси Тадзири о том, как можно было бы обмениваться и соревноваться своими виртуальными питомцами. По легенде, эта мысль пришла к разработчику, когда он увидел жука, ползущего по проводу между приставками Game Boy. Фантастический мир покемонов поражает своим многообразием. Однако Сатоси Тадзири оказался не просто мечтателем.Покемоны — это создания всевозможных форм и размеров, живущие в природе рядом с людьми. Большинство покемонов не умеют говорить и могут лишь произнести свое имя. В данный момент вселенную покемонов населяют более 700 существ. О покемонах заботятся их владельцы, их называют')


bot.infinity_polling(none_stop=True)

