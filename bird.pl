bird(sparrow).
bird(eagle).
bird(parrot).
bird(crow).
bird(penguin).
bird(ostrich).
bird(kiwi).

cannot_fly(penguin).
cannot_fly(ostrich).
cannot_fly(kiwi).

can_fly(X) :- bird(X), \+ cannot_fly(X).

check(X) :-
    bird(X),
    (   can_fly(X)
    ->  write(X), write(' can fly.'), nl
    ;   write(X), write(' cannot fly.'), nl
    ).
check(X) :-
    \+ bird(X),
    write(X), write(' is not in the bird database.'), nl.