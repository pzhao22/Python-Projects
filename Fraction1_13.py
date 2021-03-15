class Fraction():
    def __init__(self,n,d):
        if isinstance(n,int) and isinstance(d,int):
            if d < 0:
                n = -n
                d = -d
            common = gcd(n,d)
            self.num = n // common
            self.den = d // common
        else:
            raise ValueError("Numerator and denominator must be integers")
        

    @property
    def num(self):
        return self._num
    
    @property
    def den(self):
        return self._den
    
    @num.setter
    def num(self,n):
        self._num = n
    
    @den.setter
    def den(self,d):
        self._den = d
    
    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __repr__(self):
        return f"Fraction(num={self.num},den={self.den})"

    def __add__(self,other):
        dNew = self.den * other.den
        nNew = self.num*other.den + other.num*self.den
        return Fraction(nNew,dNew)

    __radd__ = __add__
    __iadd__ = __add__

    def __sub__(self,other):
        dNew = self.den * other.den
        nNew = self.num*other.den - other.num*self.den
        return Fraction(nNew,dNew)

    def __mul__(self,other):
        dNew = self.den * other.den
        nNew = self.num * other.num
        return Fraction(nNew,dNew)
    
    def __truediv__(self,other):
        dNew = self.den * other.num
        nNew = self.num * other.den
        return Fraction(nNew,dNew)

    def __eq__(self,other):
        if self.num == other.num and self.den == other.den:
            return True
        else: 
            return False
    
    def __ne__(self,other):
        if self.num != other.num:
            return True
        else: 
            return False

    def __gt__(self,other):
        float1 = self.num / self.den
        float2 = other.num / other.den
        if float1 > float2:
            return True
        else: 
            return False
    
    def __lt__(self,other):
        float1 = self.num / self.den
        float2 = other.num / other.den
        if float1 < float2:
            return True
        else: 
            return False
    
    def __ge__(self,other):
        float1 = self.num / self.den
        float2 = other.num / other.den
        if float1 >= float2:
            return True
        else: 
            return False
    
    def __le__(self,other):
        float1 = self.num / self.den
        float2 = other.num / other.den
        if float1 <= float2:
            return True
        else: 
            return False


def gcd(m,n):
    while (m % n != 0):
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

def main():
    test1 = Fraction(-2,4)
    test2 = Fraction(2,-4)
    test1 += test2
    print(test1==test2)
    print(test2.__repr__())
main()

