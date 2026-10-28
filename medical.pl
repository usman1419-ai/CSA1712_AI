% Patient symptoms
has(john,  fever).
has(john,  cough).
has(john,  body_ache).

has(mary,  sneezing).
has(mary,  runny_nose).
has(mary,  sore_throat).

has(ravi,  fever).
has(ravi,  chills).
has(ravi,  sweating).

has(anita, fever).
has(anita, headache).
has(anita, stomach_pain).

has(kumar, high_thirst).
has(kumar, frequent_urination).
has(kumar, fatigue).

% Diagnosis rules
diagnose(P, flu)      :- has(P, fever), has(P, cough), has(P, body_ache).
diagnose(P, cold)     :- has(P, sneezing), has(P, runny_nose), has(P, sore_throat).
diagnose(P, malaria)  :- has(P, fever), has(P, chills), has(P, sweating).
diagnose(P, typhoid)  :- has(P, fever), has(P, headache), has(P, stomach_pain).
diagnose(P, diabetes) :- has(P, high_thirst), has(P, frequent_urination), has(P, fatigue).

% Treatment advice
advice(flu,      'Rest, fluids and paracetamol. Consult a doctor if fever persists.').
advice(cold,     'Rest, warm fluids, steam inhalation.').
advice(malaria,  'Consult a doctor immediately for a blood test and antimalarial drugs.').
advice(typhoid,  'Consult a doctor, take antibiotics as prescribed, drink boiled water.').
advice(diabetes, 'Check blood sugar, follow a diet plan and consult a doctor.').

report(P) :-
    diagnose(P, D),
    write(P), write(' may have '), write(D), nl,
    advice(D, A), write('Advice: '), write(A), nl.
report(P) :-
    \+ diagnose(P, _),
    write('No diagnosis possible for '), write(P), nl.