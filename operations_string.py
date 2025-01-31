s1 = "hello"
s2 = "world"
print(s1 + " " + s2)
print(s1, "hello")
print(3*s2)

print(s1, len(s1))
print((3*s2), len((3*s2)))
for c in s2:
    print (c)

s3 = ""
for c in s2:
    s3 += (4*c)
print(s3)

print("h" in s1)
print("d" in s2)
print("d" in s3)