# Реализовать, с учетом ооп подхода, приложение.
# Для проведения исследований с генеалогическим древом.
# Идея: описать некоторое количество компонент, например:
# модель человека
# компонента хранения связей и отношений между людьми: родитель, ребёнок - классика, но можно подумать и про отношение, брат, свекровь, 
# сестра и т. д.
# компонент для проведения исследований
# дополнительные компоненты, например отвечающие за вывод данных в консоль, загрузку и сохранения в файл, получение\построение отдельных 
# моделей человека
# Под “проведением исследования” можно понимать получение всех детей выбранного человека.
class generation:
    def __init__(self, x, y, z):
        self.checking(x)
        self.__fio = x
        self.checking_2(y)
        self.__year_of_birth = y
        self.checking_3(z)
        if "." in z:
            z = z.replace(".", "")
        self.__parents = z.split(",")


    @classmethod
    def checking(cls, name):
        name = name.split()
        if len(name) == 3:
            for i in name:
                if not(i.isalpha()):
                    print("ФИО записывается в таком формате: фамилия имя отчество, кириллицей пожалуйста!")
                    return
        else:
            print("ФИО записывается в таком формате: фамилия имя отчество, кириллицей пожалуйста! Нехватает данных!")
            return
    def checking_2(cls, year):
        year = year.split(".")
        for i in year:
            if not(i.isdigit()):
                print("Год рождения записывается в таком формате: дд.мм.гггг, числами пожалуйста!")
                return
        if not(int(year[0]) > 0 and int(year[0]) < 31):
            print("День рождения не может быть меньше ноля и больше 31")
            return
        if not(int(year[1]) > 0 and int(year[1]) <= 12):
            print("Месяц рождения не может быть меньше единицы и больше 12")
            return
        if not(int(year[2]) > 1850 and int(year[2]) <= 2022):
            print("Год рождения не может быть меньше 1850 и больше 2022")
            return
    @classmethod
    def checking_3(cls, name_old):
        if "." in name_old:
            name_old = name_old.replace(".", "")
        name_old = name_old.replace(",", "")
        name_old = name_old.split()
        if len(name_old) == 6 or len(name_old) == 4:
            for i in name_old:
                if not(i.isalpha() or i == "-"):
                    print("ФИО записывается в таком формате: фамилия имя отчество, фамилия имя отчество-кириллицей пожалуйста!")
                    return
        else:
            print("ФИО записывается в таком формате: фамилия имя отчество, фамилия имя отчество-кириллицей пожалуйста!")
            return
    @staticmethod
    def check_parent(list_object):
        list_child = []
        for i in list_object:
            for j in list_object:
                for k in j._generation__parents:
                    if k[0] == " ":
                        k = k.replace(" ", "", 1)
                    if i._generation__fio == k:
                        if hasattr(i, "_generation__children"):
                            prov = True
                            for l in i._generation__children:
                                if l == j._generation__fio:
                                    prov = False
                                    break
                            if prov:
                                list_child.append(j._generation__fio)
                        else:
                            list_child = []
                            qwe = j._generation__fio
                            list_child.append(qwe)
                            setattr(i, "_generation__children", list_child)

    @staticmethod
    def del_тon_existent(list_object):
        for i in list_object:
            list_child = []
            if hasattr(i, "_generation__children"):
                children = 0
                leni = len(i._generation__children)
                while children < leni:
                    list_child.append(i._generation__children[children])
                    children += 1
                couter = 0
                lenner = 0
                while lenner < len(list_child):
                    cout = 0
                    j = 0
                    while j < len(list_object):
                        if list_child[couter] == list_object[j]._generation__fio:
                            cout += 1
                        j += 1
                    if cout == 0:
                        i._generation__children.pop(couter)
                        if len(i._generation__children) == 0:
                            delattr(i, "_generation__children")
                    couter += 1
                    lenner += 1
            else: continue

Alexei = generation("Бобкин Алексей Ильич", "13.12.2022", "Бобкин Илья Викторович, Бобкина Надежда Александровна")
Anastaisha = generation("Мишкина Анастасия Александровна", "13.01.2002", "Мишкин Александр Витальевич, Мишкина Наталья Александровна")
Alex = generation("Мишкин Александр Витальевич", "13.01.1985", "Мишкин Анатолий Витальевич, Мишкина Тося Викторовна")
Galia = generation("Мишкина Галина Александровна", "23.08.2007", "Мишкин Александр Витальевич, Мишкина Наталья Александровна")
Natalia = generation("Мишкина Наталья Александровна", "27.08.1982", "Бобкин Илья Викторович, Бобкина Надежда Александровна")
lister = [Alexei, Anastaisha, Natalia, Galia, Alex]
generation.check_parent(lister)
# generation.del_тon_existent(lister)

def output_children(object):
    if hasattr(object, "_generation__children"):
        print(object._generation__children)
    else: print("Детей нету")

def greeting():
    print("Приветствуем вас в нашем приложении \"Генеологическое древо\"")
    print("Список возможностей нашего приложения")

def menu():
    print()
    print("1 - Показать список имеющихся людей")
    print("2 - Добавить новое лицо")
    print("3 - Удалить из списка")
    print("4 - Найти по фио")
    print("5 - выйти из приложения")
    x = input("Введите цифру: ")
    print()
    if int(x) < 1 and int(x) > 5:
        print("Можно ввести цифру не больше 5 и не меньше 1")
        return
    return int(x)

def show_list(lister):
    for i in lister:
        print(i._generation__fio)

def add():
    fio = input(("Введите фио: "))
    g_r = input("Введите год рождения: ")
    parent = input("Введите фио родителей, если кто-то неизвестен, введите прочерк: ")
    objecter = generation(fio, g_r, parent)
    lister.append(objecter)
    generation.check_parent(lister)
    generation.del_тon_existent(lister)
    print()
    show_list(lister)
    

def deleter(stroka):
    i = 0
    while i < len(lister):
        if stroka == lister[i]._generation__fio:
            lister.pop(i)
        i += 1
    generation.check_parent(lister)
    generation.del_тon_existent(lister)
    print()
    show_list(lister)

def search(stroka):
    for i in lister:
        if stroka in i._generation__fio:
            print(i._generation__fio)
            return i

greeting()
while True:
    x = menu()

    if x == 1:
        show_list(lister)

    elif x == 2:
        add()

    elif x == 3:
        stroka = input("Введите фио человека, которого надо удалить из древа: ")
        for i in lister:
            if stroka in i._generation__fio:
                deleter(i._generation__fio)

    elif x == 4:
        stroka = input("Введите фио человека, которого надо найти: ")
        cont = search(stroka)
        answer = input("Показать детей найденного человека?(1-да, 2-нет): ")
        if answer == "1":
            output_children(cont)

    elif x == 5:
        print("Досвидос!")
        break

