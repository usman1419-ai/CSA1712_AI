hanoi(N) :- move(N, left, right, center).

move(0, _, _, _) :- !.
move(N, From, To, Via) :-
    M is N-1,
    move(M, From, Via, To),
    format('Move disk ~w from ~w to ~w~n', [N, From, To]),
    move(M, Via, To, From).