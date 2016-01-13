import string

alph = list(string.ascii_lowercase)
print alph

enter_val = (raw_input("Enter your word :")).lower()

print "Your word is : .... " + enter_val

temp = list()
non_val = list()


def letterchanges(str):
    
    for i in enter_val:
        for t in alph:
        	#print alph.index(t)
        	if t == i:
        		if i != 'z':
        			pos = alph.index(t)
        			temp.append(alph[pos+1])
        		elif i == 'z':
        			temp.append('a')
        	if i not in alph and i not in non_val:
        		non_val.append(i)




                 

letterchanges(enter_val)

test = ''.join(temp)
test1= ''.join(non_val)
print "Your new word is : .....",  test + test1
print "Done"
print "Bye"
