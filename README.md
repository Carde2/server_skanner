# server_skanner--tvomel
Сканер майнкрафт серверов, для поиска существующих серверов по ноде/айпи и тд

## Плановый принцип работы:
1) Ввод айпи/домена
   Если домен - он через несколько пунктов переводится в айпи
   Если айпи - продолжаем работу
2) Ввод информацию о том, что это.
   Домен? - переводим в айпи
   Айпи? - работаем дальше
3) С какого по какой порты сканировать?
   пример 20000 to 25565
4) Начало сканирования
   Сервер существует? - Получаем две строки его MOTD
   Сервер не существует? - Идем дальше и пропускаем его
5) Запись результатов в txt файл, для дальнейшего использования.
   IP:PORT
   MOTD1:
   MOTD2:
6) Завершение работы, сохранение txt файла

### Что готово?
- [ ] GUI
- [X] Перевод домена в ip
- [X] Сканирование
- [X] Запись в txt
