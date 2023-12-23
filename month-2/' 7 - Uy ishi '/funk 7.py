def MinMax(a, b, c, d):
    min_value = min(a, b, c, d)
    max_value = max(a, b, c, d)
    return min_value, max_value


a = int(input())
b = int(input())
c = int(input())
d = int(input())


min_value, max_value = MinMax(a,b, c, d)
print(f"X: {min_value}")
print(f"Y: {max_value}")
