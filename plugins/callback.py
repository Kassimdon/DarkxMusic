from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from modules.config import BOT_USERNAME

HOME_TEXT = """
ʜᴇʟʟᴏ [{}](tg://user?id={})
ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ɴᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴀɴᴅ ɴᴏ ʟᴀɢ ɪssᴜᴇ ᴡɪᴛʜ ʙᴇsᴛ sᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs
ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ [sᴜᴍɪᴛ ʏᴀᴅᴀᴠ](https://t.me/Mr_DiSasTer_XD)...
━━━━━━━━━━━━━━━━━━━**"""

SUDO_CMD = """
🌾 **sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅs :**
๏ /gcast : ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
๏ /eval or /sh : ʀᴜɴs ᴛʜᴇ ɢɪᴠᴇɴ ᴄᴏᴅᴇ ᴏɴ ᴛʜᴇ ʙᴏᴛ's ᴛᴇʀᴍɪɴᴀʟ.
๏ /rmw : ᴄʟᴇᴀʀs ᴀʟʟ ᴛʜᴇ ᴄᴀᴄʜᴇ ᴩʜᴏᴛᴏs ᴏɴ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.
๏ /rmp : ᴄʟᴇᴀʀs ᴛʜᴇ ʀᴀᴡ ғɪʟᴇs ᴏғ ᴛʜᴇ ʙᴏᴛ.
๏ /rmd : ᴄʟᴇᴀʀs ᴛʜᴇ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ғɪʟᴇs ᴏɴ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.""",

"""

USERS_CMD = """

"""




@Client.on_callback_query(filters.regex("home"))
async def home(_, query: CallbackQuery):
    await query.edit_message_text(f"{HOME_TEXT}".format(query.message.chat.first_name, query.message.chat.id),
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("🛟 sᴜᴘᴘᴏʀᴛ", url="https://t.me/TheSupportBots"),
            InlineKeyboardButton("🌾 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/TechQuard")
        ],
        [
            InlineKeyboardButton("🧰 ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_cmd"),
            InlineKeyboardButton("🎃 ᴍᴏʀᴇ ɪɴғᴏ", callback_data="more_info")
        ]
   
     ]
  ),
)






@Client.on_callback_query(filters.regex("help_cmd"))
async def others(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʜᴇʏᴀ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ :""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌾 sᴜᴅᴏ ᴄᴍᴅ ", callback_data="sudo_users"),
                    InlineKeyboardButton(
                        "🍃 ᴜsᴇʀs ᴄᴍᴅ", callback_data="users_cmd"),
                ],
                [
                    InlineKeyboardButton(
                        "🎓 ᴍᴀɪɴᴛᴀɪɴᴇʀ", url="https://t.me/Mr_Disaster_Xd"),
                    InlineKeyboardButton(
                        "🍀 ᴍᴏʀᴇ ɪɴғᴏ", callback_data="moreinfo")
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home")
                ]
           ]
        ),
    )




@Client.on_callback_query(filters.regex("more_info"))
async def repoinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʜᴇʀᴇ ᴀʙᴏᴜᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : 
ᴀɴᴅ ʙᴏᴛ ʟɪsᴛs ᴀɴᴅ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ.
ᴛʜɪs ʀᴇᴘᴏ ɪs ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴅᴇᴘʟᴏʏɪɴɢ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ғᴀᴄɪɴɢ ʜᴇʀᴏᴋᴜ ᴀᴄᴄᴏᴜɴᴛ ʙᴀɴɴɪɴɢ ᴘʀᴏʙᴇʟᴍ.

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔗 ɢɪᴛʜᴜʙ", url=f"https://github.com/Sumit9969/DarkxMusic"),
                    InlineKeyboardButton(
                        "💌 ʏᴏᴜᴛᴜʙᴇ", url=f"https://youtube.com/channel/UCtI7hbY-BD7wvuIzoSU0cEw")
                ],
                [
                    InlineKeyboardButton(
                        "👾 ʙᴏᴛ ʟɪsᴛs", url="https://t.me/TechQuardBot"),
                    InlineKeyboardButton(
                        "🎓 ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Mr_DiSasTer_XD")
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home")
                ]
           ]
        ),
     )
    
@Client.on_callback_query(filters.regex("sudo_users"))
async def home(_, query: CallbackQuery):
    await query.edit_message_text(f"{SUDO_CMD}".format(query.message.chat.first_name, query.message.chat.id),
    reply_markup=InlineKeyboardMarkup(
            [              
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="help_cmd")
                ]
           ]
        ),
     )



 @Client.on_callback_query(filters.regex("users_cmd"))
async def home(_, query: CallbackQuery):
    await query.edit_message_text(f"{USERS_CMD}".format(query.message.chat.first_name, query.message.chat.id),
    reply_markup=InlineKeyboardMarkup(
            [              
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="help_cmd")
                ]
           ]
        ),
     ) 


       
