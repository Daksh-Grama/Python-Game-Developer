test_list = [1, 4, 5, 4, 6]


print("The original list is : ", test_list)

if test_list == test_list[::-1]:
    print("The reversed list is {}".format(test_list[::-1]))
    print("It is a Palindrome")

else:
    print("The reversed list is {}".format(test_list[::-1]))
    print("It is not a Palindrome")



