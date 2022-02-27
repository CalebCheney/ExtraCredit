infile = open('book of John text.txt', 'r')

my_words  = {'Father':0, 'God':0, 'Christ':0, 'Spirit':0, 'spirit':0, 'life':0, 'man':0}

for line in infile:
    words = line.split(' ')

    for word in words:
        if word in my_words:
            my_words[word] += 1

    
infile.close()

print("Father: ", my_words['Father'], '\n',
"God: ", my_words['God'], '\n',
"Christ: ", my_words['Christ'], '\n',
"Spirit: ", my_words['Spirit'], '\n',
"spirit: ", my_words['spirit'], '\n',
"life: ", my_words['life'], '\n',
"man: ", my_words['man'], sep = '')
