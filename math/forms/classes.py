import os
import sys
import math


class Quadrat:
    def __init__(self, a=None, b=None, u=None, A=None):
        super.__init__()
        self.u = u
        self.b = b
        self.a = a
        self.A = A
        self.t = None

    def Umfang(self):
        if self.u is None:
            self.u = self.a * 2 + self.b * 2
        return self.u

    def Fläche(self):
        if self.A is None:
            self.A = self.a * self.b
        return self.A

    def umstellen(self):
        if self.a is None:
            self.t = self.u / (self.b * 2)
            self.a = self.t / 2
            return self.a
        elif self.b is None:
            self.t = self.u / (self.a * 2)
            self.a = self.t / 2
            return self.b


class Dreieck:
    def __init__(self):
        super.__init__()


class Drache:
    def __init__(self, e=None, f=None, u=None, A=None):
        super.__init__()
        self.u = u
        self.f = f
        self.e = e
        self.A = A
        self.t = None

    def Umfang(self):
        if self.u is None:
            self.u = self.e * 2 + self.f * 2
        return self.u

    def Fläche(self):
        if self.A is None:
            self.t = self.e * self.f
            self.A = self.t / 2
        return self.A

    def umstellen(self):
        if self.e is None:
            self.t = self.u / (self.f * 2)
            self.e = self.t / 2
            return self.e
        elif self.f is None:
            self.t = self.u / (self.e * 2)
            self.e = self.t / 2
            return self.f


class Paralelogramm:
    def __init__(self, a=None, b=None, u=None, A=None):
        super.__init__()
        self.u = u
        self.b = b
        self.a = a
        self.A = A
        self.t = None

    def Umfang(self):
        if self.u is None:
            self.u = self.a * 2 + self.b * 2
        return self.u

    def Fläche(self):
        if self.A is None:
            self.A = self.a * self.b
        return self.A

    def umstellen(self):
        if self.a is None:
            self.t = self.u / (self.b * 2)
            self.a = self.t / 2
            return self.a
        elif self.b is None:
            self.t = self.u / (self.a * 2)
            self.a = self.t / 2
            return self.b


class Viereck:
    def __init__(self, a=None, b=None, u=None, A=None):
        super.__init__()
        self.u = u
        self.b = b
        self.a = a
        self.A = A
        self.t = None

    def Umfang(self):
        if self.u is None:
            self.u = self.a * 2 + self.b * 2
        return self.u

    def Fläche(self):
        if self.A is None:
            self.A = self.a * self.b
        return self.A

    def umstellen(self):
        if self.a is None:
            self.t = self.u / (self.b * 2)
            self.a = self.t / 2
            return self.a
        elif self.b is None:
            self.t = self.u / (self.a * 2)
            self.a = self.t / 2
            return self.b


class raute:
    def __init__(self, e=None, f=None, u=None, A=None):
        super.__init__()
        self.u = u
        self.f = f
        self.e = e
        self.A = A
        self.t = None

    def Umfang(self):
        if self.u is None:
            self.u = self.e * 2 + self.f * 2
        return self.u

    def Fläche(self):
        if self.A is None:
            self.t = self.e * self.f
            self.A = self.t / 2
        return self.A

    def umstellen(self):
        if self.e is None:
            self.t = self.u / (self.f * 2)
            self.e = self.t / 2
            return self.e
        elif self.f is None:
            self.t = self.u / (self.e * 2)
            self.e = self.t / 2
            return self.f
