# credit: https://leetcode.com/problems/divide-two-integers/discuss/179759/Python-7-lines-(beats-99)%3A-How-you-learned-to-divide-when-you-were-7-years-old


def divide(dividend, divisor):
    # this is necessary; otherwise phase 1 never terminates
    if dividend == 0: 
        return 0

    # initialize
    i, result, p, q = map(abs, (0, 0, dividend, divisor))
    
    # phase 1
    while q << i <= p: 
        i += 1

    # phase 2
    for j in reversed(range(i)):
        if q << j <= p: 
            p, result = p - (q << j), result + (1 << j)

    # stupid leetcode restrictions
    if (dividend > 0) != (divisor > 0): # or result < -1 << 31:
        result = -result
    return min(result, (1 << 31) - 1)


def testDivide():
    print(divide(32, 3))
    print(divide(32, -3))
    print(divide(1<<31, -1))
    print(divide(1<<31, 1))
    print(divide(-1<<31, -1))
    print(divide(-1<<31, 1))
    print(divide(10, 3))
    print(divide(7, -3))


testDivide()
