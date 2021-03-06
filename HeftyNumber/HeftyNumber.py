import numpy as np
import math

class HeftyNumber:
    def __init__(self,baseCoef=0,base:"integer base"=10):
        self.base = base

        if type(baseCoef) is not int:
            self.baseCoef = baseCoef
        else:
            self.baseCoef = self.b10bn(baseCoef, base)

        self.base10 = self.__toB10()

    #TODO: add support for hefty number +=
    def __iadd__(self, rhs):
        self.base10 += rhs
        self.baseCoef = self.b10bn(int(self.base10), self.base)
        return self

    def __repr__(self):
        return str(self.baseCoef)+"b"+str(self.base)

    def __add__(self, heftyNum):
        return self.base10 + heftyNum.base10

    def __toB10(self):
        rVect = self.baseVect(self.base, self.baseCoef.shape[1] - 1)
        return self.baseCoef * rVect.T

    #### Digit access
    def __getitem__(self,idx):
        return self.baseCoef.item(self.baseCoef.shape[1]-1-idx)

    def __setitem__(self):
        pass

    def __delitem__(self):
        pass
    #####

    def plus(self,heftyNum,newBase=10):
        if type(heftyNum) is HeftyNumber:
            return HeftyNumber(self.b10bn(self.base10 + heftyNum.base10, newBase),newBase)
        else:
            return HeftyNumber(self.b10bn(self.base10 + heftyNum, newBase), newBase)

    def argmin_s(self, x, base, power) -> "[min,arg_min]":
        fundamental = base ** power
        argMin = int(x/fundamental)
        min = int(argMin * fundamental)

        return [x - min, argMin]

    def powerVect(self,base, len):
        num = [1]

        if len == 1:
            return np.array(num)
        else:
            r = 1
            for i in range(len-1):
                r = base * r
                num = [r] + num

            return np.matrix(num)

    def subtract(self,vect,scalar):
        pass

    def baseVect(self, base, n):
        num = [1]

        r = 1
        for i in range(n):
            r = base * r
            num = [r] + num

        return np.matrix(num)

    def b10bn(self,b10Num, base) -> "ndarry":
        if (base == 1):
            return np.ones(b10Num)
        if (b10Num == 0):
            return np.matrix([[0]])
        if (b10Num == 1):
            return np.matrix([[1]])

        logNum = math.log10(b10Num)/math.log10(base)
        num    = []

        if logNum % 1 == 0:
            nDigits = int(logNum) + 1
        else:
            nDigits = math.ceil(logNum)

        for i in range(nDigits - 1, 0, -1):
            b10Num, idx = self.argmin_s(b10Num, base, i)
            num.append(idx)

        num.append(b10Num)

        return np.matrix(num)

    def n(self):
        return self.baseCoef.shape[1]

    def paddedNum(self,len,paddingNum=0):
        paddedM = np.matrix(self.baseCoef)
        nPadd   = len-paddedM.shape[1]

        for i in range(nPadd):
            paddedM = np.insert(paddedM,0,paddingNum)

        return paddedM

    def b10(self):
        return int(self.base10)

    def bn(self, n):
        b10Num = self.b10()
        return self.b10bn(b10Num,n)

    def map2Lex(self,translationDict={0:'a',1:'b',2:'c',3:'d'}):
        map = []
        for i in np.nditer(self.baseCoef):
            map.append(translationDict[int(i)])

        return np.matrix(map)


