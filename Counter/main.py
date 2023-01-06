class Counter:
    def __init__(self):
        self.value = 0
    
    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def reset(self):
        self.value = 0


if __name__ == '__main__':
    c = Counter()
    print(f"Initial value: {c.value}")
    c.increment()
    print(f"Value after one increment: {c.value}")
    c.increment()
    c.increment()
    print(f"Value after two extra increment: {c.value}")
    c.decrement()
    print(f"Value after one decrement: {c.value}")
    c.reset()
    print(f"Value after reset: {c.value}")