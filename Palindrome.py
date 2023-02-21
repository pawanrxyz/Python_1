def isPalindrome(str):
    for i in range(0,int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:   
            return False
        else:
            return True
s = "racecar"
ans = isPalindrome(s)
# print(ans)
if(ans):
    print("Yes")
else:
    print("No") 