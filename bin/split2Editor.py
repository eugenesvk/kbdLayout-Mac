#!/usr/bin/env python3

import os
import sys
import unicodedata

dbg = 0

ENmac  = R'§qwertyuiop[]' + R"asdfghjkl;'"+"\\" + R'`zxcvbnm,./'
RUmac  = R'>йцукенгшщзхъ' + R'фывапролджэё'     + R']ячсмитьбю/'
ENmac += R'±QWERTYUIOP{}' + R'ASDFGHJKL:"|'     + R'ZXCVBNM<>?!@#$%^&'
RUmac += R'<ЙЦУКЕНГШЩЗХЪ' + R'ФЫВАПРОЛДЖЭЁ'     + R'ЯЧСМИТЬБЮ,!"№;%:?'
ENmac_RUmac = str.maketrans(ENmac, RUmac)
RUmac_ENmac = str.maketrans(RUmac, ENmac)

mods   	= ['⇧','⌥','⇧⌥','r','label','^','◌','']
sep    	= ' ' # no-break space
escape 	= ['\\','"']
label_h	= 'label'

def prefillDic(labels):
  outDic = dict()
  for idx, labels_row in enumerate(labels): # prefill dictionary
    for label_key in labels_row:
      outDic[label_key] = {}
      for mod in mods:
        outDic[label_key][mod] = label_key if mod == 'label' else ''
  return outDic


def parseInputLayout(fileIn, outDic):
  """parse input file and fill out our dictionary"""
  with open(fileIn) as file:
    foundLabels	= False
    labels     	= []
    while (line := file.readline()):
      line	= line.rstrip('\n').split(sep)[1:]
      if line == []: foundLabels=False; labels=[]; continue  # reset labels on an empty line
      row_h	= line[-1].lower().strip().replace(' ','')     # e.g. '⇧' or '⌥'
      row  	= [char.strip() for char in line[:-1]]         # e.g. ['§','1','2', ...,'=']
      if not foundLabels:                                  # skip untill we find labels
        if row_h == '' or label_h not in row_h: continue
        else:
          foundLabels = True
          labels = row
          continue
      if dbg >=5: print('line='+str(line))

      # store each char under a respective header label in a dictionary
      if dbg >= 3: print('lbl='+str(labels))
      if dbg >= 3: print('row='+str(row) + '   ' + 'row_h='+str(row_h)+'\n')
      for lbl_idx, lbl in enumerate(labels):
        if lbl_idx >= len(row): continue
        char  = row[lbl_idx]
        outDic[lbl][row_h] = char
    file.seek(0)                                           # return to the file's beginning


def bufferEditorConfig(outDic, layerName, language, mods_out, fileOutMod, labels, translate_labels, key_col, lbl_size):
  """save output to a text string buffer"""
  layout_title_pre = """
    {
      "backcolor": "#dbdbdb",
      "name": "TypES — """
  layout_title_post = fileOutMod.replace('-',' ')+'''",
      "author": "github.com/eugenesvk/kbdLayout-Mac",
      "radii": "6px 6px 12px 12px / 18px 18px 12px 12px",
      "css": ""
    },'''
  row1 = '"t":'+key_col+', "p":"CHICKLET","f":6,"fa":'+lbl_size
  rowQ = '"x":1.5' # no need for colors, get lost on import
  rowA = '"x":1.75'
  rowZ = '"x":1.25'
  layout_prefix = [row1,rowQ,rowA,rowZ]
  mod_label    	= r'\n'.join(mods_out).replace('r','').replace('label','')
  rShift_label 	= '[{"x":12.25,"y":-1,"w":2.25},"'+ mod_label +'"]' # right shift
  lShift_label 	= '[{"x":0    ,"y":-1,"w":1.5},"' + mod_label +'"]' # left shift
  Caps_label   	= '[{"x":0    ,"y":-2,"w":1.75},"'+ mod_label +'"]' # Caps Lock
  last_label   	= Caps_label
  key_home     	= '    {"n":true},\n'
  home_keys    	= ['f', 'j']
  backspace    	= '    {"w":1.5},\n'
  backspace_key	= ['←']
  rShift_x     	= 12.25

  layout_title = layout_title_pre + language +' '+ layerName + layout_title_post
  buffer  = ''
  buffer += '['
  buffer += layout_title + '\n'

  for idx, label in enumerate(labels): # construct a json string based on parsed keys
    buffer += '['
    if len(labels) < len(layout_prefix):
      if idx == 0:
        buffer += '{' + layout_prefix[idx+1] +', ' +layout_prefix[idx] + "},\n"
      else:
        buffer += '{' + layout_prefix[idx+1] + "},\n"
    else:
      buffer += '{' + layout_prefix[idx] + "},\n"
    for char_idx, char in enumerate(label):
      char = char.lower()
      buffer += key_home  if char in home_keys     else ''
      buffer += backspace if char in backspace_key else ''
      buffer += '    "'

      for idx,mod in enumerate(mods_out):
        oCh = outDic[char][mod]
        if mod == 'label' and language == 'Russian' and translate_labels:
          oCh = outDic[char][mod].translate(ENmac_RUmac)
        buffer	+= ('\\' if oCh in escape else '') +oCh+ (r'\n' if idx!=len(mods_out)-1 else '')
      buffer  	+= '"' + (',' if char != label[-1] else '') + '\n'
    buffer    	+= '],\n'
  buffer      	+= last_label
  buffer      	+= '] \n'
  if dbg >= 3: print(buffer)
  return buffer


