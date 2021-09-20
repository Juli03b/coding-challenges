# LINK TO LEETCODE: https://leetcode.com/problems/find-the-town-judge/
from typing import List

def find_judge(n: int, trust: List[List[int]]) -> int:
    """
    In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

    If the town judge exists, then:

        1. The town judge trusts nobody. 
        2. Everybody (except for the town judge) trusts the town judge.
        
        There is exactly one person that satisfies properties 1 and 2. You are given an array trust where trust[i] = [ai, bi]
        representing that the person labeled ai trusts the person labeled bi.

    Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

    Example 1:

        Input: n = 2, trust = [[1,2]]
        Output: 2

    Example 2:

        Input: n = 3, trust = [[1,3],[2,3]]
        Output: 3

    Example 3:

        Input: n = 3, trust = [[1,3],[2,3],[3,1]]
        Output: -1

    Example 4:

        Input: n = 3, trust = [[1,2],[2,3]]
        Output: -1

    Example 5:

        Input: n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
        Output: 3
    """
    if not n: return -1
    if not trust and n == 1: return 1

    get_is_judge_by_label = dict()
    get_trusters_by_trustee = dict()

    # Loop over trust and any person that trusts should be set to false in people dict,
    # because the judge trusts no one.
    for truster, trustee in trust: 
        get_is_judge_by_label[truster] = False

        # Add truster to trustee's truster set
        trustee_set = get_trusters_by_trustee.get(trustee, set())
        trustee_set.add(truster)

        # Set the set to the set in the object (it is a diffrent reference)
        get_trusters_by_trustee[trustee] = trustee_set

    for truster, trustee in trust:
        # If there are n - 1 unquie labels (people) in the trustee set,
        #  and the person hasn't trusted anyone return their label.
        if len(get_trusters_by_trustee.get(trustee)) == n - 1 and get_is_judge_by_label.get(trustee, True):
            return trustee
    return -1
# 4
# [[1,2],[1,3],[2,1],[2,3],[1,4],[4,3],[4,1]]
print(find_judge(1, [[1,2],[1,3],[2,1],[2,3],[1,4],[4,3],[4,1]]))