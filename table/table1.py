def table1(n, A, B):
    i, j, k = 0, 0, -1
    while i < n and j < n:
        if A[i] < B[j]:
            i = i + 1
        elif A[i] > B[j]:
            j = j + 1
        else:
            if k == -1:
                k += 1
                A[k] = A[i]
            elif A[i] != A[k]:
                k += 1
                A[k] = A[i]
            i += 1
            j += 1
    return A


def reverse(L, left, right):
    """ 倒置顺序表 """
    while left < right:
        tmp = L[left]
        L[left] = L[right]
        L[right] = tmp
        left += 1
        right -= 1
    return L


def table2(A):
    n, m, k = 4, 3, 0
    i = n
    while i < (n + m):
        if A[i] > A[i-1]:
            pass
        else:
            tmp = A[i]
            j = i - 1
            while j >= k:
                if A[j] > tmp:
                    A[j + 1] = A[j]
                    j -= 1
                else:
                    break
            A[j + 1] = tmp
        i = i + 1
    return A


if __name__ == '__main__':
    # A = [1, 2, 3,  3, 7]
    # B = [1, 3, 3, 9, 10]
    # print(table1(5, A, B))
    # print(reverse(A, 0, len(A)-1))
    print(table2([1, 2, 5, 7, 3, 4, 6]))
