class Solution(object):
    @staticmethod
    def romanToInt(s: int):
        result = []
        rims = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
        }
        for i in rims:
            res = rims[i] * (s // i)
            if res:
                result.append(res)
            s = s % i
        return "".join(result)