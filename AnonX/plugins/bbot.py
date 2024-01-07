import os
import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client

app = Client("my_bot")

# Replace the following line with your actual OWNER_ID
OWNER_ID = int(os.environ.get("OWNER_ID"))

@app.on_message(filters.command(['بوت'], prefixes=""))
async def Italymusic(client: Client, message: Message):
    me = await client.get_me()
    bot_username = me.username
    bot_name = me.first_name
    italy = message.from_user.mention
    button = InlineKeyboardButton("اضف البوت الي مجموعتك🏅", url=f"https://t.me/{bot_username}?startgroup=true")
    keyboard = InlineKeyboardMarkup([[button]])
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 956893993:
             rank = "**يالهوي ده مالك السورس بنفسو ياعيال في البار😱⚡️**"
        elif user_id == OWNER_ID:
             rank = "مـالك الـبوت العظمه 🫡⚡️"
        elif member.status == 'creator':
             rank = "**مـالك الـبـار 🫡⚡️**"
        elif member.status == 'administrator':
             rank = "**مـشـرف الـبـار🫡⚡️**"
        else:
             rank = "**لاسف انت عضو فقير🥺💔**"
    except Exception as e:
        print(e)
        rank = "مش عرفنلو مله ده😒"
    async with client.iter_profile_photos("me", limit=1) as photos:
        async for photo in photos:
            await message.reply_photo(photo.file_id, caption=f"""**نعم حبيبي :** {italy} 🥰❤\n**انا اسمي القميل :** {bot_name} 🥺🙈\n**رتبتك هي :** {rank}""", reply_markup=keyboard)

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

