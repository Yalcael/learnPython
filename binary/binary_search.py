from bisect import bisect_left, bisect_right


def bisect_left(arr: list, x, lo=0, hi=None) -> int:
    hi = hi if hi is not None else len(arr)
    assert 0 <= lo <= hi <= len(arr)
    while lo < hi:
        mid = (lo + hi) // 2    # lo + (hi-lo)//2 for avoid overflow
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


# Binary search, also called bisection search, is an algorithm for finding an element quickly in a sorted array.
