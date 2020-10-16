def validate_input(func):
    def executor(a, b):
        print(".....")
        if b == 0:
            print("b can not be 0")
            return
        return func(a, b)
        
    return executor

@validate_input
def div(a, b):
    return int(a) / int(b)

print("Calling")
print(div(10,0))