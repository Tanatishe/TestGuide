from typing import Union
from guide import Guide

is_ru: bool = False


class Interface:

    def __init__(self) -> None:
        self.lang_choise()
        self = MainInterface()

    def lang_choise(self) -> None:
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
        if query in ('exit', 'выход'):
            exit()
        elif query in ('help', 'помощь'):
            self.help()
        else:
            print(['unknown command', 'неизвестная команда'][is_ru])

    def help(self) -> None:
        print(*[['commands list:\n', 'exit - quit program\n', 'help - commands list'],
                ['список команд:\n', 'выход - завершить программу\n', 'помощь - список команд']]
        [is_ru], sep='')


class MainInterface(Interface):
    def __init__(self):
        self.main_int()

    def main_int(self) -> None:
        while True:
            print([f'Here is a guide. Number of records:',
                   f'Перед вами справочник. Количество записей:'][is_ru], len(test_guide.notes))
            query: str = input([f'Enter command (help - commands list):',
                                f'Введите команду(помощь - список команд): '][is_ru]).lower()
            self.query_process(query)

    def query_process(self, query):
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
        super().help()
        print(*[['add - add note'], ['добавить - добавить запись']][is_ru])
        print(*[['edit - edit note'], ['изменить - редактировать запись']][is_ru])
        print(*[['read - open guide'], ['читать - открыть справочник']][is_ru])
        print(*[['find - find data'], ['поиск - искать данные']][is_ru])


class ReadInterface(Interface):
    def __init__(self):
        self.read_guide()

    def read_guide(self) -> None:
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
        super().help()
        print(*[['back - main menu\n'], ['назад - главное меню\n']][is_ru])


class AddInterface(Interface):
    def __init__(self):
        self.add_note()

    def add_note(self):
        notes_list = []
        notes_list.append(input([f'Enter lastname: ', f'Введите фамилию: '][is_ru]))
        notes_list.append(input([f'Enter name: ', f'Введите имя: '][is_ru]))
        notes_list.append(input([f'Enter middlename: ', f'Введите отчество: '][is_ru]))
        notes_list.append(input([f'Enter organization: ', f'Введите организацию: '][is_ru]))
        notes_list.append(input([f'Enter work_number: ', f'Введите рабочий телефон: '][is_ru]))
        notes_list.append(input([f'Enter privat_number: ', f'Введите личный телефон: '][is_ru]))
        test_guide.add_note(notes_list)


class EditInterface(Interface):

    def __init__(self):
        self.query_process()

    def query_process(self) -> None:
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
    def __init__(self):
        self.query_process()

    def query_process(self) -> None:
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
                for number in query:
                    if number in range(1, len(test_guide.notes[query]) + 1):
                        continue
                    else:
                        print(['no field N', 'нет поля №'][is_ru], {number})
                        break
            except ValueError:
                print(['enter the numbers by space',
                       'введите числа через пробел'][is_ru])


test_guide: Guide = Guide()
test = Interface()
