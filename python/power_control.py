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


def add_to_startup(message,  user_id, bot, pathToScript, scriptName):
    bot.send_message(user_id, 'Adding to startup folder...')
    pathToBat="\"C:\\Users\\" + os.getlogin() + \
              "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\telegram-remote-bot.bat\""
    os.system("echo " + pathToScript[:2] + " > " + pathToBat)  # D:
    os.system("echo cd " + pathToScript + " >> " + pathToBat)  # cd "D:\telegram-remote-bot-main\python"
    os.system("echo python " + scriptName + " >> " + pathToBat)  # python "main.py"


def del_from_startup(message,  user_id, bot):
    bot.send_message(user_id, 'Deleting from startup folder...')
    os.system("del \"C:\\Users\\" + os.getlogin() +
              "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\telegram-remote-bot.bat\"")