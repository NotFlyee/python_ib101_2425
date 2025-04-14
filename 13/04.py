nums = [int(num) for num in input().split()]
m, k = [int(num) for num in input().split()]
print(sum([num ** 2 for num in nums[m:k + 1]]))
