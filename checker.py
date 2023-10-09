#Либы
import socket
import re
import sys
import colorama
from concurrent.futures import ThreadPoolExecutor
from colorama import init
from colorama import Fore, Back, Style
from mcstatus import JavaServer
init()

#Ввод начальных данных
ipdomen = input(Fore.YELLOW + "Введите айпи/домен: ")
portfrom = int(input(Fore.YELLOW + "Введите порт, с которого пойдет скан (Лучше 20000): "))
portto = int(input(Fore.YELLOW + "Введите порт, до какого пойдет скан (Лучше 65535): "))


#Логика перевода домена в айпи
    #Получен домен
ip = socket.gethostbyname(ipdomen)
print(Fore.CYAN + f"Получен IP: {ip}\nСкан идёт с {portfrom} по {portto} порты")
#Логика скана
def check_port(port):
    cont = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cont.settimeout(1)
    try:
        cont.connect((ip, port))
        server = JavaServer.lookup(f'{ip}:{str(port)}')
        try:
            status = server.status()
            motd = status.description
            clear_motd = re.sub(r'§.', '', motd)
            print(Fore.GREEN + f"Сервер {ip}:{str(port)} существует")
            print(Fore.WHITE + f"{clear_motd}\n")
        except Exception as e:
            print(Fore.RED + f"Ошибка при получении MOTD: {e}")
        with open("servers.txt", "a") as file:
            file.write(f"{ip}:{str(port)}\nMOTD: {clear_motd}\n\n")
    except socket.error:
        print(Fore.RED + f"Сервер {ip}:{str(port)} не существует")
    finally:
        cont.close()
#Получен айпи
with ThreadPoolExecutor() as executor:
    executor.map(check_port, range(portfrom, portto))

#Выход
input("Enter для выхода!")
#Айпи для теста              65.21.127.190
#Домен для теста             d19.gamely.pro
#Всё работает
