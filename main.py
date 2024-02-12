""""
I can make documentation on english, but такой задачи в ТЗ не стояло.

Эту программу честно делал руками сутки. Наверное, (хвастовства ради) добавлю еще ссылку на
версию приложения, сделанную функционально, которую ChatGPT мне выплюнул, когда я скормил ему ТЗ.

Небольшой перечень функционала, который, по-хорошему, должен быть реализован, но в силу
отсутствия указаний в ТЗ и в целях экономии времени (уже пилю тестовое задание сутки, что,
с точки зрения тайм-менеджмента, непозволительная роскошь), отложен в долгий ящик:
    1. Возможность удаления записей.
        В свою очередь тянет за собой ряд проблем вроде обработки ключей удаленных записей в других
        интерфейсах, если мы хотим уникальные ID или динамическое присвоение ключей при
        формировании словаря и сортировка по ключу при записи для сохранения порядка.
        Все решаемо, но время(
    2. Возможность удаления/редактирования текущей записи из интерфейса просмотра.
    3. В интерфейсах, вносящих изменения (редактирование, добавлеие), дополнительное подтверждение
        вносимых изменений (y/n) и возможность выхода в главное меню без внесения оных.
    4. Возможность смены языка во время работы приложения.
    5. В интерфйесе просмотра возможность перейти к записи по номеру, без пролистывания всех.
    6. Добавление/изменение записей в текстовым файле более тонкими методами, чем полное
    переписывание.
"""
from typing import Union
from guide import Guide

is_ru: bool = False
"""
На эту переменную завязан язык интерфейса. С точки зрения open/closed from SOLID не очень
хорошо, но решаемо. Да и кому придет в голову добавлять к тестовому заданию дополнительные 
языки?
"""


class Interface:
    """Папа всех интерфейсов."""

    def __init__(self) -> None:
        """"
        Догадываюсь, что реализация работы приложения через переопределения параметра "self"
        и запуска вложенных функций не самая лучшая идея, но у меня нет опытного наставника,
        который бил бы за такое по рукам :-( (не у кого спросить насколько это плохо)
        На мой неискушенный взгляд, при допускаемой Пайтоном глубине рекурсии в 1000, вложенность
        функций глубиною 5 без передачи внутрь больших объемов данных, много памяти не тратит.

        Про классовые и абстрактные методы слышал, но уже решил делать так.

        """
        self.lang_choise()
        self = MainInterface()

    def lang_choise(self) -> None:
        """При запуске приложения выбираем язык интерфейса."""
        global is_ru
        while True:
            choose: str = input('choose language/выберите язык(en/ru):').lower()
            if choose in ['en', 'ан']:
                is_ru = False
                break
            elif choose in ['ru', 'ру']:
                is_ru = True
                break
            else:
                print('unknown command/неизвестная команда')
                continue
        print(['english language chosen', 'выбран русский язык'][is_ru])

    def query_process(self, query: 'str') -> None:
        """
        Родительская обработка запросов, которая включается, если специализированный интерфейс
        не понял, что от него хотят.
        """
        if query in ('exit', 'выход'):
            exit()
        elif query in ('help', 'помощь'):
            self.help()
        else:
            print(['unknown command', 'неизвестная команда'][is_ru])

    def help(self) -> None:
        """"Часть подсказки help которая повторяется в разных интерфейсах. Следуем принципу DRY."""
        print(*[['commands list:\n', 'exit - quit program\n', 'help - commands list'],
                ['список команд:\n', 'выход - завершить программу\n', 'помощь - список команд']]
        [is_ru], sep='')


