# iterators and generators

# shift + F6 refactor and replace a name ex: iter1

list1 = [i for i in range(1000)]

print(sum(list1))

iter1 = (i for i in range(1000))
print(sum(iter1))
# for i in iter1:
#     print(i)


class odd_nos:
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            current_no = self.num
            self.num += 2
            return current_no
        else:
            raise StopIteration()


for i in odd_nos(100):
    print(i)



