Команда для генерации логов выглядит следующим образом:
```sh
cat <<EOL > access.log
192.168.1.1 - - [28/Jul/2024:12:34:56 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.2 - - [28/Jul/2024:12:35:56 +0000] "POST /login HTTP/1.1" 200 567
192.168.1.3 - - [28/Jul/2024:12:36:56 +0000] "GET /home HTTP/1.1" 404 890
192.168.1.1 - - [28/Jul/2024:12:37:56 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.4 - - [28/Jul/2024:12:38:56 +0000] "GET /about HTTP/1.1" 200 432
192.168.1.2 - - [28/Jul/2024:12:39:56 +0000] "GET /index.html HTTP/1.1" 200 1234
EOL
```

---
Задание:
1. Подсчитать общее количество запросов;
2. Подсчитать количество уникальных IP-адресов;
3. Подсчитать количество запросов по методам (**GET**, **POST** и т.д.);
4. Найти самый популярный URL;
5. Создать отчет в виде текстового файла. Название текстового файла - `report.txt`.
