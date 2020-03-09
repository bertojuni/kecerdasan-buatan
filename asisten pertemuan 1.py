from kanren.facts import Relation, facts, fact
from kanren.core import var, run, conde

def get_sibling(x, y):
    temp = var()
    return conde((parent(temp, x), parent(temp, y)))

if __name__=='__main__':    
    parent = Relation()

    facts(parent, ("Homer", "Bart"),
                  ("Homer", "Lisa"),
                  ("Abe",  "Homer"))
    
    # bisa juga ditulis dalam fact terpisah seperti ini
    # fact(parent, "Homer", "Bart")
    # fact(parent, "Homer", "Lisa")
    # fact(parent, "Abe",  "Homer")

    x = var()
    output = run(0, x, parent(x, "Bart"))
    print("\nNama ayah Bart : ", output)

    ### contoh definisi saudara (sibling) menggunakan relasi baru
    sibling = Relation()
    facts(sibling, ("Bart", "Lisa"),
                   ("Lisa", "Bart"))
    brother = run(0, x, sibling(x, "Lisa"))
    print("\nNama saudara laki-laki Lisa : ", brother[0])
    sister = run(0, x, sibling(x, "Bart"))
    print("\nNama saudara perempuan Bart : ", sister[0])

    ''' 
        contoh definisi saudara (sibling) 
        menggunakan relasi yang sudah ada (parent)
    '''
    siblings = run(0, x, get_sibling(x, "Bart"))
    siblings = [x for x in siblings if x != "Bart"]
    print("\nNama saudara Bart : ")
    for item in siblings:
        print(item)