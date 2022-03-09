a=str(input("Enter a string:"))
print("after the given string ")
if a[-3:]=='ing' and len(a)>4:
    print(a[:3:]+'ly')
elif a[-3:]!='ing' or len(a)>=0:
    print(a+'ing')