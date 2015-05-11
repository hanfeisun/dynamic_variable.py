# By Hanfei Sun

class DynamicVariable:
    def __init__(self,init):
        self.value = init
    def withValue(self,new_val, f):
        old = self.value
        self.value = new_val
        try:
            f()
        finally:
            self.value = old

        

