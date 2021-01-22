# Тестовое задание для Back-end разработчика stilsoft.ru:

Реализовать простейший REST WebAPI на Python реализующий работу с какими-либо сущностями по CRUD сценарию:

    - Выдача списка сущностей с сортировкой, фильтрацией и разбиением на страницы.
    - Выдача конкретной сущности.
    - Редактирование/добавление сущностей с проверкой корректности введённых данных.
    - Удаление сущности.
    - Так же должна быть предусмотрена авторизация пользователей и несколько ролей для них.

Данные должны храниться в БД, для взаимодействия с БД необходимо использовать ORM Django. 

Сущности должны включать хотя бы одну дочернюю сущность (несколько связанных таблиц в БД).

Данные поступающие в API должны проверяться, желательно использовать библиотеку Django REST Framework.

Архитектура API должна быть построена с использованием паттернов проектирования с расчётом на большое приложение.

Будет плюсом наличие тестов покрывающих методы API.

Можно реализовать любую клиентскую часть для демонстрации, но фокус должен быть сделан на серверной части.


# Documentation
- Реализована только часть бекэнда
- Запуск:
    ```
    - Копировать .env.example c назаванием .env
    - docker-compose up
  ```