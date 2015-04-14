import string
nums = string.digits
def check(name):
    if type(name) is not str:
        return False
    else:
        for i in name:
            if i not in nums:
                return False
            return True
            
n = 3
lst = []
while n > 0:
    name = input('please enter your name:')
    new_name = name.capitalize()
    lst.append(new_name)
    n -= 1
print (lst)

    
