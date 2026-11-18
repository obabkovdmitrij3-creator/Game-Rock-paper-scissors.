import random
def rock_paper_scissors():
    choices = ["камень", "ножницы", "бумага"]
    player_score = 0
    computer_score = 0

    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    print("Для выхода введите 'выход'")

    while True:
        player_choice = input("\nВаш выбор (камень/ножницы/бумага):").lower()

        if player_choice == 'выход':
          break 

        if player_choice not in choices:
           print("Неверный выбор! Попробуйте снова.")
           continue

        computer_choice = random.choice(choices)

        print(f"Вы выбрали: {player_choice}")
        print(f"Компьютер выбрал: {computer_choice}")
        
        if player_choice == computer_choice:
           print("ничья!")

        elif (player_choice == 'камень' and computer_choice == 'ножницы') or\
             (player_choice == 'ножницы' and computer_choice == 'бумага') or\
             (player_choice == 'бумага' and computer_choice == 'камень'):
           print("Вы выиграли!")
           player_score += 1
        else:
           print("Компьютер выиграл!")
           computer_score += 1

        print(f"Счёт - Вы: {player_score}, Компьютер: {computer_score}")
        if player_score > computer_score:
           
           print("Поздравляем! Вы выиграли общий зачёт!")
        elif computer_score > player_score:
           print("Компьютер выиграл общий зачёт!")
        else:
           print("Общая ничья!")

rock_paper_scissors()
        
