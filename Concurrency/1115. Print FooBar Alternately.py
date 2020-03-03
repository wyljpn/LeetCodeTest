from threading import Lock
class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()

        # Don't start with bar
        self.bar_lock.acquire()

    def foo(self, printFoo):
        for i in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar):
        for i in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()


from threading import Semaphore
class FooBar_1(object):
    def __init__(self, n):
        self.n = n
        self.foo_sema = Semaphore(1)
        self.bar_sema = Semaphore(0)

    def foo(self, printFoo):
        for i in range(self.n):
            self.foo_sema.acquire()
            printFoo()
            self.bar_sema.release()

    def bar(self, printBar):
        for i in range(self.n):
            self.bar_sema.acquire()
            printBar()
            self.foo_sema.release()


import threading
from typing import Callable, Optional

class FooBar_2:
    def __init__(self, n: int) -> None:
        self.n = n
        self.condition = threading.Condition()
        self.last_printed: Optional[str] = None

    def foo(self, printFoo: Callable[[], None]) -> None:
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda: self.last_printed in (None, 'bar'))
                printFoo()
                self.last_printed = 'foo'
                self.condition.notify()

    def bar(self, printBar: Callable[[], None]) -> None:
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda: self.last_printed == 'foo')
                printBar()
                self.last_printed = 'bar'
                self.condition.notify()


# Raise a barrier which makes both threads wait for each other before they are allowed to continue.
# foo prints before reaching the barrier.
# bar prints after reaching the barrier.
from threading import Barrier

class FooBar_3:
    def __init__(self, n):
        self.n = n
        self.barrier = Barrier(2)

    def foo(self, printFoo):
        for i in range(self.n):
            printFoo()
            self.barrier.wait()

    def bar(self, printBar):
        for i in range(self.n):
            self.barrier.wait()
            printBar()


# Each thread can wait on each other to set their corresponding foo_printed and bar_printed events.
# Each thread also resets the corresponding printed events with .clear() for the next loop iteration.
from threading import Event
class FooBar_4:
    def __init__(self, n):
        self.n = n
        self.foo_printed = Event()
        self.bar_printed = Event()
        self.bar_printed.set()

    def foo(self, printFoo):
        for i in range(self.n):
            self.bar_printed.wait()
            self.bar_printed.clear()
            printFoo()
            self.foo_printed.set()

    def bar(self, printBar):
        for i in range(self.n):
            self.foo_printed.wait()
            self.foo_printed.clear()
            printBar()
            self.bar_printed.set()

