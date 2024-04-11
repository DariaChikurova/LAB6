def zadanie1():
    capitals = { "Австрия": "Вена", "Чехия": "Прага", "Германия": "Берлин",  "Италия": "Рим",  "Япония": "Токио" }
    print(capitals)
    guess = input("Введите страну: ")
    if guess in capitals:
        print(capitals[guess])
    else:
        print("Такой страны нет в списке")
    for country, capitals in sorted(capitals.items()):
        print(country, capitals)

def zadanie2():
    letter_scores = {
        1: ['а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'],
        2: ['д', 'к', 'л', 'м', 'п', 'у'],
        3: ['б', 'г', 'ж', 'з', 'ч', 'ш', 'щ', 'э', 'ю', 'я'],
        4: ['й', 'ы', 'ь'],
        5: ['ё', 'ъ'],
        8: ['ш'],
        10: ['ф', 'ц']
    }
    total_points = 0
    while True:
        user_input = input("Введите слово (для выхода введите 'exit'): ")
        if user_input.lower() == "exit":
            break
        points = 0
        #временная переменная temp используется для сохранения начального значения total_points перед его изменением
        #это позволяет сравнить новое значение total_points с начальным значением
        #если total_points не изменилось, это указывает на ошибку
        temp = total_points
        for letter in user_input:
            for score, letters in letter_scores.items():
                if letter.lower() in letters:
                    points += score
                    break
        total_points += points
        if(total_points == temp):
            print("error")
        else:
            print("Количество очков:", total_points)




while True:
    print('1. Страны')
    print('2. Эрудит')
    print('3. Выход')
    a = int(input('Выберите действие: '))
    if a == 1:
        zadanie1()
    elif a == 2:
        zadanie2()
    elif a == 3:
        break
    else:
        print('Неверное действие')