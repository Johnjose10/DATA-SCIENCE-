arr = []
n = int(input("Enter size of array:"))

for i in range(n):
    arr.append(int(input(f"Enter element {i+1} : ")))

print(f"The array is : {arr}")

for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print("Sorted array is: ",arr)



*******OUTPUT********


Enter size of array:8
Enter element 1 : 2
Enter element 2 : 4
Enter element 3 : 8
Enter element 4 : 15
Enter element 5 : 17
Enter element 6 : 28
Enter element 7 : 19
Enter element 8 : 25
The array is : [2, 4, 8, 15, 17, 28, 19, 25]
Sorted array is:  [2, 4, 8, 15, 17, 19, 25, 28]

