Regexes to parse `keyboard-layout.json`

<!-- json -->
New layout with lowercase labels
Select keys __by row__ English layout
```
1st key row (§-0-=), then to select the end (not all lines have a trailing comma)
    "[§0-9\-\=←]\\n
("|",)$
2nd key row (q-p[] and ⇥q-p[])
\\n[qwertyuiop\[\]]"
\\n[⇥qwertyuiop\[\]]"
\\n[QWERTYUIOP\[\]]"
\\n[⇥QWERTYUIOP\[\]]"
3rd key row (a-l;'\) (doesn't capture g since it has a different layout)
\\n([asdfghjkl;']|[\\]{2})"
\\n([ASDFGHJKL;']|[\\]{2})"
\\n([фывапролджэё]|[\\]{2})"
4th key row (`zx-/) (doesn't capture m since it has a different layout)
\\n[\`zxcvbnm,./]"
\\n[\]ячсмитьбю/]"
```

<!-- json -->
Old layout with capital labels
Select keys __by row__ English layout
```
1st key row (§-0-=), then to select the end (not all lines have a trailing comma)
    "[§0-9\-\=←]\\n
("|",)$
2nd key row (q-p[] and ⇥q-p[])
    "[QWERTYUIOP\[\]]\\n
    "[⇥QWERTYUIOP\[\]]\\n
3rd key row (a-l;'\)
    "([ASDFGHJKL;']|[\\]{2})\\n
4th key row (`zx-/)
    "[\`ZXCVBNM,./]\\n
```

```
,\"([0-9]|[A-Z]|[,.\\\-\=\[\]/])
    \"([0-9]|[A-Z]|[,.\\\-\=\[\]/;'])\\n
# Replace the 3rd symbol (bottom right) $1$4
(    \"([0-9]|[A-Z]|[,.\\\-\=\[\]/;'])\\n[^\\n]{1,3}\\n[^\\n]{1,3})(\\n[^\\n]{1,3})(\")
```
