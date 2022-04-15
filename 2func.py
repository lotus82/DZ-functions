def inp_year(year):
    while year != '1799':
        print("Не верно")
        year = input('Ввведите год рождения А.С.Пушкина: ')
    return True

def inp_day(day):
    while day != '6':
        print("Не верно")
        day = input('В какой день июня родился Пушкин? ')
    return True

if inp_year(input('Ввведите год рождения А.С.Пушкина: ')):
    if inp_day(input('Ввведите день рождения Пушкина? ')):
        print('Верно')