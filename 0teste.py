i = 0
while True:
    i = i + 1
    if i == 2:
        print('Skipping 2')
        continue
    if i == 5:
        print('Breaking')
        break
    print(i)

num = [2, 12, 95, 13]
num.append(1)
print(num)

words = ['Python', 'fun']
words.insert(1, 'is')
print(words)

letters = ['m', 'a', 't', 'h', 'e', 'u', 's']
print(letters.index('h'))

numb = list(range(1, 11, 2))
print(numb)

