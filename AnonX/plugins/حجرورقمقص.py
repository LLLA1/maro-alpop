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

options = ["حجرة", "ورقة", "مقص"]

def get_winner(chat_id):
    player1_choice = game_state[chat_id]["player1"]["choice"]
    player2_choice = game_state[chat_id]["player2"]["choice"]
    player1_name = game_state[chat_id]["player1"]["name"]
    player2_name = game_state[chat_id]["player2"]["name"]
    
    if player1_choice == player2_choice:
        return "تعادل"
    elif (player1_choice == "حجرة" and player2_choice == "مقص") or (player1_choice == "ورقة" and player2_choice == "حجرة") or (player1_choice == "مقص" and player2_choice == "ورقة"):
        game_state[chat_id]["player1"]["score"] += 1
        return f"{player1_name}"
    else:
        game_state[chat_id]["player2"]["score"] += 1
        return f"{player2_name}"

@app.on_message(filters.command(["حجره"], ""))
def start(client, message):
    if message.chat.id not in game_state:
        game_state[message.chat.id] = {
            "player1": {
                "name": message.from_user.first_name,
                "choice": None,
                "score": 0
            },
            "player2": {
                "name": None,
                "choice": None,
                "score": 0
            }
        }
        message.reply(
            f"{game_state[message.chat.id]['player1']['name']} بدأ لعبة حجرة ورقة مقص.\n\nانتظر اللاعب الثاني...",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("اضغط للعب", callback_data="join")],
                    [InlineKeyboardButton("𝑆𝑂𝐔𝑅𝐶𝐸 𝐴𝐿𝑃𝑂𝑃", url="https://t.me/source_alpop")]
                ]
            )
        )
    else:
        message.reply("هناك لعبة جارية بالفعل في هذه الدردشة. انتظر حتى تنتهي.")

@app.on_callback_query(filters.regex(r"^join$"))
def join(client, callback_query):
    print("Before editing message")  # Add this line
    callback_query.message.edit(
        f"{game_state[callback_query.message.chat.id]['player1']['name']} و {game_state[callback_query.message.chat.id]['player2']['name']} يلعبان حجرة ورقة مقص.\n\n👨‍💼 دور اللاعب: {game_state[callback_query.message.chat.id]['player1']['name']}",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("حجرة", callback_data="حجرة"),
                 InlineKeyboardButton("ورقة", callback_data="ورقة"),
                 InlineKeyboardButton("مقص", callback_data="مقص")],
                 [InlineKeyboardButton("●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 ⟧⟝◉━●", url="https://t.me/source_alpop")]
            ]
        )
    )
    print("After editing message")  # Add this line
