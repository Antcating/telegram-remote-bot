import telebot.util

main_menu = telebot.types.ReplyKeyboardMarkup()
main_menu.row('๐ฐ Files')
main_menu.row('๐ฏ Remote Control')
main_menu.row('๐พ Process Control')
main_menu.row('๐ป Power Control')
main_menu.row('โ PC Info Menu')
main_menu.row('๐ CMD mode')
main_menu.row('โ Exit')

power_menu = telebot.types.ReplyKeyboardMarkup()
power_menu.row('๐ Lock PC')
power_menu.row('๐ Turn Off PC')
power_menu.row('๐ Reboot PC')
power_menu.row('โ Add to startup', 'โ๏ธRemove from startup')
power_menu.row('๐ผ Back to Main')

process_menu = telebot.types.ReplyKeyboardMarkup()
process_menu.row('๐จ List Processes', '๐ช Kill process')
process_menu.row('๐ผ Back to Main')

info_menu = telebot.types.ReplyKeyboardMarkup()
info_menu.row('๐ PC Info', '๐ฆช Get ScreenShot')
info_menu.row('๐ผ Back to Main')


remote_menu = telebot.types.ReplyKeyboardMarkup()
remote_menu.row('โจ๏ธ Remote Input')
remote_menu.row('๐ฎ Shortcut menu', 'โฉ๏ธ Enter key')
remote_menu.row('๐ผ Back to Main')

shortcut_menu = telebot.types.ReplyKeyboardMarkup()
shortcut_menu.row('โจ๏ธ CTRL + ...', 'โจ๏ธ Shift + ...')
shortcut_menu.row('โจ๏ธ Custom Shortcut')
shortcut_menu.row('๐ผ Back to Main')

exit_menu = telebot.types.ReplyKeyboardMarkup()
exit_menu.row('โ Yes')
exit_menu.row('๐ผ Back to Main')

cmd_menu = telebot.types.ReplyKeyboardMarkup()
cmd_menu.row('โ๏ธHelp')
cmd_menu.row('๐ผ Back to Main')