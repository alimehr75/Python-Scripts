def largestPerimeter(A):
    A.sort()
    for i in range(len(A) - 3, -1, -1):
        print (A[i] ,A[i+1] ,A[i+2])
        # if A[i] + A[i+1] > A[i+2]:
        #     return A[i] + A[i+1] + A[i+2]
    return 0


print(largestPerimeter([1, 2, 2, 4, 5, 6]))
#  6 5 4 2 2 1
