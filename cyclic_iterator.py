import typing
import time


class CyclicIterator:
    def __init__(self, container):
        self.container = container
        self.index = 0
    
    def __iter__(self):
        return self
  
    def __next__(self):
        if self.index == len(self.container):
            self.index = 0
        next_element = self.container[self.index]
        self.index += 1
        return next_element


cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)
    time.sleep(1)


# Ожидаемый вывод
# 0
# 1
# 2
# 0
# 1
# 2
# 0
# 1
# 2
# .... 