# treating multiple inheritance


class T:
    def __init__(self, number):
        self.number = number

    def print(self):
        print(self.number)


class DT1(T):
    pass

    def __init__(self, number):
        # self.number = number
        super().__init__(number)
        print("DT1")

    def print(self):
        # super().print()
        print("print DT1")

        # does not support overloading
        # def print(self, value):
        #     pass


class DT2(T):
    def __init__(self, number):
        super().__init__(number + 10)
        print("DT2")

    def print(self):
        print("print DT2")


class DT(T):
    def __init__(self, number):
        super().__init__(number + 10)
        print("DT")


class DDT(DT, DT1, DT2):
    def __init__(self, number):
        super().__init__(number)


class T1:
    def print(self):
        print(10)
    __print = print


class T2(T1):
    def print(self):
        print(20)


class T3:
    def print(self):
        print(30)


# treating abstract methods


from abc import ABC, abstractmethod  # ABC abstract base class


class Parse(ABC):

    @abstractmethod
    def parse(self, item):
        pass

    def xprint(self):
        pass


class ParseInt(Parse):
    def parse(self, item):
        print(str(item))


class ParseStr(Parse):
    def parse(self, item):
        print(item)


if __name__ == "__main__":
    # dt1 = DT1(123)
    # dt1.print()
    #
    # ddt = DDT(123)
    # ddt.print()

    # t2 = T2()
    # t2.print()
    # t2._T1__print()
    #
    # mlist = [T1()] * 5
    # mlist.extend([T2()] * 5)
    # for item in mlist:
    #     item.print()

    ...

    # parse = Parse()
    parseint = ParseInt()
    parseint.parse(123)
    parsestr = ParseStr()
    parsestr.parse("mfdt")
    parsestr.xprint()

    # isinstance
    print(isinstance(parseint, ParseInt))
    print(issubclass(ParseInt, Parse))
    print(issubclass(ParseInt, ParseStr))
    print(issubclass(type(parsestr), Parse))











