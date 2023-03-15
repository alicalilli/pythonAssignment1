### Task 2

data_list = [
    [1, 10, 34, 110, 400, 30, 20],
    [-5, -10, 55, 120, 30],
    [2, 67, 23, 78, 200],
]

# data_list = [
#     [-1, 45, 23, 32, 999],
#     [67, 99, 23],
#     [23],
# ]

def filter(a):
    result = []
    for i in range(len(a)):  # The loop runs as many times as there are items in the list
        try:
            small_list = []
            for j in range(len(a[i])):
                # At each operation of the cycle, it enters the nested lists of the Database list.
                # The loop runs as many times as there are elements in the list.
                number = a[i][j] # Each iteration of the loop places an element of the nested list into variable number
                if number >= 10 and number <= 100: # Checking if a number is in the range 10-100
                    small_list.append(number) # The .append command adds the number stored in the number variable to the small_list
            if not small_list:  # If the list is empty, raise an exception
                raise ValueError("No valid numbers in list")
            counter = (sum(small_list) / len(small_list), min(small_list), max(small_list), sum(small_list)) # In the counter variable, the arithmetic mean of all the numbers in the small_list list is calculated, # finds out the minimum number of the list (min()), the maximum (max()), and the sum of all numbers (sum())
            result.append(tuple(counter)) # Add a tuple with the results to the result list
        except (TypeError, ValueError) as e:  # Catch TypeError and ValueError exceptions
            print(f"Error: {e}")
    return result

filter(data_list)