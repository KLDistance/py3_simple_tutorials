# when you want to make sub-class holding difference properties, but the functions are the same, do as follows

class Gun : 
    def __init__(self) :
        pass
    def Shot(self) : 
        pass

class Pistol(Gun) :
    # rewrite the shot function in Gun (base) class
    def Shot(self) :
        print("single 2.4 mm bullet is shot!")

class ShotGun(Gun) :
    # rewrite the shot function in Gun (base) class
    def Shot(self) :
        print("Cluster 3.0 mm bullets are shot!")

gun_list = [Pistol(), Pistol(), ShotGun(), Pistol()]
for iter in gun_list : 
    iter.Shot()
# but list can actually store different types, so you can also do as follows
class A :
    def Shot(self) :
        print("AAA")
class B :
    def Shot(self) :
        print("BBB")

clist = [A(), B(), A(), B()]
for iter in clist : 
    iter.Shot()