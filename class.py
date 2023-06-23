class A:
    def __init__(self,a,b,c):
        self.__a=a
        self._b=b
        self.c=c
    def display(self):
        print("class A Values:")
        print("a =", self.__a)
        print("b =", self._b)
        print("c =", self.c)
class Exception(Exception):
    pass
class B(A):
    def display(self):
        super().display()
        try:
            print("class B Values:")
            raise Exception("Cannot access 'a' as it is a private member")
        except Exception as e:
            print("Exception:", str(e))
        finally:
            print("b =", self._b)
            print("c =", self.c)
o=B(1,2,3)
o.display()