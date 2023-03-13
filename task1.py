n = "vienas du trys"
a = "vn "
b = "ayds"

n = "keturiolika"
a = "ktur"
b = "ila"

def counter(n,a,b):
    num1 = 0
    num2 = 0
    for i in a:
        if i in a:
            num1+=1
    for i in b:
        if i in b:
            num2+=1
    return 1*num1 + -1*num2

counter(n,a,b)