import os
from time import time
from datetime import datetime
from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ContentType
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from voice_to_text import AudioProcessor

load_dotenv(find_dotenv())

bot = Bot(os.getenv("TG_TOKEN"), parse_mode="HTML")
dp = Dispatcher(bot)


async def get_file_id(message: types.Message) -> str:
    """
    Get the file ID from a Telegram message.

    Args:
        message (types.Message): The Telegram message object.

    Returns:
        str: The file ID.
    """

    if message.content_type == types.ContentType.VOICE:
        return message.voice.file_id
    elif message.content_type == types.ContentType.AUDIO:
        return message.audio.file_id
    elif message.content_type == types.ContentType.DOCUMENT:
        return message.document.file_id
    else:
        return None


async def process_audio_message(message: types.Message):
    """
    Process an audio message to text.

    Args:
        message (types.Message): The Telegram message object.
    """

    start = time()
    file_id = await get_file_id(message)

    if not file_id:
        await message.reply("Формат документа не поддерживается")
        return

    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_on_disk = Path("", f"{file_id}.tmp")
    await bot.download_file(file_path, destination=file_on_disk)
    await message.reply("Аудио получено, идет обработка")

    audio_processor = AudioProcessor(file_on_disk)
    text = audio_processor.process_audio()

    if not text:
        text = "Формат документа не поддерживается"

    await message.answer(text)
    print(f"Задача выполнена за {time() - start}. Время завершения: {datetime.now()}")
    os.remove(f'{str(file_on_disk)[:-4]}_result.wav')


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    """
    Handle the /start command.

    Args:
        message (types.Message): The Telegram message object.
    """

    await message.reply("Ожидаю аудио сообщение")


@dp.message_handler(commands=["help"])
async def cmd_start(message: types.Message):
    """
    Handle the /help command.

    Args:
        message (types.Message): The Telegram message object.
    """

    await message.reply("Просто отправь мне любой войс или документ со звуком")


@dp.message_handler(content_types=[
    ContentType.VOICE,
    ContentType.AUDIO,
    ContentType.DOCUMENT
])
async def voice_message_handler(message: types.Message):
    """
    Handle voice, audio, or document messages with sound.

    Args:
        message (types.Message): The Telegram message object.
    """

    await process_audio_message(message)


if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        pass
