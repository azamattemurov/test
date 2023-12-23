def Sortlnc3(a, b, c):
    # A ning qiymatini eng kichik son qilish
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a

    # C ning qiymatini eng katta son qilish
    if b > c:
        b, c = c, b

    return a, b, c


def SortDec3(A, B, C):
    # A ning qiymatini eng katta son qilish
    if A < B:
        A, B = B, A
    if A < C:
        A, C = C, A

    # C ning qiymatini eng kichik son qilish
    if B < C:
        B, C = C, B

    return A, B, C


# Misollar
inputs = [(5, 2, 7), (10, 3, 1), (4, 4, 4)]  # muhim sonlarni o'zgartiring
for a, b, c in inputs:
    a1, b1, c1 = Sortlnc3(a, b, c)
    a2, b2, c2 = SortDec3(a, b, c)
    print(f"Input: {a}, {b}, {c}")
    print(f"Sortlnc3 Output 8 - Funksiya o\'sish: {a1}, {b1}, {c1}")
    print(f"SortDec3 Output 9 - Funksiya kamayish: {a2}, {b2}, {c2}")
    print()


