# Changelog
All notable changes to this project will be documented in this file

[unreleased]: https://github.com/eugenesvk/kbdLayout-Mac/compare/1.0.0...HEAD
## [Unreleased]
  <!-- - __Added__ -->
   <!-- + :sparkles: ??? -->
   <!-- new features -->
  <!-- - __Changed__ -->
   <!-- + ???  -->
   <!-- changes in existing functionality -->
  <!-- - __Fixed__ -->
   <!-- + :beetle: ??? -->
   <!-- bug fixes -->
  <!-- - __Deprecated__ -->
   <!-- + :poop: ??? -->
   <!-- soon-to-be removed features -->
  <!-- - __Removed__ -->
   <!-- + :wastebasket: ??? -->
   <!-- now removed features -->
  <!-- - __Security__ -->
   <!-- + :lock: ??? -->
   <!-- vulnerabilities -->

  - __Added__
    + :sparkles: `en` `ru` <kbd>🕱</kbd>`Brackets` and mapped it to <kbd>⌥</kbd><kbd>d</kbd>, pressing it enables various brackets <kbd>🕱</kbd> that terminate with the opening bracket and close the bracket on another tap of the same key (also works with <kbd>⎇</kbd> being held):
        * <kbd>d</kbd> )                                   	() parenthesis
        * <kbd>f</kbd> <kbd>🕱</kbd>`Brackets-[`            	[] square bracket
        * <kbd>j</kbd> <kbd>🕱</kbd>`Brackets-{`            	{} brace
        * <kbd>k</kbd> <kbd>🕱</kbd>`Brackets-"`            	"" regular double quote
        * <kbd>l</kbd> <kbd>🕱</kbd>`Brackets-'`            	'' regular single quote
        * <kbd>r</kbd> <kbd>🕱</kbd>`Brackets-‹`            	‹› single angle quote (single chevrons)
        * <kbd>t</kbd> <kbd>🕱</kbd>`Brackets-«`            	«» double angle quote (double chevrons)
        * <kbd>n</kbd> <kbd>🕱</kbd>`Brackets-【`            	【】 black lenticular bracket
        * <kbd>m</kbd> <kbd>🕱</kbd>`Brackets-「`            	「」 corner bracket
        * <kbd>o</kbd> <kbd>🕱</kbd>`Brackets-〔`            	〔〕 tortoise shell bracket
        * <kbd>,</kbd> <kbd>🕱</kbd>`Brackets-〈`            	〈〉 angle bracket or math ⟨⟩
        * <kbd>.</kbd> <kbd>🕱</kbd>`Brackets-⟪`            	⟪⟫ double angle bracket
        * <kbd>⇧</kbd><kbd>,</kbd> <kbd>🕱</kbd>`Brackets-⟪`	⟪⟫ double angle bracket
        * <kbd>g</kbd> <kbd>🕱</kbd>`Brackets-‘`            	‘’ curly single quote
        * <kbd>h</kbd> <kbd>🕱</kbd>`Brackets-“`            	“” double curly quote
        * <kbd>y</kbd> <kbd>🕱</kbd>`Brackets-\`            	`'' emacs quote
        * <kbd>;</kbd> <kbd>🕱</kbd>`Brackets-="`           	="" string assignment
        * <kbd>z</kbd> <kbd>🕱</kbd>`Brackets-⸨`            	⸨⸩ Double Parenthesis
        * <kbd>p</kbd>                                     	␌ formfeed

        * <kbd></kbd> ⎋
    + `en` `ru` <kbd>🕱</kbd>`Typographical`: modifier key labels to match their physical position
        * <kbd>§</kbd> ⎋
        * <kbd>q</kbd> ⭾
        * <kbd>a</kbd> ⇪
        * <kbd>`</kbd> ⇧
        * <kbd>⎇</kbd><kbd>`</kbd> 🌐
        * <kbd>z</kbd> ⎈
        * <kbd>⎇</kbd><kbd>z</kbd> ⌃
        * <kbd>x</kbd> ⎇
        * <kbd>⎇</kbd><kbd>x</kbd> ⌥
        * <kbd>c</kbd> ◆
        * <kbd>h</kbd> ✱
        * <kbd>⎇</kbd><kbd>c</kbd> ⌘
    + `en` `ru` <kbd>🕱</kbd>`Typographical`: F1–12 key labels on the numbers row
        * <kbd>1</kbd>–<kbd>5</kbd> 🔅 🔆 🎛 ▦ 💡
        * <kbd>7</kbd>–<kbd>=</kbd> ◀◀ ▶⏸ ▶▶ 🔇 🔉 🔊
    + `en` `ru` <kbd>🕱</kbd>`Typographical`: alternative symbols for common punctuation
        * <kbd>`</kbd> ˋ
        * <kbd>\</kbd> ⧵
        * <kbd>⎇</kbd><kbd>\</kbd> ＼
        * <kbd>⇧</kbd><kbd>⎇</kbd><kbd>\</kbd> ﹨
        * <kbd>⎇</kbd><kbd>,</kbd> ⸴
        * <kbd>⎇</kbd><kbd>.</kbd> ．
        * <kbd>⎇</kbd><kbd>/</kbd> ⁄
        * <kbd>⎇</kbd><kbd>;</kbd> ︔
        * <kbd>⎇</kbd><kbd>7</kbd> ﹖
        * <kbd>⇧</kbd><kbd>⎇</kbd><kbd>/</kbd> ﹖
    + `en` `ru` <kbd>🕱</kbd>`Typographical`: various other symbols
        * <kbd>⎇</kbd><kbd>b</kbd>⌨
        * <kbd>⎇</kbd><kbd>n</kbd>🔢
        * <kbd>⎇</kbd><kbd>m</kbd>🖰
  - __Changed__
    + `ru` update `🇷🇺R⇧≈🇺🇸L⇧` helper rule to include <kbd>§</kbd> (type `~`)
    + `en` `ru` <kbd>🕱</kbd>`Typographical`: move various symbols around
        * move ⏏ from <kbd>§</kbd> to <kbd>⇧</kbd><kbd>⎇</kbd><kbd>§</kbd>
        * move ↵/↩/⏎/⌤ to from <kbd>\</kbd> to <kbd>]</kbd>
        * copy ⇟/⇞ to <kbd>⎇</kbd><kbd>j</kbd>/<kbd>k</kbd>
        * move  from <kbd>a</kbd> to <kbd>⎇</kbd><kbd>a</kbd>
        * move ⌧ from <kbd>c</kbd> to <kbd>b</kbd>
    + `en` `ru` move various symbols around
        * move ° from <kbd>d</kbd> to <kbd>🕱</kbd>`Typographical`: <kbd>⎇</kbd><kbd>d</kbd> to free up for <kbd>🕱</kbd>`Brackets`

  [1.0.0]: https://github.com/eugenesvk/kbdLayout-Mac/releases/tag/1.0.0
## [1.0.0]
  - __Added__
    + :sparkles: `ru` `Russian — Math` layout
    + :sparkles: `en` <kbd>🕱</kbd>`Typographical` and mapped it to <kbd>⌥</kbd><kbd>u</kbd>, pressing it enables the following:
        * <kbd>,</kbd> ⟨     Left Angle bracket
        * <kbd>,</kbd> ⟩     Right Angle bracket
        * <kbd>8</kbd> ⁂    Asterism
        * <kbd>6</kbd> ‸     Caret
        * <kbd>⇧</kbd><kbd>⌥</kbd><kbd>6</kbd> ⁁  Caret insertion point
        * <kbd>⇧</kbd><kbd>6</kbd> ⎀   Insertion symbol
        * <kbd>/</kbd> ⁒     Commercial minus sign
        * <kbd>4</kbd> ¤     Currency sign
        * <kbd>t</kbd> †     Dagger
        * <kbd>⇧</kbd><kbd>t</kbd> ‡   Double Dagger
        * <kbd>-</kbd> ⹀     Double hyphen
        * <kbd>⇧</kbd><kbd>-</kbd> ⸗   Double hyphen
        * <kbd>e</kbd> ℮     Estimated sign
        * <kbd>d</kbd> º     Masculine ordinal indicator
        * <kbd>⇧</kbd><kbd>d</kbd> ª   Feminine ordinal indicator
        * <kbd>f</kbd> ❧     Fleuron
        * <kbd>g</kbd> ♀     Gender symbol
        * <kbd>⇧</kbd><kbd>g</kbd> ♂   Gender symbol
        * <kbd>⌥</kbd><kbd>g</kbd> ⚥   Gender symbol
        * <kbd>i</kbd> ☞     Index
        * <kbd>1</kbd>, <kbd>7</kbd> ‽ Interrobang
        * <kbd>3</kbd> №    Numero sign
        * <kbd>r</kbd> ⌑    Square lozenge
        * <kbd>p</kbd> ‴    Triple prime
        * <kbd>⇧</kbd><kbd>p</kbd> ⁗  Quadruple prime
        * <kbd>0</kbd> ⁀    Tie	
        * <kbd>s</kbd> 💀   Skull
        * <kbd>⇧</kbd><kbd>s</kbd> ☠    Skull and Crossbones
        * <kbd>⌥</kbd><kbd>s</kbd> 🕱    Black Skull And Crossbones
        * __Mac symbols__
        * <kbd>a</kbd>     Apple logo
        * <kbd>⌥</kbd><kbd>⌫</kbd> ⌦ Forward Delete
        * <kbd>q</kbd> ⎋    Escape, Esc
        * <kbd>⌥</kbd><kbd>6</kbd> ⇞   Page Up, PgUp
        * <kbd>⌥</kbd><kbd>v</kbd> ⇟   Page Down, PgDn
        * <kbd>⌥</kbd><kbd>9</kbd> ↖   Home
        * <kbd>⌥</kbd><kbd>0</kbd> ↘   End
        * <kbd>c</kbd> ⌧    Clear
        * <kbd>\`</kbd> ⏏   Eject
        * <kbd>\\</kbd> ↩ Return, Carriage Return
        * <kbd>⇧</kbd><kbd>\\</kbd> ↵ Return, Carriage Return
        * <kbd>⌥</kbd><kbd>\\</kbd> ⏎  Return, Carriage Return
        * <kbd>^</kbd><kbd>\\</kbd> ⌤  Enter
    + :sparkles: `ru` <kbd>🕱</kbd>`Typographical` and mapped it to <kbd>⌥</kbd><kbd>г</kbd>, pressing it enables the following:
        * <kbd>б</kbd> ⟨   Left Angle bracket
        * <kbd>ю</kbd> ⟩   Right Angle bracket
        * <kbd>8</kbd> ⁂  Asterism
        * <kbd>6</kbd> ‸   Caret
        * <kbd>⇧</kbd><kbd>⌥</kbd><kbd>6</kbd> ⁁  Caret insertion point
        * <kbd>⇧</kbd><kbd>6</kbd> ⎀  Insertion symbol
        * <kbd>/</kbd> ⁒   Commercial minus sign
        * <kbd>4</kbd> ¤   Currency sign
        * <kbd>е</kbd> †   Dagger
        * <kbd>⇧</kbd><kbd>е</kbd> ‡  Double Dagger
        * <kbd>-</kbd> ⹀   Double hyphen
        * <kbd>⇧</kbd><kbd>-</kbd> ⸗  Double hyphen
        * <kbd>у</kbd> ℮   Estimated sign
        * <kbd>в</kbd> º   Masculine ordinal indicator
        * <kbd>⇧</kbd><kbd>в</kbd> ª  Feminine ordinal indicator
        * <kbd>а</kbd> ❧   Fleuron
        * <kbd>п</kbd> ♀   Gender symbol
        * <kbd>⇧</kbd><kbd>п</kbd> ♂  Gender symbol
        * <kbd>⌥</kbd><kbd>п</kbd> ⚥  Gender symbol
        * <kbd>ш</kbd> ☞	Index
        * <kbd>1</kbd>, <kbd>7</kbd> ‽ Interrobang
        * <kbd>3</kbd> №  Numero sign
        * <kbd>к</kbd> ⌑  Square lozenge
        * <kbd>з</kbd> ‴  Triple prime
        * <kbd>⇧</kbd><kbd>з</kbd> ⁗ Quadruple prime
        * <kbd>0</kbd> ⁀  Tie	
        * <kbd>ы</kbd> 🕱  skull
        * __Mac symbols__
        * <kbd>ф</kbd>    Apple logo
        * <kbd>⌥</kbd><kbd>⌫</kbd> ⌦	Forward Delete
        * <kbd>й</kbd> ⎋            	Escape, Esc
        * <kbd>⌥</kbd><kbd>6</kbd> ⇞	Page Up, PgUp
        * <kbd>⌥</kbd><kbd>м</kbd> ⇟	Page Down, PgDn
        * <kbd>⌥</kbd><kbd>9</kbd> ↖	Home
        * <kbd>⌥</kbd><kbd>0</kbd> ↘	End
        * <kbd>с</kbd> ⌧            	Clear
        * <kbd>></kbd> ⏏            	Eject
        * <kbd>ё</kbd> ↩            	Return, Carriage Return
        * <kbd>⇧</kbd><kbd>ё</kbd> ↵	Return, Carriage Return
        * <kbd>⌥</kbd><kbd>ё</kbd> ⏎	Return, Carriage Return
        * <kbd>^</kbd><kbd>ё</kbd> ⌤	Enter
    + :sparkles: `en` `ru` diacritics <kbd>🕱</kbd>s to <kbd>^</kbd><kbd>§</kbd>–<kbd>=</kbd>:
        * <kbd>^</kbd><kbd>§</kbd> → <kbd>🕱</kbd>`grave`
        * <kbd>^</kbd><kbd>1</kbd> → <kbd>🕱</kbd>`acute`
        * <kbd>^</kbd><kbd>2</kbd> → <kbd>🕱</kbd>`grave`
        * <kbd>^</kbd><kbd>3</kbd> → <kbd>🕱</kbd>`diaeresis`
        * <kbd>^</kbd><kbd>4</kbd> → <kbd>🕱</kbd>`tilde`
        * <kbd>^</kbd><kbd>5</kbd> → <kbd>🕱</kbd>`macron`
        * <kbd>^</kbd><kbd>6</kbd> → <kbd>🕱</kbd>`circumflex`
        * <kbd>^</kbd><kbd>7</kbd> → <kbd>🕱</kbd>`ring`
        * <kbd>^</kbd><kbd>8</kbd> → <kbd>🕱</kbd>`dot-above`
        * <kbd>^</kbd><kbd>9</kbd> → <kbd>🕱</kbd>`breve`
        * <kbd>^</kbd><kbd>0</kbd> → <kbd>🕱</kbd>`caron`
        * <kbd>^</kbd><kbd>-</kbd> → <kbd>🕱</kbd>`dot-below`
        * <kbd>^</kbd><kbd>=</kbd> → <kbd>🕱</kbd>`cedilla`
    + `en` more <kbd>🕱</kbd>'Copyright' symbols
        * <kbd>o</kbd> (ɔ)
        * <kbd>l</kbd> 🄯 (U+01F12F)
        * <kbd>s</kbd> ℠
        * <kbd>p</kbd> ℗
    + `ru` more <kbd>🕱</kbd>'Copyright' symbols
        * <kbd>щ</kbd>, <kbd>о</kbd> (ɔ)
        * <kbd>д</kbd>л</kbd> 🄯 (U+01F12F)
        * <kbd>ы</kbd> ℠
        * <kbd>з</kbd> ℗
    + :sparkles: `en` more symbols to <kbd>🕱</kbd>`OldCyrillic`:
        * <kbd>9</kbd> ҁ
        * <kbd>⌥</kbd><kbd>i</kbd> ї
        * <kbd>r</kbd> ѯ
        * <kbd>t</kbd> є
        * <kbd>p</kbd> ꙁ
        * <kbd>⌥</kbd><kbd>p</kbd> ꙃ
        * <kbd>;</kbd> ꙉ
        * <kbd>j</kbd> ꙋ
        * <kbd>w</kbd> ѡ
        * <kbd>s</kbd> ꙑ
        * <kbd>.</kbd> ꙗ
        * <kbd>'</kbd> ѥ
        * <kbd>z</kbd> ѫ
        * <kbd>⌥</kbd><kbd>z</kbd> ѭ
        * <kbd>f</kbd> ѧ
        * <kbd>⌥</kbd><kbd>f</kbd> ѩ
        * <kbd>c</kbd> ѱ
        * <kbd>,</kbd> ѣ
        * Previously mapped symbols:
        * <kbd>q</kbd> ѳ
        * <kbd>e</kbd> ѣ
        * <kbd>u</kbd> ѵ
        * <kbd>i</kbd> і
        * (and the same with the Capital letters)
    + :sparkles: `ru` more symbols to <kbd>🕱</kbd>`OldCyrillic`:
        * <kbd>9</kbd> ҁ
        * <kbd>⌥</kbd><kbd>ш</kbd> ї
        * <kbd>к</kbd> ѯ
        * <kbd>е</kbd> є
        * <kbd>з</kbd> ꙁ
        * <kbd>⌥</kbd><kbd>з</kbd> ꙃ
        * <kbd>ж</kbd> ꙉ
        * <kbd>о</kbd> ꙋ
        * <kbd>ц</kbd> ѡ
        * <kbd>ы</kbd> ꙑ
        * <kbd>ю</kbd> ꙗ
        * <kbd>э</kbd> ѥ
        * <kbd>я</kbd> ѫ
        * <kbd>⌥</kbd><kbd>я</kbd> ѭ
        * <kbd>а</kbd> ѧ
        * <kbd>⌥</kbd><kbd>а</kbd> ѩ
        * <kbd>с</kbd> ѱ
        * <kbd>б</kbd> ѣ
        * Previously mapped symbols:
        * <kbd>й</kbd> ѳ
        * <kbd>у</kbd> ѣ
        * <kbd>г</kbd> ѵ
        * <kbd>ш</kbd> і
        * (and the same with the Capital letters)
    + `ru` yen ¥ to <kbd>⌥</kbd><kbd>н</kbd>
    + `en` `ru` map `⇤` to <kbd>⇧</kbd><kbd>^</kbd><kbd>⌥</kbd><kbd>⇥</kbd>
    + `en` `ru` map `⌫` to <kbd>⇧</kbd><kbd>^</kbd><kbd>⌥</kbd><kbd>⌫</kbd>
    + `ru` combining diacritics to each invoking key+number (and <kbd>^</kbd>+key+number) without modifiers if they're free: for example, entering the <kbd>🕱</kbd>`diaeresis` via <kbd>3</kbd> or <kbd>ж</kbd> you can insert a ̈ combining diaeresis via <kbd>3</kbd>, but not <kbd>ж</kbd> since it produces `ӝ` (the previous keybind of <kbd>⌥</kbd><kbd>⇧</kbd><kbd>ж</kbd> continues to work)
    + `en` combining diacritics to each invoking key+number (and <kbd>^</kbd>+key+number) without modifiers if they're free: for example, entering the <kbd>🕱</kbd>`diaeresis` via <kbd>3</kbd> or <kbd>;</kbd> you can insert a ̈ combining diaeresis via <kbd>3</kbd> or <kbd>;</kbd>  since both are free of any letters with diaeresis (the previous keybind of <kbd>⌥</kbd><kbd>⇧</kbd><kbd>;</kbd> continues to work). Same scheme for A+B combo diacritics
    + `en` `ru`   ̋ (combining double acute) to <kbd>2</kbd> (in <kbd>🕱</kbd>`acute`)
    + `en` `ru` ́ (combining acute) to <kbd>/</kbd> (in addition to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>/</kbd>), and <kbd>\'</kbd> or <kbd>⌥</kbd><kbd>⇧</kbd><kbd>\'</kbd> (in <kbd>🕱</kbd>`acute`)
        * <kbd>/</kbd>, <kbd>⌥</kbd><kbd>⇧</kbd><kbd>/</kbd> ́ (combining acute)
        * <kbd>\'</kbd>, <kbd>⌥</kbd><kbd>⇧</kbd><kbd>\'</kbd> ́ (combining acute)
    + `en` `ru` map <kbd>🕱</kbd>`Math` to <kbd>^</kbd><kbd>m</kbd>/<kbd>ь</kbd> and <kbd>🕱</kbd>`Diacritics` to <kbd>^</kbd><kbd>;</kbd><kbd>ж</kbd>
    + `en` <kbd>🕱</kbd>`Greek`: `§`, `±` to <kbd>§</kbd>, <kbd>⇧</kbd><kbd>§</kbd>
    + `en` `ru` some duplicate <kbd>⌥</kbd><kbd>Key</kbd> symbols (in <kbd>🕱</kbd>`Math` )
        * <kbd>⌥</kbd><kbd>6</kbd> ⇑
        * <kbd>⌥</kbd><kbd>v</kbd> ⇓
    + `en` `ru` map non-breaking hyphen `‑` to <kbd>⇧</kbd><kbd>^</kbd><kbd>-</kbd>
    + `en` `ru` map symbol for backspace `␈` to <kbd>^</kbd><kbd>⌥</kbd><kbd>⌫</kbd>
    + `en` `ru` map combining enclosing keycap    ⃣    to <kbd>k</kbd> / <kbd>л</kbd> (in <kbd>🕱</kbd>`Diacritics`)
  - __Changed__
    + `en` `ru` <kbd>🕱</kbd>`Greek` :
        * `π` at <kbd>⇧</kbd><kbd>g</kbd> to map 🕱`Greek` (`π` is available as a terminator for <kbd>🕱</kbd>`Math`)
        * copied `ω` to <kbd>w</kbd>, moved `ς` to <kbd>q</kbd>
        * copied `Ω` to <kbd>⇧</kbd><kbd>w</kbd>, moved <kbd>🕱</kbd>`greek-dialytika-tonos` to <kbd>⇧</kbd><kbd>q</kbd>
    + `en` `ru` `🙂` to `¦` at <kbd>⇧</kbd><kbd>⌥</kbd><kbd>\\</kbd> / <kbd>ё</kbd>
  - __Removed__
    + `en`: "fake" double acute characters comprised of combining double acute (a̋e̋i̋m̋), left only single-character ones (őű)

  [0.9.0]: https://github.com/eugenesvk/kbdLayout-Mac/releases/tag/0.9.0
## [0.9.0]
  - __Added__
    + :sparkles: `ru` <kbd>⌫</kbd> within `Math`-enclosed <kbd>🕱</kbd>s now returns to <kbd>🕱</kbd>`Math` instead of exiting to the base layer
    + :sparkles: `ru` <kbd>🕱</kbd>`Math` and mapped it to <kbd>⌥</kbd><kbd>е</kbd>, pressing it enables the following:
        * <kbd>у</kbd> ∃
        * <kbd>ш</kbd> ∩
        * <kbd>т</kbd> ℕ
        * <kbd>г</kbd> ∪
        * <kbd>6</kbd> ⇑
        * <kbd>8</kbd> ∗
        * <kbd>9</kbd> ⊂
        * <kbd>0</kbd> ⊃
        * <kbd>⌥</kbd><kbd>0</kbd> ⇝
        * <kbd>⇧</kbd><kbd>=</kbd> ≝
        * <kbd>⌥</kbd><kbd>=</kbd> ≡
        * <kbd>ф</kbd> ∀
        * <kbd>⌥</kbd><kbd>ф</kbd> ≅
        * <kbd>э</kbd> ∈
        * <kbd>и</kbd> ∵
        * <kbd>с</kbd> ℂ
        * <kbd>в</kbd> ∇
        * <kbd>й</kbd> ℚ
        * <kbd>к</kbd> ℝ
        * <kbd>е</kbd> ∴
        * <kbd>м</kbd> ⇓
        * <kbd>ч</kbd> ·
        * <kbd>я</kbd> ℤ
        * <kbd>⇧</kbd><kbd>я</kbd> ≈
        * <kbd>х</kbd> ⌊
        * <kbd>ъ</kbd> ⌋
        * <kbd>⇧</kbd><kbd>х</kbd> ⌈
        * <kbd>⇧</kbd><kbd>ъ</kbd> ⌉
        * <kbd>ж</kbd> …
        * <kbd>ю</kbd> 〉
        * <kbd>⌥</kbd><kbd>ю</kbd> ．
        * <kbd>⇧</kbd><kbd>.</kbd> ．
        * <kbd>⇧</kbd><kbd>б</kbd> ≤
        * <kbd>⇧</kbd><kbd>ю</kbd> ≥
        * <kbd>ё</kbd> ∨
        * <kbd>></kbd>, <kbd>]</kbd> ¬ (keys left of <kbd>1</kbd>/<kbd>я</kbd>)
    + :sparkles: `ru` <kbd>🕱</kbd>`math/` and mapped it to <kbd>.</kbd> (in <kbd>🕱</kbd>`Math`), pressing it enables the following:
        * <kbd>у</kbd> ∄
        * <kbd>ш</kbd> ⫛
        * <kbd>э</kbd> ∉
        * <kbd>0</kbd> ∅
        * (same with <kbd>⇧</kbd>)
        * <kbd>ё</kbd> ∧
        * <kbd>⇧</kbd><kbd>ё</kbd> ∤
    + :sparkles: `ru` <kbd>🕱</kbd>`mathO` and mapped it to <kbd>щ</kbd> (in <kbd>🕱</kbd>`Math`), pressing it enables the following:
        * <kbd>ю</kbd> ⊙
        * <kbd>.</kbd> ⊘
        * <kbd>-</kbd> ⊖
        * <kbd>=</kbd>, <kbd>⇧</kbd><kbd>=</kbd> ⊕
        * <kbd>8</kbd>, <kbd>⇧</kbd><kbd>8</kbd> ⊛
        * <kbd>ч</kbd>, <kbd>⌥</kbd><kbd>8</kbd> ⊗
    + :sparkles: `ru` <kbd>🕱</kbd>`math-` and mapped it to <kbd>-</kbd> (in <kbd>🕱</kbd>`Math`), pressing it enables the following:
        * <kbd>></kbd>, <kbd>]</kbd> ⇀ (keys left of <kbd>1</kbd>/<kbd>я</kbd>)
        * <kbd>ю</kbd> →
        * <kbd>0</kbd>, <kbd>⌥</kbd><kbd>0</kbd> ⟶
    + :sparkles: `ru` <kbd>🕱</kbd>`math=` and mapped it to <kbd>=</kbd> (in <kbd>🕱</kbd>`Math`), pressing it enables the following:
        * <kbd>0</kbd>, <kbd>⌥</kbd><kbd>0</kbd> ⟹
        * <kbd>=</kbd> ≡
        * <kbd>.</kbd> ≠
        * <kbd>ё</kbd> ⤇
        * <kbd>⌥</kbd><kbd>ё</kbd> ⟾
        * <kbd>б</kbd> ⇐
        * <kbd>ю</kbd> ⇒
    + :sparkles: `ru` <kbd>🕱</kbd>`math_` and mapped it to <kbd>⇧</kbd><kbd>-</kbd> (in <kbd>🕱</kbd>`Math`), pressing it enables the following:
        * <kbd>9</kbd> ⊆
        * <kbd>0</kbd> ⊇
        * <kbd>ё</kbd> ⟂
        * <kbd>б</kbd> ≤
        * <kbd>ю</kbd> ≥
        * (same with <kbd>⇧</kbd>)
    + :sparkles: `ru` <kbd>🕱</kbd>`math|` and mapped it to <kbd>⇧</kbd><kbd>ё</kbd> (in <kbd>🕱</kbd>`Math`), pressing it enables the following:
        * <kbd>ю</kbd> ↦
        * <kbd>⌥</kbd><kbd>0</kbd> ⟼
        * <kbd>0</kbd>, <kbd>⇧</kbd><kbd>0</kbd> ⤇
        * <kbd>-</kbd> ⊦
        * <kbd>⇧</kbd><kbd>-</kbd> ⊥
        * <kbd>=</kbd> ⊧
        * <kbd>⌥</kbd><kbd>=</kbd> ⟾
        * <kbd>⇧</kbd><kbd>=</kbd> ⊩
        * <kbd>х</kbd> ⟦
        * <kbd>ъ</kbd> ⟧
        * <kbd>⇧</kbd><kbd>ю</kbd> ▷
        * <kbd>ё</kbd>, <kbd>⇧</kbd><kbd>ё</kbd> ‖
    + :sparkles: `ru` <kbd>🕱</kbd>`math‹` and mapped it to <kbd>б</kbd> or <kbd>⇧</kbd><kbd>б</kbd> (in <kbd>🕱</kbd>`Math`), pressing it enables the following:
        * <kbd>⌥</kbd><kbd>9</kbd> ⟵
        * <kbd>0</kbd> ↔
        * <kbd>⌥</kbd><kbd>0</kbd> ⟷
        * <kbd>-</kbd> ←
        * <kbd>⌥</kbd><kbd>-</kbd> ⟵
        * <kbd>=</kbd> ⇐
        * <kbd>⌥</kbd><kbd>=</kbd> ⟸
        * <kbd>⇧</kbd><kbd>0</kbd> ⇔
        * <kbd>⇧</kbd><kbd>-</kbd> ≤
        * <kbd>⇧</kbd><kbd>=</kbd> ⇔
        * <kbd>ё</kbd>, <kbd>⇧</kbd><kbd>ё</kbd> ◁
        * <kbd>б</kbd> ←
        * <kbd>ю</kbd>, <kbd>⇧</kbd><kbd>ю</kbd> ◇
        * <kbd>⌥</kbd><kbd>ю</kbd> ⟺

  [0.8.0]: https://github.com/eugenesvk/kbdLayout-Mac/releases/tag/0.8.0
## [0.8.0]
  - __Added__
    + :sparkles: `en` <kbd>⌫</kbd> within `Math`-enclosed <kbd>🕱</kbd>s now returns to <kbd>🕱</kbd>`Math` instead of exiting to the base layer
    + :sparkles: `en` <kbd>🕱</kbd>`Math` and mapped it to <kbd>⌥</kbd><kbd>t</kbd>, pressing it enables the following:
        * <kbd>e</kbd> ∃
        * <kbd>i</kbd> ∩
        * <kbd>n</kbd> ℕ
        * <kbd>u</kbd> ∪
        * <kbd>6</kbd> ⇑
        * <kbd>8</kbd> ∗
        * <kbd>9</kbd> ⊂
        * <kbd>0</kbd> ⊃
        * <kbd>⌥</kbd><kbd>0</kbd> ⇝
        * <kbd>⇧</kbd><kbd>=</kbd> ≝
        * <kbd>⌥</kbd><kbd>=</kbd> ≡
        * <kbd>a</kbd> ∀
        * <kbd>⌥</kbd><kbd>a</kbd> ≅
        * <kbd>\'</kbd> ∈
        * <kbd>b</kbd> ∵
        * <kbd>c</kbd> ℂ
        * <kbd>d</kbd> ∇
        * <kbd>q</kbd> ℚ
        * <kbd>r</kbd> ℝ
        * <kbd>t</kbd> ∴
        * <kbd>v</kbd> ⇓
        * <kbd>x</kbd> ·
        * <kbd>z</kbd> ℤ
        * <kbd>⇧</kbd><kbd>z</kbd> ≈
        * <kbd>[</kbd> ⌊
        * <kbd>]</kbd> ⌋
        * <kbd>⇧</kbd><kbd>[</kbd> ⌈
        * <kbd>⇧</kbd><kbd>]</kbd> ⌉
        * <kbd>;</kbd> …
        * <kbd>.</kbd> 〉
        * <kbd>⌥</kbd><kbd>.</kbd> ．
        * <kbd>⇧</kbd><kbd>/</kbd> ．
        * <kbd>⇧</kbd><kbd>,</kbd> ≤
        * <kbd>⇧</kbd><kbd>.</kbd> ≥
        * <kbd>\\</kbd> ∨
        * <kbd>§</kbd>, <kbd>\`</kbd> ¬ (keys left of <kbd>1</kbd>/<kbd>z</kbd>)
    + :sparkles: `en` <kbd>🕱</kbd>`math/` and mapped it to <kbd>/</kbd> (in <kbd>🕱</kbd>`Math`), pressing it enables the following:
        * <kbd>e</kbd> ∄
        * <kbd>i</kbd> ⫛
        * <kbd>\'</kbd> ∉
        * <kbd>0</kbd> ∅
        * (same with <kbd>⇧</kbd>)
        * <kbd>\\</kbd> ∧
        * <kbd>⇧</kbd><kbd>\\</kbd> ∤
    + :sparkles: `en` <kbd>🕱</kbd>`mathO` and mapped it to <kbd>o</kbd> (in <kbd>🕱</kbd>`Math`), pressing it enables the following:
        * <kbd>.</kbd> ⊙
        * <kbd>/</kbd> ⊘
        * <kbd>-</kbd> ⊖
        * <kbd>=</kbd>, <kbd>⇧</kbd><kbd>=</kbd> ⊕
        * <kbd>8</kbd>, <kbd>⇧</kbd><kbd>8</kbd> ⊛
        * <kbd>x</kbd>, <kbd>⌥</kbd><kbd>8</kbd> ⊗
    + :sparkles: `en` <kbd>🕱</kbd>`math-` and mapped it to <kbd>-</kbd> (in <kbd>🕱</kbd>`Math`), pressing it enables the following:
        * <kbd>§</kbd>, <kbd>\`</kbd> ⇀ (keys left of <kbd>1</kbd>/<kbd>z</kbd>)
        * <kbd>.</kbd> →
        * <kbd>0</kbd>, <kbd>⌥</kbd><kbd>0</kbd> ⟶
    + :sparkles: `en` <kbd>🕱</kbd>`math=` and mapped it to <kbd>=</kbd> (in <kbd>🕱</kbd>`Math`), pressing it enables the following:
        * <kbd>0</kbd>, <kbd>⌥</kbd><kbd>0</kbd> ⟹
        * <kbd>=</kbd> ≡
        * <kbd>/</kbd> ≠
        * <kbd>\\</kbd> ⤇
        * <kbd>⌥</kbd><kbd>\\</kbd> ⟾
        * <kbd>,</kbd> ⇐
        * <kbd>.</kbd> ⇒
    + :sparkles: `en` <kbd>🕱</kbd>`math_` and mapped it to <kbd>⇧</kbd><kbd>-</kbd> (in <kbd>🕱</kbd>`Math`), pressing it enables the following:
        * <kbd>9</kbd> ⊆
        * <kbd>0</kbd> ⊇
        * <kbd>\\</kbd> ⟂
        * <kbd>,</kbd> ≤
        * <kbd>.</kbd> ≥
        * (same with <kbd>⇧</kbd>)
    + :sparkles: `en` <kbd>🕱</kbd>`math|` and mapped it to <kbd>⇧</kbd><kbd>\\</kbd> (in <kbd>🕱</kbd>`Math`), pressing it enables the following:
        * <kbd>.</kbd> ↦
        * <kbd>⌥</kbd><kbd>0</kbd> ⟼
        * <kbd>0</kbd>, <kbd>⇧</kbd><kbd>0</kbd> ⤇
        * <kbd>-</kbd> ⊦
        * <kbd>⇧</kbd><kbd>-</kbd> ⊥
        * <kbd>=</kbd> ⊧
        * <kbd>⌥</kbd><kbd>=</kbd> ⟾
        * <kbd>⇧</kbd><kbd>=</kbd> ⊩
        * <kbd>[</kbd> ⟦
        * <kbd>]</kbd> ⟧
        * <kbd>⇧</kbd><kbd>.</kbd> ▷
        * <kbd>\\</kbd>, <kbd>⇧</kbd><kbd>\\</kbd> ‖
    + :sparkles: `en` <kbd>🕱</kbd>`math‹` and mapped it to <kbd>,</kbd> or <kbd>⇧</kbd><kbd>,</kbd> (in <kbd>🕱</kbd>`Math`), pressing it enables the following:
        * <kbd>⌥</kbd><kbd>9</kbd> ⟵
        * <kbd>0</kbd> ↔
        * <kbd>⌥</kbd><kbd>0</kbd> ⟷
        * <kbd>-</kbd> ←
        * <kbd>⌥</kbd><kbd>-</kbd> ⟵
        * <kbd>=</kbd> ⇐
        * <kbd>⌥</kbd><kbd>=</kbd> ⟸
        * <kbd>⇧</kbd><kbd>0</kbd> ⇔
        * <kbd>⇧</kbd><kbd>-</kbd> ≤
        * <kbd>⇧</kbd><kbd>=</kbd> ⇔
        * <kbd>\\</kbd>, <kbd>⇧</kbd><kbd>\\</kbd> ◁
        * <kbd>,</kbd> ←
        * <kbd>.</kbd>, <kbd>⇧</kbd><kbd>.</kbd> ◇
        * <kbd>⌥</kbd><kbd>.</kbd> ⟺

  [0.7.0]: https://github.com/eugenesvk/kbdLayout-Mac/releases/tag/0.7.0
## [0.7.0]
  - __Added__
    + :sparkles: `en` `Greek` macOS layers (base, <kbd>⇧</kbd>, <kbd>⌥</kbd>, <kbd>⇧</kbd><kbd>⌥</kbd>), <kbd>🕱</kbd>`Greek` (mapped to <kbd>^</kbd><kbd>g</kbd>), and (in <kbd>🕱</kbd>`Greek`):
        * <kbd>🕱</kbd>`greek-tonos` (mapped to <kbd>;</kbd>)
        * <kbd>🕱</kbd>`diaeresis-greek` (mapped to <kbd>⇧</kbd><kbd>;</kbd>)
        * <kbd>🕱</kbd>`greek-dialytika-tonos` (mapped to <kbd>⇧</kbd><kbd>w</kbd> / <kbd>⌥</kbd><kbd>;</kbd>)
    + :sparkles: `ru` `Greek` macOS layers (base, <kbd>⇧</kbd>, <kbd>⌥</kbd>, <kbd>⇧</kbd><kbd>⌥</kbd>), <kbd>🕱</kbd>`Greek` (mapped to <kbd>^</kbd><kbd>п</kbd>), and (in <kbd>🕱</kbd>`Greek`):
        * <kbd>🕱</kbd>`greek-tonos` (mapped to <kbd>ж</kbd>)
        * <kbd>🕱</kbd>`diaeresis-greek` (mapped to <kbd>⇧</kbd><kbd>ж</kbd>)
        * <kbd>🕱</kbd>`greek-dialytika-tonos` (mapped to <kbd>⇧</kbd><kbd>ц</kbd> / <kbd>⌥</kbd><kbd>ж</kbd>)

  [0.6.0]: https://github.com/eugenesvk/kbdLayout-Mac/releases/tag/0.6.0
## [0.6.0]
  - __Added__
    + :sparkles: `en` default `U.S.` macOS layers <kbd>⌥</kbd> / <kbd>⇧</kbd><kbd>⌥</kbd> to <kbd>^</kbd><kbd>⌥</kbd> / <kbd>⇧</kbd><kbd>^</kbd><kbd>⌥</kbd>
    + :sparkles: `ru` default `Russian - PC` macOS layers <kbd>⌥</kbd> / <kbd>⇧</kbd><kbd>⌥</kbd> to <kbd>^</kbd><kbd>⌥</kbd> / <kbd>⇧</kbd><kbd>^</kbd><kbd>⌥</kbd>
    + :sparkles: `en` <kbd>🕱</kbd>`Diacritics` and mapped it to <kbd>^</kbd><kbd>\'</kbd> — after this <kbd>🕱</kbd> is pressed, the following keys are mapped to the following diacritic <kbd>🕱</kbd>s:
        * <kbd>1</kbd>, <kbd>/</kbd> → <kbd>🕱</kbd>`acute` (`´`)
        * <kbd>2</kbd>, <kbd>\`</kbd>, <kbd>\\</kbd> → <kbd>🕱</kbd>`grave` (`` ` ``)
        * <kbd>3</kbd>, <kbd>;</kbd>  → <kbd>🕱</kbd>`diaeresis` (`¨`)
        * <kbd>4</kbd>, <kbd>n</kbd>  → <kbd>🕱</kbd>`tilde` (`˜`)
        * <kbd>5</kbd>, <kbd>o</kbd>  → <kbd>🕱</kbd>`macron` (`¯`)
        * <kbd>6</kbd>       → <kbd>🕱</kbd>`circumflex` (`ˆ`)
        * <kbd>7</kbd>, <kbd>r</kbd>  → <kbd>🕱</kbd>`ring` (`˚`)
        * <kbd>8</kbd>, <kbd>i</kbd>  → <kbd>🕱</kbd>`dot-above` (`˙`)
        * <kbd>9</kbd>, <kbd>q</kbd>  → <kbd>🕱</kbd>`breve` (`˘`)
        * <kbd>0</kbd>, <kbd>v</kbd>  → <kbd>🕱</kbd>`caron` (`ˇ`)
        * <kbd>-</kbd>, <kbd>u</kbd>  → <kbd>🕱</kbd>`dot-below` (`◌̣`)
        * <kbd>=</kbd>, <kbd>z</kbd>  → <kbd>🕱</kbd>`cedilla` (`¸`)
        * ,     <kbd>h</kbd> → <kbd>🕱</kbd>`double-acute`
        * ,     <kbd>\'</kbd> → <kbd>🕱</kbd>`horn`
        * ,     <kbd>j</kbd> → <kbd>🕱</kbd>`hook-above`
        * ,     <kbd>g</kbd> → <kbd>🕱</kbd>`ogonek` (`˛`)
    + :sparkles: `ru` <kbd>🕱</kbd>`Diacritics` and mapped it to <kbd>^</kbd><kbd>\'</kbd> — after this <kbd>🕱</kbd> is pressed, the following keys are mapped to the following diacritic <kbd>🕱</kbd>s:
        * <kbd>1</kbd>, <kbd>.</kbd> → <kbd>🕱</kbd>`acute` (`´`)
        * <kbd>2</kbd>, <kbd>></kbd>, <kbd>]</kbd> → <kbd>🕱</kbd>`grave` (`` ` ``)
        * <kbd>3</kbd>, <kbd>ж</kbd>  → <kbd>🕱</kbd>`diaeresis` (`¨`)
        * <kbd>4</kbd>, <kbd>т</kbd>  → <kbd>🕱</kbd>`tilde` (`˜`)
        * <kbd>5</kbd>, <kbd>щ</kbd>  → <kbd>🕱</kbd>`macron` (`¯`)
        * <kbd>6</kbd>       → <kbd>🕱</kbd>`circumflex` (`ˆ`)
        * <kbd>7</kbd>, <kbd>к</kbd>  → <kbd>🕱</kbd>`ring` (`˚`)
        * <kbd>8</kbd>, <kbd>ш</kbd>  → <kbd>🕱</kbd>`dot-above` (`˙`)
        * <kbd>9</kbd>, <kbd>й</kbd>  → <kbd>🕱</kbd>`breve` (`˘`)
        * <kbd>0</kbd>, <kbd>м</kbd>  → <kbd>🕱</kbd>`caron` (`ˇ`)
        * <kbd>-</kbd>, <kbd>г</kbd>  → <kbd>🕱</kbd>`dot-below` (`◌̣`)
        * <kbd>=</kbd>, <kbd>я</kbd>  → <kbd>🕱</kbd>`cedilla` (`¸`)
        * ,     <kbd>р</kbd> → <kbd>🕱</kbd>`double-acute`
    + :sparkles: `ru` <kbd>🕱</kbd>`dot-above` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>ш</kbd>, pressing it enables the following:
        * <kbd>␠</kbd> ˙ (stand-alone dot above)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>ш</kbd>  ̇ (combining dot above)
    + :sparkles: `ru` <kbd>🕱</kbd>`dot-below` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>г</kbd>, pressing it enables the following:
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>г</kbd> ̣ (combining dot below)
    + `en` map <kbd>🕱</kbd>`breve+dot-below` to <kbd>-</kbd> (in <kbd>🕱</kbd>`breve`)
    + :sparkles: `en` <kbd>🕱</kbd>`ogonek` and mapped it to <kbd>g</kbd> (in <kbd>🕱</kbd>`Diacritics`), pressing it enables the following:
        * <kbd>a</kbd> ą
        * <kbd>e</kbd> ę
        * <kbd>i</kbd> į
        * <kbd>o</kbd> ǫ
        * <kbd>u</kbd> ų
        * (and the same with the Capital letters)
        * <kbd>␠</kbd> ˛ (stand-alone ogonek)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>g</kbd>  ̨ (combining ogonek)
    + :sparkles: `en` <kbd>🕱</kbd>`ogonek+macron` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd> (in <kbd>🕱</kbd>`ogonek`), pressing it enables the following:
        * <kbd>o</kbd> ǭ
        * (and the same with the Capital letters)
    + :sparkles: `en` <kbd>🕱</kbd>`horn` and mapped it to <kbd>\'</kbd> (in <kbd>🕱</kbd>`Diacritics`), pressing it enables the following:
        * <kbd>o</kbd> ơ
        * <kbd>u</kbd> ư
        * (and the same with the Capital letters)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>\'</kbd>  ̛ (combining horn)
    + :sparkles: `en` <kbd>🕱</kbd>`hook-above` and mapped it to <kbd>j</kbd> (in <kbd>🕱</kbd>`Diacritics`), pressing it enables the following:
        * <kbd>a</kbd> ả
        * <kbd>e</kbd> ẻ
        * <kbd>i</kbd> ỉ
        * <kbd>o</kbd> ỏ
        * <kbd>u</kbd> ủ
        * <kbd>y</kbd> ỷ
        * (and the same with the Capital letters)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>j</kbd> ̉ (combining hook above)
    + :sparkles: `en` <kbd>🕱</kbd>`horn+dot-below` and mapped to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>u</kbd> or <kbd>-</kbd> (in <kbd>🕱</kbd>`horn`), pressing it enables the following:
        * <kbd>o</kbd> ợ
        * <kbd>u</kbd> ự
        * (and the same with the Capital letters)
    + :sparkles: `en` <kbd>🕱</kbd>`horn+hook-above` and mapped to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>j</kbd> (in <kbd>🕱</kbd>`horn`), pressing it enables the following:
        * <kbd>o</kbd> ở
        * <kbd>u</kbd> ử
        * (and the same with the Capital letters)
    + :sparkles: `en` <kbd>🕱</kbd>`horn+tilde` and mapped to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>n</kbd> or <kbd>4</kbd> (in <kbd>🕱</kbd>`horn`), pressing it enables the following:
        * <kbd>o</kbd> ỡ
        * <kbd>u</kbd> ữ
        *  (and the same with the Capital letters)
    + :sparkles: `en` <kbd>🕱</kbd>`horn+acute` and mapped to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>/</kbd> or <kbd>1</kbd> (in <kbd>🕱</kbd>`horn`), pressing it enables the following:
        * <kbd>o</kbd> ớ
        * <kbd>u</kbd> ứ
        * (and the same with the Capital letters)
    + :sparkles: `en` <kbd>🕱</kbd>`horn+grave` and mapped to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>\`</kbd> or <kbd>2</kbd> or <kbd>\`</kbd> (in <kbd>🕱</kbd>`horn`), pressing it enables the following:
        * <kbd>o</kbd> ờ
        * <kbd>u</kbd> ừ
        * (and the same with the Capital letters)
    + :sparkles: `en` <kbd>🕱</kbd>`circumflex+hook-above` and mapped to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>j</kbd> (in <kbd>🕱</kbd>`circumflex`), pressing it enables the following:
        * <kbd>a</kbd> ẩ
        * <kbd>e</kbd> ể
        * <kbd>o</kbd> ổ
        * (and the same with the Capital letters)
    + :sparkles: `en` <kbd>🕱</kbd>`breve+hook-above` and mapped to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>j</kbd> (in <kbd>🕱</kbd>`breve`), pressing it enables the following:
        * <kbd>a</kbd> ẳ
        *  (and the same with the Capital letters)
  - __Changed__
    + `en` <kbd>⌘</kbd><kbd>⌥</kbd> / <kbd>⇧</kbd><kbd>⌘</kbd><kbd>⌥</kbd> to regular <kbd>a</kbd>–<kbd>z</kbd> / <kbd>A</kbd>–<kbd>Z</kbd> layers
    + `ru` <kbd>⌘</kbd><kbd>⌥</kbd> to regular <kbd>a</kbd>–<kbd>z</kbd> layer (<kbd>⇧</kbd><kbd>⌘</kbd><kbd>⌥</kbd> was already <kbd>a</kbd>–<kbd>z</kbd>)
    + `ru` `en` <kbd>^</kbd><kbd>⌥</kbd><kbd>⇥</kbd> to insert `⇥`

  [0.5.0]: https://github.com/eugenesvk/kbdLayout-Mac/releases/tag/0.5.0
## [0.5.0]
  - __Added__
    + :sparkles: `en` <kbd>🕱</kbd>`dot-above` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>i</kbd>, pressing it enables the following:
        * <kbd>a</kbd>–<kbd>z</kbd> ȧ–ż (except for <kbd>q</kbd><kbd>u</kbd><kbd>i</kbd><kbd>j</kbd><kbd>k</kbd><kbd>l</kbd><kbd>v</kbd>)
        * (and the same with the Capital letters)
        * <kbd>I</kbd> İ
        * <kbd>␠</kbd> ˙ (stand-alone dot above)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>i</kbd>  ̇ (combining dot above)
    + :sparkles: `en` <kbd>🕱</kbd>`dot-below` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>u</kbd>, pressing it enables the following:
        * <kbd>a</kbd>–<kbd>z</kbd> ạ–ẓ (except for <kbd>c</kbd><kbd>f</kbd><kbd>g</kbd><kbd>i</kbd><kbd>j</kbd><kbd>p</kbd><kbd>x</kbd>)
        * (and the same with the Capital letters)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>u</kbd> ̣ (combining dot below)
    + :sparkles: `en` <kbd>🕱</kbd> `DotBelow+Macron` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd> — (after <kbd>🕱</kbd>`dot-below` is pressed) after this <kbd>🕱</kbd> is pressed, the following keys are mapped to:
        * <kbd>l</kbd> ḹ
        * <kbd>r</kbd> ṝ
        * (and the same with the Capital letters)
    + :sparkles: `en` <kbd>🕱</kbd> `DotBelow+DotAbove` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>i</kbd> — (after <kbd>🕱</kbd>`dot-below` is pressed) after this <kbd>🕱</kbd> is pressed, the following keys are mapped to:
        * <kbd>s</kbd> ṩ
        * (and the same with the Capital letters)
    + :sparkles: `en` <kbd>🕱</kbd> `DotAbove+Macron` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd> — (after <kbd>🕱</kbd>`dot-above` is pressed) after this <kbd>🕱</kbd> is pressed, the following keys are mapped to:
        * <kbd>a</kbd> ǡ
        * <kbd>o</kbd> ȱ
        * (and the same with the Capital letters)
    + :sparkles: `en` <kbd>🕱</kbd> `Tilde+Macron` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd> (in <kbd>🕱</kbd>`tilde`), pressing it enables the following:
        * <kbd>o</kbd> ȭ
        * (and the same with the Capital letters)
    + :sparkles: `en` <kbd>🕱</kbd> `Diaeresis+Macron` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd> (in <kbd>🕱</kbd>`diaeresis`), pressing it enables the following:
        * <kbd>a</kbd> ǟ
        * <kbd>o</kbd> ȫ
        * <kbd>u</kbd> ǖ
        * (and the same with the Capital letters)
    + :sparkles: `en` <kbd>🕱</kbd> `Breve+DotBelow` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>u</kbd> (in <kbd>🕱</kbd>`breve`), pressing it enables the following:
        * <kbd>a</kbd> ặ
        * (and the same with the Capital letters)
    + :sparkles: `en` <kbd>🕱</kbd> `Acute+DotAbove` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>i</kbd> (in <kbd>🕱</kbd>`acute`), pressing it enables the following:
        * <kbd>s</kbd> ṥ
        * (and the same with the Capital letters)
    + :sparkles: `en` <kbd>🕱</kbd> `Caron+DotAbove` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>i</kbd> (in <kbd>🕱</kbd>`caron`), pressing it enables the following:
        * <kbd>s</kbd> ṧ
        * (and the same with the Capital letters)
    + :sparkles: `en` <kbd>🕱</kbd> `Circumflex+DotBelow` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>u</kbd> (in <kbd>🕱</kbd>`circumflex`), pressing it enables the following:
        * <kbd>a</kbd> ậ
        * <kbd>e</kbd> ệ
        * <kbd>o</kbd> ộ
        * (and the same with the Capital letters)
  - __Fixed__
    + :beetle: removed duplicate `acute-2`, restored `acute`

  [0.4.0]: https://github.com/eugenesvk/kbdLayout-Mac/releases/tag/0.4.0
## [0.4.0]
  - __Added__
    + :sparkles: `en` <kbd>🕱</kbd>`Copyright` and mapped it to <kbd>⌥</kbd><kbd>c</kbd>, pressing it enables the following:
        * <kbd>c</kbd> ©
        * <kbd>r</kbd> ®
        * <kbd>t</kbd> ™
    + :sparkles: `ru` <kbd>🕱</kbd>`Copyright` and mapped it to <kbd>⌥</kbd><kbd>с</kbd>, pressing it enables the following:
        * <kbd>с</kbd> ©
        * <kbd>к</kbd><kbd>р</kbd> ®
        * <kbd>е</kbd><kbd>т</kbd> ™
    + :sparkles: `en` <kbd>🕱</kbd>`OldCyrillic` and mapped it to <kbd>⌥</kbd><kbd>o</kbd>, pressing it enables the following:
        * <kbd>q</kbd> ѳ
        * <kbd>e</kbd> ѣ
        * <kbd>u</kbd> ѵ
        * <kbd>i</kbd> і
    + :sparkles: `ru` <kbd>🕱</kbd>`OldCyrillic` and mapped it to <kbd>⌥</kbd><kbd>щ</kbd>, pressing it enables the following:
        * <kbd>й</kbd> ѳ
        * <kbd>у</kbd> ѣ
        * <kbd>г</kbd> ѵ
        * <kbd>ш</kbd> і
    + :sparkles: `en` <kbd>🕱</kbd>`macron` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd>, pressing it enables the following:
        * <kbd>a</kbd> ā
        * <kbd>e</kbd> ē
        * <kbd>i</kbd> ī
        * <kbd>o</kbd> ō
        * <kbd>u</kbd> ū
        * <kbd>y</kbd> ȳ
        * <kbd>g</kbd> ḡ
        * (and the same with the Capital letters)
        * <kbd>␠</kbd> ¯ (stand-alone macron)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd>  ̄ (combining macron)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>q</kbd>  ᷌  (combining macron-breve)
    + :sparkles: `en` add 🕱 dead sub-key `Macron+Grave` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>\`</kbd> or <kbd>\`</kbd> (in <kbd>🕱</kbd>`macron`), pressing it enables the following:
        * <kbd>e</kbd> ḕ
        * <kbd>o</kbd> ṑ
        * (and the same with the Capital letters)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>\`</kbd>  ᷆ (combining Macron-Grave)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd> ᷅ (combining Grave-Macron)
    + :sparkles: `en` add 🕱 dead sub-key `Macron+Acute` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>;</kbd> or <kbd>;</kbd> (in <kbd>🕱</kbd>`macron`), pressing it enables the following:
        * <kbd>e</kbd> ḗ
        * <kbd>o</kbd> ṓ
        * (and the same with the Capital letters)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>/</kbd> ᷄ (combining Macron-Acute)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd> ᷇ (combining Acute-Macron)
    + :sparkles: `ru` <kbd>🕱</kbd>`macron` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>щ</kbd>, pressing it enables the following:
        * <kbd>й</kbd> ӣ
        * <kbd>у</kbd> ӯ
        * <kbd>и</kbd> ӣ
        * (and the same with the Capital letters)
        * <kbd>␠</kbd> ¯ (stand-alone macron)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>щ</kbd>  ̄ (combining macron)

  [0.3.0]: https://github.com/eugenesvk/kbdLayout-Mac/releases/tag/0.3.0
## [0.3.0]
  - __Added__
    + :sparkles: `ru` <kbd>🕱</kbd>`space` and mapped it to <kbd>^</kbd><kbd>␠</kbd>, pressing it enables the following:
        * <kbd>о</kbd> word joiner
        * <kbd>я</kbd>, <kbd>0</kbd> zero-width
        * <kbd>р</kbd>, <kbd>в</kbd> hair
        * <kbd>е</kbd> thin
        * <kbd>и</kbd> narrow no-break
        * <kbd>з</kbd>, <kbd>.</kbd>, <kbd>п</kbd> punctuation
        * <kbd>а</kbd>, <kbd>ф</kbd> figure
        * <kbd>т</kbd>, <kbd>н</kbd> en
        * <kbd>ь</kbd>, <kbd>м</kbd> em
        * <kbd>г</kbd>, <kbd>у</kbd> open box
        * <kbd>ы</kbd>, <kbd>с</kbd> symbol for space
        * <kbd>⇧</kbd><kbd>ы</kbd>, <kbd>⇧</kbd><kbd>с</kbd> blank symbol
        * <kbd>-</kbd> non-breaking hyphen
    + `ru` spaces of various widths, mapped to <kbd>␠</kbd> with various modifiers
        * <kbd>^</kbd><kbd>⌥</kbd>            	hair
        * <kbd>⌥</kbd><kbd>⌘</kbd>            	thin
        * <kbd>⇧</kbd><kbd>^</kbd>            	punctuation
        * <kbd>⇧</kbd><kbd>^</kbd><kbd>⌥</kbd>	figure
        * <kbd>⇧</kbd><kbd>⌥</kbd><kbd>⌘</kbd>	en
        * <kbd>^</kbd><kbd>⌥</kbd><kbd>⌘</kbd>	em
        * (already included in the layout)
        * <kbd>⌥</kbd>            	no-break
        * <kbd>⇧</kbd><kbd>⌥</kbd>	zero-width
  - __Changed__
    + `ru` Modifiers with <kbd>^</kbd>: split into 5 additional modifier layers (#10 <kbd>^</kbd>, #11 <kbd>^</kbd><kbd>⇧</kbd>, #12 <kbd>^</kbd><kbd>⌥</kbd>, #13 <kbd>^</kbd><kbd>⌥</kbd><kbd>⇧</kbd>, #14 <kbd>^</kbd><kbd>⌥</kbd><kbd>⌘</kbd>) to allow more assignments, e.g., to <kbd>␠</kbd>

[0.2.0]: https://github.com/eugenesvk/kbdLayout-Mac/releases/tag/0.2.0
## [0.2.0]
  - __Added__
    + :sparkles: `en` <kbd>🕱</kbd>`space` and mapped it to <kbd>^</kbd><kbd>␠</kbd> — after a <kbd>🕱</kbd> is pressed, spaces of various widths are mnemonically mapped to:
        * <kbd>j</kbd> word joiner
        * <kbd>z</kbd>, <kbd>0</kbd> zero-width
        * <kbd>h</kbd> hair
        * <kbd>t</kbd> thin
        * <kbd>b</kbd> narrow no-break
        * <kbd>p</kbd>, <kbd>.</kbd> punctuation
        * <kbd>f</kbd> figure
        * <kbd>n</kbd> en
        * <kbd>m</kbd> em
        * <kbd>u</kbd> open box
        * <kbd>s</kbd> symbol for space
        * <kbd>⇧</kbd><kbd>s</kbd> blank symbol
        * <kbd>-</kbd> non-breaking hyphen
    + `en` spaces of various widths, mapped to <kbd>␠</kbd> with various modifiers
        * <kbd>^</kbd><kbd>⌥</kbd>            	hair
        * <kbd>⌥</kbd><kbd>⌘</kbd>            	thin
        * <kbd>⇧</kbd><kbd>^</kbd>            	punctuation
        * <kbd>⇧</kbd><kbd>^</kbd><kbd>⌥</kbd>	figure
        * <kbd>⇧</kbd><kbd>⌥</kbd><kbd>⌘</kbd>	en
        * <kbd>^</kbd><kbd>⌥</kbd><kbd>⌘</kbd>	em
        * (already included in the layout)
        * <kbd>⌥</kbd>            	no-break
        * <kbd>⇧</kbd><kbd>⌥</kbd>	zero-width
  - __Changed__
    + `en` Modifiers with <kbd>^</kbd>: split into 5 additional modifier layers (#9 <kbd>^</kbd>, #10 <kbd>^</kbd><kbd>⇧</kbd>, #11 <kbd>^</kbd><kbd>⌥</kbd>, #12 <kbd>^</kbd><kbd>⌥</kbd><kbd>⇧</kbd>, #13 <kbd>^</kbd><kbd>⌥</kbd><kbd>⌘</kbd>) to allow more assignments, e.g., to <kbd>␠</kbd>

[0.1.0]: https://github.com/eugenesvk/kbdLayout-Mac/releases/tag/0.1.0
## [0.1.0]
  - __Added__
    + :sparkles: original Ilya Birman Typography Layout
    + :sparkles: Math layout
  - __Changed__
    + English layout: many various updates to the original layout
    + Russian layout: many various updates to the original layout
