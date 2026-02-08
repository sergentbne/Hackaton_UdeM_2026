import string
import numpy as np
import math
class Transformer:
    def __init__(self):
        self.__map = dict(zip(range(26), string.ascii_lowercase))
        self.__reverse = {y: x for x, y in self.__map.items()}
    def transform_to_str(self,i):
        if type(i) == int: 
            return self.__map[i%26]
        else:
            return i
    def transform_to_int(self, i):
        if i.isalpha():
            return self.__reverse[i]
        else:
            return i



def decrypt(ciphertext, key, trans):
    to_rem = (key * math.ceil(len(ciphertext) / len(key)))[:len(ciphertext)]
    to_rem = list(map(trans.transform_to_int, to_rem))
    cipher_as_numb = list(map(trans.transform_to_int, ciphertext))
    list_of_numb = []
    index = 0
    for i in cipher_as_numb:
        if type(i) == int:
            list_of_numb.append(i-to_rem[index])
            if index < 7:
                print(i-to_rem[index], i, to_rem[index])
            index += 1
        else:
            list_of_numb.append(i)
    return "".join(map(trans.transform_to_str, list_of_numb))
    
ciphertext = r"""omkhhz wfhylsqkp wv bys qcdphz ft wqdsv tvhwmig rn kvh icdkissw igdhii cq imsuixs lv nflbksq trbjcruh. tvhwmi tumhihvtm dvrzbazg giksv jrqn bf hkm rfdj dowpvadbzqlie oo-szbgq (t. og 801-873), eyc iwiadtcm gmmsowgsg bys pmkvrl kc ezvon kzdkmig. omkhhz wfhylsqkp oqicmvqj udqesg qddrzkoqkv wq mlfrxv klby hkm usymccsuvbw ww ardrpom kmsm zb dl 1450, nvhzvwq wes pcjh hakwpiks wpv opwlbw ww hbxv fhylwumu trz vofp cswbvfiwia. oqeuxqjhv cjs omkhhz wfhylsqkp oqicmvqj ov i iigqdsqbrfb bvqkvzexm wcu trbjcruh qusqbztlkrhlwe, kkmis lb zg siihlklzdzcm hnwsfbzjh ij oq qerlkrhlwe ci eyswpvf dv lbnvfkq eiwwqeu vgjhhu zg dtgvdjvhlk, jmotrplk, ff llvcjzrdkqt.

hkm lgh ww zhbksu nistcvbfqvg dvu tumhihvtm dvrzbazg strmv i wiqlrahvkoo zfzh qe qugghroiopa rbg avjhzrz zwir scqnom xopmj, wqkcigqeu kieupie, gfzrpetv, krzuzh ier wpv hhtvjlazcq orah aycz eysht ft iwihxvv. cqm ft wpv sdzcwhak rhatflxkwrvj wq kcovazqdt cwwmiowcis rn rdstpwqo kvh secztvrjm ft hvxzlay zhbksu nistcvbfg kc vwcjlvx o fzpdwwxfdu zg iwlbg qe sgorf dtcoq xfs'v nrarcj gwwim "wpv urtu-pxo", nvhzv hkm dswpfr la jifkvgvnlzog rdstzsg bf rhkzdkmi o pmjgdov uldzbj bys owtowqfb rn r humrgxzv vllusq jp qdxkolv bwgl.

ysujvfw a. qwp, qe vla tzdajwf qehuwuifbffb kimsbfuuigvb bvlw kfrha rbg avqumk kuqkwqo, xwymj hkm vbjtzgk tvhwmi tumhihvtm vmhihvts da "vhdwe flayr ontax opdzj mymfqe", wpv arak qrudcq tvhwmi ddqig da "kv km rb um vf lv fb db er vb vg hv ft wm vr rz kw kq rg ww", rbg bys pwjh fwdarv ucxjcsg tvhwmig da "cz hm jg rw kh in if qv gd fk". uwinvfhvk kdgj ci kfiqbzbj krb szfrxkv gruvkkik rlnwsumeh rzusua.

cswbvf izvexmeqlmj ooaf vddv o vbicqo vtimth rv kvh lvgloe ci afah svmewrfg trmrckg. wpv arak tumhihvk zhbksua rfh xcofmu cq bys kwds uwn ci bys etzqnmeggmithz kmsmnflbvf, wpv rywion svmewrfg trmrck, qrtvads rbg wkvhz fdwqdwcmu zdgfiwa.

sfddf jrcj oymq fhafzxb cs gmiblmi bldvox lv rlnwwfcks."""

trans = Transformer()
print([trans.transform_to_int(i) for i in "omkhhz"])
print([trans.transform_to_int(i) for i in "dirodi"])
print(decrypt(ciphertext, "diro", trans))
print(trans.transform_to_str(13))

