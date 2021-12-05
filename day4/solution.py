from utils import read_input


def do1():
    nums, arrs = read_input()

    for num in nums:
        for arr in arrs:
            arr[arr==num] = -1
            if -5 in arr.sum(axis=0) or -5 in arr.sum(axis=1):
                print(arr[arr!=-1].sum() * num)
                return


def do2():
    nums, arrs = read_input()

    for num in nums:
        for arr in arrs:
            arr[arr == num] = -1
            if -5 in arr.sum(axis=0) or -5 in arr.sum(axis=1):
                print(arr[arr != -1].sum() * num)
                arr[:] = 9999


do1()
print()
do2()