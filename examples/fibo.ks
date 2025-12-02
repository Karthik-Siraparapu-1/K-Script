print:'--- Fibonacci Series ---'
a = 0
b = 1
count = 0
limit = 10

loop: count < limit do:
    print:a
    temp = a + b
    a = b
    b = temp
    count = count + 1