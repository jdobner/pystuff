def append_score(score, scores=None):
    if not scores:
        scores = [score]
    else:
        scores.append(score)
    return scores




print(append_score(88))
print(append_score(77))
print(append_score(55, [22,55,88]))