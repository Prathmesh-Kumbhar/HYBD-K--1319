# Herarchichal Inheritance

# Parent class (Base class)
class A:
    def m1(self):
        property=["Car","House","Money","Gold","Bike","Farm","Iphone"]
        print(property)

# B inherits from A (Single + Hierarchical Inheritance)
class B(A):
    def m2(self):
        prop1=["Car","House","Money"]
        print(prop1)

# C also inherits from A (Hierarchical Inheritance)
class C(A):
    def m3(self):
        prop2=["Gold","Bike","Farm"]
        print(prop2)

# Independent class (no inheritance from A)
class D:
    def m4(self):
        property1=["Car","House","Money","Gold","Bike","Farm"]
        print(property1)

# F inherits from both C and D (Multiple Inheritance)
class F(C,D):
    def m5(self):
        pass

# E inherits from B (Multilevel Inheritance: A - B - E)
class E(B):
    def m6(self):
        prop1=["Iphone"]
        print(prop1)

# G inherits from E (Multilevel Inheritance: A - B - E - G)
class G(E):
    def m7(self):
        prop=["Farm","New House"]
        print(prop)

# Creating object of class G and access the elements
jay=G()
jay.m1()
jay.m2()
jay.m6()
jay.m7()

print("-"*60)

# Creating object of class F and access the elements
viru=F()
viru.m1()
viru.m3()
viru.m4()
viru.m5()

# The parent of Class A
print(A.__mro__)    # (<class '__main__.A'>, <class 'object'>)

# The parent of Class B
print(B.__mro__)    # (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

# The parent of Class C
print(C.__mro__)    #c(<class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# The parent of Class D
print(D.__mro__)    # (<class '__main__.D'>, <class 'object'>)

# The parent of Class E
print(E.__mro__)    # (<class '__main__.E'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

# The parent of Class F
print(F.__mro__)    # (<class '__main__.F'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.D'>, <class 'object'>)

# The parent of Class G
print(G.__mro__)    # (<class '__main__.G'>, <class '__main__.E'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
















