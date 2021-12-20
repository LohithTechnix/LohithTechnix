class Insertion():
	def __init__(self,list):
		self.list=list
	def sort(self):
		for i in range(1,len(self.list)): # 1,2,3,4,5
			k = self.list[i] #4,3
			j = i-1 #0
			while j >= 0 and k < self.list[j]: 
				self.list[j] = self.list[j+1] #self.list[1]= 5
				j -= 1
			self.list[j+1] = k #self.list[0]=4
			print(self.list)
			return self.list


insert= Insertion(list(map(int,input().split())))
print(insert.sort())

#bubble sort maximum at the end of list
'''l = 5,4,3,2,1
4,3,2,1,5
3,2,1,4,5
2,1,3,4,5
1,2,3,4,5
k = 5
k = 1
0 = 4'''
#l= 1,4,3,2,5 # bubble sort
#l= 1,2,3,4,5
# class Bubble():
	# def __init__(self,list):
	# 	self.list=list
	# def sort(self):
	# 	for i in range(len(self.list)):
	# 		for j in range(len(self.list)-i-1):
	# 			if self.list[j]>self.list[j+1]:
	# 				self.list[j],self.list[j+1]=self.list[j+1],self.list[j]
	# 		print(self.list)
	# 	return self.list1

#quick sort
#take last element as pivot
#high and low
# while low<high if element< or > current element
#dividing list into 2 parts based on pivot
# class Quick():

# 	def partition(self,l,low,high):
# 		i=low-1#-1
# 		pivot = l[high]
# 		for j in range(low,high):
# 			if l[j]<=pivot:
# 				i+=1#0
# 				l[j],l[i]= l[i],l[j]
# 		l[i+1],l[high]= l[high],l[i+1]
# 		print(l)
# 		return i+1

# 	def sort(self,l, low, high):
# 		if len(l) ==1:
# 			return l
# 		if low < high:
# 			p = self.partition(l, low, high)
# 			self.sort(l,low, p-1)
# 			self.sort(l,p+1,high)


# insert =Insertion()	
# insert.sort([0,4,3,2,1])