def fibonacci(num):
    fibonacciList = []

    for i in range(num):
        if i == 0 or i==1:
            fibonacciList.append(i)
        else:
            fibonacciList.append(fibonacciList[i-1] + fibonacciList[i-2])
    print(fibonacciList)

fibonacci(10)
