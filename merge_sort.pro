split([], [], []).
split([X], [X], []).
split([L, R | Rest], [L | RemainingLeft], [R | RemainingRight]) :-
    split(Rest, RemainingLeft, RemainingRight).

myMerge(X, [], X).
myMerge([], X, X).
myMerge([LH | LR], [RH | RR], Result) :-
    LH >= RH,
    myMerge([LH | LR], RR, RemainingMerged),
    append([RH], RemainingMerged, Result).
myMerge([LH | LR], [RH | RR], Result) :-
    LH < RH,
    myMerge(LR, [RH | RR], RemainingMerged),
    append([LH], RemainingMerged, Result).

mergeSort([], []).
mergeSort([X], [X]).
mergeSort(List, X) :-
    split(List, Left, Right),
    mergeSort(Left, SortedLeft),
    mergeSort(Right, SortedRight),
    !,
    myMerge(SortedLeft, SortedRight, X).
