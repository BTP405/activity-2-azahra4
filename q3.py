def wordCount(t):
    word_dict = {}
    with open(t, 'r') as file:
        for line_number, line in enumerate(file, start=1): #Attach count of the line number into the linenumber variable with the line thats being read and start at 1 -default starts @ 0
            words = line.split() #split the line at every empty space and save it in a list words. 
            for word in words:
                word = word.strip() #Strip of the whitespaces
                if word not in word_dict:
                    word_dict[word] = [line_number]
                elif line_number not in word_dict[word]:
                    word_dict[word].append(line_number)
    return word_dict

print(wordCount("q3_test.txt"))