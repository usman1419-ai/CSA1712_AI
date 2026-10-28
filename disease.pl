diet(diabetes,      'Low sugar, high fibre, whole grains, green vegetables').
diet(hypertension,  'Low salt, fruits, vegetables, low-fat dairy').
diet(obesity,       'Low calorie, high protein, plenty of vegetables and water').
diet(anaemia,       'Iron-rich foods: spinach, beetroot, dates, pulses, citrus fruits').
diet(heart_disease, 'Low fat, low cholesterol, oats, nuts, fish').
diet(typhoid,       'Soft, bland, easily digestible food, boiled water, banana, rice').

avoid(diabetes,      'Sweets, sugary drinks, white bread, fried food').
avoid(hypertension,  'Pickles, processed food, excess salt, caffeine').
avoid(obesity,       'Fast food, sugary drinks, fried snacks').
avoid(anaemia,       'Tea or coffee with meals, junk food').
avoid(heart_disease, 'Red meat, butter, fried food, excess salt').
avoid(typhoid,       'Spicy, oily and raw food, street food').

suggest_diet(Disease) :-
    diet(Disease, Eat),
    avoid(Disease, Avoid),
    write('Disease : '), write(Disease), nl,
    write('Eat     : '), write(Eat), nl,
    write('Avoid   : '), write(Avoid), nl.
suggest_diet(Disease) :-
    \+ diet(Disease, _),
    write('No diet information available for '), write(Disease), nl.