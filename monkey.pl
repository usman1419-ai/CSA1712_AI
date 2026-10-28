% state(MonkeyPosition, OnFloor/OnBox, BoxPosition, HasBanana)

place(atdoor).
place(middle).
place(atwindow).

% move(State, Action, NewState)
move(state(middle, onbox, middle, hasnot), grasp,
     state(middle, onbox, middle, has)).

move(state(P, onfloor, P, H), climb,
     state(P, onbox, P, H)).

move(state(P1, onfloor, P1, H), push(P1, P2),
     state(P2, onfloor, P2, H)) :- place(P2), P1 \= P2.

move(state(P1, onfloor, B, H), walk(P1, P2),
     state(P2, onfloor, B, H)) :- place(P2), P1 \= P2.

solve(state(_, _, _, has), _, []).
solve(S1, Visited, [Action|Rest]) :-
    move(S1, Action, S2),
    \+ member(S2, Visited),
    solve(S2, [S2|Visited], Rest).

% finds the shortest plan first
plan(Start, Plan) :-
    length(Plan, _),
    solve(Start, [Start], Plan).

canget(State) :- plan(State, _).

print_plan([]).
print_plan([A|T]) :- write(A), nl, print_plan(T).

run :-
    plan(state(atdoor, onfloor, atwindow, hasnot), Plan),
    print_plan(Plan).