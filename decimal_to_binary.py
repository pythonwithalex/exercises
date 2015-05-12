import math

def max_times(target, base=2):
    '''
    n, prev = 0, None
    while base**n <= target:
        prev = n
        n+=1
    return prev
    '''
    return math.floor(math.log(target,base))
    

def dec_to_bin(target, max_twos, base=2):
    binary_str = ''
    for num in range(max_two,-1,-1):
        max_div = base**num
        if max_div <= target:
            binary_str += '1'
            target -= max_div
        else:
            binary_str += '0'
    return binary_str

def main():
    target = 16
    max_twos = max_times(target)
    binary_str = dec_to_bin(target, max_twos)
    print 'Your result: {}'.format(binary_str)
    print 'actual result: {:8}'.format(str(bin(int(binary_str,2))))

main()
