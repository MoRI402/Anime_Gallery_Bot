from Helper.helper import start_text, help_text
from config import bot
from telethon import events

class start():

    @bot.on(events.NewMessage(pattern=r"^/start$|^/start"))
    async def event_handler_start(event):
        await bot.send_message(
            event.chat_id,
            start_text,
            file='https://images.app.goo.gl/w9Bk5gpJwWB8dKw86'
        )

    @bot.on(events.NewMessage(pattern=r"^/help$|^/help"))
    async def event_handler_help(event):
        await bot.send_message(
            event.chat_id,
            help_text
            )

   
