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
                   f'Перед вами справочник. Количество записей:'][is_ru], test_guide.length)
            query: str = input([f'Enter command (help - commands list):',
                                f'Введите команду(помощь - список команд): '][is_ru]).lower()
            self.query_process(query)

    def query_process(self, query):
        if query in ('read', 'читать'):
            self = ReadInterface()
        elif query in ('add', 'добавить'):
            self = AddInterface()
        else:
            super().query_process(query)

    def help(self) -> None:
        super().help()
        print(*[['read - open guide'], ['читать - открыть справочник']][is_ru])
        print(*[['add - add note'], ['добавить - добавить запись']][is_ru])


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
        now_page: int = abs(now_page) % test_guide.length
        now_page: int = test_guide.length if now_page == 0 else now_page
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


test_guide: Guide = Guide()
test = Interface()
