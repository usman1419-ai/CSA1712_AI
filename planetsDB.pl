% planet(Name, PositionFromSun, DiameterKm, Moons)
planet(mercury, 1, 4879,   0).
planet(venus,   2, 12104,  0).
planet(earth,   3, 12756,  1).
planet(mars,    4, 6792,   2).
planet(jupiter, 5, 142984, 95).
planet(saturn,  6, 120536, 146).

has_moons(P)     :- planet(P, _, _, M), M > 0.
bigger_than(A,B) :- planet(A,_,DA,_), planet(B,_,DB,_), DA > DB.