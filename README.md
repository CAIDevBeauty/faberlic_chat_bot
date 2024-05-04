# Чат-бот Faberlic

Привет! Я бот-консультант Faberlic раздела ухода за волосами. Я отвечу на любой ваш вопрос по заказам или помогу сделать заказ

## Команда проекта:

Шухман Арина (@ArinaUshch)

Изюмова Анастасия (@starminalush)


## Как использовать

### Склонировать репозиторий:

```shell
git clone https://github.com/CAIDevBeauty/faberlic_chat_bot.git
cd faberlic_chat_bot
```

### Подготовка

1. Заполнить файл .env при примеру .env.template
2. Заполнить файл models_api/.env по примеру models_api/.env.template 
3. Заполнить файл tg_bot/.env по примеру tg_bot/.env.template

Внимание: для корректной работы нужен VPN, так как используются модели OpenAI

### Запуск бота

#### С помощью Docker Compose

```shell
sudo docker compose up --build -d 
```

### Схема состояний и элементов бота
![image](https://github.com/CAIDevBeauty/faberlic_chat_bot/assets/103132748/204656fb-0b12-45df-a14d-f264efb2e86d)

### Примеры работы
<img width="814" alt="image" src="https://github.com/CAIDevBeauty/faberlic_chat_bot/assets/103132748/41be2bf0-e2e1-4293-97ab-00b36d869773">

<img width="814" alt="image" src="https://github.com/CAIDevBeauty/faberlic_chat_bot/assets/103132748/0409f83f-fa56-4288-bb30-6cffb36734b6">

<img width="835" alt="image" src="https://github.com/CAIDevBeauty/faberlic_chat_bot/assets/103132748/a914dd4e-184e-4db6-ae13-d138f3dd412e">

### Тестирование
1. Запустить сервис с моделями командой
```shell
sudo docker compose up --build -d backend
```
или
```shell
cd models_api && uvicorn main:app --host 0.0.0.0
```
2. Запустить тест
```shell
(cd tg_bot && pytest tests)
```
Внимание: тест упадет, потому что в нем есть ответы, сгенерированные GPT. Тест стоит рассматривать как жизнеспособный пример работы бота.



