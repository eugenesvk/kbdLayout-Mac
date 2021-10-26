#!/usr/bin/env python3

import os
import unicodedata

# paste all the characters that the layouts support here, duplicates are fine
allChars =r"""
<!-- ` 1 2 3 4 5  6 7 8 9 0 - = ⌫       -->
<!-- ~ ! @ # $ %  ^ & * ( ) _ +    ⇧    -->
<!-- ` ¹ ² ³ $ ‰  ↑ § ∞ ← → — ≠      ⌥  -->
<!-- ◌̀ ¡ ½ ⅓ ¼ ‱ ◌̂ ¿ · ‹ › – ±    ⇧ ⌥ -->
<!-- ◌̀ ◌́ ◌̀ ◌̈ ◌̃ ◌̄  ◌̂ ◌̊ ◌̇ ◌̆ ◌̌ ◌̣ ◌̧     ^   -->
<!-- § ¡ ™ £ ¢ ∞  § ¶ • ª º – ≠ ␈  ^⌥ -->
<!-- ± ⁄ € ‹ › ﬁ  ﬂ ‡ ° · ‚ — ± ⌫ ⇧^⌥ -->

<!-- ⇥ q w e r  t  y u  i o  p [ ]      -->
<!--                            { }  ⇧   -->
<!--    ⎋ ∑ € ◊ 🕱π ¥ 🕱⎀ ◌ 🕱ѣ ′ [ ]    ⌥ -->
<!--    ◌̆ ⌃ ⇪ ◌̊ ℃   ◌̣  ◌̇  ◌̄ ″ { }  ⇧ ⌥ -->
<!--                                 ^   -->
<!-- ⇥ œ ∑ ◌́  ® †  ¥ ◌̈  ◌̂  ø π “ ‘   ^⌥ -->
<!-- ⇤ Œ „ ´ ‰  ˇ  Á ¨  ˆ  Ø ∏ ” ’  ⇧^⌥ -->

<!--   a s d f  g h j k l ;  ' \      -->
<!--                      :  " |  ⇧   -->
<!--   ≈ § ° £  π ₽ „ “ ” ‘  ’ ÷     ⌥-->
<!--   ⌥⇧ ⌀ ℉ ⌘ ◌̋ ✓ √ λ ◌̈  ¦ ⇧ ⌥ -->
<!--           🕱ε         ◌ ◌      ^  -->
<!--   å ß ∂ ƒ  © ˙ ∆ ˚ ¬ …  æ «   ^⌥ -->
<!--   Å Í Î Ï  ˝ Ó Ô  Ò Ú Æ »  ⇧^⌥ -->

<!-- ` z x  c v b n  m , . /        -->
<!-- ~                 < > ?  ⇧    -->
<!-- ` Ω × 🕱© ↓ ß ¶  − « » ÷     ⌥ -->
<!-- ◌̀ ◌̧ ✗  ¢ ◌̌ ẞ ◌̃  • „ “ ◌́  ⇧ ⌥ -->
<!--                🕱π         ^   -->
<!-- ◌̀ Ω ≈  ç √ ∫ ◌̃  µ ≤ ≥ ÷   ^⌥ -->
<!-- ` ¸ ˛  Ç ◊ ı ˜  Â ¯ ˘ ¿  ⇧^⌥ -->

Diacritics: ◌̀ `grave` ◌́ `acute` ◌̈ `diaeresis` ◌̃ `tilde` ◌̄ `macron` ◌̂ `circumflex` ◌̊ `ring` ◌̇ `dot-above` ◌̆ `breve` ◌̌ `caron` ◌̣ `dot-below` ◌̧ `cedilla` ◌̨ `ogonek` ◌̋ `double-acute` ◌̉ `hook-above` ◌̛ `horn`
| ◌̀ `grave`                  | Àà èÈ ìÌ òÒ ùÙ ǹǸ Ẁẁ ỳỲ  `  ̀ |
  | ◌́ `acute`                  | Áá éÉ íÍ óÓ úÚ ýÝ Ćć Ĺĺ ńŃ Ŕŕ Śś Źź Ǵǵ Ḿḿ Ṕṕ Ẃẃ  ´ ́ |
  | ◌̈ `diaeresis`              | Ää ëË ïÏ öÖ üÜ ÿŸ Ẅẅ Ẍẍ ¨ ̈ |
  | ◌̃ `tilde`                  | Ãã ñÑ õÕ ĩĨ ũŨ Ṽṽ ỹỸ  ˜ ̃ |
  | ◌̄ `macron`                 | āĀ ēĒ īĪ ōŌ ūŪ ȳȲ ḡḠ ¯ ̄  <kbd>⌥</kbd><kbd>⇧</kbd><kbd>q</kbd> ᷌   |
  | ◌̂ `circumflex`             | Ââ êÊ îÎ ôÔ ûÛ Ĉĉ Ĝĝ Ĥĥ Ĵĵ Ŝŝ Ŵŵ ŷŶ Ẑẑ  ˆ ̂ |
  | ◌̊ `ring`                   | Åå ůŮ ˚ ̊ |
  | ◌̇ `dot-above`              | Ȧȧ Ċċ ėĖ Ġġ ȯȮ Ḃḃ Ḋḋ Ḟḟ Ḣḣ İ  Ṁṁ ṅṄ Ṗṗ Ṙṙ Ṡṡ Ṫṫ Ẇẇ Ẋẋ ẏẎ Żż  ˙  ̇ |
  | ◌̆ `breve`                  | Ăă ĕĔ Ğğ ĭĬ ŏŎ ŭŬ ˘ ̆  <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd> ᷋ |
  | ◌̌ `caron`                  | Čč Ďď ěĚ ňŇ Řř Šš Ťť Žž Ǎǎ ǐǏ ǰ  ǒǑ ǔǓ Ǧǧ Ǩǩ Ȟȟ ˇ ̌   |
  | ◌̣ `dot-below`              | Ḅḅ Ḍḍ Ḥḥ Ḳḳ Ḷḷ Ṃṃ ṇṆ Ṛṛ Ṣṣ Ṭṭ Ṿṿ Ẉẉ Ẓẓ Ạạ ẹẸ ọỌ ụỤ ỵỴ  ̣  ̣ |
  | ◌̧ `cedilla`                | Çç Ģģ Ķķ Ļļ ņŅ Ŗŗ Şş Ţţ ȩȨ Ḑḑ Ḩḩ  ̧ ¸ |
  | ◌̨ `ogonek`                 | ąĄ ęĘ įĮ ǫǪ ųŲ ˛  ̨  |
  | ◌̋ `double-acute`           | Őő Űű ˝ ̋ |
  | ◌̉ `hook-above`             | ảẢ ẻẺ ỉỈ ỏỎ ủỦ ỷỶ ̉  |
  | ◌̛ `horn`                   | ơƠ ưƯ  ̛  |
  |   __Combo__                 |     |
  | ◌́̇ `acute+dot-above`       | ṥṤ |
  | ◌̈̄ `diaeresis+macron`      | ǟǞ ȫȪ ǖǕ |
  | ◌̃̄ `tilde+macron`          | ȭȬ |
  | ◌̄̀ `macron+grave`          | ḕḔ ṑṐ ᷆  ᷅  |
  | ◌̄́ `macron+acute`          | ḗḖ ṓṒ ᷄  ᷇  |
  | ◌̣̂ `circumflex+dot-below`  | ậẬ ệỆ ộỘ |
  | ◌̂̉ `circumflex+hook-above` | ẩẨ ểỂ ổỔ |
  | ◌̇ `dot-above`              | Ȧȧ Ėė Ȯȯ Ẏẏ İ Żż Ḃḃ Ċċ Ḋḋ Ḟḟ Ġġ Ḣḣ Ṁṁ Ṅṅ Ṗṗ Ṙṙ Ṡṡ Ṫṫ Ẇẇ Ẋẋ ˙  ̇  |
  | ◌̇̄ `dot-above+macron`      | ǡǠ ȱȰ |
  | ◌̣̣ `dot-below`             | Ạạ Ẹẹ Ọọ Ụụ Ỵỵ Ḅḅ Ḍḍ Ḥḥ Ḳḳ Ḷḷ Ṃṃ Ṇṇ Ṛṛ Ṣṣ Ṭṭ Ṿṿ Ẉẉ Ẓẓ  ̣  |
  | ◌̣̄ `dot-below+macron`      | ḹḸ ṝṜ |
  | ◌̣̇ `dot-below+dot-above`   | ṩṨ |
  | ◌̆̉ `breve+hook-above`      | ẳẲ |
  | ◌̣̆ `breve+dot-below`       | ặẶ |
  | ◌̌̇ `caron+dot-above`       | ṧṦ |
  | ◌̨̄ `ogonek+macron`         | ǭǬ |
  | ◌̛̣ `horn+dot-below`        | ợỢ ựỰ |
  | ◌̛̉ `horn+hook-above`       | ởỞ ửỬ |
  | ◌̛̃ `horn+tilde`            | ỡỠ ữỮ |
  | ◌̛́ `horn+acute`            | ớỚ ứỨ |
  | ◌̛̀ `horn+grave`            | ờỜ ừỪ |

  ⃣   Combining Enclosing Keycap

Math: 🕱 α β γ Γ δ Δ ε ζ η θ Θ ι κ λ Λ μ ν ξ Ξ π Π ρ σ Σ τ υ φ Φ χ ψ Ψ ω Ω ℂ ℕ ℚ ℝ ℤ ” “ ¶ ° … ⌊ ⌋ ⌈ ⌉ 〈 〉 ⟦ ⟧
↑ ↓ ⇑ ⇓ ← → ↔ ⇐ ⇒ ⇔ ⟵ ⟶ ⟷ ⟸ ⟹ ⟺ ↦ ⤇ ⟼ ⟾ ⇀ ⇝ ¬ ∨ ∧ ∀ ∃ ∄
． ⊦ ⊩ ⊧ ⟂ ⊥ ∅ ∈ ∉ ∪ ∩ ⫛ ⊂ ⊃ ⊆ ⊇ ∗ ÷ × ｜ ‖ ∤ ◁ ▷ ◇ ∘ · ⊗ ⊛ ⊖ ⊕ ⊘ ⊙ ≝ ≠ ≡ ≈ ≅ ≤ ≥ ∴ ∵ ∞ ∇ ² ³ √

Spaces:  ⁠​       ␣␠‑

Typographical: ⟨ ⟩ ⁂ ‸ ⁁ ⎀ ⁒ ¤ † ‡ ⹀ ⸗ ℮ º ª ❧ ♀ ♂ ⚥ ☞ ‽ № ⌑ ‴ ⁗ ⁀ 🕱 💀 ☠
 ⌦ ⎋ ⇞ ⇟ ↖ ↘ ⌧ ⏏ ↩ ↵ ⏎ ⌤

  Old Cyrillic
   § 1 2 3 4 5 6 7 8 9 0 - = 
                     ҁ       r
                     Ҁ       ⇧

   q w e r t y u i o p [ ] 
   ѳ ѡ ѣ ѯ є   ѵ і   ꙁ     r
   Ѳ Ѡ Ѣ Ѯ Є   Ѵ І   Ꙁ     ⇧
                 ї   ꙃ     ⌥
                 Ї   Ꙃ     ⇧⌥

   a s d f g h j k l ; ' \ 
     ꙑ   ѧ     ꙋ     ꙉ ѥ   r
     Ꙑ   Ѧ     Ꙋ     Ꙉ Ѥ   ⇧
         ѩ                 ⌥
         Ѩ                 ⇧⌥

   ` z x c v b n m , . / 
     ѫ   ѱ         ѣ ꙗ   r
     Ѫ   Ѱ         Ѣ Ꙗ   ⇧
     ѭ                   ⌥
     Ѭ                   ⇧⌥

Copyright: ® ™ (ɔ) ℗ ℠ 🄯 ©

Greek
<!-- Greek -->
<!-- §                                 -->
<!--                               ⌥  -->
<!-- ±                            ⇧  -->
<!--   ¹ ² ³ £ § ¶ ° • “ ° ± ½     ⌥ -->
<!-- Μ έ ί ή ό Ώ ^   Ρ Κ ύ _ +    ⇧⌥ -->
<!--   ς ω ε ρ τ υ θ ι ο π           -->
<!--   ◌΅ Ω Ε Ρ Τ Υ Θ Ι Ο Π       ⇧  -->
<!--   · ― € ® ™ ¥ ­ † œ ≈ « »       ⌥ -->
<!--   ― Β Έ Δ     Ξ Ν Τ   { }    ⇧⌥-->
<!--   α σ δ φ γ η ξ κ λ ◌΄           -->
<!--   Α Σ Δ Φ Γ Η Ξ Κ Λ  ◌̈       ⇧   -->
<!--   … ß ÷ ≠ © ½ ≤ ≥ ¬ ◌΅ ' ¦     ⌥ -->
<!--   ά ρ   Π Ϊ ≠ § ° ·  : " Ζ   ⇧⌥ -->
<!--   ζ χ ψ ω β ν μ                  -->
<!--   Ζ Χ Ψ Ω Β Ν Μ              ⇧  -->
<!-- ` §   ç ±   ‘ ’ « » /          ⌥-->
<!-- Μ     Χ Ά   Ό Ύ   ώ ?        ⇧⌥ -->
greek-tonos ◌΄: έΈ ύΎ ίΊ όΌ άΆ ήΉ ώΏ
diaeresis-greek ◌̈: ϋΫ ϊΪ
greek-dialytika-tonos ◌΅: ΰ ΐ
"""

