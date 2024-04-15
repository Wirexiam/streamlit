# Lamborghini Data Viewer

## Описание проекта

Приложение "Lamborghini Data Viewer" предназначено для загрузки и визуализации данных о продажах и акциях компании Lamborghini. Это интерактивное приложение разработано на базе Streamlit и позволяет пользователям загружать данные из различных файлов, а затем анализировать их через визуальные графики.

## Датасеты

Данные представлены в двух файлах:
1. `LamboData.xlsx` - Этот файл содержит информацию о продажах автомобилей и ценах акций компании за разные года. Структура данных включает следующие колонки:
   - **Year**: Год
   - **Sales**: Количество проданных автомобилей в этом году
   - **Growth**: Рост продаж относительно предыдущего года
   - **Open**: Стартовая цена акций в начале года
   - **High**: Максимальная цена акций в течение года
   - **Low**: Минимальная цена акций в течение года
   - **Close**: Закрывающая цена акций в конце года

2. `Lambo-Future.csv` - Файл содержит прогнозные данные о продажах и росте:
   - **Sales**: Прогнозируемое количество продаж
   - **Growth**: Ожидаемый рост продаж

## Функциональность приложения

- Загрузка данных из выбранного файла.
- Отображение загруженных данных в таблице.
- Визуализация данных с помощью графиков, в зависимости от доступных колонок в загруженном файле.

## Автор

Данила Шестаков - Alfe2230@gmail.com
