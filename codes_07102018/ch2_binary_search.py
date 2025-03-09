#coding=utf-8
def binary_search(A, k):
    first = 0
    last = len(A)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if A[midpoint] == k:
            found = True
        else:
            if k < A[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

if __name__ == "__main__": 
    print(binary_search([3, 4, 5, 8],2))