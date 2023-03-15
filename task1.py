### Task 1


n = "vienas du trys"
a = "vn "
b = "ayds"

# n = "keturiolika"
# a = "ktur"
# b = "ila"

def counter(n,a,b):
    num1 = 0
    num2 = 0
    for i in a: # Using the loop, we count how many elements are in the string a
        if i in n: #Checking for characters in string n
            num1+=1
    for i in b: # Using the loop, we count how many elements are in the string b
        if i in n: #Checking for characters in string n
            num2+=1

    return 1*num1 + -1*num2 # We calculate the result
counter(n,a,b)