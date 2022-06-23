def fourSum(nums, target):
    def findNsum(nums, target, N, result, results):
        print("=================")
        print("nums: " + str(nums) + ", target: " + str(target) + ", N: " + str(N) + ", result: " + str(result) + ", results: " + str(results))
        if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
            print("-----------1-----------")
            return
        if N == 2: # two pointers solve sorted 2-sum problem
            print("-----------2-----------")
            l,r = 0,len(nums)-1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    print(results)
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else: # recursively reduce N
            print("-----------3-----------")
            for i in range(len(nums)-N+1):
                print("i: " + str(i) + ", nums[i-1]: " + str(nums[i-1]) + ", nums[i]: " + str(nums[i]))
                if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                    print("step into")
                    findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
                    print("step out")
                    print("nums: " + str(nums) + ", target: " + str(target) + ", N: " + str(N) + ", result: " + str(result) + ", results: " + str(results))

    results = []
    findNsum(sorted(nums), target, 4, [], results)
    return results

res = fourSum([1,0,-1,0,-2, 2], 0)
print(res)