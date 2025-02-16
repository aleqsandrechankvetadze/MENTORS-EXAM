def anagrams(s,p):

    return sorted(s) == sorted(p)

print(anagrams("silent","listen"))
print(anagrams("abc","bac"))
print(anagrams("abc","bacd"))