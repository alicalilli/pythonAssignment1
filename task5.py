### Task 5


x = 'aaavvvfdff'

def text_compression(x):
    compressed_text = ""
    counter = 1 # Counter variable in which the number of characters will be written
    for i in range(len(x)-1): # the loop runs as many times as there are characters in string x.
        # We subtract one from the length of the array x (len(x)-1) so that later during the check it does not go beyond its boundaries
        if x[i] == x[i+1]: # If the current letter of the list is equal to the next letter then add +1 to the counter
            counter+=1
        else:
            compressed_text = compressed_text +x[i] + str(counter) #If not, then we add the current letter and the counter variable to the compressed_text variable.
            counter=1 # Update the counter for the next count
    compressed_text = compressed_text +x[i] + str(counter) #We write down the last results of the calculation, because the loop did not do this
    
    return compressed_text

text_compression(x)