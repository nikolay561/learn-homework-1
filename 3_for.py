"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school = [{'school_class': '4a', 'scores': [3, 4, 5, 4, 2]},
              {'school_class': '5b', 'scores': [3, 5, 5, 5, 3]},
              {'school_class': '7a', 'scores': [2, 4, 4, 4, 4]},
              ]
    
    scores_sum_4a = 0
    scores_sum_5b = 0
    scores_sum_7a = 0

    for i in school[0]['scores']:
        scores_sum_4a += i

    for i in school[1]['scores']:
        scores_sum_5b += i

    for i in school[2]['scores']:
        scores_sum_7a += i

    all_scores = scores_sum_4a + scores_sum_5b + scores_sum_7a

    print(f'Средний балл по всей школе - {all_scores / (len(school[0]["scores"]) + len(school[1]["scores"]) + len(school[1]["scores"]))}')
    print(f'Средний балл в классе 4а - {scores_sum_4a / len(school[0]["scores"])}')
    print(f'Средний балл в классе 5b - {scores_sum_5b / len(school[1]["scores"])}')
    print(f'Средний балл в классе 7а - {scores_sum_7a / len(school[2]["scores"])}')

    
if __name__ == "__main__":
    main()
