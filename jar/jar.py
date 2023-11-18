class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity of a jar can't be negative")
        else:
            self._capacity = capacity
            self._size = 0


    def __str__(self):
        return f"{self._size * '🍪'}"

    def deposit(self, n):
        if self._size + n <= self._capacity:
            self._size += n
        else:
            raise ValueError("The jar does not have enough space for that many cookies.")

    def withdraw(self, n):
        if self._size >= n:
            self._size -= n
        else:
            raise ValueError("The jar does not have that many cookies.")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


# cookie_jar = Jar(10)
# cookie_jar.deposit(10)
# print(str(cookie_jar))

# cookie_jar.deposit(40)
# print(str(cookie_jar))

# cookie_jar.withdraw(2)
# print(str(cookie_jar))

# cookie_jar.withdraw(20)
# print(str(cookie_jar))

# cookie_jar = Jar(-10)
# cookie_jar.deposit(1)
# print(str(cookie_jar))