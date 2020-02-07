import telepot
import time, random
from flask import Flask,request
import os
# print(TelegramBot.getMe())

pm = 0
roles = []
answers = {"greet":"Aqa ya ali ... Welcome to mafia..","maf":"How many Mafs ? ", "jok":"How many Joks ? ", "ready":"Ready to reveal ? (Type ok) ", "cit":"How many Cits ? ",}
token = '841835067:AAF3X7WHkBnjoRqbr7SlffK_hf6LFI3Wsow'
bot = telepot.Bot(token)
server = Flask(__name__)

def giveNdel(chat_id, role):
        response = role
      
        role = bot.sendMessage(chat_id, response)
        time.sleep(5)
        mes1 = bot.sendMessage(chat_id, "Will be removed in ..")
        time.sleep(1)
        mes2 = bot.sendMessage(chat_id, "3")
        time.sleep(1)
        mes3 = bot.sendMessage(chat_id, "2")
        time.sleep(1)
        mes4 = bot.sendMessage(chat_id, "1")
        time.sleep(1)
        bot.deleteMessage(telepot.message_identifier(role))
        bot.deleteMessage(telepot.message_identifier(mes1))
        bot.deleteMessage(telepot.message_identifier(mes2))
        bot.deleteMessage(telepot.message_identifier(mes3))
        bot.deleteMessage(telepot.message_identifier(mes4))
        time.sleep(3)
        mes2 = bot.sendMessage(chat_id, "Next one,Ready ?  (Type ok)")


def handle(msg):
    global pm, roles
    """
    Handler function for incoming messages
    """

    # Get sender details
    user_name = msg["from"]["first_name"]
    txt = msg['text']
    print(txt)

    # Get message details
    content_type, chat_type, chat_id = telepot.glance(msg)
    # print()
    # print()
    # print(f'{user_name}:')
    # print(txt)
    # print()
    # print()

    # Proceed if message type is text
    if content_type == "text":
        command = msg["text"].lower()
        if 'start' in command:
            bot.sendMessage(chat_id, answers["greet"])
            time.sleep(3)
            bot.sendMessage(chat_id, answers["maf"])
            pm = 1

        elif pm == 1 and 'start' not in command:
            maf_num = int(txt)
            roles += ( ["Mafia"] * maf_num )
            bot.sendMessage(chat_id, answers["jok"])
            pm += 1

        elif pm == 2 and 'start' not in command:
            jok_num = int(txt)
            roles += ( ["Joker"] * jok_num )
            bot.sendMessage(chat_id, answers["cit"])
            pm += 1

        elif pm == 3 and 'start' not in command:
            cit_num = int(txt)
            roles += ( ["Citizen"] * cit_num )
            bot.sendMessage(chat_id, answers["ready"])
            pm += 1

        elif pm == 4 and 'ok' in command:
            if len(roles) > 0:
                random.shuffle(roles)
                rl ="------   " + roles.pop() + "   ------"
                giveNdel(chat_id, rl)
            else:
                bot.sendMessage(chat_id, "Start Again :)  (Type start)")	

        else:
        	bot.sendMessage(chat_id, "Type Start .")




        # print("got command {}".format(command))

        # Check if the command is predefined and fetch response


@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://vast-cliffs-78404.herokuapp.com/' + token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


# if __name__ == "__main__":
#     """ Starting block """

#     # Read the API token from untracked file
#     # jokmafcit

#     # Instantiate the telegram bot
#     # bot = telepot.Bot(token)

#     # Add handler to handle incoming messages
#     bot.message_loop(handle)
#     # bot.message_loop(say)

#     while 1:
#         time.sleep(50)
# 	# print("--------------")
# 	print(messages)	
