from subprocess import PIPE, Popen
from keyboards import main_menu
import telebot.util

def cmd_mode(message, user_id, bot):  # I have no idea what the sense of this function
        bot.register_next_step_handler(message, cmd_working_flow, user_id, bot)


def cmd_working_flow(message, user_id, bot):
    if message.text == '🔼 Back to Main':
        bot.send_message(user_id, 'Back to the main menu', reply_markup=main_menu)
        return
    elif message.text == '❗️Help':
        bot.send_message(user_id, 'Enter command and it will execute\n'
                                  'For example, dir or ls\n'
                                  'There is no save of current directory, so you should '
                                  'move between directories in the same command. for example:\n'
                                  'cd ../.. & dir')
        cmd_mode(message, user_id, bot)
    else:
        commandResult = Popen(message.text, shell=True, stdout=PIPE, stderr=PIPE, text=True)
        outputText = commandResult.stdout.read()
        errorText = commandResult.stderr.read()
        if outputText:  # Output checking
            for oneMessage in telebot.util.smart_split(outputText.encode('cp1251').decode('cp866')):
                bot.send_message(message.from_user.id, oneMessage)  # Encoding for Windows
        if errorText:  # Error checking
            bot.send_message(message.from_user.id,
                             'ERRORS:\n' + errorText.encode('cp1251').decode('cp866')[:4088])
        if not outputText and not errorText:  # if not error and output
            bot.send_message(message.from_user.id, 'No output')
        cmd_mode(message, user_id, bot)
