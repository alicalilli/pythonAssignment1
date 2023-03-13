x = 'aaavvvfdff'

def text_compression(x):
    compressed_text = ""
    counter = 1
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            counter+=1
        else:
            compressed_text = compressed_text +x[i] + str(counter)
            counter=1
    compressed_text = compressed_text +x[i] + str(counter)

    return compressed_text

text_compression(x)