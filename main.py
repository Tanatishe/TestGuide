from directory import Directory
class Interface:
    is_ru = False

    def __init__(self):
        self.lang_choise()
        self.main_int()

    def lang_choise(self):
        choose = input('choose language/выберите язык(eng/ru):')
        is_ok = True
        if choose in ['eng', 'анг']:
            self.is_ru = False
        elif choose in ['ru', 'рус']:
            self.is_ru = True
        else:
            print('unknown command/неизвестная команда')
            self.lang_choise()
            return
        print(['english language chosen', 'выбран русский язык'][self.is_ru])
        self.main_int()

    def main_int(self):
        pass

    def help_int(self):
        pass


test = Interface()
