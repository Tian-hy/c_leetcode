#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList: return []
        found, q, nq = False, {beginWord}, set()
        while q and not found:
            words -= set(q)
            for x in q:
                for y in [x[:i]+c+x[i+1:] for i in range(n) for c in string.ascii_lowercase]:
                    if y in words:
                        if y == endWord: 
                            found = True
                        else: 
                            nq.add(y)
                        tree[x].add(y)
            q, nq = nq, set()
        def bt(x): 
            print(x)
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
        return bt(beginWord)

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

    def findLadders1(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        res, length = [], 0
        queue = collections.deque()
        queue.append((beginWord, 1, (beginWord, ), wordList))

        while queue:
            # print("================")
            # print(queue)
            word, step, visited, wList = queue.popleft()
            if length != 0 and step > length:
                break

            tmp = []
            for idx, wl in enumerate(wList):
                # print(wList, end=", ")
                if self.is_differ_by_a_letter(word, wl):
                    tmp.append(wl)
                    vis = visited+(wl, )
                    queue.append((wl, step+1, vis, wList[:idx]+wList[idx+1:]))
                    # print((wl, step+1, vis, wList[:idx]+wList[idx+1:]))
                    if wl == endWord:
                        length = len(vis) if length == 0 else length
                        if length == len(vis):
                            res.append(list(vis))
                        else:
                            return res
                # else:
                #     print("not differ by a letter")
        return res
        # while queue:
        #     word, step, visited = queue.popleft()
        #     if length != 0 and step > length:
        #         break

        #     for wl in wordList:
        #         if wl in visited:
        #             continue
        #         if self.is_differ_by_a_letter(word, wl):
        #             vis = visited+(wl, )
        #             queue.append((wl, step+1, vis))
        #             if wl == endWord:
        #                 length = len(vis) if length == 0 else length
        #                 if length == len(vis):
        #                     res.append(list(vis))
        #                 else:
        #                     return res
        # return res
                        
# @lc code=end

