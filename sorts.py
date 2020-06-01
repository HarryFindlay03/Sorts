import random
import time

class Sorts:
	def __init__(self, numbers):
		self.arr = numbers

	def bubble(self):
		t0 = time.time()
		n = len(self.arr)
		for i in range(0, (n - 1)):
			for j in range(0, (n - i - 1)):
				if self.arr[j] > self.arr[j + 1]:
					self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
		t1 = time.time()
		total = t1 - t0
		tup = (self.arr, total)
		return(tup) 

	def insertion(self):
		t0 = time.time()
		n = len(self.arr)
		for i in range(0, n):
			currentVal = self.arr[i]
			pos = i
			while  pos > 0 and self.arr[pos - 1] > currentVal:
				self.arr[pos] = self.arr[pos - 1]
				pos -= 1
			self.arr[pos] = currentVal
		t1 = time.time()
		total = t1 - t0
		tup = (self.arr, total)
		return(tup)
	
	def mergeSort(self, arr): # Recursive function, has to take the arr as a parameter.
		t0 = time.time()
		if(len(arr) > 1):
			mid = len(arr) // 2
			leftHalf = arr[:mid]
			rightHalf = arr[mid:]

			self.mergeSort(leftHalf)
			self.mergeSort(rightHalf)

			i = 0
			j = 0
			k = 0

			while i < len(leftHalf) and j < len(rightHalf):
				if leftHalf[i] < rightHalf[j]:
					arr[k] = leftHalf[i]
					i += 1
				else:
					arr[k] = rightHalf[j]
					j += 1
				k += 1

			while i < len(leftHalf):
				arr[k] = leftHalf[i]
				i += 1
				k += 1
			
			while j < len(rightHalf):
				arr[k] = rightHalf[j]
				j += 1
				k += 1
		t1 = time.time()
		total = t1 - t0
		tup = (arr, total)
		return(tup)
	
	### QUICK SORT

	def partition(self, arr, start, end):
		i = (start - 1) # Index of smaller element
		pivot = arr[end]

		for j in range(start, end):
			if arr[j] <= pivot:
				i = i + 1
				temp = arr[i]
				arr[i] = arr[j]
				arr[j] = temp
		
		temp = arr[i + 1]
		arr[i + 1] = arr[end]
		arr[end] = temp
		return(i + 1)

	def quickSort(self, arr, start, end):
		t0 = time.time()
		if start < end:
			# pi is partitioning index, arr[p] is now at right place
			pi = self.partition(arr, start, end)

			#Seperately sort elements before and after partition

			self.quickSort(arr, start, pi - 1)
			self.quickSort(arr, pi + 1, end)
		t1 = time.time()
		total = t1 - t0
		tup = (arr, total)
		return(tup)


def menu(choice, arr):
	x = Sorts(arr)
	# Returned as a tuple [0] = the sorted array, [1] = the time taken
	if choice == 1: # Bubble
		print("With List Length of: ", len(numbers))
		print("Time Taken: ", x.bubble()[1])
	elif choice == 2: # Insetion
		print("With List Length of: ", len(numbers))
		print("Time Taken: ", x.insertion()[1])
	elif choice == 3: # Merge
		print("With List Length of: ", len(numbers))
		print("Time Taken: ", x.mergeSort(numbers)[1])
	elif choice == 4:  # Quick
		print("With List Length of: ", len(numbers))
		print("Time Taken: ", x.quickSort(numbers, 0, len(numbers) - 1)[1])
	

file = open('numbers.txt', 'r')

for line in file:
	lineList = line.strip().split()

numbers = lineList

choice = int(input("(1) Bubble    (2) Insetion    (3) Merge    (4) Quick : "))

menu(choice, numbers)

