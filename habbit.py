import streamlit as st
from datetime import date

# Установка заголовка приложения
st.title("Трекер привычек")

# Инициализация списка привычек в состоянии сессии
if 'habits' not in st.session_state:
    st.session_state['habits'] = {}

# Функция для добавления новой привычки
def add_habit(name, days_goal):
    if name and name not in st.session_state['habits']:
        st.session_state['habits'][name] = {
            'цель_по_дням': days_goal,
            'пройдено_сегодня': False,
            'дни_выполнены': 0,
            'общее_количество_дней': days_goal,
            'последняя_день_выполнения': None
        }

# Ввод для новой привычки
имя_привычки = st.text_input("Введите новую привычку")
цель_по_дням = st.number_input("Установите цель по количеству дней", min_value=1, step=1)
if st.button("Добавить привычку"):
    add_habit(имя_привычки, цель_по_дням)

# Фильтр привычек по статусу
статус_фильтра = st.radio("Фильтр по статусу", ('Все', 'Выполнено сегодня', 'Не выполнено сегодня'))

# Отображение привычек с чекбоксами
st.write("Статус привычек")
for habit, data in st.session_state['habits'].items():
    # Фильтрация по статусу
    if статус_фильтра == 'Выполнено сегодня' and not data['пройдено_сегодня']:
        continue
    elif статус_фильтра == 'Не выполнено сегодня' and data['пройдено_сегодня']:
        continue
    col1, col2, col3 = st.columns([4, 2, 2])
    with col1:
        st.write(habit)
    with col2:
        if st.button(f"Отметить выполненным {habit}"):
            if not data['пройдено_сегодня']:
                data['пройдено_сегодня'] = True
                data['дни_выполнены'] += 1
                data['последняя_день_выполнения'] = date.today()
    with col3:
        if st.button(f"Сбросить {habit}"):
            if data['пройдено_сегодня']:
                data['пройдено_сегодня'] = False

# Отображение прогресса
st.write("Прогресс привычек")
for habit, data in st.session_state['habits'].items():
    прогресс = data['дни_выполнены'] / data['цель_по_дням']
    st.write(f"{habit}: {data['дни_выполнены']} из {data['цель_по_дням']} дней")
    st.progress(прогресс)

# Напоминание о невыполненных привычках за день
if st.button("Показать невыполненные привычки сегодня"):
    невыполненные = [habit for habit, data in st.session_state['habits'].items() if not data['пройдено_сегодня']]
    if невыполненные:
        st.write("Невыполненные привычки:")
        for habit in невыполненные:
            st.write(habit)
    else:
        st.write("Все привычки выполнены на сегодня!")