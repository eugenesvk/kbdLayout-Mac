#!/usr/bin/env python3

# label1   	= r" § 1 2 3 4 5 6 7 8 9 0 - = ← "
# label1_ru	= r" > 1 2 3 4 5 6 7 8 9 0 - = ← "
# labelQ = r" → q w e r t y u i o p [ ] "
# labelQ_ru	= r" → й ц у к е н г ш щ з х ъ "
label1    = r" § 1 2 3 4 5 6 7 8 9 0 - = "
label1_ru	= r" > 1 2 3 4 5 6 7 8 9 0 - = "
labelQ   	= r" q w e r t y u i o p [ ] "
labelQ_ru	= r" й ц у к е н г ш щ з х ъ "
labelA   	= r" a s d f g h j k l ; ' \ "
labelA_ru	= r" ф ы в а п р о л д ж э ё "
labelZ   	= r" ` z x c v b n m , . / "
labelZ_ru	= r" ] я ч с м и т ь б ю / "
labels   	= [\
  label1.replace(' ',''),
  labelQ.replace(' ',''),
  labelA.replace(' ',''),
  labelZ.replace(' ','')]
labels_ru	= [\
  label1_ru.replace(' ',''),
  labelQ_ru.replace(' ',''),
  labelA_ru.replace(' ',''),
  labelZ_ru.replace(' ','')]

EN   	 = '`qwertyuiop[]' + "asdfghjkl;'"   + """zxcvbnm,./"""
RU   	 = 'ёйцукенгшщзхъ' + "фывапролджэ"   + """ячсмитьбю."""
EN   	+= '~QWERTYUIOP{}' + 'ASDFGHJKL:"'   + """ZXCVBNM<>?""" + """!@#$%^&"""
RU   	+= 'ЁЙЦУКЕНГШЩЗХЪ' + 'ФЫВАПРОЛДЖЭ'   + """ЯЧСМИТЬБЮ,""" + """!"№;%:?"""
ENmac	 = '§qwertyuiop[]' + "asdfghjkl;'\\" + """`zxcvbnm,./"""
RUmac	 = '>йцукенгшщзхъ' + "фывапролджэё"  + """]ячсмитьбю/"""
ENmac += '±QWERTYUIOP{}' + 'ASDFGHJKL:"|'  + """ZXCVBNM<>?!@#$%^&"""
RUmac += '<ЙЦУКЕНГШЩЗХЪ' + 'ФЫВАПРОЛДЖЭЁ'  + """ЯЧСМИТЬБЮ,!"№;%:?"""

EN_RU      	= str.maketrans(EN, RU)
RU_EN      	= str.maketrans(RU, EN)
ENmac_RUmac	= str.maketrans(ENmac, RUmac)
RUmac_ENmac	= str.maketrans(RUmac, ENmac)

pad = 13
for idx, label in enumerate(labels):
  ru_trans = label.translate(ENmac_RUmac)
  ru_ref   = labels_ru[idx]
  comp = ru_trans == labels_ru[idx]
  print(ru_trans.ljust(pad) + ' ¦=¦ ' + ru_ref.ljust(pad) + '   ' + str(comp))
