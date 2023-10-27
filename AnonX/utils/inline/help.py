from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"fallen_back",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["ADMINS"],
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text=_["AUTH"],
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text=_["BROADCAST"],
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["BL-CHAT"],
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text=_["BL-USER"],
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text=_["C PLAY"],
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["GBAN"],
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text=_["LOOP"],
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text=_["MAINTENANCE"],
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["PING"],
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text=_["PLAY"],
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text=_["SHUFFLE"],
                    callback_data="help_callback hb12",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["SEEK"],
                    callback_data="help_callback hb13",
                ),
                InlineKeyboardButton(
                    text=_["SONG"],
                    callback_data="help_callback hb14",
                ),
                InlineKeyboardButton(
                    text=_["SPEED"],
                    callback_data="help_callback hb15",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
