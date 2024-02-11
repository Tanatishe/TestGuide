import os


class Guide:
    notes: dict = {}
    test_dict: dict = {
        1: {
            'lastname': 'Ivanov',
            'name': 'Ivan',
            'middlename': 'Ivanovich',
            'organization': 'Google',
            'work_number': '+12225555555',
            'privat_number': '+79527777777'

        },
        2: {
            'lastname': 'Smith',
            'name': 'John',
            'middlename': '',
            'organization': 'Amazon',
            'work_number': '+12225512355',
            'privat_number': '+133312686756'

        },
        3: {
            'lastname': 'Gilfoyle',
            'name': 'Bertram',
            'middlename': '',
            'organization': 'Pied Piper',
            'work_number': '+12221234567',
            'privat_number': '+10106668666'

        },
    }

    def __init__(self):
        self.notes: dict = self.open_dict()

    def open_dict(self):
        contacts = {}
        if os.path.isfile('text.txt'):
            with open('text.txt', 'r') as file:
                for line in file.readlines():
                    contact = line[1:].strip().split(', ')
                    contacts[int(line[0])] = {
                        'lastname': contact[1],
                        'name': contact[2],
                        'middlename': contact[3],
                        'organization': contact[4],
                        'work_number': contact[5],
                        'privat_number': contact[6]

                    }
        else:
            contacts = self.test_dict
        return contacts

    def add_note(self, notes_list):
        new_key: int = len(self.notes) + 1
        self.notes[new_key] = {'lastname': notes_list[0],
                               'name': notes_list[1],
                               'middlename': notes_list[2],
                               'organization': notes_list[3],
                               'work_number': notes_list[4],
                               'privat_number': notes_list[5]}
        self.save_dict()

    def save_dict(self):
        with open('text.txt', 'w') as file:
            for number, note in self.notes.items():
                line = ', '.join(note.values())
                line = str(number) + ', ' + line
                file.write(line + '\n')

    def edit_note(self, query: int, sub_query: int, fields_list: list, new_val: str) -> None:
        self.notes[query][fields_list[sub_query]] = new_val
        self.save_dict()
