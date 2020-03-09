from kanren.facts import Relation, facts, fact
from kanren.core import var, run
from kanren.goals import membero

ukuran = Relation()
warna = Relation()
gelap = Relation()
jenis = Relation()

facts(ukuran, ("beruang", "besar"),
			  ("gajah", "besar"),
			  ("semuat", "kecil"),
			  ("kucing", "kecil"))
facts(warna,  ("beruang", "cokelat"),
			  ("kucing", "hitam"),
			  ("semut", "hitam"),
			  ("gajah", "kelabu"))
facts(jenis,  ("beruang", "karnivora"),
			  ("kucing", "karnivora"),
			  ("semut", "omnivora"),
			  ("gajah", "herbivora"))
fact(gelap, "hitam")
fact(gelap, "cokelat")

x = var()

herbivora = run(0, x, jenis(x, "karnivora"))
print("hewan jenis karnivora :", herbivora)