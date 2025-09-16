#check if valid mirror spell or not.
def check(s):
    i=0
    j=0
    while i<j:
        while i<j and not s[i].isalnum():
            i+=1
        while i<j and not s[j].isalnum():
            j-=1
        if s[i].lower() != s[j].lower():
            return "Corrupted Spell"
        i+=1
        j-=1
    return "Valid Mirror Spell"

s = "No lemon, No Melons!"
print(check(s))