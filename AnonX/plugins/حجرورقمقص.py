from pyrogram import Client, filters
from random import choice
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from AnonX import app


game_state = {}

@app.on_callback_query(filters.regex(r"^(حجرة|ورقة|مقص)$"))
def choose(client, callback_query):
    chat_id = callback_query.message.chat.id
    if chat_id in game_state:
        user_choice = callback_query.data
        user_name = callback_query.from_user.first_name

        if user_name == game_state[chat_id]["player1"]["name"]:
            game_state[chat_id]["player1"]["choice"] = user_choice
            callback_query.message.edit(
                f"👨‍💼 اللاعب الأول: {game_state[chat_id]['player1']['name']} لقد لعب \n\n👨‍💼 اللاعب الثاني: {game_state[chat_id]['player2']['name']} اختر الآن...",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("حجرة", callback_data="حجرة"),
                         InlineKeyboardButton("ورقة", callback_data="ورقة"),
                         InlineKeyboardButton("مقص", callback_data="مقص")],
                         [InlineKeyboardButton("●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●", url="https://t.me/UIU_II")]
                    ]
                )
            )
        elif user_name == game_state[chat_id]["player2"]["name"]:
            game_state[chat_id]["player2"]["choice"] = user_choice

            if game_state[chat_id]["player1"]["choice"] is not None:
                winner = get_winner(chat_id)
                name_player1 = game_state[chat_id]['player1']['name']
                name_player2 = game_state[chat_id]['player2']['name']
                choice_player1 = game_state[chat_id]['player1']['choice']
                choice_player2 = game_state[chat_id]['player2']['choice']
                player1_score = game_state[chat_id]['player1']['score']
                player2_score = game_state[chat_id]['player2']['score']
                callback_query.message.edit(
                    f"⌯━─━─━─━──━─━─━─━─━─━─━──━⌯\n\n⚠️ الإسم : {name_player1}\n\n❓ الإختيار : {choice_player1}\n\n🛒 النقاط : {player1_score}\n\n⌯━─━─━─━──━─━─━─━─━─━─━──━⌯\n\n⚠️ الإسم : {name_player2}\n\n❓ الإختيار : {choice_player2}\n\n🛒 النقاط : {player2_score}\n\n⌯━─━─━─━──━─━─━─━─━─━─━──━⌯\n\n🕺 اللاعب الفائز هو ⤵️ \n\n{winner}\n\n⌯━─━─━─━──━─━─━─━─━─━─━──━⌯"
                )
                del game_state[chat_id]
            else:
                callback_query.message.edit(
                    f"👨‍💼 اللاعب الأول: {game_state[chat_id]['player1']['name']} لقد لعب \n\n👨‍💼 اللاعب الثاني: {game_state[chat_id]['player2']['name']} اختر الآن...",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton("حجرة", callback_data="حجرة"),
                             InlineKeyboardButton("ورقة", callback_data="ورقة"),
                             InlineKeyboardButton("مقص", callback_data="مقص")],
                             [InlineKeyboardButton("●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚  ⟧⟝◉━●", url="https://t.me/source_alpop")]
                        ]
                    )
                )
        else:
            callback_query.answer("أنت لست جزء من هذه اللعبة.", show_alert=True)
    else:
        callback_query.answer("لا توجد لعبة جارية في هذه الدردشة.", show_alert=True)
