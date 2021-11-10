conjunto = {11, 22, 33, 44, 55}
sub = {11, 22}

print(sub.issubset(conjunto))
print(conjunto.issuperset(sub))
print(sub.isdisjoint(conjunto))
print(conjunto.isdisjoint(sub))