class MainInterface(Interface):
    """Основной класс в котором крутим приложение."""

    def __init__(self):
        """Запускаем крутилку при инициализации."""
        self.main_int()

    def main_int(self) -> None:
        """Крутилка. Когда спец интерфейсы отрабатывают - возвращаемся сюда."""
        while True:
            print([f'Here is a guide. Number of records:',
                   f'Перед вами справочник. Количество записей:'][is_ru], len(test_guide.notes))
            query: str = input([f'Enter command (help - commands list):',
                                f'Введите команду(помощь - список команд): '][is_ru]).lower()
            self.query_process(query)

    def query_process(self, query):
        """Направо пойдешь..."""
        if query in ('read', 'читать'):
            self = ReadInterface()
        elif query in ('add', 'добавить'):
            self = AddInterface()
        elif query in ('edit', 'изменить'):
            self = EditInterface()
        elif query in ('find', 'поиск'):
            self = FindInterface()
        else:
            super().query_process(query)

    def help(self) -> None:
        """"Самая большая хелпушка в программе."""
        super().help()
        print(*[['add - add note'], ['добавить - добавить запись']][is_ru])
        print(*[['edit - edit note'], ['изменить - редактировать запись']][is_ru])
        print(*[['read - open guide'], ['читать - открыть справочник']][is_ru])
        print(*[['find - find data'], ['поиск - искать данные']][is_ru])


class ReadInterface(Interface):
    """"
    Если я правильно понял формулировку 'Вывод постранично записей из справочника на экран'
    В общем, по одной их выводит.
    """

    def __init__(self):
        self.read_guide()

    def read_guide(self) -> None:
        """
        Во время работы программы данные хранятся в словаре формата ключ-айдишка : вложенный
        словарь. Выводим по одной записи.
        """
        now_page: int = 1
        flag = True
        while flag:
            print([f'Note N: ', f'Запись №: '][is_ru], now_page, '\n',
                  [f'lastname: ', f'фамилия: '][is_ru], test_guide.notes[now_page]['lastname'], '\n',
                  [f'name: ', f'имя: '][is_ru], test_guide.notes[now_page]['name'], '\n',
                  [f'middlename: ', f'отчество: '][is_ru], test_guide.notes[now_page]['middlename'], '\n',
                  [f'organization: ', f'организация: '][is_ru], test_guide.notes[now_page]['organization'], '\n',
                  [f'work_number: ', f'рабочий телефон: '][is_ru], test_guide.notes[now_page]['work_number'], '\n',
                  [f'privat_number: ', f'личный телефон: '][is_ru], test_guide.notes[now_page]['privat_number'],
                  '\n')
            now_page, flag = self.query_process(now_page, flag)

    def query_process(self, now_page, flag) -> Union[int, None]:
        """Крутим страницы. Внизу реализовано замыкание ряда в круг. Работает стабильно только
        при сплошной нумерации айдишек (в данной сборке это так)."""
        while True:
            query: str = input([f'Enter command (n - next, b - previous, help - commands list): ',
                                f'Введите команду(с - следующая, ч - предыдущая, помощь - список команд): '][
                                   is_ru]).lower()
            if query in ['n', 'с']:
                now_page += 1
                break
            elif query in ['b', 'ч']:
                now_page -= 1
                break
            elif query in ['back', 'назад']:
                flag = False
                break
            else:
                super().query_process(query)
        now_page: int = abs(now_page) % len(test_guide.notes)
        now_page: int = len(test_guide.notes) if now_page == 0 else now_page
        return now_page, flag

    def help(self) -> None:
        "Хэлпушка."
        super().help()
        print(*[['back - main menu\n'], ['назад - главное меню\n']][is_ru])


class AddInterface(Interface):
    """Интерфейс добавления записей."""

    def __init__(self):
        """Как обычно"""
        self.add_note()

    def add_note(self):
        """
        Форимируем список значений и отправляем в метод справочника, который применит их в словарь.
        """
        notes_list = []
        notes_list.append(input([f'Enter lastname: ', f'Введите фамилию: '][is_ru]))
        notes_list.append(input([f'Enter name: ', f'Введите имя: '][is_ru]))
        notes_list.append(input([f'Enter middlename: ', f'Введите отчество: '][is_ru]))
        notes_list.append(input([f'Enter organization: ', f'Введите организацию: '][is_ru]))
        notes_list.append(input([f'Enter work_number: ', f'Введите рабочий телефон: '][is_ru]))
        notes_list.append(input([f'Enter privat_number: ', f'Введите личный телефон: '][is_ru]))
        test_guide.add_note(notes_list)


