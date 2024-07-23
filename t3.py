inf = float('inf')

def find_max_weight(a):
    n = len(a)
    sum = [0] * (n + 1)
    a.sort()

    for i in range(1, n + 1):
        sum[i] = sum[i - 1] + a[i - 1]

    ans = -inf
    for i in range(1, n + 1):
        mmax = a[i - 1]
        for j in range(1, min(i, n - i + 1)):
            add_l = sum[i - 1] - sum[i - j - 1]
            add_r = sum[n] - sum[n - j]
            mmax = max(mmax, (add_l + add_r + a[i - 1]) / (2 * j + 1))
        ans = max(ans, mmax - a[i - 1])

    return "{:.2f}".format(ans)

# Example usage
a = [1, 3, 5, 9]
result = find_max_weight(a)
print(result)