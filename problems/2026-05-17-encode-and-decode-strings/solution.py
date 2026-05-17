from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += f"{len(s)}#{s}"

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]
            decoded.append(word)

            i = j + 1 + length

        return decoded


if __name__ == "__main__":
    codec = Codec()

    cases = [
        ["lint", "code", "love", "you"],
        ["a,b", "c"],
        ["", "#", "hello#world", "12#abc"],
        [],
    ]

    for case in cases:
        assert codec.decode(codec.encode(case)) == case
