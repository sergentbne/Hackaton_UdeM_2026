import string

ALPHABET_LO = string.ascii_lowercase
ALPHABET_UP = string.ascii_uppercase
ALPHABET_LEN = 26


def decrypt(text: str, shift: int) -> str:
    """
    Decrypts a Caesar-ciphered string by shifting letters *backward* by `shift`.
    Non-letter characters are left unchanged.
    `shift` can be any integer; values >26 wrap automatically.
    """
    shift = shift % ALPHABET_LEN

    def shift_char(ch):
        if ch in ALPHABET_LO:
            return ALPHABET_LO[(ALPHABET_LO.index(ch) - shift) % ALPHABET_LEN]
        if ch in ALPHABET_UP:
            return ALPHABET_UP[(ALPHABET_UP.index(ch) - shift) % ALPHABET_LEN]
        return ch

    return "".join(shift_char(c) for c in text)


def main():
    ciphertext = r"""Kf xzcu ivwzevu xfcu kf grzek kyv czcp
Kf kyifn r gviwldv fe kyv mzfcvk
Kf jdffky kyv ztv fi ruu refkyvi ylv
Lekf kyv irzesfn fi nzky krgvi-czxyk
Kf jvvb kyv svrlkvflj vpv fw yvrmve kf xriezjy
Zj nrjkvwlc reu izuztlcflj votvjj"""
    plaintext = decrypt(ciphertext, 17)
    print(plaintext)


if __name__ == "__main__":
    main()
