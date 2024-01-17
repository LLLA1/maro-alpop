

import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint




@app.on_message(
    command(["مميزات","مميزات البوب","مميزات سورس البوب","مميزات السورس"])
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**مرحبآ بك عزيزي » {message.from_user.mention}**في قسم مميزات سورس البوب ميوزك\n
⩹━⊷⌯⌞ 𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊 ⌝⌯⊶━⩺

★قايمه مميزات سورس البوب 

★ميزه ⦂ كتم+ الغاء كتم+ مسح المكتومين
★ميزه ⦂ همسه
★ميزه ⦂ زخرفة+زخرفه+النص( في نوعين زخرفه و زخرفة )
★ميزه ⦂ ترحيب دخول و خروج الاعضاء 
★ميزه ⦂ جروب بيجيب الجروب+الرابط+ايدي
★ميزه ⦂ الالعاب +كت+تويت+العاب متطوره
★ميزه ⦂ التسليه بيجيب اوامر التسليه
★ميزه ⦂ ايدي بالرد بالصوره
★ميزه ⦂ جمالي برد بالصوره ونسبه
★ميزه ⦂ اذاعه خاص+بالتثبيت+بالمساعد+عام
★ميزه ⦂ نزول تلقائي للمساعد لعدم وجود حد فالكول
★ميزه ⦂ بث مباشر للقنوات 
★ميزه ⦂ اسمي بيجب الاسم
★ميزه ⦂ سورس بيجب السورس
★ميزه ⦂ كشف
★ميزه ⦂ تاك لكل الاعضاء
★ميزه ⦂ مبرمج
★ميزه ⦂ المنشئ+المالك+صاحب الخرابه
★ميزه ⦂ الاحصائيات
★ميزه ⦂ اذكار
★ميزه ⦂ دعوه في كول
★ميزه ⦂  دعوه فالخاص بتاع البوت
★ميزه ⦂ غنيلي او غ
★ميزه ⦂ بايو
★ميزه ⦂ خروج المساعد من جروبات لعدم تقطيع صوت..البوت
★ميزه ⦂ سوال/اصراحه
★ميزه ⦂ ذكاء اصتناعي /gpt
★ميزه ⦂ رفع و تنزيل مطور 
★ميزه ⦂ افلام
★ميزه ⦂ مين في الكول+بتعرف مين في الكول و عددهم
★ميزه ⦂ بايو
★ميزه ⦂ الرابط
★ميزه ⦂ حكمه
★ميزه ⦂ لو  - لو خيروك
★ميزه ⦂ انصحنى
★ميزه ⦂ احروف - حروف


⩹━⊷⌯⌞ 𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊 ⌝⌯⊶━⩺""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𖧊 𝐒𝐎𝐔𝐑𝐂𝐄 𝐀𝐋𝐏𝐎𝐏 𖧊", url=f"https://t.me/source_alpop"),                        
                 ],[
                InlineKeyboardButton(
                        "close", callback_data="close"),
               ],
          ]
        ),
    )

