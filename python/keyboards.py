import telebot.util

main_menu = telebot.types.ReplyKeyboardMarkup()
main_menu.row('🛰 Files')
main_menu.row('🌯 Remote Control')
main_menu.row('💾 Process Control')
main_menu.row('💻 Power Control')
main_menu.row('❗ PC Info Menu')
main_menu.row('🏑 CMD mode')
main_menu.row('❌ Exit')

power_menu = telebot.types.ReplyKeyboardMarkup()
power_menu.row('👀 Lock PC')
power_menu.row('🔌 Turn Off PC')
power_menu.row('🔃 Reboot PC')
power_menu.row('➕ Add to startup', '✖️Remove from startup')
power_menu.row('🔼 Back to Main')

process_menu = telebot.types.ReplyKeyboardMarkup()
process_menu.row('🖨 List Processes', '🪓 Kill process')
process_menu.row('🔼 Back to Main')

info_menu = telebot.types.ReplyKeyboardMarkup()
info_menu.row('🎛 PC Info', '🦪 Get ScreenShot')
info_menu.row('🔼 Back to Main')


remote_menu = telebot.types.ReplyKeyboardMarkup()
remote_menu.row('⌨️ Remote Input')
remote_menu.row('🏮 Shortcut menu', '↩️ Enter key')
remote_menu.row('🔼 Back to Main')

shortcut_menu = telebot.types.ReplyKeyboardMarkup()
shortcut_menu.row('⌨️ CTRL + ...', '⌨️ Shift + ...')
shortcut_menu.row('⌨️ Custom Shortcut')
shortcut_menu.row('🔼 Back to Main')

exit_menu = telebot.types.ReplyKeyboardMarkup()
exit_menu.row('✅ Yes')
exit_menu.row('🔼 Back to Main')

cmd_menu = telebot.types.ReplyKeyboardMarkup()
cmd_menu.row('❗️Help')
cmd_menu.row('🔼 Back to Main')