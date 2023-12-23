class Errors(Exception):
    def __init__(self, *args: object):
        self.message = 'Ha biz error ni topdik !...'
        super().__init__(self.message, *args)