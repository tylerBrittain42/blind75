# non optimal solution
def maxProfit(prices):
    abs_max = 0
    for i in range(0, len(prices) - 1):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] >= abs_max:
                abs_max = prices[j] - prices[i]
    return abs_max


def maxProfit2(prices):
    maxSum = 0
    localMax = 0
    localMin = 10**4
    for i, e in enumerate(prices):
        print(f'min:{localMin} max:{localMax}')
        if e < localMin:
            localMin = e
            localMax = e
        else:
            if e > localMax:
                localMax = e
                if localMax - localMin > maxSum:
                    maxSum = localMax - localMin
    print(f'min:{localMin} max:{localMax}')

    return maxSum



input = [3,2,6,5,0,3]
print(maxProfit2(input))
