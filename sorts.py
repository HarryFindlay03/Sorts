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

def menu(choice, arr):
	x = Sorts(arr)
	# Returned as a tuple [0] = the sorted array, [1] = the time taken
	if choice == 1:
		print("Time Taken: ", x.bubble()[1])
	elif choice == 2:
		print("Time Taken: ", x.insertion()[1])
	elif choice == 3:
		print("Time Taken: ", x.mergeSort(numbers)[1])
	elif choice == 4:
		bubbleTime = x.bubble()[1]
		insertionTime = x.insertion()[1]
		if insertionTime < bubbleTime:
			print("With list length: ", len(numbers), "...")
			print("The insertion sort was faster than the bubble sort by: ", (bubbleTime - insertionTime), "seconds")
		elif bubbleTime < insertionTime:
			print("With list length: ", len(numbers, "..."))
			print("The bubble sort was faster than the insertion sort by: ", (insertionTime - insertionTime), "seconds")


file = open('numbers.txt', 'r')

for line in file:
	lineList = line.strip().split()

numbers = lineList

choice = int(input("(1) Bubble    (2) Insetion    (3) Merge : "))

menu(choice, numbers)

