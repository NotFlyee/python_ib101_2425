nums = [int(num) for num in input().split()]
m, k = [int(num) for num in input().split()]
print(sum(nums[m:k + 1]))
