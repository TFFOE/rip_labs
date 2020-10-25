from lab_python_fp.gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.used = set()
        self.index = 0
        self.items = items if type(items) is list else [i for i in items]
        self.ignore_case = True if len(kwargs) > 0 and kwargs['ignore_case'] == True else False

    def __next__(self):
        while True:
            if (self.index >= len(self.items)):
                raise StopIteration
            else:
                current = self.items[self.index]
                self.index += 1
                if (self.ignore_case and current not in self.used or not self.ignore_case and str(current).lower() not in self.used):
                    self.used.add(
                        current if self.ignore_case else str(current).lower())
                    return current

    def __iter__(self):
        return self
