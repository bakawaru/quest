import random

# ---------- ФУНКЦИИ ----------

def show_menu():
    print("\n1 - Идти вперёд")
    print("2 - Отдохнуть")
    print("3 - Освоить местность")
    print("4 - Инвентарь")
    print("5 - Поискать сокровища")  # Новая функция в меню
    print("выход - Завершить игру")

def show_status(health, turns, money, inventory):
    print(f"\nЗдоровье: {health} | Монеты: {money} | Ход: {turns}")
    print(f"Инвентарь: {inventory}")

def apply_damage(health, damage):
    print(f"Ты получаешь урон {damage}!")
    return health - damage

def heal(health, amount):
    print(f"Ты восстанавливаешь {amount} здоровья.")
    return health + amount

def add_money(money, amount):
    return money + amount

# --- НОВАЯ ФУНКЦИЯ (Квест: поиск сокровищ) ---
def search_treasure(money, inventory, health):
    print("\nТы внимательно осматриваешь окрестности...")
    # Случайное событие от 1 до 4
    event = random.randint(1, 4)
    
    if event == 1:
        found_money = random.randint(10, 50)
        money = add_money(money, found_money)
        print(f"Удача! Ты нашел кошель с монетами. (+{found_money} монет)")
        
    elif event == 2:
        found_item = random.choice(["Старинный меч", "Зелье удачи", "Амулет"])
        inventory.append(found_item)
        print(f"Ты нашел сундук, внутри лежит: {found_item}. Добавлено в инвентарь.")
        
    elif event == 3:
        print("Ты наступил на скрытую ловушку!")
        health = apply_damage(health, 15)
        print("Нужно быть осторожнее.")
        
    else:
        print("Ты долго бродил, но ничего не нашел. Только устал.")
        health = apply_damage(health, 5)
        
    return money, inventory, health
# ----------------------------------------------

def process_turn(choice, health, money, inventory):
    if choice == "1":
        money = add_money(money, 30)
        print("Ты нашёл монеты!")
        
    elif choice == "2":
        health = heal(health, 20)
        
    elif choice == "3":
        print("Ты нашел кафе.")
        action = input("Хочешь зайти? ").lower().strip()
        if action == "зайти":
            if money >= 1:
                money = money - 1
                health = heal(health, 40)
            else:
                print("У тебя нет монет, чтобы заплатить.")
        elif action == "пройти мимо":
            print("Ты ничего не нашел.")
        else:
            print("Я тебя не понял.")
            
    elif choice == "4":
        print("\nВ твоём рюкзаке:")
        if len(inventory) == 0:
            print("- (пусто)")
        else:
            for item in inventory:
                print(f"- {item}")
                
    # НОВЫЙ ПУНКТ МЕНЮ
    elif choice == "5":
        money, inventory, health = search_treasure(money, inventory, health)
        
    else:
        print("Неизвестная команда.")

    return health, money, inventory


# ---------- ОСНОВНОЙ ЦИКЛ ИГРЫ ----------
def start_game():
    health = 100
    money = 10
    turns = 0
    inventory = []
    
    print("Добро пожаловать в текстовый квест!")
    
    while health > 0:
        show_status(health, turns, money, inventory)
        show_menu()
        
        choice = input("\nТвой выбор: ").lower().strip()
        
        if choice == "выход":
            print("Ты завершил игру. До встречи!")
            break
            
        # Обрабатываем ход
        health, money, inventory = process_turn(choice, health, money, inventory)
        turns += 1
        
        # Проверка на проигрыш
        if health <= 0:
            print("\nТы потерял всё здоровье... Игра окончена.")
            break

# Запуск игры (если файл запускают напрямую)
if __name__ == "__main__":
    start_game()