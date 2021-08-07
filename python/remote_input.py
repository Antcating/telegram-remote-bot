from pynput.keyboard import Key, Controller


def remote_input_handler(user_id, bot):
    bot.send_message(user_id, 'Send me remote input string')


def remote_input(message, user_id, bot, type):
    keyboard = Controller()
    if type == 'input':
        keyboard.type(message.text)
        bot.send_message(user_id, 'Remote input successfully sent')
    elif type == 'enter':
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        bot.send_message(user_id, 'Enter sent')