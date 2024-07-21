from aiogram import Router, F
from aiogram.types import Message, FSInputFile, InputPaidMediaVideo
from aiogram.filters import CommandStart
from bot.app.download import Downloader
from bot.get_lastest_video import last_modified_file
import os
import re

router = Router()
ytd = Downloader()

ascii_art = '''
   ('-.                     ) (`-.    _ .-') _            _ (`-.  
  ( OO ).-.                  ( OO ). ( (  OO) )          ( (OO  ) 
  / . --. /,--.    ,--. ,--.(_/.  \_)-\     .'_ ,--.    _.`     \ 
  | \-.  \ |  |.-')|  | |  | \  `.'  /,`'--..._)|  |.-'(__...--'' 
.-'-'  |  ||  | OO |  | | .-')\     /\|  |  \  '|  | OO |  /  | | 
 \| |_.'  ||  |`-' |  |_|( OO )\   \ ||  |   ' ||  |`-' |  |_.' | 
  |  .-.  (|  '---.|  | | `-' .'    \_|  |   / (|  '---.|  .___.' 
  |  | |  ||      ('  '-'(_.-/  .'.  \|  '--'  /|      ||  |      
  `--' `--'`------' `-----' '--'   '--`-------' `------'`--'      
'''

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(ascii_art)

@router.message(F.text)
async def return_video(message: Message):
    await message.answer("⌛")
    links = str(message.text).split(", ")
    dynamic_path = f"bot/videos/{message.from_user.id}"
    filename = last_modified_file(dynamic_path, len(links))
    await ytd.download_video(links, dynamic_path)
    if len(links) >= 2:
        async for i in range(len(links)):
            await message.answer_video(
            video=FSInputFile(
            path=filename[i]
        ))


    print(str(filename))
    await message.answer_video(
        video=FSInputFile(
            path=filename[0]
        )
        )
