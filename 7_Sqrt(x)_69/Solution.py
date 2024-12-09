x = 4 
# Output: 2

x = 100
# Output: 2

def mySqrt(x: int) -> int:
    right = x 
    left = 0

    while left < right:
        mid = (right + left ) // 2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            right = mid
        else:
            left = mid + 1
    return left - 1

print(mySqrt(x))