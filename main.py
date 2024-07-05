import telebot 
from config import token
from random import randint
from logic import Pokemon, Wizard, Fighter

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, 'Покемоны (pokemon – «карманный монстр») родились из фантазий Сатоси Тадзири о том, как можно было бы обмениваться и соревноваться своими виртуальными питомцами. По легенде, эта мысль пришла к разработчику, когда он увидел жука, ползущего по проводу между приставками Game Boy. Фантастический мир покемонов поражает своим многообразием. Однако Сатоси Тадзири оказался не просто мечтателем.Покемоны — это создания всевозможных форм и размеров, живущие в природе рядом с людьми. Большинство покемонов не умеют говорить и могут лишь произнести свое имя. В данный момент вселенную покемонов населяют более 700 существ. О покемонах заботятся их владельцы, их называют')

@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.from_user.username in Pokemon.pokemons.keys() and message.reply_to_message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")

@bot.message_handler(commands=['info_enemy'])
def info_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            res = enemy.info()
            bot.send_message(message.chat.id, res)

@bot.message_handler(commands=['feed'])
def eat(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.feed())

bot.infinity_polling(none_stop=True)

