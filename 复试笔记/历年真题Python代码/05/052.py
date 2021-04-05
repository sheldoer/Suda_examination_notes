def equal_prime(n):
    """
    `2005`年复试上机题
    把一个数表示成若干个素数的和.
    注， 此题不用这个方法。
    """

    def judge_prime(n):
        if n == 0 or n == 1: return False
        if n == 2: return True
        if n % 2 == 0: return False
        # 判断
        if 0 in [n % i for i in range(2, int(n ** 0.5 + 1))]:
            return False
        return True

    def DFS(n, index=0, sum=0, primes=[], L=[], S=None):
        if S is None:
            S = set()
        if (sum > n):
            return
        # sum==n 找到了这样的一组数字
        if index < len(primes):
            if sum == n:
                if tuple(L) not in S:  # 避免重复输出
                    print(L)
                    S.add(tuple(L))
            L.append(primes[index])
            DFS(n, index, sum + primes[index], primes, L, S)
            L.pop()
            DFS(n, index + 1, sum, primes, L, S)

    plist = [i for i in range(n + 1) if judge_prime(i)]
    DFS(n, 0, 0, plist, S=set())
equal_prime(9)
