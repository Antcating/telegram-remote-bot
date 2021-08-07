import pyautogui


def remote_input_handler(user_id, bot):
    bot.send_message(user_id, 'Send me remote input string')


def remote_input(message, user_id, bot, type):
    if type == 'input':
        pyautogui.typewrite(message.text)
        bot.send_message(user_id, 'Remote input successfully sent')
    elif type == 'enter':
        pyautogui.typewrite(['enter'])
        bot.send_message(user_id, 'Enter sent')
    elif type == 'ctrl':
        pyautogui.hotkey('ctrl', message.text)
        bot.send_message(user_id, 'Shortcut sent sent')