# приветствие
print('Здравствуйте, вы долны вводить по одной маленькой букве, чтобы отгодать слово. Или угадать слово сразу. Введите #сдаться чтобы сдаться. И #help чтобы узнать правтла и команды.')

# создание списка со словами
sl = {'кот', 'котенок', 'лошадь', 'собака', 'осел', 'мышь'}      

 # переменные для сокрашения текста в коде
napom = 'Напоминаем вам нужно ввести одну маленькую букву русского алфавита, которую вы еще не вводили е = ё. Или угадать слово. Введите #сдаться чтобы сдаться. И #help чтобы узнать правила и команды.'
zanovo = 'Попрубуйте ввести заново.'

popit = 1                   # переменная для числа потраченых попыток
zero_index = 0              # переменная которая используется для сравнения как 0 и как индек для поиска буквы
ugad_sl = ''                # переменная которой будет присваиваться угадываемое слово(из звездочек и угаданных букв)
len_vibr_sl = len(vibr_sl)  # создание переменной равной длине выбраногго слова

# выбор слова
vibr_sl = sl.pop()

# вывод слова с буквами замененными на звездочки
for i in range(len_vibr_sl):
    print('*', end=(''))

# ввод числа попыток
chislo_popit = int(input('Введите число попыток.'))

# вход в основной цикл
for i in range(chislo_popit):
    
    # игрок вводит букву/слово
    vvod = input()
    
    # проверка, на то что введена одна русская буква
    if len(vvod) == 1 and ord(vvod) > (ord('а') - 1) and ord(vvod) < (ord('я') + 1):
        
        # проверка, на то что буква в слове
        if vvod in vibr_sl:
            
            # собирание слова с угаданными буквами
            for s in range(len_vibr_sl):
                
                # проверка, на то что индекс за пределами строки
                if zero_index > len_vibr_sl or zero_index == len_vibr_sl:
                    zero_index = len_vibr_sl -1
                else:
                    if vvod == vibr_sl[zero_index]:
                        tek_sim = vibr_sl[zero_index]
                    else:
                        tek_sim = '*'
                    ugad_sl += tek_sim
                    zero_index += 1

            # печать слова с угаданными буквами
            print(ugad_sl, end=('\n'))

            # обнуление индекса
            zero_index = 0

            # проверка на победу
            if ugad_sl == vibr_sl:
                print('Ура вы победили! Вам пондобилось', popit, 'попыток.')
                break                   

            # обнуление переменных
            ugad_sl = ''
            tek_sim = ''
        else:
            print(zanovo , napom)

    # проверка на попытку угадать слово
    elif len(vvod) == len_vibr_sl and '#' not in vvod:

        # проверка на победу 2
        if vvod == vibr_sl:
            print('Ура вы победили! Вам понадобилось', popit, 'попыток.')
            break
        else:
            print(zanovo, napom)

    # проверка на ввод #help
    elif '#help' in vvod:
        print(napom)

    # проверка на ввод #сдаться
    elif '#сдаться' in vvod:
        print('Увы вы проиграли(((')
        break
    else:
        print(zanovo, napom)

    # трата попытки
    popit += 1                  
