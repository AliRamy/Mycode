from itertools import product 
  
def maxiMize(k):
    finalArr = list()
    mostMax = 0
    for counterOne in range(k):
        arr = list(map(int, input().rstrip().split()))
        finalArr.append(arr)
    tuplesArr = list(product(*finalArr))
    for counterTwo in range(len(tuplesArr)):
        squareSum = 0
        for counterThree in range(k):
            squareSum = squareSum + tuplesArr[counterTwo][counterThree]**2
        relativeMax = squareSum % m
        if relativeMax >= mostMax:
            mostMax = relativeMax

    return mostMax

if __name__ == '__main__':
    k , m = map(int,input().split())
    print(maxiMize(k))