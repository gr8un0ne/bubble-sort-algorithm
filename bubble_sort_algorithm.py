num = int(input("Enter how many numbers are there:   "))
array = []
for x in range (0,num):
    array.append(int(input("Enter number:   ")))
print("Original array:   ",array)
index = num - 1
sort_status_a = True
sort_status_d = True
for z in range (0,index):
    if array[z] > array[z + 1]:
        sort_status_a = False
while sort_status_a == False: 
    for y in range (0,index):
        if array[y] > array[y + 1]:
            replaced = array[y]
            array[y] = array[y + 1]
            array[y + 1] = replaced
    for z in range (0,index):
        if array[z] > array[z + 1]:
            sort_status_a = False
            break
        else:
            sort_status_a = True
print("Sorted array (ascending) :   ", array)
for z in range (0,index):
    if array[z] < array[z + 1]:
        sort_status_d = False
while sort_status_d == False:
    for y in range (0,index):
        if array[y] < array[y + 1]:
            replaced = array[y]
            array[y] = array[y + 1]
            array[y + 1] = replaced
    for z in range (0,index):
        if array[z] < array[z + 1]:
            sort_status_d = False
            break
        else:
            sort_status_d = True
print("Sorted array (descending):   ", array)


