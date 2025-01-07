# %%
def countDivisiblePairs(arr, k, x):
    # Write your code here
    n = len(arr)
    left = 0
    right = 0
    n_pairs = 0
    
    while right < n:
        if arr[right] - arr[left] < (k - 1)*x:
            right += 1
        elif arr[right] - arr[left] > k*x:
            left += 1
        else: 
            counter = 0
            for num in range(arr[left], arr[right] + 1):
                if num % x == 0:
                    counter += 1
                if counter == k:
                    n_pairs += 1
    return n_pairs

arr = [1,13,4,7,16,10]
countDivisiblePairs(arr, 1, 3)