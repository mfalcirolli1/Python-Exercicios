# Manipulate Lists

x = [16, 2, 5, 11, 10, 1]
print(x)
x.sort()
print(x)
x.sort(reverse=True)
print(x)
x.reverse()
print(x)

print(min(x))
print(max(x))
print(sum(x))

x.append(95)
print(x)
x.insert(4, 8)
print(x)

x.remove(1)
print(x)
x.pop()
print(x)
print(x.clear())

new_x = x.copy()
print(new_x)
