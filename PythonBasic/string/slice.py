s = 'Hello, world'
s1 = s
s2 = s[2:4]
s3 = s[::-1]
s4 = s[:]

print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(s4))