def ans(word):
    kk = word[::-1]
    if kk == word:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
x = "abba"
y = "abbc"
z = "a b b a"

print( ans(x),"\n", ans(y),"\n" , ans(z))