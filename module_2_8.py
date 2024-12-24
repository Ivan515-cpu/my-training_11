calls = 0 # Объявляем глобальную переменную calls для подсчета вызовов

def count_calls():
    global calls # выбираем значение глобальной переменной calls
    calls += 1 # Увеличиваем значение переменной на 1 и обновляем calls для подсчета вызовов других функций

def string_info(string): # Объявляем функецию string_info с переменной string (строка для анализа)
    count_calls() # вызываем функцию count_calls отслеживаем число вызовов string_info
    return len(string), string.upper(), string.lower() # len(string) - длинна строки,
    # string.upper() - перевод строки в верхний регистр, string.lower() - перевод строки в нижний регистр
    #  Все три результата возвращаются как один кортеж
def is_contains(string, list_to_search): # Проверяем, содержится ли строка string в списке строк list_to_searth
    count_calls() # выбираем строку
    string_lower = string.lower() # Переводим строку в нижний регистр (функция lower)
    list_lower = [item.lower() for item in list_to_search] # переводим список в нижний регистр
    return string_lower in list_lower # Непосредственная проверка наличия строки в списке

print(string_info('Наше дело правое! Победа будет за нами!')) # Примеры вызовов функций
print(string_info("Ехал грека через реку"))
print(string_info('God does not love America, God saves Russia!'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Пример ДА (True)
print(is_contains('Колесо', ['Топор', 'Домкрат', 'КолЕсо'])) # Пример ДА (True)
print(is_contains('Колесо', ['Мотор', 'Домкрат'])) # Пример НЕТ (False)

print(calls) # Вывод количества вызовов функций
