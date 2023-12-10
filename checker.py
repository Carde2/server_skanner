import socket, re, sys, colorama
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore
from mcstatus import JavaServer
init()

print(Fore.MAGENTA + """
   ______  __                             __
  / ____ \/ /__   ______  ____ ___  ___  / /
 / / __ `/ __/ | / / __ \/ __ `__ \/ _ \/ / 
/ / /_/ / /_ | |/ / /_/ / / / / / /  __/ /  
\ \__,_/\__/ |___/\____/_/ /_/ /_/\___/_/   
 \____/                                     
 """)



#Ввод начальных данных
ipdomen = input(Fore.CYAN + "Введите айпи/домен: ")
ip = socket.gethostbyname(ipdomen)
print(Fore.CYAN + f"Получен IP: {ip}")
portfrom = int(input(Fore.CYAN + "Введите порт, с которого пойдет скан (Лучше 20000): "))
portto = int(input(Fore.CYAN + "Введите порт, до какого пойдет скан (Лучше 65535): "))
print(Fore.CYAN + f"Скан идёт с {portfrom} по {portto} порты")
numbertxt = input(Fore.CYAN + "Доп текст для подписи txt файла (servers_[ваша часть].txt): ")
print(Fore.CYAN + f"Название файла: servers_{numbertxt}.txt")

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
            clear_motd = re.sub(r'§.|&.', '', motd)
            print(Fore.GREEN + f"Сервер {ip}:{str(port)} существует" + Fore.WHITE + f"\n{clear_motd}\n")
        except Exception as error:
            print(Fore.RED + f"Сервер {ip}:{str(port)} Есть\nНо произошла ошибка при получении MOTD: \n" + Fore.LIGHTRED_EX + f"{error}\n")
            with open(f"NONE_servers_{numbertxt}.txt", "a") as file:
                file.write(f"{ip}:{str(port)}\nНе удалось получить MOTD, возможно сервер недействителен\n\n")
        with open(f"servers_{numbertxt}.txt", "a") as file:
                file.write(f"{ip}:{str(port)}\nMOTD: {clear_motd}\n\n")
    except socket.error:
        print(Fore.RED + f"Сервер {ip}:{str(port)} не существует")
    finally:
        cont.close()
with ThreadPoolExecutor() as executor:
    executor.map(check_port, range(portfrom, portto+1))


#Выход
input("Enter для выхода!")
