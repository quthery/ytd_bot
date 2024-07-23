from aiogram import Router, F
from aiogram.types import Message, FSInputFile, InputPaidMediaVideo
from aiogram.filters import CommandStart
from bot.app.download import Downloader
from bot.get_lastest_video import last_modified_file
import os


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
    
    await ytd.download_video(links, dynamic_path)
    filename = last_modified_file(dynamic_path)
    
    if len(links) >= 2:
        await message.bot.delete_message(chat_id=message.chat.id, 
                                         message_id=message.message_id-1)
        for i in range(len(links)):
            await message.answer_video(
                video=FSInputFile(
                    path=filename[i]
                )
            )
    else:
        await message.answer_video(
            video=FSInputFile(
                path=filename[0]
            )
        )
        os.remove(dynamic_path)


