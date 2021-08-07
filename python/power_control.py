import  ctypes, os
import telebot as tb
tb_token = 'token here'
bot = tb.TeleBot(tb_token)
user_id = id here

def turn_off_pc(message):
    bot.send_message(user_id, 'Turning off PC...')
    os.system("shutdown /s /t 1")


def lock_win(message):
    bot.send_message(user_id, 'Locking your PC...')
    ctypes.windll.user32.LockWorkStation()