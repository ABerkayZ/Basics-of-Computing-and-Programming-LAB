string1 = input("Enter an odd length string: ")
if len(string1)%2==1:

    middle = string1[len(string1)//2]
    print("Middle character:",middle)
if len(string1) % 2 == 0:


    left_middle = string1[(len(string1) - 1) // 2]
    right_middle = string1[len(string1) // 2]
    print("Middle character: ",left_middle, right_middle)

first_half = string1[:len(string1)//2]
if len(first_half)%2==0:
    first_half = string1[:(len(string1)-1) // 2]
    print("First half:",first_half)
else:
    print("First half:",first_half)

second_half = string1[len(string1)//2:]
if len(second_half)%2==0:
    second_half = string1[(len(string1)+1)// 2:]
    print("Second half:",second_half)
else :
    print("Second half:",second_half)