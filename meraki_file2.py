# a=open("people.txt","r")
# r=a.read()
# print(r)
f=open("people.txt","r")
nol=0
for line in f:
    nol+=1
print(nol)    