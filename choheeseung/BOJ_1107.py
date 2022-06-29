n = int(input())  # 이동하려는 채널
m = int(input())  # 고장난 버튼 개수

if m == 0:
    button = list()
else:
    button = list(map(int, input().split()))  # 고장난 버튼

count = abs(100 - n)

for i in range(1000001):
    nums = str(i)

    for j in range(len(nums)):
        if int(nums[j]) in button:
            break

        elif j == len(nums) - 1:
            count = min(count, abs(int(nums) - n) + len(nums))

print(count)
