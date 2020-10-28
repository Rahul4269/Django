'''s="this is python"
for x in iter(s):
    print(x)

s = "this is python"
itr=iter(s)
print(next(itr))
print(next(itr))'''

s="this is python"
for x in iter(s):
    print(x)

s = "this is python"
itr=iter(s)
for i in range (0,len(s)):
    print(next(itr))

