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


def add_to_startup(message,  user_id, bot, path):
    bot.send_message(user_id, 'Adding to startup folder...')
    os.system("echo python \"" + path +
              "\" > \"C:\\Users\\" + os.getlogin() +
              "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\telegram-remote-bot.bat\"")


def del_from_startup(message,  user_id, bot):
    bot.send_message(user_id, 'Deleting from startup folder...')
    os.system("del \"C:\\Users\\" + os.getlogin() +
              "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\telegram-remote-bot.bat\"")