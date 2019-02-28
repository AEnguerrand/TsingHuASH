def score(Tag1,Tag2):
    Set1,Set2 = set(Tag1),set(Tag2)
    inc = len(Set1.intersection(Set2))
    ex1 = len(Set1) - inc
    ex2 = len(Set2) - inc
    return min([inc,ex1,ex2])