class EditInterface(Interface):
    """Интерфейс изменения записей."""

    def __init__(self):
        """Ага."""
        self.query_process()

    def query_process(self) -> None:
        """
        Просим ввести номер записи для изменения. Так как превращаем в инт (да и чтобы продемонстрировать знания)
        ловим исключения ВалуеЕрор.
        """
        while True:
            query: str = input(['enter the number of the entry to be changed: ',
                                'введите номер изменяемой записи: '][is_ru])
            try:
                if int(query) in test_guide.notes:
                    print([f'the entry N {query} will be changed',
                           f'будет изменена запись № {query}'][is_ru])
                    break
                else:
                    print([f'no entry N {query}',
                           f'нет записи № {query}'][is_ru])
            except ValueError:
                print(['enter the number',
                       'ну, число же надо'][is_ru])

        self.edit_note(int(query))

    def edit_note(self, query: int) -> None:
        """
        Вводим изменяемое поле и новое значение и засылаем методу справочника со всеми нужными ему данными.
        Наверное, можно уменьшить количество передаваемой информации, да и исходя из сингл-респонсибилити разбить на 2
        функции, но в голову мне это пришло только при составлении документации, а тратить еще сутки на переписывание
        и тестирование - страшно.
        """
        counter = 0
        for field, val in test_guide.notes[query].items():
            counter += 1
            print(str(counter) + '.', field, val)

        fields_list = ['lastname', 'name', 'middlename', 'organization', 'work_number', 'privat_number']

        while True:
            sub_query: str = input(['enter the number of the field to be changed: ',
                                    'введите номер изменяемого поля: '][is_ru])
            try:
                if int(sub_query) in range(1, len(test_guide.notes[query]) + 1):
                    print([f'the field {fields_list[int(sub_query) - 1]} will be changed',
                           f'будет изменено поле {fields_list[int(sub_query) - 1]}'][is_ru])
                    new_val: str = input(['enter new value: ',
                                          'введите новое значение: '][is_ru])
                    test_guide.edit_note(int(query), int(sub_query) - 1, fields_list, new_val)
                    print(['changed', 'изменено'][is_ru])
                    break
                else:
                    print([f'no field {sub_query}',
                           f'нет поля № {sub_query}'][is_ru])
            except ValueError:
                print(['enter the number',
                       'ну, число же надо'][is_ru])


class FindInterface(Interface):
    """Поиск."""
    def __init__(self):
        """Пыщ!"""
        self.query_process()

    def query_process(self) -> None:
        """
        Просим ввести номера полей для поиска, перехватываем исключения. Отдельно ловим пустой ввод, так как он
        пролезает через трай.
        """
        counter = 0
        for field in test_guide.notes[1]:
            counter += 1
            print(str(counter) + '.', field)

        fields_list = ['lastname', 'name', 'middlename', 'organization', 'work_number', 'privat_number']

        while True:
            query: str = input(['enter the numbers of the fields for find(by space): ',
                                'введите номера полей для поиска (через пробел): '][is_ru])
            try:
                query: list = list(map(int, query.split()))
                if len(query) == 0:
                    print(['enter something', 'напечатай что-нибудь'][is_ru])
                    continue
                for number in query:
                    if number in range(1, len(test_guide.notes[1]) + 1):
                        continue
                    else:
                        print(['no field N', 'нет поля №'][is_ru], number)
                        break
                else:
                    self.search_query(query, fields_list)
                    break
            except ValueError:
                print(['enter the numbers by space',
                       'введите числа через пробел'][is_ru])

    def search_query(self, query: list, fields_list: list) -> None:
        """
        Ищем по заданным полям. Выводим построчно.
        """
        search_query = input(['enter find query: ', 'что ищем?: '][is_ru]).lower()
        answer = {}
        for i in query:
            for n, j in test_guide.notes.items():
                if search_query in j[fields_list[i - 1]].lower():
                    answer[n] = j

        if len(answer) > 0:
            for i in sorted(answer):
                print(f'{i}.', *answer[i].values())
        else:
            print(['no such records', 'нет подходящих записей'][is_ru])


test_guide: Guide = Guide()
"""Инициализируем словарь."""
test = Interface()
"""Зпускаем процесс."""

