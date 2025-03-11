"""It is well known that for any instance of the stable matching problem, a stable matching
exists, and the Gale-Shapley algorithm returns one such matching. However, the Gale-Shapley algorithm does not provide
much insight into the other stable matchings which may exist. In this question, we aim to find the set of all stable matchings.
A natural approach would be to (i) enumerate all possible matchings, and then (ii) check the stability of each matching. Part
(a), (b) and (c) below are designed to achieve this task in consecutive steps.
Consider an instance with n men and n women. Observe that fixing the order of men as [1,2,...,n], a matching can be
defined by the order of the women. For instance, if we have three men whose order is fixed to [1,2,3] and we order three
women as [2,3,1], we will be describing the matching {(man1,woman2),(man2,woman3),(man3,woman1)}. Therefore, we can find all possible matchings between men and women by simply fixing the order of men as [1,2,...,n] and
finding all possible orderings of women.
The pseudocode below provides a function that can be used to enumerate all possible ordering of women. For instance,
executing Orders(All, [1,2,3], []) for an empty array All = [] would yield
All = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]].
Implement a Python function, Orders(), for the Orders algorithm provided as in above pseudocode. Note that this
function should not have any return value.
Given a list of all matchings between n men and n women, along with the mens’ and women’s preferences, your task is
to devise an algorithm that returns the number of stable matchings. Consider the stable matching instance with 7 men
and 7 women (each group indexed by 0 to 6) defined by the preference matrices below. Starting indices by 0, row i of
MenPreferences (WomenPreferences) provides the list of woman (man) indices in the preference order of man (woman)
indexed by i, from the most preferred to the least. For example, the first man, indexed by 0, prefers the woman indexed
by 5 the most and the woman indexed by 1 the least (see below code snippets). Provide a python function, named
FindAllStableMatchings() that returns the total number of stable matchings."""

def Orders(Array,Start,End):
    if not Start:
        Array.append(End)
    else:
        n=len(Start)
        for i in range(n):
            NextEnd=End+[Start[i]]  
            NextStart=Start[:i]+Start[i+1:]  
            Orders(Array,NextStart,NextEnd)  
def is_stable(match, MenPref, WomenPref):
    n=len(match)
   
    woman_for_man=match
    man_for_woman=[0]*n
    for man,woman in enumerate(match):
        man_for_woman[woman]=man
    
    for m in range(n):
        for w in range(n):
            current_woman=woman_for_man[m]
            current_man=man_for_woman[w]
            
            if MenPref[m].index(w)<MenPref[m].index(current_woman):
                if WomenPref[w].index(m)<WomenPref[w].index(current_man):
                    return False
    return True

def FindAllStableMatchings(MenPref,WomenPref):
    n=len(MenPref)
    all_matches = []
    Orders(all_matches,list(range(n)), [])
    
    stable_count = 0
    for match in all_matches:
        if is_stable(match,MenPref,WomenPref):
            stable_count+=1
            
    return stable_count

MenPref = [
    [5, 6, 4, 2, 0, 3, 1],
    [0, 5, 1, 2, 4, 3, 6],
    [3, 6, 1, 2, 5, 0, 4],
    [1, 2, 5, 0, 6, 4, 3],
    [6, 0, 2, 4, 3, 1, 5],
    [2, 1, 4, 0, 3, 6, 5],
    [5, 6, 4, 2, 0, 1, 3]
]

WomenPref = [
    [0, 4, 3, 1, 5, 2, 6],
    [5, 1, 4, 6, 3, 2, 0],
    [1, 5, 4, 2, 6, 3, 0],
    [0, 1, 4, 5, 3, 2, 6],
    [5, 2, 4, 1, 0, 6, 3],
    [5, 6, 3, 2, 0, 1, 4],
    [2, 6, 5, 3, 4, 0, 1]
]

nstable=FindAllStableMatchings(MenPref,WomenPref)
print(nstable) 