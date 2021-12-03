def adder(*nums):
    sum = 0
    
    for n in nums:
        sum += n

    print("Сумма чисел: ", sum)

adder(0, 5)
adder(4, 5, 0, 7)
adder(1, 2, 0, 0, 100006)