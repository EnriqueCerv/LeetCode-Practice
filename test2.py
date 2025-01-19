# %%
def solution(x):
    # Write your code here
    def fibonacci(arr):
        arr.append(arr[-2] + arr[-1])
        return arr
    
    fib = [0,1]
    while fib[-1] < x:
        fib = fibonacci(fib)
    
    closest = min(x - fib[-2], fib[-1] - x)
    return closest 

solution(24)
# %%
def solution(A):
    # Write your code here
    
    def gradeChange(arr):
        n = len(arr)
        changes = [0]*n
        
        for i in range(1,n - 1):
            if arr[i - 1] > arr[i] and arr[i + 1] > arr[i]:
                changes[i] = 1
            elif arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
                changes[i] = -1
        
        for i in range(n):
            arr[i] += changes[i]
            
        return arr
        
    initGrade = A
    postGrade = gradeChange(initGrade)
    print(initGrade, postGrade)
    
    while initGrade != gradeChange(initGrade):

        # print(initGrade, gradeChange(initGrade))
        initGrade = gradeChange(initGrade)

    return gradeChange(initGrade)
solution([1,7,3,4,3,5])
# %%
def solution(A):
    # Write your code here
    n = len(A)
    
    # def gradeChange(arr):
    #     n = len(arr)
    #     changes = [0]*n
        
    #     for i in range(1,n - 1):
    #         if arr[i - 1] > arr[i] and arr[i + 1] > arr[i]:
    #             changes[i] = 1
    #         elif arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
    #             changes[i] = -1
        
    #     for i in range(n):
    #         arr[i] += changes[i]
            
    #     return arr
        
    initGrade = A
    finalGrade = [0]*n
    changes = [0]*n 
    for i in range(1,n - 1):
        if initGrade[i - 1] > initGrade[i] and initGrade[i + 1] > initGrade[i]:
            changes[i] = 1
        elif initGrade[i - 1] < initGrade[i] and initGrade[i + 1] < initGrade[i]:
            changes[i] = -1
    for i in range(n):
        finalGrade[i] = changes[i] + initGrade[i]
    
    while initGrade != finalGrade:
        initGrade = finalGrade
        finalGrade = [0]*n
        changes = [0]*n 
        for i in range(1,n - 1):
            if initGrade[i - 1] > initGrade[i] and initGrade[i + 1] > initGrade[i]:
                changes[i] = 1
            elif initGrade[i - 1] < initGrade[i] and initGrade[i + 1] < initGrade[i]:
                changes[i] = -1
        for i in range(n):
            finalGrade[i] = changes[i] + initGrade[i]
        
    return finalGrade

solution([1,7,3,4,3,5])