# ToxicityFilterBot
# 🛡️ Telegram Toxicity Filter Bot

Telegram-бот для автоматической модерации комментариев и фильтрации токсичных/оскорбительных сообщений в группах обсуждений каналов. 

Проект написан на **Python 3.14** с использованием фреймворка **aiogram 3** и нейросетевой модели текстовой классификации от **Hugging Face**.

## 🚀 Технологический стек
* **Python 3.14**
* **aiogram 3.x** — асинхронная библиотека для работы с Telegram Bot API
* **transformers & PyTorch** — запуск ML-модели `sismetanin/rubert-toxic-pikabu-2ch`
* **python-dotenv** — безопасное управление переменными окружения

## ⚡ Особенности бота
* 🔍 **ML-модерация в реальном времени:** классификация сообщений с помощью RuBERT.
* 🛡️ **Защита администраторов:** автоматический пропуск сообщений от владельцев и админов чата.
* ⏱️ **Автоудаление спама и предупреждений:** удаляет токсичное сообщение и отправляет временно предупреждение с HTML-упоминанием нарушителя (удаляется через 7 секунд).
* 🎯 **Фильтрация по типам чата:** реагирует только на сообщения в группах и супергруппах (комментариях).

## 🛠️ Установка и запуск

1. **Клонируйте репозиторий:**
   ```bash
   git clone [https://github.com/fmarichev/ToxicityFilterBot.git](https://github.com/your-username/SpamFilterBot.git)
   cd SpamFilterBot
2. Создайте и активируйте виртуальное окружение:
   python -m venv .venv
   source .venv/bin/activate  # для Linux/macOS
   .venv\Scripts\activate     # для Windows
3. Установите зависимости:
   pip install -r requirements.txt
4. Настройте переменные окружения:
   Создайте файл .env на основе .env.example:
   BOT_TOKEN=your_telegram_bot_token_here
5. Запустите бота:
   python main.py