def save2File(buffer, filePath):
  """write prepared output to file"""
  print('Saving symbols to ' + os.path.abspath(filePath))
  with open(filePath, "wt") as file:
    file.write(buffer)



def main() -> int:
  label1    	= R" § 1 2 3 4 5 6 7 8 9 0 - = ← ".replace(' ','')
  label1s   	= R" § 1 2 3 4 5 6 7 8 9 0 - = ".replace(' ','')
  labelQ    	= R" → q w e r t y u i o p [ ] ".replace(' ','')
  labelQs   	=   R" q w e r t y u i o p [ ] ".replace(' ','')
  labelA    	= R" a s d f g h j k l ; ' \ ".replace(' ','')
  labelZ    	= R" ` z x c v b n m , . / ".replace(' ','')
  label1_ru 	= [ch.translate(ENmac_RUmac) for ch in label1]
  label1s_ru	= [ch.translate(ENmac_RUmac) for ch in label1s]
  labelQ_ru 	= [ch.translate(ENmac_RUmac) for ch in labelQ]
  labelQs_ru	= [ch.translate(ENmac_RUmac) for ch in labelQs]
  labelA_ru 	= [ch.translate(ENmac_RUmac) for ch in labelA]
  labelZ_ru 	= [ch.translate(ENmac_RUmac) for ch in labelZ]

  names	= [\
    { 'fileIn':{'English':'in_Typo', 'Russian':'in_Typo'},
      'layer':'Typographical',
      'fileOutPre':'../helper/layout-editor/types-—-',
      'fileOutMod':"-⇧¦⌥¦⇧⌥",
      'fileOutExt':'.json',
      'labels':{'English':[label1,labelQs,labelA,labelZ],  # labels should match input data
                'Russian':[label1,labelQs,labelA,labelZ]},
      'translate_labels': True,
      'mods_out':[ '⇧'   , 'r'    , '⌥'   , 'label' , '', '', '', '','⇧⌥'  , '^'],
      'key_col':r'"#006400\n#000000\n#377bb5\n#666666\n  \n  \n  \n  \n#00aaff\n#ff0000"',
      'lbl_size':'[ 0     ,  0     ,  0     ,  2     ,  0,  0,  0,  0,  4     ,  4]' },
      #'lbl_size':'[1     ,  7     ,  3     ,  9     ,  0 , 0 , 4 , 6,  2     ,  5     ,  8]' }
      #             ↖        ↙        ↗        ↘       F←  F→   ←   →   ↑        •        ↓   FC
      #            TL       BL       TR       BR       FL  FR  CL  CR  TC       CC        BC  FC
      # Left, Right | Top, Bottom | Center | Front
      # modifiers should match input data, and their order — output label positions
    { 'fileIn':{'English':'in_Copyright', 'Russian':'in_CopyrightRu'},
      'layer':'Copyright',
      'fileOutPre':'../helper/layout-editor/types-—-',
      'fileOutMod':"",
      'fileOutExt':'.json',
      'labels':{'English':[labelQs,labelA,labelZ],
                'Russian':[labelQs_ru,labelA_ru,labelZ_ru]},
      'translate_labels': False,
      'mods_out':[ ''     , 'r'    , ''     , 'label'],
      'key_col':r'"       \n#000000\n       \n#666666"',
      'lbl_size':'[ 0     ,  0     , 0      ,  2]' },
      #             ↖        ↙        ↗        ↘
    { 'fileIn':{'English':'in_Diacritics', 'Russian':'in_DiacriticsRu'},
      'layer':'Diacritics',
      'fileOutPre':'../helper/layout-editor/types-—-',
      'fileOutMod':"-⇧⌥¦⌃¦◌",
      'fileOutExt':'.json',
      'labels':{'English':[label1s,labelQs,labelA,labelZ],
                'Russian':[label1s_ru,labelQs_ru,labelA_ru,labelZ_ru]},
      'translate_labels': False,
      'mods_out':[ ''     , '◌'    , '⇧⌥'  , 'label', '', '', '', '', '', '^'],
      'key_col':r'"       \n#000000\n#377bb5\n#666666\n  \n  \n  \n  \n  \n#ff0000"',
      'lbl_size':'[ 0     ,  0     , 0      ,  2     , 0 , 0 , 0 , 0 , 0 ,  0]' }
      #             ↖        ↙        ↗        ↘                            •
     ]
  languages    	= ['English','Russian']
  fpInRel      	= '../helper/' # path relative to './bin'
  fpOutSymb_pre	= '../helper/Symbols-'

  scriptPath	= os.path.dirname(__file__)
  for name in names:
    mods_out  	= name['mods_out']
    key_col   	= name['key_col'].replace(' ','')
    lbl_size  	= name['lbl_size'].replace(' ','')
    fileOutMod	= name['fileOutMod']

    for language in languages:
      labels          	= name['labels'][language]
      translate_labels	= name['translate_labels']

      fileIn  	= os.path.join(scriptPath, fpInRel+'/'+ name['fileIn'][language])
      fpOutRel	= name['fileOutPre'] + language +'-'+ name['layer'] + fileOutMod + name['fileOutExt']
      fileOut 	= os.path.join(scriptPath, fpOutRel.lower())
      outDic  	= prefillDic(labels)

      parseInputLayout(fileIn, outDic)
      if dbg >= 3: print(outDic)

      buffer = bufferEditorConfig(outDic, name['layer'], language, mods_out, fileOutMod, labels, translate_labels, key_col, lbl_size)
      save2File(buffer, fileOut)

  return 0

if __name__ == '__main__':
  sys.exit(main())
