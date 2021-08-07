# -*- coding: utf-8 -*-
import os, configparser
import telebot as tb
import telebot.util

from processes import list_message, kill, process_killing
from info import pc_info, get_screenshot
from files import dir_location, list_dir
from power_control import turn_off_pc, lock_win


def update_config():
    config.read('config.ini')
    return config


config = configparser.ConfigParser()
config = update_config()
tb_token = config['TelegramBot']['token']
user_id = int(config['Admin']['id'])


bot = tb.TeleBot(tb_token)


main_menu = telebot.types.ReplyKeyboardMarkup()
main_menu.row('🛰 Files')
main_menu.row('💾 Process Control')
main_menu.row('💻 Power Control')
main_menu.row('❗ PC Info Menu')

power_menu = telebot.types.ReplyKeyboardMarkup()
power_menu.row('👀 Lock PC', '🔌 Turn Off PC')
power_menu.row('🔼 Back to Main')

process_menu = telebot.types.ReplyKeyboardMarkup()
process_menu.row('🖨 List Processes', '🪓 Kill process')
process_menu.row('🔼 Back to Main')

info_menu = telebot.types.ReplyKeyboardMarkup()
info_menu.row('🎛 PC Info', '🦪 Get ScreenShot')
info_menu.row('🔼 Back to Main')


@bot.message_handler(commands=['start', 'help'])
def welcome_message(message):
    if message.from_user.id == user_id:
        bot.send_message(user_id,
                         'Hello, this is process manager for your PC.',
                         reply_markup=main_menu)


@bot.message_handler(content_types=['text'])
def reply_handler(message):
    if message.from_user.id == user_id:
        if message.text == '💾 Process Control':
            bot.send_message(user_id, '💾 Process Control', reply_markup=process_menu)
        if message.text == '🖨 List Processes':
            list_message(message)
        elif message.text == '🪓 Kill process':
            kill(message)
            bot.register_next_step_handler(message,
                                           process_killing)

        if message.text == '💻 Power Control':
            bot.send_message(user_id, '💻 Power Control', reply_markup=power_menu)
        if message.text == '🔌 Turn Off PC':
            turn_off_pc(message,  user_id, bot)
        elif message.text == '👀 Lock PC':
            lock_win(message, user_id, bot)

        if message.text == '❗ PC Info Menu':
            bot.send_message(user_id, '❗ PC Info Menu', reply_markup=info_menu)
        if message.text == '🎛 PC Info':
            pc_info(message, user_id, bot)
        elif message.text == '🦪 Get ScreenShot':
            get_screenshot(message, user_id, bot)

        elif message.text == '🛰 Files':
            dir_location(message, user_id, bot)
            bot.register_next_step_handler(message,
                                           list_dir,
                                           path_upd=0,
                                           kbd_upd=0,
                                           user_id=user_id,
                                           bot=bot
                                           )

        if message.text == '🔼 Back to Main':
            bot.send_message(user_id, '🔼 Back to Main', reply_markup=main_menu)

        elif message.text == '🏑 CMD mode':
            bot.send_message(user_id, 'Entering CMD commands mode')
            cmd_mode(message)


@bot.callback_query_handler(func=lambda call: True)
def file_send(call):
    if call.data == "🔼":
        if call.message.text == '.':
            curr_dir = os.path.join(os.getcwd(), call.data).rsplit('\\', maxsplit=2)[0] + '\\'
        else:
            curr_dir = call.message.text
        curr_dir = curr_dir.rsplit('\\', maxsplit=2)
        if len(curr_dir) == 2 and ':' in curr_dir[0]:
            curr_dir = curr_dir[0].split(':')[0] + ':'
        else:
            curr_dir = curr_dir[0] + '\\'
        list_dir(call.message,
                 path_upd=curr_dir,
                 kbd_upd=0,
                 user_id=user_id,
                 bot=bot)
    elif call.data in ["⏪", "⏩"]:
        if call.message.text == '.':
            curr_dir = os.path.join(os.getcwd(), call.data) + '\\'
        else:
            curr_dir = call.message.text
        curr_dir_list = os.listdir(curr_dir)
        count_text = call.message.json['reply_markup']['inline_keyboard'][0][0]['text']
        try:
            count_id = [i for i, s in enumerate(curr_dir_list) if count_text in s][0]
            if call.data == "⏪":
                keyboard_page = count_id // 10 - 1
            elif call.data == "⏩":
                keyboard_page = count_id // 10 + 1
            list_dir(call.message,
                     path_upd=0,
                     kbd_upd=keyboard_page,
                     user_id=user_id,
                     bot=bot)
        except AttributeError:
            bot.answer_callback_query(call.id, 'Internal Error occurred')

    else:
        try:
            if call.message.text == '.':
                doc_to_send = open(call.data, 'rb')
            else:
                doc_to_send = open(call.message.text + call.data, 'rb')
            file = bot.send_document(call.from_user.id, doc_to_send)

        except PermissionError:
            if call.message.text == '.':
                curr_dir = os.path.join(os.getcwd(), call.data) + '\\'
            else:
                curr_dir = os.path.join(call.message.text, call.data) + '\\'
            list_dir(call.message, curr_dir,
                     kbd_upd=0,
                     user_id=user_id,
                     bot=bot)
        except FileNotFoundError:
            if call.message.text == '.':
                curr_dir = os.path.join(os.getcwd(), call.data) + '\\'
            else:
                curr_dir = call.message.text
            curr_dir_list = os.listdir(curr_dir)
            count_text = call.message.json['reply_markup']['inline_keyboard'][0][0]['text']
            count_id = [i for i, s in enumerate(curr_dir_list) if count_text in s][0]
            file_to_send = open(curr_dir+ curr_dir_list[count_id], 'rb')
            bot.send_document(user_id, file_to_send)
        except telebot.apihelper.ApiException as telebot_error:
            if telebot_error.result.status_code == 400:
                bot.send_message(user_id, 'File is empty')


bot.polling()
