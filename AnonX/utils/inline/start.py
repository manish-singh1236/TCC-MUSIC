from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from AnonX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀🎼ADD ME TO YOUƦ GƦOUᴩ🎼🥀",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀🎼ʜᴇʟᴘ🎼🥀",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="🥀🎼ꜱᴇᴛᴛɪɴɢꜱ🎼🥀", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥀🎼ᴏᴡɴᴇʀ🎼🥀", user_id=OWNER),
            InlineKeyboardButton(
                text="🥀🎼ꜱᴜᴘᴘᴏʀᴛ🎼🥀", url=config.SUPPORT_GROUP
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀🎼ADD ME TO YOUƦ GƦOUᴩ🎼🥀",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀🎼ʜᴇʟᴘ🎼🥀", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(text="ᴀʙᴏᴜᴛ", callback_data="cb_about")
        ],
        [
            InlineKeyboardButton(
                text="🥀🎼ᴄʜᴀɴɴᴇʟ🎼🥀", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(text="🥀🎼ᴏᴡɴᴇʀ🎼🥀", user_id=OWNER)
        ],
     ]
    return buttons
