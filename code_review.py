def check(a):
    if isinstance(a, str):
        raise KeyError('input wasn\'t a number')
        
    if a % 3 == 0 and a % 5 == 0:
        return 'FizzBuzz'
    if a % 3 == 0:
        return u'Fizz'
    if a % 5 == 0:
        return u'Buzz'

    return a


if __name__ == '__main__':
    import sys
    try:
        for num in xrange(1, sys.argv[0]):
            print check(num)
    except Exception:
        print 'failed'
