
def my_generator():
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print("Generator Shu. ")

gen = my_generator()
next(gen)
gen.close()


# Errorni ko'rmoqchi bolsangiz try va exceptni o'chiring !
