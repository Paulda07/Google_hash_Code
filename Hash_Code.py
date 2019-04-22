#from collections import Counter
def cal_pic(l, length):
	# for i in l:
	# 	dp[i] = 0
	final_list = []
	s = []
	final_set = []
	H_V = []
	len1 = []
#	temp_set = set()
	for i in range(0,length):
		n= l[i]
		H_V.append( n[0])
		len1.append( n[2])
		n = n[4:-1]
		s.append(n) 
	print (s[0])
	string = ''	
	for i in range (0, length):
		Stri = "hi"
		temp_set = {Stri}
#		lis = [temp_set]
#		print(lis)
#		print (s[1])
		for j in s[i]:
#			print (j)
			if j==' ':
				
					temp_set.add(string)
					string = ''
#					temp_set.discard('hi')
					

			else:
				string = string+j

#				print (string)
		temp_set.add(string)
		string = ''
		temp_set.discard('hi')
#		print (temp_set)
		
		final_set.append(temp_set)
	print (final_set)
	for i in range (0, length):
		final_list.append([H_V[i], len1[i], final_set[i]])
	return final_list

if __name__ == "__main__":
	l = []
	#print (l)
	f = open("a_example.txt", "r")
	for i in f:
		l.append(i)

	#print (l)
	n = l[0]
	n = n[0]
	length  = int(n)
	#print (length)
	l.pop(0)
	#print (l)
	final_list = cal_pic(l, length)
	dp = []
	for i in range (0, len(final_list)):
		dp.append(0)
	g=[]
	v=[]
	for u in final_list:
	    for h in u:
	        if(h[0]=='H'):
	            g.append(u)
	            break
	        else:
	            v.append(u)
	            break
	print (g, v)
	ret_min(g, v)

def ret_min(g, v):	
	done = []
	for i in range (0, len(final_list)):
		for j in range (0, len(final_list)):
			if (i==j):
				break
			elif (j is in done): 
				break
			g1 = g[i]
			g2 = g[j]
			if (set(g1[3]).intersection(set(g2[3])) is not set()):
				if 