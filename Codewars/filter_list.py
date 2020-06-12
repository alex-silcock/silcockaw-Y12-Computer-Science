# filter a list into just integers
list = ([1,2,'a','b'])

def filter_list(list):
    sortedList = []
    for i in range(len(list)):
        try:
            sortedList.append(int(list[i]))
        except ValueError:
            continue
    return sortedList

a = filter_list(list)
print(a)