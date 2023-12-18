import sys, socket, re, os, logos, time
from concurrent.futures import ThreadPoolExecutor
from mcstatus import JavaServer
from pystyle import *

# Цвета
PP = Colors.purple
RED = Colors.red
DRED = Colors.dark_red
CN = Colors.cyan
GN = Colors.green
WH = Colors.white
# Логотипы
AU = logos.autor

# Менюшки
BOX = Box.DoubleCube
BL = Box.Lines

# pystyle цвета
CC = Center.Center
CH = Colorate.Horizontal
CV = Colorate.Vertical

# From -> To
BtC = Colors.blue_to_purple
PtB = Colors.purple_to_blue

print(f"{PP}{AU}\n")

# Начальные данные (Айпи, порт начала, порт конца, название файла сейва)
ip = socket.gethostbyname(input(f"{CN}Введите IP или домен: "))
print(f"Получен IP: {ip}")
port_from = int(input("Введите начальный порт: "))
port_to = int(input("Введите конечный порт: "))
filename = "servers_" + input("Введите название файла (servers_[ваша часть].txt): ")
none_server = f"None_Server_{filename}"

# Сообщение о данных сканирования (Айпи, порты с какого по какой идет скан, название файла)
print("\033[H\033[J")
print(PP + BL(f"""
Айпи: {ip}
Порт начала: {port_from}
Конечный порт: {port_to}
Название файла: {filename}.txt
"""))

#Логика скана
def skan(port):
    # Создание socket (sock)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Настройки для удобства 
    #  1 - Время между повторами;  
    #  2 - Нормальный айпи сервера;
    # (Вместо {ip}:{port} в каждой строке)
    sock.settimeout(1)
    serv = f'{ip}:{port}'
    try:
         # Подключение к серверу
        sock.connect((ip, port))
        serv2 = JavaServer.lookup(serv)
        try:
            status = serv2.status()
            query = serv2.query()
            motd = re.sub(r'§.|&.', '', {status.description})
            print(f"{GN}Сервер {serv} существует.{WH}\n{motd}\n")
        except Exception as error:
            print(f"{RED}Сервер {serv} получить невозможно. \nВозможно сервера нет!\n{DRED}{error}\n")
            with open(f"{none_server}.txt", "a") as file:
                file.write(f"{serv}\nНе удалось получить MOTD\n\n")
        with open(f"{filename}.txt", "a") as file:
                file.write(f"{serv}\n{status.players.online}\n{', '.join(query.players.names)}\n{motd}\n")
    except socket.error:
        print(RED + f"Сервер {serv} не существует")
    finally:
        sock.close()
with ThreadPoolExecutor() as executor:
    executor.map(skan, range(port_from, port_to+1))

# Выход
input(PP + "Enter для выхода!")
