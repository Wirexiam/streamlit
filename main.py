import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Функция для загрузки и предварительной обработки данных
@st.cache
def load_data():
    data = pd.read_csv('car_prices.csv')
    # Use errors='coerce' to handle any data that cannot be converted to dates
    data['saledate'] = pd.to_datetime(data['saledate'], errors='coerce')
    # Drop rows where 'saledate' is NaT after coercion
    data = data.dropna(subset=['saledate'])
    return data

data = load_data()

# Селектор для выбора марки
make = st.sidebar.selectbox('Выберите марку', data['make'].unique())

# Фильтрация моделей на основе выбранной марки
models = data[data['make'] == make]['model'].unique()
selected_models = st.sidebar.multiselect('Выберите модель', models)

# Если модели не выбраны, используем все модели выбранной марки
if not selected_models:
    selected_models = models

# Селекторы для дальнейшей фильтрации данных
year_range = st.sidebar.slider('Выберите диапазон годов', int(data['year'].min()), int(data['year'].max()), (2010, 2020))
odometer_range = st.sidebar.slider('Выберите диапазон пробега', 0, int(data['odometer'].max()), (0, 100000))
condition = st.sidebar.radio('Выберите состояние', data['condition'].unique())

# Фильтрация данных по марке, модели, году, пробегу и состоянию
filtered_data = data[
    (data['make'] == make) &
    (data['model'].isin(selected_models)) &
    (data['year'].between(year_range[0], year_range[1])) &
    (data['odometer'].between(odometer_range[0], odometer_range[1])) &
    (data['condition'] == condition)
]

# График MMR от состояния автомобиля
st.subheader('Market Value (MMR) от состояния автомобиля')
fig, ax = plt.subplots()
sns.boxplot(x=filtered_data['condition'], y=filtered_data['mmr'], ax=ax)
ax.set_xlabel('Состояние')
ax.set_ylabel('Market Value (MMR)')
st.pyplot(fig)

# График средней цены продажи по выбранным маркам и моделям
st.subheader('Средняя цена продажи для выбранных марок и моделей')
if not filtered_data.empty:  # Проверяем, что фильтрованные данные не пустые
    average_price_by_selected_models = filtered_data.groupby(['make', 'model'])['sellingprice'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 8))  # Вы можете настроить размер фигуры под свои нужды
    average_price_by_selected_models.plot(kind='bar', ax=ax)
    ax.set_xlabel('Марка и модель')
    ax.set_ylabel('Средняя цена продажи')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    st.pyplot(fig)
else:
    st.error('Нет данных для отображения. Пожалуйста, измените фильтры.')

# График корреляции между пробегом и ценой продажи
st.subheader('Корреляция между пробегом и ценой продажи')
if not filtered_data.empty:  # Проверяем, что фильтрованные данные не пустые
    fig, ax = plt.subplots()
    sns.scatterplot(x=filtered_data['odometer'], y=filtered_data['sellingprice'], ax=ax)
    ax.set_xlabel('Пробег')
    ax.set_ylabel('Цена продажи')
    st.pyplot(fig)
else:
    st.error('Нет данных для отображения. Пожалуйста, измените фильтры.')