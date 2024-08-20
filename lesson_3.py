user_select=int(input(print('Введи номер домашнього завдання:\n1. Калькулятор\n2. Дії зі списками')))
match user_select:
    case 1:
        number1 = int(input(print('Обрано калькулятор. Введи перше число:')))
        calculator_select = int(input(print('Обери дію, яку потрібно виконати:\n1. Додати\n2. Відняти\n3. Помножити\n4. Поділити')))
        number2 = int(input(print('Введи друге число:')))
        match calculator_select:
            case 1:
                result = number1 + number2
                print(result)
            case 2:
                result = number1 - number2
                print(result)
            case 3:
                result = number1 * number2
                print(result)
            case 4:
                result = number1 / number2
                print(result)
            case _:
                print('Такої дії не було в списку, будь уважніше!')
    case 2:
        lst = [12,1.2,'lst', 999, 1]
        list_select = int(input(print('Маємо такий список:', lst, 'Що ми з ним зробимо?:\n1. Преміщення останнього елементу на початок\n2. Розділення списку на два списка')))
        match list_select:
            case 1:
                lst.insert(0, lst[-1])
                lst.pop(-1)
                print('Новий список:', lst)
            case 2:
                half = type(len(lst)/2)
                if half == int:
                    lst1 = lst[:len(lst)//2]
                    lst2 = lst[len(lst)//2:]
                    print(lst1, lst2)
                else:
                    lst1 = lst[:len(lst) // 2+1]
                    lst2 = lst[len(lst) // 2+1:]
                    print(lst1, lst2)
            case _:
                print('Не було там такого числа! Будь уважніше!')
    case _:
        print('Така опція відсутня, будь уважніше!')









