male(john).   male(tom).    male(bob).
female(susan). female(mary). female(anna). female(alice).

parent(john, tom).   parent(susan, tom).
parent(john, mary).  parent(susan, mary).
parent(tom, bob).    parent(anna, bob).
parent(tom, alice).  parent(anna, alice).

father(X, Y)  :- parent(X, Y), male(X).
mother(X, Y)  :- parent(X, Y), female(X).
child(X, Y)   :- parent(Y, X).
son(X, Y)     :- child(X, Y), male(X).
daughter(X, Y):- child(X, Y), female(X).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
grandfather(X, Z) :- grandparent(X, Z), male(X).
grandmother(X, Z) :- grandparent(X, Z), female(X).

sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
brother(X, Y) :- sibling(X, Y), male(X).
sister(X, Y)  :- sibling(X, Y), female(X).

uncle(X, Y) :- brother(X, P), parent(P, Y).
aunt(X, Y)  :- sister(X, P), parent(P, Y).

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).