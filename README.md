# Telegram Remote Administration Tool

***

**DISCLAIMER** | Telegram Remote Administration Tool can **only** be used at **your** PC. Do not be evil!

***

<p align="center">
    <img src="preview.gif" width="320", height="614"> </br>
    *Remote Access preview*
</p>



## Features
Telegram Remote Administration Tool can:
- Browse files and send selected to chat.
- Turn Off and Lock Down PC.
- Get Info about PC.
- Take ScreenShoots.
- Process viewing and killing.
- more to come...

## Usage

If you configured everything correct - you will be able to go to bot and type `/start` or `/help` to get the buttons to control PC. 
Buttoms explanation: 
- Files - fully implemented file browser in Telegram for your PC. You can use it to get files remotely - just click on the file, you need. 
- Process control - contains submenu, that can be used to getting information about running processes and killing them.
- Power Control - contains submenu, that can be used to Lock and Turn Off PC.
- PC Info - contains submenu, that can be used to get information about PC and take ScreenShots.

## Installation and Init Configuration
### Installation
This project has to be hosted on **PC, that you want to have remote access to**. </br>
First of all, this project written using Python, so you will have to install Python package on your system. You can find packages for different operating systems on Python official page. On the next step you will have to download this repository. My recommendation is to use Git, but you can use what ever you want. Commands for git:
```
git clone https://github.com/Antcating/telegram-remote-bot.git
cd telegram-remote-bot/python
```
After downloading you have to install dependencies:
```
pip3 install -r requirements.txt
```
### Init Configuration
Configuration

Before the first run, you have to change configuration file config.ini:
```
[TelegramBot]
token = bot_token

[Admin]
id = admin_id 
```
All of the rows are necessary to make the bot working.
- Telegram Remote Administration Tool uses Telegram Bots, so you will have to go to [BotFather](https://t.me/BotFather) and create bot using its instructions. After creating bot, BotFather will return token to access the HTTP API. You will have to copy-paste it to the configuration file on the 'token' row.
- Due to basic security reasons, only approved administrator will be able to have access to PC. So, you have to get your Telegram id. You can to it, for example, using [this bot](https://t.me/userinfobot). Your id you paste to the config on the 'id' row.

## Thanks

- [PyTelegramBotApi](https://github.com/eternnoir/pyTelegramBotAPI)
- [Keyboa](https://github.com/torrua/keyboa)

Author: [@regular_patty](https://t.me/regular_patty)
