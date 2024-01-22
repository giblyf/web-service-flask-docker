# Web Service с использованием Flask и Docker Compose

Этот проект представляет собой пример веб-сервиса, построенного с использованием Flask и контейнеризированного с помощью Docker.

## Требования

- Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
- Docker Compose: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

## Установка и Запуск

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/giblyf/web-service-flask-docker.git
    cd web-service-flask-docker
    ```

2. Создайте и запустите Docker контейнеры с использованием Docker Compose:

    ```bash
    docker-compose up -d
    ```

## Endpoint'ы

Проект поддерживает HTTP GET-запрос на эндпоинт /pick_regno
Запрос содержит параметры строки запроса (query parameters)

### Параметры:

| Argument                   | Type          |
|----------------------------|---------------|
| regno_recognize            | str           |
| afts_regno_ai              | str           |
| recognition_accuracy       | num           |
| afts_regno_ai_score        | num           |
| afts_regno_ai_char_scores  | list          |
| afts_regno_ai_length_scores| list          |
| camera_type                | num           |
| camera_class               | num           |
| time_check                 | date          |
| direction                  | num           |


## Пример
Запрос:
http://localhost:5001/pick_regno?regno_recognize=А939НО19&afts_regno_ai=А939НО190&recognition_accuracy=6.4&afts_regno_ai_score=0.8689166903495789&afts_regno_ai_char_scores=0.9998925924301147, 200.9999872446060181, 200.9999798536300659, 200.9999990463256836, 200.9988356232643127, 200.9998175501823425, 201.0, 200.999994158744812, 200.8702163696289062&afts_regno_ai_length_scores=3.2404470773350624e-10, 203.236617363011618e-10, 203.2367283853140805e-10, 203.2651523151905337e-10, 203.234087164738497e-10, 203.259402747701756e-10, 203.2362224011706076e-10, 204.545459564297971e-09, 202.996458192683349e-08, 201.0, 203.2479344214131345e-10&camera_type=Стационарная&camera_class=Астра-Трафик&time_check=2021-08-01+09:02:59&direction=0

Результат работы функции pick_regno возвращается в виде HTTP-ответа в формате JSON: 
```
{
  "class_0_probability": 0.6580280475011289,
  "class_1_probability": 0.34197195249887113
}
```

## Особенности реализации и почему именно так: 

### 1. Flask: 
- Flask был выбран в качестве веб-фреймворка из-за своей легкости и простоты использования. Он позволяет быстро создать REST API с минимальным количеством кода.
- Flask имеет хорошую документацию и обширное сообщество, что облегчает поддержку и разработку.
### 2. Docker: 
- Использование Docker обеспечивает изоляцию окружения, что делает сервис переносимым и легко масштабируемым.
- Docker-контейнер позволяет упаковать все зависимости, включая модель и скрипт, в одну единицу развертывания.

## Дополнительные настройки

- Порт, на котором работает веб-сервис, можно изменить в файле [docker-compose.yml](Docker-compose.yml).
- Дополнительные настройки Docker и Docker Compose могут быть внесены в [Dockerfile](Dockerfile) и [docker-compose.yml](docker-compose.yml) соответственно.

## Остановка и Удаление

Чтобы остановить и удалить контейнеры, выполните:

```bash
docker-compose down
