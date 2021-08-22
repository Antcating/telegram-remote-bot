import telebot, psutil
import os


def list_message(message, user_id, bot):
    processes_list_send = list(set(os.popen('wmic process get description').read().split('\n\n')))
    processes_list_send.sort()
    text_message = '\n'.join(processes_list_send)
    if len(text_message) > 4000:
        splited_text_message = telebot.util.smart_split(text_message,
                                                        4000)
        for text_message in splited_text_message:
            bot.send_message(user_id,
                             text_message)
    else:
        bot.send_message(user_id,
                         text_message)


def kill(message, user_id, bot):
    bot.send_message(user_id,
                     'Send me a process name to kill')


def process_killing(message, user_id, bot):
    # Getting processes list
    processes_list = os.popen('wmic process get description, processid').read().split('\n\n')
    for process_n in range(len(processes_list)):
        processes_list[process_n] = processes_list[process_n].strip().rsplit(maxsplit=1)

    pid_name = message.text
    for process in processes_list:
        if process != []:
            if process[0] == pid_name:
                p_temp = psutil.Process(int(process[1]))
                p_temp.terminate()
    bot.send_message(user_id,
                     'Process %s successfully killed' %message.text)

