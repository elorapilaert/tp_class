class Point :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def norm(self):
        return (self.x**2+self.y**2)**(1/2)



# pour tester

try:
    p = Point(3, 4)
    assert (p.x, p.y) == (3, 4)
    assert p.norm() == 5.0
    assert repr(p) == "Point(3, 4)"
    q = Point(0, 1)
    assert (q.x, p.x) == (0, 3)
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')

print(p)

# 1) ce sont les 2 même fonctions
# 2) on ne donne pas d'argument à la fonction norm(), appeler p.norm() revient à donner un argument à une fonction qui n'en nécessite pas...
# 3) On affiche la même chose qu'avec __repr__ mais les deux éléments n'ont pas le même type dans python 

class Bad:
    def __init__(self):
        items=[]
        self.items=items

    def add(self, x):
        self.items.append(x)

a, b = Bad(), Bad()
a.add(1)
print(b.items)

# 1) car si on rajoute un élément dans items (initialisé dans Bad) cela le rajoute dans les items de tous les élémens de Bad
# 2) en rajoutant un attribut items au self, celui-ci est lié simplement à l'élément choisi et non à l'ensemble des éléments de Bad


class Tirelire :
    def __init__(self):
            pieces=[]
            self.pieces=pieces

    def deposit(self, value : float):
        if value<=0 :
            raise ValueError
        
        else :
            self.pieces.append(value)

    def total(self) :
        res=0
        for x in self.pieces :
            res+=x
        return res

    def __len__(self):
        return len(self.pieces)
    
    def __repr__(self) :
        return f"Tirelire({len(self)} coins, total={self.total()})"

# pour tester


# pour tester

try:
    t = Tirelire()
    t.deposit(0.5)
    t.deposit(1)
    assert len(t) == 2
    assert t.total() == 1.5
    assert repr(t) == "Tirelire(2 coins, total=1.5)"
    other = Tirelire()
    assert len(other) == 0
    try:
        other.deposit(-1)
    except ValueError:
        pass
    else:
        raise Exception("a negative value should raise ValueError")
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')





