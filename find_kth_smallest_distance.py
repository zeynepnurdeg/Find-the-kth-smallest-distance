def num_of_distances(nums):
    lenght = len(nums)
    return ((lenght * (lenght - 1)) / 2)


def smallest_distance_pair(nums, k):
    nums.sort()

    arr = []
    lenght = len(nums)
    for i in range(lenght - 1):
        for j in range(i + 1, lenght): 
            arr.append(abs(nums[i] - nums[j]))

    arr.sort()
    return arr[k - 1]
    

nums = []

while True:
    num = int(input("Enter a number (Enter a negative number to stop): "))
    if num < 0:
        break
    nums.append(num)


size = num_of_distances(nums)
k = None

while True:
    k = int(input("Enter the kth distance you want to see: "))
    if k <= size and k > 0:
        break

result = smallest_distance_pair(nums, k)

print(result)