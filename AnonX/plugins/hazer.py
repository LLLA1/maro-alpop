from pyrogram import Client, filters
from pyrogram.types import Message

app = Client("my_bot")


@app.on_message(filters.command(["بوت"]))
async def handle_bot_command(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if message.text == "e":
        member_count = await client.get_chat_member_count(chat_id)
        await message.reply(f"عدد أعضاء المجموعة: {member_count}")

    elif message.text in ["اطردني", "غادر"]:
        await client.kick_chat_member(chat_id, user_id)
        await message.reply_text("تم حظرك من المجموعة")

    elif message.text in ["حظر", "طرد", "حضر"]:
        if message.reply_to_message and message.reply_to_message.from_user:
            member_to_ban = message.reply_to_message.from_user.id
            await client.kick_chat_member(chat_id, member_to_ban)
            await message.reply_text(f"تم حظر العضو بنجاح")

    elif message.text in ["الغاء حظر", "الغاء الحظر"]:
        if message.reply_to_message and message.reply_to_message.from_user:
            member_to_unban = message.reply_to_message.from_user.id
            await client.unban_chat_member(chat_id, member_to_unban)
            await message.reply_text(f"تم الغاء حظر العضو بنجاح")

app.run()
