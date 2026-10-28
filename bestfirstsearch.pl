% Directed graph
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(e, g).
edge(f, g).

% Heuristic values (estimated cost to goal g)
h(a, 10).
h(b, 6).
h(c, 8).
h(d, 7).
h(e, 3).
h(f, 4).
h(g, 0).

% Open list holds paths (head = current node, stored reversed)
best_first(Start, Goal, Path) :-
    bfs([[Start]], Goal, RevPath),
    reverse(RevPath, Path).

bfs([[Goal|Rest]|_], Goal, [Goal|Rest]).
bfs([[N|Rest]|Queue], Goal, Path) :-
    N \= Goal,
    findall([M, N|Rest],
            ( edge(N, M), \+ member(M, [N|Rest]) ),
            NewPaths),
    append(Queue, NewPaths, Open),
    sort_by_h(Open, Sorted),
    bfs(Sorted, Goal, Path).

% sort open list by heuristic of the head node (lowest h first)
sort_by_h(Paths, Sorted) :-
    findall(H-P, ( member(P, Paths), P = [N|_], h(N, H) ), Pairs),
    keysort(Pairs, SortedPairs),
    findall(P, member(_-P, SortedPairs), Sorted).