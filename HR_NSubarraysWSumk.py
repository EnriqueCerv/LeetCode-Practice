# %%

# Given array arr and target k, find number of subarrays with sum == k

arr = [1,2,3,0]
k = 3

# Should return 3 for [1,2],[3],[3,0]

def subarrayCounter(arr,k):

    n = len(arr)
    dp = [[0]*n for i in range(n)]

    for i in range(n):
        dp[i][i] = arr[i]

    counter = 0
        
    for i in range(n):
        for j in range(i+1, n):
            dp[i][j] = dp[i][j-1] + arr[j]
    
    for i in range(n):
        for j in range(i, n):
            if dp[i][j] == k:
                counter += 1
    
    return counter

subarrayCounter(arr,k)
# %%

def maxArray(arr, k):
    n = len(arr)
    subs = [[0]*n for i in range(n)]
    count = 0

    # for i in range(n):
    #     subs[i][i] = arr[i]

    for i in reversed(range(n)):
        for j in range(i, n):
            subs[i][j] = arr[j] + subs[i][j-1]
            if subs[i][j] == k:
                count += 1
                # print(i,j)
    
    return count

# %%
# Tests


# Test Case 1: Basic Case
arr1 = [1, 1, 1]
k1 = 2
expected1 = 2  # Subarrays: [1,1], [1,1]

# Test Case 2: Single Element Matches Target
arr2 = [3, 1, 2, 4]
k2 = 4
expected2 = 2  # Subarrays: [4], [1,2,1]

# Test Case 3: All Elements Equal Target
arr3 = [2, 2, 2]
k3 = 2
expected3 = 3  # Subarrays: [2], [2], [2]

# Test Case 4: No Subarrays Sum to Target
arr4 = [1, 2, 3, 6]
k4 = 10
expected4 = 0 # No valid subarrays

# Test Case 5: Negative Numbers Included
arr5 = [1, -1, 2, 3, -2]
k5 = 3
expected5 = 3  # Subarrays: [1,-1,2,1], [3], [2,3,-2]

# Test Case 6: Large Array with Duplicates
arr6 = [1, 2, 1, 2, 1]
k6 = 3
expected6 = 4  # Subarrays: [1,2], [2,1], [1,2], [2,1]

# Test Case 7: Target is Zero
arr7 = [1, -1, 2, -2, 3]
k7 = 0
expected7 = 3  # Subarrays: [1,-1], [2,-2], [-1,2,-2,3]

# Test Case 8: All Zeros in Array
arr8 = [0, 0, 0, 0]
k8 = 0
expected8 = 10  # All subarrays sum to zero

# Test Case 9: Large Values in Array
arr9 = [100, 50, -50, 100]
k9 = 100
expected9 = 4  # Subarrays: [1000000], [500000,-500000,1000000], [1000000]

# Test Case 10: Empty Array
arr10 = []
k10 = 5
expected10 = 0  # No subarrays

# Collecting all test cases
test_cases = [
    (arr1, k1, expected1),
    (arr2, k2, expected2),
    (arr3, k3, expected3),
    (arr4, k4, expected4),
    (arr5, k5, expected5),
    (arr6, k6, expected6),
    (arr7, k7, expected7),
    (arr8, k8, expected8),
    (arr9, k9, expected9),
    (arr10, k10, expected10),
]

# Example of how you could run the test cases
for arr, k, expected in test_cases:
    print(maxArray(arr, k) == expected, arr, k)
# %%
