import os
from keyboa import Keyboa


controls = ["⏪","🔼", "⏩"]
controls = Keyboa(items=controls, items_in_row=3).keyboard


def dir_location(message, user_id, bot):
    bot.send_message(user_id, 'Send me directory to see. \n'
                              'Type . to see current directory')


def list_dir(message, path_upd, kbd_upd,  user_id, bot):
    global send_smg_pages
    if path_upd == 0:
        curr_dir = message.text
    else:
        curr_dir = path_upd
    try:
        if len(os.listdir(curr_dir)) < 13:
            dir_list = os.listdir(curr_dir)
            dir_list.append("🔼")
            kb = Keyboa(items=dir_list, items_in_row=1).keyboard
            bot.send_message(user_id,
                             curr_dir,
                             reply_markup=kb)
        elif kbd_upd != 0:
            keyboard_page = kbd_upd
            kb_array = keyboard_control(curr_dir)
            if keyboard_page >= len(kb_array):
                keyboard_page -= len(kb_array)
            elif keyboard_page < 0:
                keyboard_page += len(kb_array)
            kb = kb_array[keyboard_page]
            try:
                bot.edit_message_reply_markup(user_id, send_smg_pages.id, reply_markup=kb)
            except NameError:
                pass  # Case when user use old file switcher (from previous session)
        else:
            keyboard_page = 0
            kb_array = keyboard_control(curr_dir)
            kb = kb_array[keyboard_page]
            send_smg_pages = bot.send_message(user_id,
                                              curr_dir,
                                              reply_markup=kb)
    except FileNotFoundError as e:
        bot.send_message(user_id, 'Wrong path!')
    except PermissionError:
        # elevate.elevate()
        # list_dir(message, path_upd=0, kbd_upd=0)
        bot.send_message(user_id, 'You dont have permission')


def keyboard_control(curr_dir):
    curr_dir_list = os.listdir(curr_dir)
    array_files = []
    kb_array = []
    n_pages = len(curr_dir_list) // 10 + 1
    for n in range(n_pages):
        if n + 1 < n_pages:
            array_files.append(list(curr_dir_list[10 * n:10 * (n + 1)]))
        else:
            array_files.append(list(curr_dir_list[10 * n:]))
    for array in array_files:
        for item_n in range(len(array)):
            if len(array[item_n]) > 15:
                array[item_n] = array[item_n][:15]
        if array != []:
            kb = Keyboa(items=array, items_in_row=1).keyboard
            kb = Keyboa.combine(keyboards=(kb, controls))
            kb_array.append(kb)
    return kb_array
