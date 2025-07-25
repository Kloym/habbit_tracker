# Streamlit Habit Tracker

Добро пожаловать в **Streamlit Habit Tracker** — простое и удобное приложение для отслеживания и формирования полезных привычек. С помощью этого приложения вы сможете создавать привычки, отмечать их выполнение, следить за прогрессом и мотивировать себя на новые достижения!

## Описание

Streamlit Habit Tracker — это веб-приложение на базе Streamlit, которое помогает вам вырабатывать и поддерживать полезные привычки. Вы можете добавлять привычки, устанавливать цели, отмечать выполнение, видеть напоминания и анализировать свой прогресс с помощью наглядных графиков.

## Основные функции

- **Добавление привычек:** Вводите название, описание и цель по количеству дней для каждой привычки.
- **Отметка выполнения:** Отмечайте выполнение привычки за текущий день одним кликом.
- **Напоминания:** Получайте напоминания о невыполненных привычках за сегодня.
- **Фильтрация:** Фильтруйте привычки по статусу (выполнено/не выполнено сегодня).
- **Редактирование и удаление:** Управляйте своими привычками — редактируйте и удаляйте их при необходимости.
- **Визуализация прогресса:** Следите за прогрессом по каждой привычке с помощью прогресс-баров.

## 🚀 Быстрый старт

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/Kloym/habbit_tracker.git
   cd STREAMLIT

2. **Установите зависимости через poetry:**
    poetry install

3. **Активируйте виртуальное окружение poetry:**
    poetry shell

4. **Запустите приложение:**
    make start
    или напрямую: streamlit run habbit.py

## 🛠️ Функционал

1. **Добавление, редактирование и удаление привычек**
2. **Установка цели по количеству дней для каждой привычки**
3. **Отметка выполнения привычки за день**
4. **Напоминания о невыполненных привычках**
5. **Фильтрация привычек по статусу**
6. **Визуализация прогресса**

## 📁 Структура проекта

    .
    ├── .venv/                # Виртуальное окружение (игнорируется git)
    ├── .gitignore
    ├── Makefile              # Быстрый запуск через make
    ├── habbit.py        # Основной код приложения
    ├── poetry.lock
    ├── pyproject.toml        # Зависимости poetry

## 💡 Примечания

1. Для работы необходим Python 3.8+
2. Все зависимости устанавливаются через poetry
3. Для запуска используйте make или команду streamlit