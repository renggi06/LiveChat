from bot.bot import Bot
from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message, 
   InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
)
from bot import (
START_TEXT, START_IMG, URL_BUTTON) 

@Bot.on_message(filters.command("start"))
async def gstart(client: Client, message: Message):
     buttons = [
        [
            InlineKeyboardButton(
                "𝗖𝗛𝗔𝗡𝗡𝗘𝗟",
                url = URL_BUTTON)
        ]
    
    ]
     await message.reply_photo(
                photo= START_IMG, 
                caption = START_TEXT.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id, 
                language = message.from_user.language_code, 
                dc = message.from_user.dc_id
            ),
        reply_markup = InlineKeyboardMarkup(buttons),
        quote = True
    )             
            


@Client.on_message(filters.command("help"))
async def help(client: Client, message: Message):
  await message.reply_text("""𝗝𝘂𝘀𝘁 𝗜𝗻𝗳𝗼 𝗨𝗻𝘁𝘂𝗸 𝗨𝘀𝗲𝗿:

• Silahkan pilih dan kirim konten yang ingin kalian Donate
• Tunggu sampai Admin Online, Chat kalian pasti akan dibalas

𝗨𝗻𝘁𝘂𝗸 𝗔𝗱𝗺𝗶𝗻:

•/ban <alasan> - memblokir anak dajjal
•/unban - membuka blokir anak haram

𝗡𝗼𝘁𝗲:<code> Jangan melakukan spam Chat jika tidak ingin diban</code>
"""	
    )
