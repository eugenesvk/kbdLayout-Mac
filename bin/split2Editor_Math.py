#!/usr/bin/env python3

import os
import sys
import unicodedata
from collections import OrderedDict

dbg = 0

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
dicIndex	= ['row#', 'rowQ', 'rowA', 'rowZ']

outDic = OrderedDict()
for row in dicIndex:
  outDic[row] = OrderedDict()

# outformat "⇧\n⌥\n⇧⌥\nlabel"
  # shift,alt    ,alt-shift ,label
  # topL ,bottomL,topR      ,bottomR
keys_all	= ['⇧','⌥','⇧⌥','label','r']
keys    	= ['⇧','⌥','⇧⌥','label'] # order is important!
for idx, label in enumerate(labels): # prefill dictionary
  for char in label:
    outDic[dicIndex[idx]][char] = {}
    for key in keys_all:
      outDic[dicIndex[idx]][char][key] = char if key == 'label' else ''


languages    	= ['English', 'Russian']
stringOut    	= ''
charOut      	= ''
curRow       	= ''
curmode      	= 'r'
modes        	= ['⇧','⌥','⇧⌥']
fpInRel      	= '../helper/in_mathEn'
fpOutRel_pre 	= '../helper/layout-editor/types-—-'
fpOutRel_post	= '-⌥¦⇧⌥.json'
scriptPath   	= os.path.dirname(__file__)
fileIn       	= os.path.join(scriptPath, fpInRel)

sep   	= ' ' # no-break space
escape	= ['\\','"']

# 1 parse input file and fill out our dictionary
with open(fileIn) as file:
  for idx, label in enumerate(labels):
    if dbg >=3: print('label='+str(label))
    foundHeader	= False
    curRow     	= ''
    while (line := file.readline()):             # e.g.  ∀ Σ Δ 
      line = line.rstrip('\n')
      if dbg >=5: print('idx='+str(idx)+'   line=¦'+str(line)+"¦")
      if line == '':
        if foundHeader: break                             # end of a label
        else: continue                                    # skip an empty line
      for mode in modes:                                  # parse any ⌥,⇧⌥
        if line.replace(" ",'').endswith(sep+mode):
          curmode = mode

      # cut off everything before the 1st / after the last separator (inclusive of sep)
      fist_sep = line.find(sep)
      if fist_sep >= 0: line = line[fist_sep+1:]
      last_sep = line.rfind(sep)
      if last_sep >= 0: line = line[:last_sep]

      rowChars = line.replace(' ','').split(sep)           # list with each element
      if dbg >= 4: print(rowChars)
      if label == ''.join(rowChars):
        foundHeader = True
        if dbg >= 4: print(str(rowChars)+' ⟵  foundHeader')
        continue
      else:
        if not foundHeader:                      # line without a previous header, skip
          continue
      for char_idx, char in enumerate(label):
        outDic[dicIndex[idx]][char][curmode] = rowChars[char_idx]
      if dbg >= 4: print('row=' + dicIndex[idx] +' ¦ '+ str(outDic[dicIndex[idx]]))
    file.seek(0)                                 # return to the file's beginning
    curmode = 'r'
    # stringOut += '\n'
if dbg >= 3: print(outDic)

# 3 prepare output data
# common formatting variables
layout_title_pre = """
  {
    "backcolor": "#dbdbdb",
    "name": "TypES — """
layout_title_post = """ ⌥¦⇧⌥",
    "author": "github.com/eugenesvk/kbdLayout-Mac",
    "radii": "6px 6px 12px 12px / 18px 18px 12px 12px",
    "css": ""
  },"""
layout_row1 = r'{"t": "#006400\n#000000\n#377bb5\n#666666","p": "CHICKLET","f": 6,"fa": [0,0,0,2]},'
# no need to add colors, they get lost on import
layout_rowQ = r'{"x":1.5 },' #r'{"x":1.5 , "t":"#006400\n#000000\n#377bb5\n#666666"},'
layout_rowA = r'{"x":1.75},' #r'{"x":1.75, "t":"#006400\n#000000\n#377bb5\n#666666"},'
layout_rowZ = r'{"x":1.25},' #r'{"x":1.25, "t":"#006400\n#000000\n#377bb5\n#666666"},'
layout_prefix = [\
  layout_row1,
  layout_rowQ,
  layout_rowA,
  layout_rowZ]
# last_label  	= r"""[{"y":-1,"w":1.25},"⇧\n\n⌥\n"]"""
rShift_label  	= r"""[{"x":12.25,"y":-1,"w":2.25},"\n⌥\n⇧⌥\n"]""" # right shift
lShift_label  	= r"""[{"x":0    ,"y":-1,"w":1.5},"\n⌥\n⇧⌥\n"]""" # left shift
Caps_label    	= r"""[{"x":0    ,"y":-2,"w":1.75},"\n⌥\n⇧⌥\n"]""" # Caps Lock
last_label    	= Caps_label
# key_colors  	= r'"t":"#006400\n#000000\n#377bb5\n#666666"'
# key_home    	= '    {' + key_colors + ',' + '"n":true' + '},\n'
# key_home_not	= '    {' + key_colors                    + '},\n'
key_home_nocol	= '    {"n":true},\n'
home_keys     	= ['f', 'j']
backspace     	= '    {"w":1.5},\n'
backspace_key 	= ['←']
rShift_x      	= 12.25


mathNm	= 'Math'

for language in languages:
  fpOutRel	= fpOutRel_pre + language.lower() +'-'+ mathNm.lower() + fpOutRel_post
  fileOut 	= os.path.join(scriptPath, fpOutRel)

  layout_title = layout_title_pre + language +' '+ mathNm + layout_title_post
  stringOut = ''
  stringOut += '['
  stringOut += layout_title + '\n'

  for idx, label in enumerate(labels): # construct a json string based on parsed keys
    stringOut += '['
    stringOut += layout_prefix[idx] + "\n"
    for char_idx, char in enumerate(label):
      char = char.lower()
      stringOut += key_home_nocol if char in home_keys     else ''
      stringOut += backspace      if char in backspace_key else ''
      # stringOut += (key_home if char in home_keys else key_home_not)
      stringOut += '    "'

      for key in keys:
        oCh = outDic[dicIndex[idx]][char][key]
        if key == 'label' and language == 'Russian':
          oCh = labels_ru[idx][char_idx]
        stringOut	+= ('\\' if oCh in escape else '') + oCh + (r'\n' if key != keys[-1] else '')
      stringOut  	+= '"' + (',' if char != label[-1] else '') + '\n'
    stringOut    	+= '],\n'
  stringOut      	+= last_label
  stringOut      	+= '] \n'
  if dbg >= 3: print(stringOut)

  # 3 write prepared output to file
  print('Saving symbols to ' + os.path.abspath(fileOut))
  with open(fileOut, "wt") as file:
    file.write(stringOut)
