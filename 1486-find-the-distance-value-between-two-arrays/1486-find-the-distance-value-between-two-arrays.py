class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # distance between arr1 and arr2
        # arr1[i]가 distance 값에 포함되려면, arr2의 모든 원소와의 거리(|arr1[i] - arr2[j]|) > d보다 커야 한다.
        count = 0
        for i in range(len(arr1)):
            valid = True
            for j in range(len(arr2)):
                res = abs(arr1[i] - arr2[j])
                if res <= d :
                    valid = False
                    break
            if valid:
                count += 1
        return count

