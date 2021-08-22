import ctypes, os


def turn_off_pc(message,  user_id, bot):
    bot.send_message(user_id, 'Turning off PC...')
    os.system("shutdown /s /t 1")

def reboot_pc(message,  user_id, bot):
    bot.send_message(user_id, 'Reboot PC...')
    os.system("shutdown /r /t 1")

def lock_win(message,  user_id, bot):
    bot.send_message(user_id, 'Locking your PC...')
    ctypes.windll.user32.LockWorkStation()
