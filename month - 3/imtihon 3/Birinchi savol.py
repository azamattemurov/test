file = open("data.csv", "r")

while True:
    try:
        number = int(input("Son kiriting: "))
        if number > 10000 or number < 1:
            print("Sonlar 1 va 10000 oralig'ida bo'lishi kerak!")
            continue
        break
    except:
        print("Faqat son kiriting!")

numbers = list(map(int, file.readlines()))
print(max(numbers[:number]))


file.close()