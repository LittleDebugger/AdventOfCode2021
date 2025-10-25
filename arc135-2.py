a = input()
nums = [int(x) for x in input().split()]


def go(i, ii):
    global nums
    run = [i, ii, nums[0] - i - ii]

    for ix in range(1, len(nums)):
        if run[-1] + run[-2] > nums[ix]:
            return

        run.append(nums[ix] - run[-1] - run[-2])
    print('Yes')
    print(' '.join([str(x) for x in run]))
    exit()


for i in range(0, nums[0] + 1):
    remainder = nums[0] - i + 1
    secondMax = remainder
    if len(nums) > 1:
        secondMax = nums[1] + 1
    secondMin = 0
    if len(nums) > 2:
        secondMin = (nums[0] - i + 1 - nums[2]) + 1
    for ii in range(max(0, secondMin), min(remainder, secondMax)):
        go(i, ii)

print('No')
