>**Есть три [набора данных](https://disk.yandex.ru/d/EJU5clkFkhWklA):**
> 1. Таблица `movies`:
> > - `movie_id`: ID фильма
> > - `title`: Название фильма
> > - `genre`: Жанр фильма
> > - `release_date`: Дата выхода (в формате `YYYY-MM-DD`)
> > - `budget`: Бюджет фильма
> 2. Таблица `actors`:
> > - `actor_id`: ID актера
> > - `name`: Имя актера
> > - `birth_date`: Дата рождения актера (в формате `YYYY-MM-DD`)
> > - `country`: Страна актера
> 3. Таблица `movie_actors`:
> > - `movie_id`: ID фильма
> > - `actor_id`: ID актера

> **Необходимые к выполнению задания:**
> 1. Чтение данных: загрузите данные из **CSV** файлов в `DataFrame`;
> 2. Создание временных таблиц: создайте временные таблицы для данных о фильмах, актерах и связях между ними;
> 3. SQL-запросы:
>     - Найдите топ-5 жанров по количеству фильмов;
>     - Найдите актера с наибольшим количеством фильмов;
>     - Подсчитайте средний бюджет фильмов по жанрам;
 >    - Найдите фильмы, в которых снялось более одного актера из одной страны.