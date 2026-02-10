# %%


# Given a string of length N containing '_' for empty space and 'H' for house. 
# Write a function that gives the minimum number of water tanks you can place.
# A house can collect water froma water tank if it is adjacent to it on the left 
# or on the right. 
# For example, S = '-H-HH--' should output two with the example 
# configuration '-HTHHT-' where T is a tank. 
# If not possible, return -1
    

def placement(arr):
    n = len(arr)
    count = 0
    arr = list(arr)

    for idx, ele in enumerate(arr):
        if ele == 'H':
            if (idx - 1 >= 0 and arr[idx - 1] == "T") or (idx + 1 < n and arr[idx + 1] == "T"):
                continue
                
            if idx + 1 < n and arr[idx + 1] == "-":
                arr[idx + 1] = 'T'
                count += 1
                print(ele, idx)
                # continue
            elif idx - 1 >= 0 and arr[idx - 1] == "-":
                arr[idx - 1] = 'T'
                count += 1
                print(ele, idx)
                # continue
            else:
                return -1
    return count, arr
# %%
street = "-H-HH--"
placement(street)
