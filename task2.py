data_list = [
    [1, 10, 34, 110, 400, 30, 20],
    [-5, -10, 55, 120, 30],
    [2, 67, 23, 78, 200],
]

data_list = [
    [-1, 45, 23, 32, 999],
    [67, 99, 23],
    [23],
]

def filter(a):
    for i in range(len(a)):
        small_list = []
        for j in range(len(a[i])):
            number = a[i][j]
            if number >= 10 and number <= 100:
                small_list.append(number)
        result = (sum(small_list) / len(small_list),min(small_list),max(small_list),sum(small_list))
    return result

filter(data_list)

