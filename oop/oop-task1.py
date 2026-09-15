class ErrorCounter:
    def __init__(self, initial_count: int = 0):
        self._count = initial_count
    def increase(self) -> None:
        self._count += 1
    def get(self) -> int:
        return self._count

counter = ErrorCounter()
for _ in range(3):
    counter.increase()

print(counter.get())