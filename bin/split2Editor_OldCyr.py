#!/usr/bin/env python3

import os
import sys
import unicodedata

dbg = 0

# label1	= r" § 1 2 3 4 5 6 7 8 9 0 - = ← "
# labelQ	= r" → q w e r t y u i o p [ ] "
label1  	= r" § 1 2 3 4 5 6 7 8 9 0 - = "
labelQ  	= r" q w e r t y u i o p [ ] "
labelA  	= r" a s d f g h j k l ; ' \ "
labelZ  	= r" ` z x c v b n m , . / "
labels  	= [\
  label1.replace(' ',''),
  labelQ.replace(' ',''),
  labelA.replace(' ',''),
  labelZ.replace(' ','')]

ENmac	 = '§qwertyuiop[]' + "asdfghjkl;'\\" + """`zxcvbnm,./"""
RUmac	 = '>йцукенгшщзхъ' + "фывапролджэё"  + """]ячсмитьбю/"""
ENmac += '±QWERTYUIOP{}' + 'ASDFGHJKL:"|'  + """ZXCVBNM<>?!@#$%^&"""
RUmac += '<ЙЦУКЕНГШЩЗХЪ' + 'ФЫВАПРОЛДЖЭЁ'  + """ЯЧСМИТЬБЮ,!"№;%:?"""
ENmac_RUmac	= str.maketrans(ENmac, RUmac)
RUmac_ENmac	= str.maketrans(RUmac, ENmac)

mods    	= ['⇧','⌥','⇧⌥','r','label','na','']
mods_out	= ['' , 'r' , '⌥' , 'label']
            #  \n  ꙁ \n  tr \n br
            #no , reg ,  alt , label

outDic = dict()
for idx, labels_row in enumerate(labels): # prefill dictionary
  for label_key in labels_row:
    outDic[label_key] = {}
    for mod in mods:
      outDic[label_key][mod] = label_key if mod == 'label' else ''

languages    	= ['English', 'Russian']
stringOut    	= ''
charOut      	= ''
fpInRel      	= '../helper/in_OldCyr'
fpOutRel_pre 	= '../helper/layout-editor/types-—-'
fpOutRel_pos 	= '-⌥¦⇧⌥.json'
fpOutSymb_pre	= '../helper/Symbols-'
scriptPath   	= os.path.dirname(__file__)
fileIn       	= os.path.join(scriptPath, fpInRel)

header 	= '¦header'
label_h	= 'l'
sep_in 	= '¦' # broken-bar
sep    	= ' ' # no-break space
escape 	= ['\\','"']

# 1 parse input file and fill out our dictionary
with open(fileIn) as file:
  foundHeader	= False
  headers    	= []
  while (line := file.readline()):                         # e.g. p¦ꙁ¦Ꙁ¦ꙃ¦Ꙃ¦
    line = line.rstrip('\n')
    if not foundHeader and header in line:
      foundHeader = True
      headers = line.replace(header,'').split(sep_in)      # e.g. [l,r,⇧,⌥,⌥⇧]
      label_i = headers.index(label_h)
      continue
    if not headers: continue                         # skip lines untill we find a header
    if sep_in not in line: continue                  # skip lines without a separator
    if line == '': continue                          # skip empty lines

    line_parsed = line.split(sep_in)
    if dbg >=5: print('idx='+str(idx)+'   line=¦'+str(line)+"¦")
    for hd_idx, hd in enumerate(headers):
      if hd_idx >= len(line_parsed): continue
      char  = line_parsed[hd_idx]
      label = line_parsed[label_i]
      outDic[label][hd] = char

  if dbg >= 4: print('row=' + dicIndex[idx] +' ¦ '+ str(outDic))
  file.seek(0)                                 # return to the file's beginning
if dbg >= 3: print(outDic)

# 3 prepare output data
# common formatting variables
layerName	= 'OldCyrillic'
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
rShift_label  	= r"""[{"x":12.25,"y":-1,"w":2.25},"\n\n⌥\n"]""" # right shift
lShift_label  	= r"""[{"x":0    ,"y":-1,"w":1.5},"\n\n⌥\n"]""" # left shift
Caps_label    	= r"""[{"x":0    ,"y":-2,"w":1.75},"\n\n⌥\n"]""" # Caps Lock
last_label    	= Caps_label
# key_colors  	= r'"t":"#006400\n#000000\n#377bb5\n#666666"'
# key_home    	= '    {' + key_colors + ',' + '"n":true' + '},\n'
# key_home_not	= '    {' + key_colors                    + '},\n'
key_home_nocol	= '    {"n":true},\n'
home_keys     	= ['f', 'j']
backspace     	= '    {"w":1.5},\n'
backspace_key 	= ['←']
rShift_x      	= 12.25


def saveEditorConfig(language='English', mods_out=['','r','⌥','label']):
  fpOutRel	= fpOutRel_pre + language.lower() +'-'+ layerName.lower() + fpOutRel_pos
  fileOut 	= os.path.join(scriptPath, fpOutRel)

  layout_title = layout_title_pre + language +' '+ layerName + layout_title_post
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

      for mod in mods_out:
        oCh = outDic[char][mod]
        if mod == 'label' and language == 'Russian':
          oCh = outDic[char][mod].translate(ENmac_RUmac)
        stringOut	+= ('\\' if oCh in escape else '') + oCh + (r'\n' if mod != mods_out[-1] else '')
      stringOut  	+= '"' + (',' if char != label[-1] else '') + '\n'
    stringOut    	+= '],\n'
  stringOut      	+= last_label
  stringOut      	+= '] \n'
  if dbg >= 3: print(stringOut)

  # 3 write prepared output to file
  print('Saving symbols to ' + os.path.abspath(fileOut))
  with open(fileOut, "wt") as file:
    file.write(stringOut)

def saveLayoutData(language='English', mods_out=['r','⌥','label']):
  fpOutSymb	= fpOutSymb_pre + language[:2] +' '+ layerName
  fileOut  	= os.path.join(scriptPath, fpOutSymb)

  stringOut = ''

  for idx, labels_row in enumerate(labels): # construct a layout string based on parsed keys
    if language == 'Russian':
      stringOut += sep + sep.join(labels_row).translate(ENmac_RUmac) + sep + '\n'
    else:
      stringOut += sep + sep.join(labels_row) + sep + '\n'

    for mod in mods_out:
      if mod == 'label': continue
      for lbl_idx, label_key in enumerate(labels_row):
        label_key = label_key.lower()
        oCh = outDic[label_key][mod]
        stringOut	+= sep + (' ' if oCh == '' else oCh)
      stringOut  	+= sep + mod + '\n'
    stringOut    	+= '\n'
  if dbg >= 3: print(stringOut)

  # 3 write prepared output to file
  print('Saving symbols to ' + os.path.abspath(fileOut))
  with open(fileOut, "wt") as file:
    file.write(stringOut)

for language in languages:
  saveEditorConfig(language, mods_out)
  saveLayoutData(language, ['r','⇧','⌥','⇧⌥'])
