#!/usr/bin/env python3

# label1   	= R" § 1 2 3 4 5 6 7 8 9 0 - = ← "
# label1_ru	= R" > 1 2 3 4 5 6 7 8 9 0 - = ← "
# labelQ = R" → q w e r t y u i o p [ ] "
# labelQ_ru	= R" → й ц у к е н г ш щ з х ъ "
label1    = R" § 1 2 3 4 5 6 7 8 9 0 - = "
label1_ru	= R" > 1 2 3 4 5 6 7 8 9 0 - = "
labelQ   	= R" q w e r t y u i o p [ ] "
labelQ_ru	= R" й ц у к е н г ш щ з х ъ "
labelA   	= R" a s d f g h j k l ; ' \ "
labelA_ru	= R" ф ы в а п р о л д ж э ё "
labelZ   	= R" ` z x c v b n m , . / "
labelZ_ru	= R" ] я ч с м и т ь б ю / "
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

EN   	 = R'`qwertyuiop[]' + R"asdfghjkl;'"   + R'zxcvbnm,./'
RU   	 = R'ёйцукенгшщзхъ' + R'фывапролджэ'   + R'ячсмитьбю.'
EN   	+= R'~QWERTYUIOP{}' + R'ASDFGHJKL:"'   + R'ZXCVBNM<>?' + R'!@#$%^&'
RU   	+= R'ЁЙЦУКЕНГШЩЗХЪ' + R'ФЫВАПРОЛДЖЭ'   + R'ЯЧСМИТЬБЮ,' + R'!"№;%:?'
ENmac	 = R'§qwertyuiop[]' + R"asdfghjkl;'\"  + R'`zxcvbnm,./'
RUmac	 = R'>йцукенгшщзхъ' + R'фывапролджэё'  + R']ячсмитьбю/'
ENmac += R'±QWERTYUIOP{}' + R'ASDFGHJKL:"|'  + R'ZXCVBNM<>?!@#$%^&'
RUmac += R'<ЙЦУКЕНГШЩЗХЪ' + R'ФЫВАПРОЛДЖЭЁ'  + R'ЯЧСМИТЬБЮ,!"№;%:?'

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
