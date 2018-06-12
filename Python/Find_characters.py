# input
word_list = ['hello','world','my','name','is','Anna']
char = "o"
new_list=[]
for x in word_list:
    if x.find("o")!= -1:
        new_list.append(x)

print "The new list is: ",new_list