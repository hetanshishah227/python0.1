str = "Hello World"
vowel = "AEIOUaeiou"
count = 0
for char in str:
    if char in vowel:
        count += 1
print(count)
    