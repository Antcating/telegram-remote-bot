import telebot as tb
import os

def cmd_mode(message):
    bot.register_next_step_handler(message,
                                   cmd_working_flow)


def cmd_working_flow(message):
    if message.text == 'exit_cmd':
        return
    else:
        bot.send_message(message.from_user.id,
                         os.system('cmd /c "'+ message.text +'"'))
        cmd_mode(message)
