class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        if denominator == 0:
            return ""

        result = ""
        if (numerator < 0) ^ (denominator < 0):
            result += "-"
        numerator, denominator = abs(numerator), abs(denominator)

        result += str(numerator // denominator)

        if numerator % denominator == 0:
            return result

        result += "."
        remainder_dict = {}
        remainder = numerator % denominator

        while remainder != 0 and remainder not in remainder_dict:
            remainder_dict[remainder] = len(result)
            remainder *= 10
            result += str(remainder // denominator)
            remainder %= denominator

        if remainder in remainder_dict:
            result = result[:remainder_dict[remainder]] + \
                "(" + result[remainder_dict[remainder]:] + ")"

        return result
