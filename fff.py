from colorama import Fore, Style, init
import re
import time 

init(autoreset=True)

user_data = {
    "@reqlib": {
        "номер": "Номер-ненайдено",
        "дата регистрации": "15 октября 2024 год",
        "айди": "6649538880"
    }
}
user_data = {
    "@pythondevoleper": {
        "номер": "Номер-ненайдено",
        "дата регистрации": "14 апреля 2024 год",
        "айди": "7150261279"
    }
}

def main_menu():
    print(Fore.GREEN + '''██████╗  █████╗ ███╗   ██╗ ██████╗██╗  ██╗ █████╗     ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗██╔══██╗████╗  ██║██╔════╝██║  ██║██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██████╔╝███████║██╔██╗ ██║██║     ███████║███████║       ██║   ██║   ██║██║   ██║██║     
██╔═══╝ ██╔══██║██║╚██╗██║██║     ██╔══██║██╔══██║       ██║   ██║   ██║██║   ██║██║     
██║     ██║  ██║██║ ╚████║╚██████╗██║  ██║██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝''')
    print(Fore.GREEN + "1) панча намбер сеарч")
    print(Fore.GREEN + "2) панча юсернейм сеарч")
    print(Fore.GREEN + "3) снос")
    print(Fore.GREEN + "4) флуд кодами")
    print(Fore.GREEN + "5) автор")
    print(Fore.GREEN + "6) ддос")  

def search_by_number():
    valid_numbers = ["+7 999 635 8210", "+7 999 635 1234"]  
    
    number = input("Введите номер телефона в формате +7 XXX XXX XXXX: ")
   
    if not re.match(r'^\+7 \d{3} \d{3} \d{4}$', number):
        print("Нету нечего.")
        return
    
    if number in valid_numbers:
        messages = ["Ф-эболов", "И-рекюлиб", "О-визивеч", "Адрс-хз", "Соцсети-хз"]
        for message in messages:
            print(message)
    else:
        print("Нету нечего.")

def search_by_username():
    username = input("Введите юзернейм: ")
    
    if username in user_data:
        info = user_data[username]
        print(f"Номер: {info['номер']}")
        print(f"Дата регистрации: {info['дата регистрации']}")
        print(f"Айди: {info['айди']}")
    else:
        print("Юзернейм не найден.")

def delete_user():
    username = input("Введите юзернейм: ")
    user_id = input("Введите айди: ")
    
    print("Загрузка...") 
    for percent in range(0, 101, 5):  
        print(f"{percent}%", end='\r')  
        time.sleep(1)  

    print("\nУспешно снесено.") 

def flood_codes():
    number = input("Введите номер для флудов: ")
    
  
    print("Флуд успешно отправлен.")

def author_info():
    print("Создатель софта: @pan4ito")
    print("Канал софта: @scary_komaru")

def ddos_attack():
    url = input("Введите URL web site: ")
    print("Атака началась")
    time.sleep(0.1) 
    print("200")
    time.sleep(0.1)
    print("200")
    time.sleep(0.1)
    print("200") 
    time.sleep(0.1)
    print("200")
    time.sleep(0.1)
    print("200")
    time.sleep(0.1) 
    print("200")
    time.sleep(0.1)
    print("200")
    time.sleep(0.1)
    print("200") 
    time.sleep(0.1)
    print("200")
    time.sleep(0.1)
    print("200")
    time.sleep(0.1) 
    print("200")
    time.sleep(0.1)
    print("200")
    time.sleep(0.1)
    print("200") 
    time.sleep(0.1)
    print("200")
    time.sleep(0.1)
    print("200")
    time.sleep(1)
    print("502") 
def main():
    
    while True:
        time.sleep(2)
        main_menu()
        choice = input("Введите номер пункта меню: ")
        
        if choice == "1":
            search_by_number()
        elif choice == "2":
            search_by_username()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            flood_codes()
        elif choice == "5":
            author_info()
        elif choice == "6":
            ddos_attack()  
        elif choice == "0":
        	
            break  
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":  
    main()