class Solution(object):
    def romanToInt(self, s: int):
        result = []
        rims = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            5: "V",
            4: "IV",
            1: "I",
        }
        for i in rims:
            res = rims[i] * (s // i)
            if res:
                result.append(res)
            s = s % i
        return "".join(result)



d = Solution()
print(d.romanToInt(4444))