# Teplova

def test_function(l):
    def inner_function(j):
        j = 3
        print("Я в области видимости функции test_function")

    inner_function(3)
    if l > 3:
        print("The number is correct")
    else:
        print("Incorrect")

test_function(60)
test_function(0)
test_function(3)
#inner_function(3)