class ErrorWord(Exception):
    def __init__(self, *args: object):
        self.message = 'Ha kalit soz topildi !'
        super().__init__(self.message, *args)
