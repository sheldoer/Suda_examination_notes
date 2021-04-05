def read_file():
        with open('data.txt', encoding='utf-8') as file:
            arr = file.read().split()
        return list(map(int, arr))
arr=read_file()

def count(arr: list):
        ls = [0] * 10
        for num in arr:
            if num == 0:
                ls[0] += 1
            else:
                while num:
                    num, h = divmod(num, 10)
                    ls[h] += 1
        print(ls)
count(arr)

def make_prime(n):
    nums = [1] * n
    nums[0], nums[1] = 0, 0
    for i in range(2, n):
        if nums[i]:
            for j in range(i * i, n, i):
                nums[j] = 0
    return nums
