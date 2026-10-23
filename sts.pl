student(ravi,  cs101).
student(anita, cs102).
student(kiran, cs101).

teacher(kumar, cs101).
teacher(devi,  cs102).

subject(cs101, 'Data Structures').
subject(cs102, 'Operating Systems').

teaches(T, Subject) :- teacher(T, C), subject(C, Subject).
taught_by(S, T)     :- student(S, C), teacher(T, C).