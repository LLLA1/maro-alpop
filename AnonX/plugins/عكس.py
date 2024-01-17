import asyncio
import random
from pyrogram import filters, Client
from pyrogram.types import Message
from strings.filters import command
from AnonX import app
import config



txt = [
    "**- اسرع واحد يدز العكس** ~ ( بارده)",
    "**- اسرع واحد يدز العكس** ~ ( اجيت)",
    # ... (add more items as needed)
]

correct_answers = [
    "بارده",
    "اجيت",
    # ... (add the correct answers corresponding to each item in txt)
]

current_question_index = 0

@app.on_message(command(["عكس", "", ""]))
async def game_handler(client: Client, message: Message):
    global current_question_index

    if current_question_index >= len(txt):
        await message.reply("تم انتهاء الأسئلة.")
        return

    current_question = txt[current_question_index]
    correct_answer = correct_answers[current_question_index]

    if message.text.lower() == correct_answer:
        await message.reply("إجابة صحيحة!")
        current_question_index += 1

        if current_question_index < len(txt):
            await message.reply(f"السؤال الحالي: {txt[current_question_index]}")
        else:
            await message.reply("تم انتهاء الأسئلة. شكرًا للمشاركة.")
    else:
        await message.reply("إجابة خاطئة. حاول مرة أخرى.")

# Additional code for starting the game or triggering the first question can be added as needed
