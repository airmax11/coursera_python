"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution 
by hour of the day for each of the messages. You can pull the hour out from the 'From ' 
line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour 
as shown below. Note that the autograder does not have support for the sorted() function.

"""

file_name = raw_input ("Enter yor file name:")

if len (file_name) < 1 :
	file_name = "mbox-short.txt"


open_file = open (file_name)


new_list = list ()

for line in open_file:
	if line.startswith ("From "):
		line.rstrip()

		#temp_count =



		temp_val = line.split()

		temp_val2 = temp_val[5]
		test = temp_val2[:2]


		new_list.append (test)


new_dic = dict ()


for line in new_list:
	new_dic[line] = new_dic.get (line, 0) + 1


reversed_dic = list ()

for key , val in new_dic.items ():
	test = ( key, val )
	reversed_dic.append(test)

reversed_dic.sort (reverse = False)

for key, val in reversed_dic:
	print key, val
	








