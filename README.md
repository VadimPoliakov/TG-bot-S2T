# Voice-to-Text Telegram Bot

Этот проект представляет собой Telegram-бота, который преобразует аудиосообщения в текст. Бот поддерживает форматы аудио и голосовых сообщений, а также документов с аудио.

## Описание

Бот позволяет пользователям отправлять аудиосообщения и документы с аудио в чат, после чего он преобразует их в текстовый формат с автоматической пунктуацией.

## Особенности

- Поддерживает форматы аудио, голосовых сообщений и документов с аудио.
- Преобразует аудиосообщения в текст с автоматической пунктуацией.
- Интерфейс команд /start и /help для пользователей.

## Установка и запуск

1. Склонируйте этот репозиторий на свой локальный компьютер:

```bash
git clone https://github.com/VadimPoliakov/TG-bot-S2T.git
```

2. Установите необходимые зависимости:

```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` и укажите в нем свой токен Telegram Bot API:

```env
TG_TOKEN=ваш_токен
```

### Модель Vosk и FFmpeg

*Vosk* - оффлайн-распознавание аудио и получение из него текста. Модели доступны на сайте [проекта](https://alphacephei.com/vosk/models "Vosk - оффлайн-распознавание аудио"). Скачайте модель, разархивируйте и поместите папку model с файлами в папку models/vosk.
- [vosk-model-ru-0.42       - 1.8 Гб](https://alphacephei.com/vosk/models#:~:text=Russian-,vosk%2Dmodel%2Dru%2D0.42,-1.8G) - лучше распознает, но дольше и весит много.
- [vosk-model-small-ru-0.22 - 45 Мб](https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip "Модель vosk-model-small-ru-0.22 - 45 Мб") - хуже распознает, но быстрее и весит мало.

*FFmpeg* - набор open-source библиотек для конвертирования аудио- и видео в различных форматах.
Скачайте с сайта [проекта](https://ffmpeg.org/download.html "FFmpeg - набор open-source библиотек для конвертирования аудио- и видео в различных форматах.") и установите


4. Запустите бота:

```bash
python main.py
```

## Использование

- Отправьте аудиосообщение или документ с аудио в чат бота.
- Бот автоматически преобразует аудио в текст и добавляет пунктуацию.
- Результат будет отправлен в чат.

## Структура проекта

- `main.py`: Основной файл, который обрабатывает входящие сообщения и запускает процесс преобразования аудио.
- `voice_to_text.py`: Модуль для обработки аудио, включая конвертацию и преобразование в текст.
- `.env`: Файл конфигурации для хранения токена Telegram Bot API.
- `requirements.txt`: Список зависимостей проекта.

## Зависимости

Проект использует следующие библиотеки и инструменты:

- [aiogram](https://github.com/aiogram/aiogram): Для работы с Telegram Bot API.
- [vosk](https://github.com/alphacep/vosk-api): Для распознавания речи.
- [pydub](https://github.com/jiaaro/pydub): Для работы с аудиофайлами.
- [ffmpeg](https://www.ffmpeg.org/): Для конвертации аудио в WAV формат.
- [recasepunc](https://github.com/MaxwellRebo/recasepunc): Для автоматической пунктуации текста.
