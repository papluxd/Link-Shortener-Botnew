# ©AKBOTZ

import re
import aiohttp

from os import environ
from pyrogram import Client, filters
from pyrogram.types import *

API_ID = environ.get('API_ID','4682685')
API_HASH = environ.get('API_HASH','3eba5d471162181b8a3f7f5c0a23c307')
BOT_TOKEN = environ.get('BOT_TOKEN','5739114690:AAELqrowdFBQmTKDmguShUBNNepuQk4XQh8')
API_KEY = environ.get('API_KEY','8e4849c23d89ae57f671ae64d3680a0e817e0e7e')
API_URL = environ.get('API_URL','https://droplink.co/api')
API_URL1 = environ.get('API_URL1','https://gplinks.in/api')
API_KEY1 = environ.get('API_KEY1','60289db9d54284dc2c90aa61d259342d5790f7d0')
akbotz = Client('link shortener bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=100)

print("Developer: @AKBotZ , Join & Share Channel")
print("Bot is Started Now")

@akbotz.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "I'm Link Shortener bot. Just send me link and get short link, You can also send multiple links seperated by a space or enter.\n\n**Developer:** @movie_time_botonly")


@akbotz.on_message(filters.private & filters.text & filters.incoming)
async def link_handler(bot, message):
    link_pattern = re.compile('https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}', re.DOTALL)
    links = re.findall(link_pattern, message.text)
    if len(links) <1:
        await message.reply("No links Found in this text",quote=True)
        return
    for link in links:
        try:
            short_link = await get_shortlink(link)
            await message.reply(f"𝐇𝐞𝐫𝐞 𝐢𝐬 𝐘𝐨𝐮𝐫 𝐒𝐡𝐨𝐫𝐭𝐞𝐧𝐞𝐝 𝐋𝐢𝐧𝐤(DROPLINK)\n\n𝐎𝐫𝐢𝐠𝐢𝐧𝐚𝐥 𝐋𝐢𝐧𝐤: {link}\n\n𝐒𝐡𝐨𝐫𝐭𝐞𝐧𝐞𝐝 𝐋𝐢𝐧𝐤: `{short_link}`",quote=True,disable_web_page_preview=True)
        except Exception as e:
            await message.reply(f'𝐄𝐫𝐫𝐨𝐫: `{e}`', quote=True)


            
            
            
            
@akbotz.on_message(filters.private & filters.text & filters.incoming)

async def link_handler(bot, message):

    link_pattern = re.compile('https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}', re.DOTALL)

    links = re.findall(link_pattern, message.text)

    if len(links) <1:

        await message.reply("No links Found in this text",quote=True)

        return

    for link in links:

        try:

            short_link = await get_shortlink(link)

            await message.reply(f"𝐇𝐞𝐫𝐞 𝐢𝐬 𝐘𝐨𝐮𝐫 𝐒𝐡𝐨𝐫𝐭𝐞𝐧𝐞𝐝 𝐋𝐢𝐧𝐤(GPLINK)\n\n𝐎𝐫𝐢𝐠𝐢𝐧𝐚𝐥 𝐋𝐢𝐧𝐤: {link}\n\n𝐒𝐡𝐨𝐫𝐭𝐞𝐧𝐞𝐝 𝐋𝐢𝐧𝐤: `{short_link}`",quote=True,disable_web_page_preview=True)

        except Exception as e:

            await message.reply(f'𝐄𝐫𝐫𝐨𝐫: `{e}`', quote=True)
            
            
async def get_shortlink(link):
    url = API_URL
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]
async def get_shortlink(link):
    url = API_URL1
    params = {'api': API_KEY1, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


akbotz.run()
