from storage import load_data, save_data
from datetime import date

def show_menu():
    print("\n1. Добавить привычку")
    print("2. Отметить выполнение")
    print("3. Показать привычки")
    print("4. Выход")

def main():
    data = load_data()

    while True:
        show_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Название привычки: ")
            if name in data:
                print("Такая привычка уже существует.")
            else:
                data[name] = []
                save_data(data)
                print("Привычка добавлена.")

        elif choice == "2":
            name = input("Название привычки: ")
            if name in data:
                today = str(date.today())
                if today not in data[name]:
                    data[name].append(today)
                    save_data(data)
                    print("Выполнение отмечено.")
                else:
                    print("Сегодня уже отмечено.")
            else:
                print("Привычка не найдена.")

        elif choice == "3":
            if not data:
                print("Привычек пока нет.")
            else:
                for habit, days in data.items():
                    print(f"{habit}: выполнено {len(days)} раз")

        elif choice == "4":
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод.")

main()