data_list = [
    [1, 10, 34, 110, 400, 30, 20],
    [-5, -10, 55, 120, 30],
    [2, 67, 23, 78, 200],
]

def subtract_x(func): #function for subtraction x that returns the mean, maximum and minimum values, and sum
    def func_wrapper(a, x):
        #subtaction of x with a new result and applying it to func(a)
        return [(mean-x, min_val-x, max_val-x, sum_val-x) for mean, min_val, max_val, sum_val in func(a)]
    return func_wrapper

@subtract_x #Applying subtract_x function to filter function without changing the code
def filter(a):
    result = []
    for i in range(len(a)): # The loop runs as many times as there are items in the list
        small_list = []
        for j in range(len(a[i])):
            # At each operation of the cycle, it enters the nested lists of the Database list.
            # The loop runs as many times as there are elements in the list.
            number = a[i][j] # Each iteration of the loop places an element of the nested list into variable number
            if number >= 10 and number <= 100: # Checking if a number is in the range 10-100
                small_list.append(number)  # The .append command adds the number stored in the number variable to the small_list
        counter = (sum(small_list) / len(small_list), min(small_list), max(small_list), sum(small_list))
        # In the counter variable, the arithmetic mean of all the numbers in the small_list list is calculated,
        # finds out the minimum number of the list (min()), the maximum (max()), and the sum of all numbers (sum())
        result.append(tuple(counter)) # Add a tuple with the results to the result list

    return result

x = 10
for row in filter(data_list, x): #for getting each result in a new line
    print(row)
