from kanren.facts import Relation, facts
from kanren.core import var, run

father = Relation()
facts(father, ("slamet", "amin"),
      ("slamet", "nanang"),
      ("amin", "badu"),
      ("amin", "budi"),
      ("anang", "didi"),
      ("anang", "firman"),
      ("anang", "reka"))
x = var()
anak = run(1, x, father(x, "amin"))
print("Nama Ayahnya : ", anak[0])