charExclude = r"""
<!-- English TypES -->
<!-- ` 1 2 3 4 5 6 7 8 9 0 - = -->
<!--   q w e r t y u i o p [ ] -->
<!--   a s d f g h j k l ; ' \ -->
<!-- ` z x c v b n m , . /     -->
<!--   Q W E R T Y U I O P     -->
<!--   A S D F G H J K L       -->
<!-- ` Z X C V B N M           -->
"""

outHeader = """\
| Symbol  | U+…  | HTML | Unicode name |
| :-----: | :--: | :--: | :----------- |
"""

charNm     	= ''
charList   	= []
filePathRel	= '../helper/SymbolsAll_Names.md'
scriptPath 	= os.path.dirname(__file__)
targetFile 	= os.path.join(scriptPath, filePathRel)

for char in allChars:
  if char not in charExclude:
    charNm     	= unicodedata.name(char,'').title()
    codepoint  	= ord(char)
    codepoint_u	= 'u+{:04x}'.format(codepoint)       # four-digit lowercase hex
    code_html  	= '&#{};'.format(codepoint)
    if charNm:
      if (codepoint_u,code_html, char,charNm) not in charList: # include only unique symbols
        charList.append((codepoint_u,code_html, char,charNm))

charListSorted	= sorted(charList)                   # sort symbols by Unicode number

print('Saving symbols to ' + os.path.abspath(targetFile))
with open(targetFile, "wt") as file:                 # write 'Symbol U+code Name' to 'SymbolsAll_Names.txt'
  file.write(outHeader)
  for charQuad in charListSorted:
    # print(charQuad[1] +' '+ charQuad[0] +' '+ charQuad[2])
    file.write('| '+ charQuad[2] +' | `'+ charQuad[0] +'` | `'+ charQuad[1] +'` | '+ charQuad[3] +' |')
    file.write("\n")
