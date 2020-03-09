from kanren.facts import Relation, facts
from kanren.core import var, run, conde

def grandparent(x, y):
    temp = var()
    return conde((parent(x, temp), parent(temp, y)))

def sibling(x, y):
    temp = var()
    return conde((parent(temp, x), parent(temp, y)))

def uncle(x, y):
    temp = var()
    return conde((parent(temp, x), grandparent(temp, y)))

if __name__=='__main__':
    parent = Relation()

    facts(parent, ("Slamet", "Amin"),
                  ("Slamet", "Anang"),
                  ("Amin", "Badu"),
                  ("Amin", "Budi"),
                  ("Anang", "Didi"),
                  ("Anang", "Dudu"),
                  ("Anang", "Dadi"))

    x = var()

    father = "Slamet"
    anak = run(0, x, parent(father, x))
    print("\nNama anak-anak " + father + ": ")
    for item in anak:
        print(item)

    child = "Amin"
    ayah = run(1, x, parent(x, child))
    print("\nNama ayah " + child + ": ")
    for item in ayah:
        print(item)


    grandpa = run(1, x, grandparent(x, "Didi"))
    print("\nNama kakek Didi : ")
    for item in grandpa:
        print(item)

    sibling = run(0, x, sibling(x, "Didi"))
    sibling = [x for x in sibling if x != "Didi"]
    print("\nNama saudara Didi : ")
    for item in sibling:
        print(item)

    uncle = run(0, x, uncle(x, "Didi"))
    name_father = run(0, x, parent(x, "Didi"))[0]    
    uncle = [x for x in uncle if x != name_father]
    print("\nNama paman Didi : ")
    for item in uncle:
    	print(item)