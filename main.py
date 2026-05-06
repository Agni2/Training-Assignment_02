import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    k = int(input_data[n+1])
    
    remainder_check = a[0] % k
    for x in a:
        if x % k != remainder_check:
            print("-1")
            return
    
    a.sort()
    median = a[n // 2]
    
    total_ops = 0
    for x in a:
        total_ops += abs(x - median) // k
            
    print(total_ops)

if __name__ == "__main__":
    solve()