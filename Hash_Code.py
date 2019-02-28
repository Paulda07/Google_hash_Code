from collections import Counter
l = []
#print (l)
f = open("a_example.txt", "r")
for i in f:
	l.append(i)

#print (l)
n = l[0]
n = n[0]
length  = int(n)
print (length)
l.pop(0)
print (l)

def cal_pic(l, length):
	# for i in l:
	# 	dp[i] = 0
	s = []
	final_set = []
	H_V = 'I'
	lenq = 0
#	temp_set = set()
	for i in range(0,length):
		n= l[i]
		H_V = n[0]
		len1 = n[3]
		n = n[4:-1]
		s.append(n) 
	print (s)
	string = ''	
	for i in range (0, length):
		Stri = "hi"
		temp_set = {Stri}
		lis = [temp_set]
#		print(lis)
		Stri 
		for j in s[0]:
			print (j)
# 			if j==' ':
				
# 					temp_set.add(string)
# 					string = ''
# 					print (temp_set)
# 			else:
# 				string = string+j
# #				print (string)
# 		final_set.append(temp_set)
# 		temp_set.clear()
# #	print (final_set)
# cal_pic(l, length)
