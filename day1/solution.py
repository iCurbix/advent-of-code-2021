from utils import read_file_numbers

nums = read_file_numbers()
inc = 0
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        inc += 1

print(inc)

inc = 0
for i in range(3, len(nums)):
    if nums[i] > nums[i - 3]:
        inc += 1

print(inc)
