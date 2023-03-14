

'''checking if a given integer is palindrome (by assigning it to a string):'''

# def palin(n):
#     if str(n) == str(n)[::-1]:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")

'''checking if given integer is  palindrome (without assigning it to string'''

def palin(n):
    temp = n
    reverse=0

    while temp!=0:
        reverse = (reverse*10) + (temp%10) #1 , #1*10+12%10=12, #12*10+1%10=121
        temp = temp//10 #12 #1 #0 loop terminates

    if n==reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")

#palin(10)
#palin(1331)
palin(12321)