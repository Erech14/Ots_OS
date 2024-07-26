# импорт пакетов в проект
import time

# имитация старта OS
OS = "Starting OtsOS"
print(OS)
time.sleep(2)
print("OS запущена")
time.sleep(1)

# основной функционал
# настройка OS 
while True:
    lang = input("Какой язык вы собираетесь использовать? RU/EN: ")
    if lang == 'RU':
        time.sleep(1)
        print("Язык по умолчанию установлен")
        time.sleep(0.7)
        print("Для получения дополнительной информации введите 'help'")
        # команды
        while True:
            time.sleep(0.3)
            command = input("Введите команду: ")
            time.sleep(0.2)
            if command == 'help':
                print("help - вызывает помощь")
                print("pas - пасхалка")
                print("time - текущее время")
            if command == 'pas':
                def decode(string):
                    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
                    decoded_string = ""
                    for char in string:
                        if char in alphabet:
                            decoded_string += alphabet[(alphabet.index(char) + 10) % 33]
                        else:
                            decoded_string += char
                    return decoded_string

                print(decode("абвгдеёжз"))
                
            if command == 'time':
            	current_time = time.localtime()
            	hours = current_time.tm_hour
            	minutes = current_time.tm_min
            	print(f"Системное время: {hours}:{minutes}")
    else:
        print("В вашей системе не установлены необходимые пакеты")
