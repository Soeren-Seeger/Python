friends = ["Jim", "Karen", "Houston"]

print(friends.index("Jim"))

for names in friends:
    for letters in friends[friends.index(names)]:
        print(letters)

for names in friends:
    for letters in names:
        print(letters)

for index in range(10):
    print(str(index + 1))  # index ist ein int
for index in range(10):
    print(index)  # index ist ein STRING !!
print(friends.count("Jim "))
