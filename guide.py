class Guide:
    def __init__(self):
        self.notes: dict = {
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
                'privat_number': '+13336666666'

            },
        }
        self.length: int = len(self.notes)
