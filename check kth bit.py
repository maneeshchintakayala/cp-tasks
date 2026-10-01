# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
def check_kth_bit():
    input_data = sys.stdin.read().split()
    if not input_data:
        return 
    n = int(input_data[0])
    k = int(input_data[1])
    bit_status = (n >> k) & 1 
    print(bit_status)
if __name__ == '__main__':
    check_kth_bit()
