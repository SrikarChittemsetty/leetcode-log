from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord("a")] += 1

            groups[tuple(count)].append(word)

        return list(groups.values())


def normalize(groups):
    return sorted(sorted(group) for group in groups)


if __name__ == "__main__":
    s = Solution()
    assert normalize(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == normalize(
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    )
    assert normalize(s.groupAnagrams([""])) == normalize([[""]])
    assert normalize(s.groupAnagrams(["a"])) == normalize([["a"]])
