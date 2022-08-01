# План действий
# 1. Создать простейший калькулятор               Выполнено
# 2. Добавить поддержку отрицательных чисел       Выполнено
# 3. Добавить поддержку чисел больше 10           Выполнено
# 4. Задать приоритеты                            Выполнено
# 5. Добавить возможность использовать скобки     Выполнено
# 6. Добавить проверку введенных данных           Выполнено
# 7. Оформить в виде функции и тд                 Выполнено
# 8. Добавить случаи нескольких операторов        Выполнено
# 9. Добавить поддержку дробных чисел             Выполнено
# 10. Добавить поддержку комплексных чисел
# 11. Расширить кол-во операций до инженерных
# 12. Добавить проверку ввода нескольких 
# операторов подряд
# 13. Добавить поддержку округления               Выполнено
# 14. Сделать оконное приложение                  Выполнено (правда коряво)

# 1. Создаем простейший калькулятор
# 1.1 Словарь из возможных операций
dict_operations = {'-': lambda x, y: x - y, 
             '+': lambda x, y: x + y, 
             '*': lambda x, y: x * y, 
             '/': lambda x, y: x / y,
             '^': lambda x, y: x ** y,
             '%': lambda x, y: x % y,
             '&': lambda x, y: x // y}

# 1.2 Функция расчета факторила. В словарь не добавлял из-за того, чтобы не 
# импортировать его в самом начале программы, а только если он есть
def fact(x):
    from math import factorial
    return factorial(x)
# 2. Создание калькулятора

# 2.1. Проверка входных данных
def is_valid(calculation_string, n):
    
    # Если n (заданная точность) - не число, то False
    try:
        n = int(n)
    except ValueError:
        return False
    
    # 2.2 Форматирование исходной строки с выражением к нужно для дальнейших
    # преобразований
    
    # Если i не в списке разрешенных символов, если кол-во '(' не равно кол-ву
    # ')', если начинается с +/*^ или заканчивается на -+/*^, то False
    for i in calculation_string:
        if i not in '01234!56789-&%.+/)(* ' or calculation_string.count('(') != calculation_string.count(')') or calculation_string.strip()[-1] in '-+*&%^/' or calculation_string.strip()[0] in '+/%&*^':
            return False
    return True

# 2.3 Создание списка из преобразованной строки

# Убираем все пробелы, приводим к нужному виду. 
# И создаем список из всех входящих элементов.
def list_calculation_creatior(calculation_string):
    # Обрабатываем изначальную строку: 1) убираем все пробелы 2) заменяем ** на
    # ^ 3) заменяем )( на )*( - чтобы можно было умножать скобки без оператора
    # 4) заменяем *- на *-1* и /- на *-1/, для реализации умножения и деления
    # скобок
    calculation_string_replaced = calculation_string.strip().replace(' ', '').replace('**', '^').replace(')(', ')*(').replace('*-','*-1*').replace('/-', '*-1/').replace('+-', '-').replace('//', '&')
    list_of_calculation = []
    j = -1
    for i in range(len(calculation_string_replaced)):
        
        # Если i меньше j, то все эти элементы обработаны, поэтому скип
        if i < j:
            continue
        
        # если есть скобка, то добавляем ее в список
        if calculation_string_replaced[i] in ')(':
            list_of_calculation.append(calculation_string_replaced[i]) 
            
        # если i-ый элемент в '+-!*/^' и при этом сформированный список не
        # нулевой и его последний элемент не является знаком, то добавляем в
        # него найденный оператор
        elif calculation_string_replaced[i] in '+-!*&%/^' and len(list_of_calculation) > 0 and list_of_calculation[-1] not in '-+*%&/^(':
            list_of_calculation.append(calculation_string_replaced[i])
            
        # если же найден не оператор, а число:
        else:
            j = i + 1
            
            # будем обрабатывать строку до тех пор, пока не наткнемся на НЕ число
            while j < len(calculation_string_replaced):
                if not calculation_string_replaced[j].isdigit():
                    # если нашли НЕ число и если это точка, то продолжим - для
                    # реализации чисел с плавающей точкой. Если это не точка - 
                    # то выходим из цикла
                    if calculation_string_replaced[j] != '.':
                        break
                j += 1
            
            # после цикла у нас есть индекс начала числа и индекс его конца
            # добавляем срез исходной строки в наш список
            list_of_calculation.append(calculation_string_replaced[i:j])
            
    # Если список начинается с -, то добавим 0 в самое начало, чтобы изменить
    # выражение вида '- -1' на '0 - -1'.
    if list_of_calculation[0] == '-':
        list_of_calculation.insert(0, 0)
    return list_of_calculation

# 3. Сам калькулятор

# Присваиваем первый элемент значению общей суммы - реализуем "левую свертку"
# Если первое число - отрицательное, то делаем строку и дальше - int
def calculator(list_of_calculation):
    total = float(list_of_calculation[0])
    j = 0
    for i in range(len(list_of_calculation)):
        # Скипаем уже обработанные элементы списка.
        if i <= j:
            continue
        # Если следующий элемент есть в ключах, то это значит, что это - операция. 
        # Находим эту операцию в ключах и вычисляем значение i + 1 элемента и
        # total в соответствии с этой операцией
        if list_of_calculation[i] in dict_operations:
            # Если i + 1 элемент - знак минуса, то мы смотрим на элемент i + 2 и 
            # создаем отрицательное число из строки от i + 1 до i + 3 (не включительно)
            total = dict_operations[list_of_calculation[i]](
                total, float(list_of_calculation[i + 1]))
            # Запоминаем, где заканчивается наше число
            j = i + 1
        elif list_of_calculation[i] == '!':
            total += fact(int(list_of_calculation[i-1]))
            j = i + 1
    return total

# 3.1 Задание приоритетов для операций

# Приоритеты для / и *. Перебираем циклом список до тех пор, пока в нем есть
# / или * в виде функции
def priority_operations(list_of_calculation):
    while '*' in list_of_calculation or '/' in list_of_calculation or '^' in list_of_calculation or '!' in list_of_calculation or '%' in list_of_calculation or '&' in list_of_calculation:
        if '!' in list_of_calculation:
            
            # Если есть !, ищем его индекс
            a = list_of_calculation.index('!')
            
            # Вызываем простейший калькулятор от ! и двух соседних элементов
            b = fact(int(list_of_calculation[a - 1]))
            
            # удаляем ! и 2 соседних элемента, возвращая в список результат
            del list_of_calculation[a - 1: a + 1]
            list_of_calculation.insert(a - 1, b)    
            
        if '^' in list_of_calculation:
            
            # Если есть ^, ищем его индекс
            a = list_of_calculation.index('^')
            
            # Вызываем простейший калькулятор от ^ и двух соседних элементов
            b = calculator([list_of_calculation[a - 1],
                           list_of_calculation[a], list_of_calculation[a + 1]])
            
            # удаляем ^ и 2 соседних элемента, возвращая в список результат
            del list_of_calculation[a - 1: a + 2]
            list_of_calculation.insert(a - 1, b)
        if '/' in list_of_calculation:
            
            # Если есть /, ищем его индекс
            a = list_of_calculation.index('/')
            
            # Вызываем простейший калькулятор от / и двух соседних элементов
            b = calculator([list_of_calculation[a - 1],
                           list_of_calculation[a], list_of_calculation[a + 1]])
            
            # удаляем / и 2 соседних элемента, возвращая в список результат
            del list_of_calculation[a - 1: a + 2]
            list_of_calculation.insert(a - 1, b)
            
        if '&' in list_of_calculation:
            
            # Если есть &, ищем его индекс
            a = list_of_calculation.index('&')
            
            # Вызываем простейший калькулятор от & и двух соседних элементов
            b = calculator([list_of_calculation[a - 1],
                           list_of_calculation[a], list_of_calculation[a + 1]])
            
            # удаляем & и 2 соседних элемента, возвращая в список результат
            del list_of_calculation[a - 1: a + 2]
            list_of_calculation.insert(a - 1, b)
            
        if '*' in list_of_calculation:
            
            # Если есть *, ищем его индекс
            a = list_of_calculation.index('*')
            
            # Вызываем простейший калькулятор от * и двух соседних элементов
            b = calculator([list_of_calculation[a - 1],
                           list_of_calculation[a], list_of_calculation[a + 1]])
            
            # удаляем * и 2 соседних элемента, возвращая в список результат
            del list_of_calculation[a - 1: a + 2]
            list_of_calculation.insert(a - 1, b)
            
        if '%' in list_of_calculation:
            
            # Если есть %, ищем его индекс
            a = list_of_calculation.index('%')
            
            # Вызываем простейший калькулятор от % и двух соседних элементов
            b = calculator([list_of_calculation[a - 1],
                           list_of_calculation[a], list_of_calculation[a + 1]])
            
            # удаляем % и 2 соседних элемента, возвращая в список результат
            del list_of_calculation[a - 1: a + 2]
            list_of_calculation.insert(a - 1, b)

    return calculator(list_of_calculation)

# 3.2 Задание приоритетов для скобок

# Функция для задачи приоритетов скобкам.
def priority_brackets(list_of_calculation):
    z = 0
    new_list = []
    # Цикл выполняется до тех пор, пока в списке есть скобки
    while '(' in list_of_calculation or ')' in list_of_calculation:
        # для нахождения "внутренних" скобок ищем последнюю '(' перед первой ')'
        # и запоминаем ее индекс
        if list_of_calculation[z] == '(':
            a = z
        # как только находим первое вхождение ')', то запоминаем индекс.
        # индекс последнего вхождения '(' уже есть. 
        # после этого вызываем priority_operations для подсчета содержимого
        # в скобках, удаляем скобки с содержимым и вставляем вместо результат
        # в конце возвращаемся в начало строки на z = 0 и повторяем до тех пор
        # пока в списке есть скобки
        if list_of_calculation[z] == ')':
            b = z 
            new_list = list_of_calculation[a + 1: b]
            if len(new_list) == 2:
                new_list.insert(0, 0)
            x = priority_operations(new_list)
            del list_of_calculation[a: b + 1]
            list_of_calculation.insert(a, x)
            z = -1
        z += 1
    return list_of_calculation

# В итоге: вернется список, в котором будут выполнены сначала все операции со
# знаком ^, затем со знаком *, затем со знаком /, а затем вызывается простейший 
# калькулятор для оставшихся выражений. Если на входе не будет операций - то 
# калькулятор вернет исходных список

# 4. Непосредственно основаная функция

# Основная фукция
def main(calculation_string, n):
    # Валидация входных данных
    if is_valid(calculation_string, n):
        
        # Создание листа из входной строки
        list_of_calculation = list_calculation_creatior(calculation_string)
        
        # Расчет ответа
        a = priority_operations(priority_brackets(list_of_calculation))
        
        # Вывод ответа с заданной точностью
        return round(a, int(n))
    else:
        return 'Введены недопустимые символы'

# 4.1 Проверка на импорт

# Если импортировать - это не выполняется
if __name__ == '__main__':
    
    # Исходная строка с выражением. 
    calculation_string = input() 
    
    # Заданная точность
    n = input()
    
    print(main(calculation_string, n))

