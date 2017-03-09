def check(a):
    if isinstance(a,str):
      raise KeyError('input wasn\'t a number')

    if a % 3 == 0 and a % 5 == 0:
        return u'FizzBuzz'
    if a % 3 == 0:
        return u'Fizz'
    if a % 5 == 0:
        return u'Buzz'

    return a


if __name__ == '__main__':
    import sys

    # the only valid input is a positive integer
    if not sys.argv[1].isdigit():
      raise KeyError('input wasn\'t a positive integer')

    try:
        for num in xrange(1, int(sys.argv[1])):
            print check(num)
    except Exception:
        print 'failed'
