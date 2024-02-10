from typing import Union
from guide import Guide


class Interface:
    is_ru: bool = False

    def __init__(self) -> None:
        pass

    def lang_choise(self) -> None:
        while True:
            choose: str = input('choose language/выберите язык(eng/ru):').lower()
            if choose in ['eng', 'анг']:
                self.is_ru: bool = False
                break
            elif choose in ['ru', 'рус']:
                self.is_ru: bool = True
                break
            else:
                print('unknown command/неизвестная команда')
                continue
        print(['english language chosen', 'выбран русский язык'][self.is_ru])


class MainInterface(Interface):
    def __init__(self):
        pass



    def main_int(self) -> None:
        while True:
            print([f'Here is a guide. Number of records: ',
                   f'Перед вами справочник. Количество записей: '][self.is_ru], test_guide.length)
            query: str = input([f'Enter command (help for commands list): ',
                                f'Введите команду(помощь - список команд): '][self.is_ru]).lower()
            self.query_process_main(query)

    def query_process_main(self, query):
        if query in ('read', 'читать'):
            self.read_guide()
        else:
            self.query_process(query)

    def query_process(self, query: 'str') -> None:
        if query in ('exit', 'выход'):
            exit()
        elif query in ('help', 'помощь'):
            self.help_int()
        else:
            print(['unknown command', 'неизвестная команда'][self.is_ru])

    def help_int(self) -> None:
        print(*[['commands list:\n', 'exit - quit program\n', 'read - open guide\n'],
                ['список команд:\n', 'выход - завершить программу\n', 'читать - открыть справочник\n']]
        [self.is_ru])

    def read_guide(self) -> None:
        now_page: int = 1
        while True:
            print([f'Note N: ', f'Запись №: '][self.is_ru], now_page, '\n',
                  [f'Lastname: ', f'Фамилия: '][self.is_ru], test_guide.notes[now_page]['lastname'], '\n', )
            now_page: int = self.query_process_read(now_page)

    def query_process_read(self, now_page) -> Union[int, None]:
        while True:
            query: str = input([f'Enter command (n - next, b - previous): ',
                                f'Введите команду(с - следующая, ч - предыдущая): '][self.is_ru]).lower()
            if query in ['n', 'с']:
                now_page += 1
                break
            elif query in ['b', 'ч']:
                now_page -= 1
                break
            else:
                self.query_process(query)
        now_page: int = abs(now_page) % test_guide.length
        now_page: int = test_guide.length if now_page == 0 else now_page
        return now_page


test_guide: Guide = Guide()
test = Interface()
