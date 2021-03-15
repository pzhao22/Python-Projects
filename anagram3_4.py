# O(n) vs O(n^2) implementation of finding whether two strings of equal length are anagrams
import time
import string

# Sort the lists (strings are immutable), then compare
def quadratic_method1(s1,s2):
    bool_ = True
    list1 = list(s1)
    list2 = list(s2)
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            bool_ = False
    return bool_

# Compare each character with other string - remove from other list if matches
def quadratic_method2(s1,s2):
    bool_ = True
    list1 = list(s1)
    list2 = list(s2)
    i = 0
    while i < len(list1) and bool_ == True:
        found = False
        j = 0
        while j < len(list1) and found != True:
            if list1[i] == list2[j]:
                found = True
                list2[j] = None
            else:
                j += 1
        if found == True:
            list2[j] = None
        else:
            bool_ = False
        i+=1
    return bool_

# I used dicts here. Can also use lists of size 26, index matched to each letter by deriving value of each char (ord)
def linear_method(s1,s2):
    bool_ = True
    count1 = dict.fromkeys(string.ascii_lowercase,0)
    count2 = dict.fromkeys(string.ascii_lowercase,0)
    for i in range(len(s1)):
        count1[s1[i]] += 1
        count2[s2[i]] += 1
    
    for key in count1:
        if count1[key] != count2[key]:
            bool_ = False
            break
    return bool_

def main():

    s1 = "heart"
    s2 = "earts"

    t1 = time.time()
    bool1 = quadratic_method1(s1,s2)
    t2 = time.time()
    bool2 = quadratic_method2(s1,s2)
    t3 = time.time()
    bool3 = linear_method(s1,s2)
    t4 = time.time()

    print(f"Quadratic method 1 took {t2-t1} seconds. Anagram? {bool1}")
    print(f"Quadratic method 2 took {t3-t2} seconds. Anagram? {bool2}")
    print(f"Linear method took {t4-t3} seconds. Anagram? {bool3}")

main()