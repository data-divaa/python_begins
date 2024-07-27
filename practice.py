def palindrome(string_list):
    a = ""
    result = []
    for i in string_list:
        for k in range(len(i)-1,-1,-1):
            a = a + i[k]
    return a

string_list = list(input("enter:").split())
print(palindrome(string_list))
