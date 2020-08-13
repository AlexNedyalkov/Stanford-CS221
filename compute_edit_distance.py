def compute_edit_distance(s, t):
    cache = {}  # (m, n) => result
    """
    Returns the maximum edit distance between s and t
    :param s: string s
    :param t: string t
    :return: function recurse
    """
    def recurse(m : int, n : int):

        if (m, n) in cache:
            return cache[(m, n)]
        if m == 0:  # Base case
            result =  n
        elif n == 0: # Base case
            result =  m
        elif s[m - 1] == t[n - 1]: # Last letter matches
            return recurse(m-1, n-1)
        else:

            subCost = 1 + recurse(m -1, n - 1)
            delCost = 1 + recurse(m-1, n)
            insCost = 1 + recurse(m, n-1)

            result =  min(subCost, delCost, insCost)

        cache[(m, n)] = result

        return result


    return recurse(len(s), len(t))

print(compute_edit_distance("dcats" * 10, "cat" * 10))