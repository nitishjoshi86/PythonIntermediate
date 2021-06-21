""" with open('notes.txt','w') as file:
    file.write('something done thing')

 """

class managefile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exc: ', exc_type, exc_value)
        print('exit')

with managefile('notes.txt') as file:
    print('do some stuff')
    file.write('some to do.......bla bla....')
print('continue')