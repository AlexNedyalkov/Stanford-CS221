def compute_edit_distance(s : str, t : str):
    """
    Returns the maximum edit distance between s and t
    :param s: string s
    :param t: string t
    :return: function recurse
    """
    def recurse(m : int, n : int):

        if m == 0:
            return n
        elif n == 0:
            return m
        elif s[m - 1] == t[n - 1]: # Last letter matches
            recurse(m-1, n-1)
        else:

            subCost = 1 + recurse(m -1, n - 1)
            delCost = 1 + recurse(m-1, n)
            insCost = 1 + recurse(m, n-1)

            return min(subCost, delCost, insCost)


    return recurse(len(s), len(t))
