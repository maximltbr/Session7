print(dir("hello"))
print(help("hi".capitalize))

print("i like to go to school".capitalize())
print("IS THIS SUPPOSED TO WORK".capitalize())
print("hello".center(50,"x"))
print("gmail.com".find("."))
s = "i see a cat who like to cat while i cat on a cat"

# find all occurrences
pos = 0
while True:
    pos = s.find("cat",pos)
    if pos == -1:
        break
    print("found cat on position", pos)
    pos += 1

# Join

# lower
s = "I SEE A LOT OF THINGS!"
print(s.lower())

# upper
s = "i see a lot of things!"
print(s.upper().capitalize())

# replace - replaces x with y
s = "i see a cat who likes to eat a rat. what a good cat"
print(s.replace("c", "r"))
print(s.replace("cat", "lion"))
s = "Hello, kind sir! How are you today?"
print(s.replace(",", "").replace(".", "").replace("?","").replace("!",""))

# split
s = "i like to go shopping"
print(s.split())
splitted = s.split()
print("XX".join(splitted))