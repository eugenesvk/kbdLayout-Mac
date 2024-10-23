#!/usr/bin/env python3

import os
import unicodedata
import copy
from collections import OrderedDict

dbg = False

# labelQ = r" → q w e r t y u i o p [ ] "
label1   	= R" § 1 2 3 4 5 6 7 8 9 0 - = ← "
labelQ   	= R" q w e r t y u i o p [ ] "
labelA   	= R" a s d f g h j k l ; ' \ "
labelZ   	= R" ` z x c v b n m , . / "
labels   	= [label1.replace(' ','')
         	  ,labelQ.replace(' ','')
         	  ,labelA.replace(' ','')
         	  ,labelZ.replace(' ','')]
subMathDK	= ['math-','math/','math=','math_','mathO','math|','math‹']
dicIndex 	= ['row#', 'rowQ', 'rowA', 'rowZ']

outDic = OrderedDict()
for mathDK in subMathDK:
  outDic[mathDK] = OrderedDict()
  for row in dicIndex:
    outDic[mathDK][row] = OrderedDict()

# outformat "⇧\nr\n⌥\n§",
  # shift,regular,alt ,label
  # topL ,bottomL,topR,bottomR
keys      = ['⇧','r','⌥','label'] # order is important!
for mathDK in subMathDK:
  for idx, label in enumerate(labels): # prefill dictionary
    for char in label:
      outDic[mathDK][dicIndex[idx]][char] = {'⇧':'','r':'','⌥':'','label':char}

stringOut    	= ''
charOut      	= ''
mode         	= 'r'
modes        	= ['⇧', '⌥']
charDK       	= ''
fpInRel      	= '../helper/in_math'
fpOutRel_pre 	= '../helper/layout-editor/mathDK/types-—-english-🕱'
fpOutRel_post	= '-⇧¦⌥.json'
scriptPath   	= os.path.dirname(__file__)
fileIn       	= os.path.join(scriptPath, fpInRel)

escape	= ['\\','"']

# 1 parse input file and fill out our dictionary
with open(fileIn) as file:
  for idx, label in enumerate(labels):
    while (line := file.readline()):             # =¦⇐¦math‹
      if line.rstrip() and line.rstrip() in modes:
        if dbg: print('mode shifts from {' + mode + '} to ' + line.rstrip())
        mode = line.rstrip()
      for mathDK in subMathDK:
        if mathDK in line:
          charDK	= mathDK
          line  	= line.replace(charDK,'')
      if not charDK: continue
      for char in label:
        if line.lower().startswith(char): # char in line.lower()
          charOut = line.lower().rstrip().replace(' ','').replace('¦','').replace(char,'')
          outDic[charDK][dicIndex[idx]][char][mode] = charOut
    file.seek(0)                                 # return to the file's beginning
    mode = 'r'
    # stringOut += '\n'


# 3 prepare output data
# common formatting variables
layout_title_pre = """
  {
    "backcolor": "#dbdbdb",
    "name": "TypES — English 🕱"""
