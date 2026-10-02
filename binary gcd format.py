# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def binary_gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a
    
   
    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1
        
    
    while (a & 1) == 0:
        a >>= 1
        
    
    while b != 0:
        
        while (b & 1) == 0:
            b >>= 1
            
        if a > b:
            a, b = b, a
            
        b = b - a  
    return a << shift

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) >= 2:
        a = int(input_data[0])
        b = int(input_data[1])
        print(binary_gcd(a, b))

if __name__ == '__main__':
    main()
