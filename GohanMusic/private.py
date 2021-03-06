from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from config import BOT_NAME, BOT_USERNAME, OWNER, SUPPORT_GROUP
from GohanMusic.msg import Messages as tr
from helpers.filters import command


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""
<b>ðð» Hallo {message.from_user.mention}
ðï¸ Nama Saya [{BOT_NAME}](https://t.me/{BOT_USERNAME})

ð¤ Saya Adalah Bot Canggih Yang Dibuat Untuk Memutar Musik Di Obrolan Suara Grup Telegram

âï¸ Klik Tombol Bantuan Untuk Mendapatkan Informasi Cara Menggunaka Bot</b>
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â á´á´á´Êá´Êá´á´É´ á´á´ É¢Êá´á´á´ â",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ð¬ sá´á´á´á´Êá´", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton("á´á´á´ á´Êá´á´á´Ê ð§ð»âð»", url=f"https://t.me/{OWNER}"),
                ],
                [
                    InlineKeyboardButton(text="âï¸ Êá´É´á´á´á´É´", callback_data="helps+1"),
                    InlineKeyboardButton("á´á´É´á´sÉª ð", callback_data="donate"),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""
<b>ðð» Hallo [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})
ðï¸ Nama Saya [{BOT_NAME}](https://t.me/{BOT_USERNAME})

ð¤ Saya Adalah Bot Canggih Yang Dibuat Untuk Memutar Musik Di Obrolan Suara Grup Telegram

âï¸ Klik Tombol Bantuan Untuk Mendapatkan Informasi Cara Menggunaka Bot</b>
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â á´á´á´Êá´Êá´á´É´ á´á´ É¢Êá´á´á´ â",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ð¬ sá´á´á´á´Êá´", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton("á´á´á´ á´Êá´á´á´Ê ð§ð»âð»", url=f"https://t.me/{OWNER}"),
                ],
                [
                    InlineKeyboardButton(text="âï¸ Êá´É´á´á´á´É´", callback_data="helps+1"),
                    InlineKeyboardButton("á´á´É´á´sÉª ð", callback_data="donate"),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("donate"))
async def donate(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""
<b>â¨ Selamat datang [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

â¢ Jika berminat berdonasi anda bisa kirim donasi ke pulsa atau ke saldo dana seikhlasnya

â¢ [zeinzo](tdrki_1) terimakasih donasimu begitu berarti bagi saya</b>
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="á´á´á´Êá´ÊÉª", callback_data="cbstart")],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""
<b>Perintah semua anggota grup
â¢ /play (judul lagu)Â - Untuk Memutar lagu yang Anda minta melalui YouTube
â¢ /song (judul lagu) - Untuk Mendownload lagu dari YouTube
â¢ /vsong (judul video) - Untuk Mendownload Video di YouTube
â¢ /search (judul lagu/video)Â - Untuk Mencari link di YouTube dengan detail

Perintah semua admin grup
â¢ /pause - Untuk Menjeda pemutaran Lagu
â¢ /resume - Untuk Melanjutkan pemutaran Lagu yang di pause
â¢ /skip - Untuk Menskip pemutaran lagu ke Lagu berikutnya
â¢ /end - Untuk Memberhentikan pemutaran Lagu
â¢ /reload - Untuk Segarkan daftar admin</b>
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¬ sá´á´á´á´Êá´", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton("á´á´á´ á´Êá´á´á´Ê ð§ð»âð»", url=f"https://t.me/{OWNER}"),
                ]
            ]
        ),
    )


help_callback_filter = filters.create(
    lambda _, __, query: query.data.startswith("helps+")
)


@Client.on_callback_query(help_callback_filter)
def helps_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split("+")[1])
    client.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=tr.HELPS_MSG[msg],
        reply_markup=InlineKeyboardMarkup(map(msg)),
    )


def map(pos):
    if pos == 1:
        button = [
            [
                InlineKeyboardButton(text="â¬ï¸", callback_data="cbstart"),
                InlineKeyboardButton(text="â¡ï¸", callback_data="helps+2"),
            ]
        ]
    elif pos == len(tr.HELPS_MSG) - 1:
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [
                InlineKeyboardButton(text="â¬ï¸", callback_data=f"helps+{pos-1}"),
                InlineKeyboardButton(text="â¡ï¸", callback_data="cbstart"),
            ]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text="â¬ï¸", callback_data=f"helps+{pos-1}"),
                InlineKeyboardButton(text="â¡ï¸", callback_data=f"helps+{pos+1}"),
            ],
        ]
    return button
