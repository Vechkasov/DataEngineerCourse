> [Данные о погоде](https://disk.yandex.ru/d/7Y7ZQgxUKizQsw) представлены в формате **CSV** и содержат следующие столбцы:
>> - `station_id`: ID метеостанции
>> - `date`: Дата наблюдения (в формате `YYYY-MM-DD`)
>> - `temperature`: Средняя температура в градусах Цельсия
>> - `precipitation`: Количество осадков в миллиметрах
>> - `wind_speed`: Средняя скорость ветра в метрах в секунду

> **Необходимые к выполнению задания:**
> 1. Чтение данных: загрузите данные из **CSV** файлов в `DataFrame`;
> 2. Обработка данных: 
>> - Преобразуйте столбец date в формат даты;
>> - Заполните пропущенные значения, если такие в CSV-файле есть (например, используя средние значения по метеостанциям).
> 3. Анализ данных:
>>    - Найдите топ-5 самых жарких дней за все время наблюдений.
>>    - Найдите метеостанцию с наибольшим количеством осадков за последний год.
>>    - Подсчитайте среднюю температуру по месяцам за все время наблюдений.