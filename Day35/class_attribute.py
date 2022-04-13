class Smith:
    surname = 'test'
    profession = 'IT'

    def __init__(self, name, profession=None):
        self.name = name
        self.profession = profession


a = Smith('Soumya')
print(a.name)
print(a.profession)
