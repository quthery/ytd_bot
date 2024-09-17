from aiogram import Router, F
from aiogram.types import Message, FSInputFile, InputPaidMediaVideo
from aiogram.filters import CommandStart
from bot.app.download import Downloader
from bot.get_lastest_video import last_modified_file
import shutil


router = Router()
ytd = Downloader()




@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет 👋")

@router.message(F.text)
async def return_video(message: Message):
    url = Downloader.get_direct_link(str(message.text))
    print(url)
    
    link = Downloader.get_direct_link1(str(message.text))
    print(link)
    await message.answer(url)
    await message.answer(link)


