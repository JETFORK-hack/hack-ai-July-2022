# Решение от команды JETFORK

# Настройка перед запуском
1. Необходимо загрузить файлы с zip-кодами в формате csv в папку `app/resources/zipcodes`. Формат файла должен быть `zipcodes.ru.csv`, где `ru` - код страны (это важно). Разделитель `,`;
2. Необходимо загрузить данные с датасетом в формате xslx в папку `app/resources/datasets`;
2. Необходимо загрузить словарь расшифровок ВЕД `app/resources/veds`. Разделителем является `;`!


## Запуск контейнеров
```shell
 docker-compose -f docker-compose.yml up -d --build
```
после старта контейнеров поднимутся:
* база, доступная по 0.0.0.0:5432
* сервис по адресу 0.0.0.0:8000


# Настройка после запуска
1. Загрузка данных **датасета** в БД. Убедитесь, что файл или файлы есть в папке `app/resources/datasets`
```shell
docker exec -it hack_app python manage.py load_datasets
```

2. Загрузка **словарей-расшифровок ВЕД** в БД. Убедитесь, что файл или файлы есть в папке `app/resources/veds`
```shell
docker exec -it hack_app python manage.py load_veds
```

