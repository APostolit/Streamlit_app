import streamlit as st

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Домашняя",   # Текст на вкладке браузера
    page_icon="🏠",          # Иконка на вкладке браузера
    layout="wide",           # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Свернуть боковую панель
)

# Текст по центру
# st.columns(3)[1].header("Главная страница")
st.markdown("## 🏢 Главная страница")

# Текст с начала страницы
st.markdown("#### Кнопки на домашней странице")

cont = st.container(border=True, width=500)
# Создание колонок
with cont:
    left, middle, right = st.columns(3)
    # Создание кнопок в колонках
    if left.button("Кнопка 1", width="stretch"):
        left.markdown("Нажата простая кнопка")
    if middle.button("Кнопка 2", icon="😃", width="stretch"):
        middle.markdown("Нажата кнопка с эмодзи")
    if right.button("Кнопка 3", icon=":material/mood:", width="stretch"):
        right.markdown("Нажата кнопка с иконкой")

st.markdown("#### Вывод изображений")
cont_1 = st.container(border=True, width=500, height=300)
with cont_1:
    col1, col2, col3 = st.columns(3, width=500)
    with col1:
        st.text("Кошка")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.text("Собака")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.text("Сова")
        st.image("https://static.streamlit.io/examples/owl.jpg")