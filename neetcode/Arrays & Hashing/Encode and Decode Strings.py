class Solution:
    def encode(self, strs: list[str]) -> str:
        result = []
        for string in strs:
            if len(string) == 0:
                encoding = '-1'
            else:
                encoding = ','.join([str(ord(char)) for char in string])
            result.append(encoding)
        return ';'.join(result)

    def decode(self, s: str) -> list[str]:
        if (len(s) == 0):
            return []
        strs = s.split(';')
        results = []
        for encoding in strs:
            if encoding == '-1':
                decoding = ''
            else:
                decoding = ''.join([chr(int(ec_char)) for ec_char in encoding.split(',')])
            results.append(decoding)
        return results