layout_title_post = """ ⇧¦⌥",
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
rShift_label  	= r"""[{"x":12.25,"y":-1,"w":2.25},"⇧\n\n⌥\n"]""" # right shift
# key_colors  	= r'"t":"#006400\n#000000\n#377bb5\n#666666"'
# key_home    	= '    {' + key_colors + ',' + '"n":true' + '},\n'
# key_home_not	= '    {' + key_colors                    + '},\n'
key_home_nocol	= '    {"n":true},\n'
home_keys     	= ['f', 'j']
backspace     	= '    {"w":1.5},\n'
backspace_key 	= ['←']
rShift_x      	= 12.25

for mathDK in subMathDK:
  # 2 remove left-most empty buttons (same # from each row to maintain alignment)
        # outDic[mathDK][dicIndex[idx]][char] = {'⇧':'','r':'','⌥':'','label':char}
  # get the first non-empty element from all combinations
  last_label    	= rShift_label
  first_nonempty	= []
  labels_cut = copy.deepcopy(labels) # so that labels don't get overwritten
  for idx, label in enumerate(labels):
    first_nonempty.append(len(label)-1)
    if dbg: print('first_nonempty='+str(first_nonempty))
    tmpDic = outDic[mathDK][dicIndex[idx]]
    for char_idx, char in enumerate(label):
      combo = tmpDic[char]['⇧']+tmpDic[char]['r']+tmpDic[char]['⌥']
      if dbg: print(char+" @"+str(char_idx)+" ⟶   "+'combo='+str(combo))
      if combo != '':
        first_nonempty[idx] = char_idx
        break
    if dbg: print('first_nonempty='+str(first_nonempty))
  if dbg: print('first_nonempty(idx)='+str(first_nonempty))
  min_first_nonempty = min(first_nonempty)
  if dbg and mathDK == 'math/': print('mathDK='+mathDK + ': first_nonempty='+str(first_nonempty)+', min='+str(min_first_nonempty))
  if min_first_nonempty > 1: # don't bother cutting off fewer than 2 keys
    layout_prefix[1] = r'{"x":0.5 },' # layout_rowQ
    layout_prefix[2] = r'{"x":0.75},' # layout_rowA
    # § and ` keys are "+1" in row1/Z,
    extra_cut_1Z = 0 if min_first_nonempty == min(first_nonempty[0],first_nonempty[3]) else 1   # ... if they're not limiting, cut one extra
    save_cut_QA =  1 if min_first_nonempty == min(first_nonempty[0],first_nonempty[3]) else 0   # ... and if they're, cut one fewer from the QA rows
    new_x = rShift_x - min_first_nonempty - extra_cut_1Z
    last_label = '[{"x":'+str(new_x)+r''',"y":-1,"w":2.25},"⇧\n\n⌥\n"]'''
    if dbg: print('extra_cut_1Z='+str(extra_cut_1Z) + ', save_cut_QA='+str(save_cut_QA))
    for idx, label in enumerate(labels):
      if idx in [0,3]:
        labels_cut[idx] = labels[idx][min_first_nonempty + extra_cut_1Z:]
      if idx in [1,2]:
        labels_cut[idx] = labels[idx][min_first_nonempty - save_cut_QA:]
  if dbg: print('mathDK='+mathDK + ': last_label='+str(last_label))
  if dbg: print('labels_cut='+str(labels_cut))


  mathDK_san = mathDK.replace('/','⁄').replace('|','¦')
  fpOutRel	= fpOutRel_pre + mathDK_san + fpOutRel_post
  fileOut 	= os.path.join(scriptPath, fpOutRel)

  layout_title = layout_title_pre + mathDK_san + layout_title_post
  stringOut = ''
  stringOut += '['
  stringOut += layout_title + '\n'

  for idx, label in enumerate(labels_cut): # construct a json string based on all parsed keys
    stringOut += '['
    stringOut += layout_prefix[idx] + "\n"
    for char in label:
      char = char.lower()
      stringOut += (key_home_nocol if char in home_keys else '')
      stringOut += (backspace if char in backspace_key else '')
      # stringOut += (key_home if char in home_keys else key_home_not)
      stringOut += '    "'

      for key in keys:
        oCh = outDic[dicIndex[idx]][char][key]
        stringOut	+= ('\\' if oCh in escape else '') + oCh + (r'\n' if key != keys[-1] else '')
      stringOut  	+= '"' + (',' if char != label[-1] else '') + '\n'
    stringOut    	+= '],\n'
  stringOut      	+= last_label
  stringOut      	+= '] \n'
  if dbg: print(stringOut)

  # 3 write prepared output to file
  print('Saving symbols to ' + os.path.abspath(fileOut))
  with open(fileOut, "wt") as file:
    file.write(stringOut)
