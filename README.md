# О проекте

Данный проект предназначен для автоматизированной проверки корректности работы веб-сервиса
[REQRES](https://reqres.in/).  

# Структура проекта

- api_helper - модули, содержащие методы для работы с API запросами
- data - модули, содержащие данные веб-страниц
- pages - модули, содержащие методы для работы с веб-страницами
- tests - модули, содержащие тесты

# Установка

1. Установить python.
2. Скачать веб-драйвер [Chrome](https://chromedriver.chromium.org/downloads).
3. Добавить веб-драйвер в переменное окружение PATH.
4. Открыть директорию проекта в cmd.
5. Установить зависимости.  
   В cmd прописать команду:
   `pip install -r requirements.txt`.

Проект готов к запуску.

# Запуск

- Для запуска проекта необходимо в cmd прописать команду:  

`pytest --alluredir ALLURE_DIRECTORY`,  

где `ALLURE_DIRECTORY` - путь до директории, где будут сохранены отчеты о прохождении тестов.

- Для просмотра сохраненных отчетов необходимо в cmd прописать команду:  

`allure serve ALLURE_DIRECTORY`,   

где `ALLURE_DIRECTORY` - это путь до директории, где сохранены отчеты.