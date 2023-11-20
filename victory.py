import random
humans = [1, 2, 3, 4, 5,6,7]
result = random.sample(humans, 5)
print(result) # [5, 1]

import random


def format_date(date_str):
    """ Функция для преобразования даты из формата 'dd.mm.yyyy' в текстовый формат. """
    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
              'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    day, month, year = date_str.split('.')
    return f"{int(day)} {months[int(month) - 1]} {year} года"


# Словарь известных людей и дат их рождения
people = {
    "Альберт Эйнштейн": "14.03.1879",
    "Исаак Ньютон": "04.01.1643",
    "Леонардо да Винчи": "15.04.1452",
    "Чарльз Дарвин": "12.02.1809",
    "Никола Тесла": "10.07.1856",
    "Галилео Галилей": "15.02.1564",
    "Мари Кюри": "07.11.1867",
    "Томас Эдисон": "11.02.1847",
    "Стивен Хокинг": "08.01.1942",
    "Михаил Ломоносов": "19.11.1711"
}


def start_quiz():
    correct = 0
    wrong = 0

    # Выбираем 5 случайных людей
    selected_people = random.sample(list(people.keys()), 5)

    for person in selected_people:
        # Задаем вопрос
        user_answer = input(f"Введите дату рождения {person} (в формате 'dd.mm.yyyy'): ")
        correct_answer = people[person]

        # Проверяем ответ
        if user_answer == correct_answer:
            print("Правильно!")
            correct += 1
        else:
            print(f"Неправильно. Правильный ответ: {format_date(correct_answer)}")
            wrong += 1

    # Выводим результаты
    print(f"\nПравильных ответов: {correct}, неправильных ответов: {wrong}")

    # Предлагаем начать заново
    if input("\nХотите начать снова? (да/нет): ").lower() == "да":
        start_quiz()


# Запускаем викторину
start_quiz()