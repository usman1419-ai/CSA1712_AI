person(john,  date(15, 8, 2000)).
person(mary,  date(3, 12, 1999)).
person(ravi,  date(21, 5, 2001)).

born_in_year(Name, Year) :- person(Name, date(_, _, Year)).