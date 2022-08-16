def solution(w, h):
    if w == h:
        return w * h - w
    elif w < h:
        return w * h - (2 * w)
    else:
        return w * h - (2 * (w - 1))