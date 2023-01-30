a, b = map(lambda x: int(x), input().split())
print("slog:", a+b)
print("min:", a-b)
print("multiply:", a*b)
if b != 0:
    print("del:", a/b)
else:
    print("warning")
