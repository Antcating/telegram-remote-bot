import  ctypes, os
import telebot as tb
tb_token = '1693437075:AAFLgkYejKfDYTM6cy9ktiYpvGKpKCIjlYY'
bot = tb.TeleBot(tb_token)
user_id = 232741905

def turn_off_pc(message):
    bot.send_message(user_id, 'Turning off PC...')
    os.system("shutdown /s /t 1")


def lock_win(message):
    bot.send_message(user_id, 'Locking your PC...')
    ctypes.windll.user32.LockWorkStation()