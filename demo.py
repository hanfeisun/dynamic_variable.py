from dynamic import DynamicVariable

v = DynamicVariable("init")
def p():
    print(v.value)
p()
v.withValue("changed", p)
p()    

        
