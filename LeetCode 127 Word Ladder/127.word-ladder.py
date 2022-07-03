#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def is_differ_by_a_letter(self, w1, w2):
        flag = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                flag += 1
                if flag > 1:
                    return False
        if flag == 1:
            return True
        else:
            return False

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        queue = collections.deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        while queue:
            word, step = queue.popleft()

            if self.is_differ_by_a_letter(word, endWord):
                return step+1

            for wl in wordList:
                if wl in visited:
                    continue
                if self.is_differ_by_a_letter(word, wl):
                    queue.append((wl, step+1))
                    visited.add(wl)
        return 0

# @lc code=end

