from threading import Event

class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.cnt = 0
        self.print_ = [Event(), Event(), Event()]
        self.print_[2].set()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        self.print_[2].wait()
        self.print_[2].clear()
        printNumber(0)
        self.cnt += 1
        self.print_[self.cnt % 2].set()

    def even(self, printNumber):
        self.print_[0].wait()
        self.print_[0].clear()
        self.cnt += 1
        self.print_[2].set()

    def odd(self, printNumber):
        self.print_[1].wait()
        self.print_[1].clear()
        self.cnt += 1
        self.print_[2].set()
