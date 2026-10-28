fruit_color(apple,       red).
fruit_color(apple,       green).
fruit_color(banana,      yellow).
fruit_color(mango,       yellow).
fruit_color(mango,       green).
fruit_color(grapes,      green).
fruit_color(grapes,      purple).
fruit_color(orange,      orange).
fruit_color(strawberry,  red).
fruit_color(cherry,      red).

% all fruits of a given colour (forced backtracking with fail)
fruits_of(Color) :-
    fruit_color(Fruit, Color),
    write(Fruit), nl,
    fail.
fruits_of(_).

% all colours of a given fruit
colors_of(Fruit) :-
    fruit_color(Fruit, Color),
    write(Color), nl,
    fail.
colors_of(_).

% list everything
show_all :-
    fruit_color(F, C),
    write(F), write(' is '), write(C), nl,
    fail.
show_all.