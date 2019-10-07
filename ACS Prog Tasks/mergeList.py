#Initialise lists. MergeList is an empty list
#Initialise indices I, j for each list to 0
i = 0
j = 0
list1 = [1,3,5]
list2 = [2,4,6]
mergeList = []

while ((i < len(list1)) and (j < len(list2))):
	if list1[i] < list2[j]:
		mergeList.append(list1[i]) #append item from list1
		i = i + 1
	else:
		mergeList.append(list2[j]) #append item from list2
		j = j + 1
	#endif
#endwhile

#append any items left in the other list
while i < len(list1):
	mergeList.append(list1[i])
	i = i + 1
#endwhile
while j < len(list2):
	mergeList.append(list2[j])
	j = j + 1
#endwhile

print(list1, list2, mergeList)

