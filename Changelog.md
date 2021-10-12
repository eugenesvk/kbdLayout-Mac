# Changelog
All notable changes to this project will be documented in this file

[unreleased]: https://github.com/eugenesvk/kbdLayout-Mac/compare/0.5.0...HEAD
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
    + :sparkles: `en` default macOS layers <kbd>⌥</kbd> / <kbd>⇧</kbd><kbd>⌥</kbd> to <kbd>^</kbd><kbd>⌥</kbd> / <kbd>⇧</kbd><kbd>^</kbd><kbd>⌥</kbd>
    + :sparkles: `ru` default `Russian - PC` macOS layers <kbd>⌥</kbd> / <kbd>⇧</kbd><kbd>⌥</kbd> to <kbd>^</kbd><kbd>⌥</kbd> / <kbd>⇧</kbd><kbd>^</kbd><kbd>⌥</kbd>
    +  :sparkles: `en` <kbd>🕱</kbd>`Diacritics` and mapped it to <kbd>^</kbd><kbd>\'</kbd> — after this <kbd>🕱</kbd> is pressed, the following keys are mapped to the following diacritic <kbd>🕱</kbd>s:
        * <kbd>1</kbd>, <kbd>/</kbd> → <kbd>🕱</kbd>`acute` (`´`)
        * <kbd>2</kbd>, <kbd>\`</kbd>, <kbd>\</kbd> → <kbd>🕱</kbd>`grave` (`` ` ``)
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
        * <kbd>h</kbd>       → <kbd>🕱</kbd>`double-acute`
  - __Changed__
    + `en` <kbd>⌘</kbd><kbd>⌥</kbd> / <kbd>⇧</kbd><kbd>⌘</kbd><kbd>⌥</kbd> to regular <kbd>a</kbd>–<kbd>z</kbd> / <kbd>A</kbd>–<kbd>Z</kbd> layers
    + `ru` <kbd>⌘</kbd><kbd>⌥</kbd> to regular <kbd>a</kbd>–<kbd>z</kbd> layer (<kbd>⇧</kbd><kbd>⌘</kbd><kbd>⌥</kbd> was already <kbd>a</kbd>–<kbd>z</kbd>)

  [0.5.0]: https://github.com/eugenesvk/kbdLayout-Mac/releases/tag/0.5.0
## [0.5.0]
  - __Added__
    +  :sparkles: `en` add 🕱 dead key `dot-above` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>i</kbd> — after dead key is pressed, the following keys are mapped to:
        * <kbd>a</kbd>–<kbd>z</kbd> ȧ–ż (except for <kbd>q</kbd><kbd>u</kbd><kbd>i</kbd><kbd>j</kbd><kbd>k</kbd><kbd>l</kbd><kbd>v</kbd>)
        * (and the same with the Capital letters)
        * <kbd>I</kbd> İ
        * <kbd>space</kbd> ˙ (stand-alone dot above)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>i</kbd>  ̇ (combining dot above)
    +  :sparkles: `en` add 🕱 dead key `dot-below` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>u</kbd> — after dead key is pressed, the following keys are mapped to:
        * <kbd>a</kbd>–<kbd>z</kbd> ạ–ẓ (except for <kbd>c</kbd><kbd>f</kbd><kbd>g</kbd><kbd>i</kbd><kbd>j</kbd><kbd>p</kbd><kbd>x</kbd>)
        * (and the same with the Capital letters)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>u</kbd> ̣ (combining dot below)
    +  :sparkles: `en` add 🕱 dead key `DotBelow+Macron` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd> — (after `dot-below` dead key is pressed) after dead key is pressed, the following keys are mapped to:
        * <kbd>l</kbd> ḹ
        * <kbd>r</kbd> ṝ
        * (and the same with the Capital letters)
    +  :sparkles: `en` add 🕱 dead key `DotBelow+DotAbove` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>i</kbd> — (after `dot-below` dead key is pressed) after dead key is pressed, the following keys are mapped to:
        * <kbd>s</kbd> ṩ
        * (and the same with the Capital letters)
    +  :sparkles: `en` add 🕱 dead key `DotAbove+Macron` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd> — (after `dot-above` dead key is pressed) after dead key is pressed, the following keys are mapped to:
        * <kbd>a</kbd> ǡ
        * <kbd>o</kbd> ȱ
        * (and the same with the Capital letters)
    +  :sparkles: `en` add 🕱 dead key `Tilde+Macron` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd> — (after `tilde` dead key is pressed) after dead key is pressed, the following keys are mapped to:
        * <kbd>o</kbd> ȭ
        * (and the same with the Capital letters)
    +  :sparkles: `en` add 🕱 dead key `Diaeresis+Macron'` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd> — (after `diaeresis` dead key is pressed) after dead key is pressed, the following keys are mapped to:
        * <kbd>a</kbd> ǟ
        * <kbd>o</kbd> ȫ
        * <kbd>u</kbd> ǖ
        * (and the same with the Capital letters)
    +  :sparkles: `en` add 🕱 dead key `Breve+DotBelow` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>u</kbd> — (after `breve` dead key is pressed) after dead key is pressed, the following keys are mapped to:
        * <kbd>a</kbd> ặ
        * (and the same with the Capital letters)
    +  :sparkles: `en` add 🕱 dead key `Acute+DotAbove` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>i</kbd> — (after `acute` dead key is pressed) after dead key is pressed, the following keys are mapped to:
        * <kbd>s</kbd> ṥ
        * (and the same with the Capital letters)
    +  :sparkles: `en` add 🕱 dead key `Caron+DotAbove` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>i</kbd> — (after `caron` dead key is pressed) after dead key is pressed, the following keys are mapped to:
        * <kbd>s</kbd> ṧ
        * (and the same with the Capital letters)
    +  :sparkles: `en` add 🕱 dead key `Circumflex+DotBelow` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>u</kbd> — (after `circumflex` dead key is pressed) after dead key is pressed, the following keys are mapped to:
        * <kbd>a</kbd> ậ
        * <kbd>e</kbd> ệ
        * <kbd>o</kbd> ộ
        * (and the same with the Capital letters)
  - __Fixed__
    + :beetle: removed duplicate acute-2, restored acute

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
    +  :sparkles: `en` add 🕱 dead key `OldCyrillic` and mapped it to <kbd>⌥</kbd><kbd>o</kbd> — after dead key is pressed, the following keys are mapped to:
        * <kbd>q</kbd> ѳ
        * <kbd>e</kbd> ѣ
        * <kbd>u</kbd> ѵ
        * <kbd>i</kbd> і
    +  :sparkles: `ru` add 🕱 dead key `OldCyrillic` and mapped it to <kbd>⌥</kbd><kbd>щ</kbd> — after dead key is pressed, the following keys are mapped to:
        * <kbd>й</kbd> ѳ
        * <kbd>у</kbd> ѣ
        * <kbd>г</kbd> ѵ
        * <kbd>ш</kbd> і
    +  :sparkles: `en` add 🕱 dead key `macron` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd> — after dead key is pressed, the following keys are mapped to:
        * <kbd>a</kbd> ā
        * <kbd>e</kbd> ē
        * <kbd>i</kbd> ī
        * <kbd>o</kbd> ō
        * <kbd>u</kbd> ū
        * <kbd>y</kbd> ȳ
        * <kbd>g</kbd> ḡ
        * (and the same with the Capital letters)
        * <kbd>space</kbd> ¯ (stand-alone macron)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd>  ̄ (combining macron)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>q</kbd>  ᷌  (combining macron-breve)
    +  :sparkles: `en` add 🕱 dead sub-key `Macron+Grave` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>`</kbd> or <kbd>`</kbd> — (after `macron` dead key is pressed) after dead key is pressed, the following keys are mapped to:
        * <kbd>e</kbd> ḕ
        * <kbd>o</kbd> ṑ
        * (and the same with the Capital letters)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>`</kbd>  ᷆ (combining Macron-Grave)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd> ᷅ (combining Grave-Macron)
    +  :sparkles: `en` add 🕱 dead sub-key `Macron+Acute` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>;</kbd> or <kbd>;</kbd> — (after `macron` dead key is pressed) after dead key is pressed, the following keys are mapped to:
        * <kbd>e</kbd> ḗ
        * <kbd>o</kbd> ṓ
        * (and the same with the Capital letters)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>/</kbd> ᷄ (combining Macron-Acute)
        * <kbd>⌥</kbd><kbd>⇧</kbd><kbd>o</kbd> ᷇ (combining Acute-Macron)
    +  :sparkles: `ru` add 🕱 dead key `macron` and mapped it to <kbd>⌥</kbd><kbd>⇧</kbd><kbd>щ</kbd> — after dead key is pressed, the following keys are mapped to:
        * <kbd>й</kbd> ӣ
        * <kbd>у</kbd> ӯ
        * <kbd>и</kbd> ӣ
        * (and the same with the Capital letters)
        * <kbd>space</kbd> ¯ (stand-alone macron)
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
    + `ru` spaces of various widths, mapped to <kbd>space</kbd> with various modifiers
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
    + `ru` Modifiers with <kbd>^</kbd>: split into 5 additional modifier layers (#10 <kbd>^</kbd>, #11 <kbd>^</kbd><kbd>⇧</kbd>, #12 <kbd>^</kbd><kbd>⌥</kbd>, #13 <kbd>^</kbd><kbd>⌥</kbd><kbd>⇧</kbd>, #14 <kbd>^</kbd><kbd>⌥</kbd><kbd>⌘</kbd>) to allow more assignments, e.g., to <kbd>space</kbd>

[0.2.0]: https://github.com/eugenesvk/kbdLayout-Mac/releases/tag/0.2.0
## [0.2.0]
  - __Added__
    + :sparkles: `en` 🕱 dead key `space` and mapped it to <kbd>^</kbd><kbd>space</kbd> — after a dead key is pressed, spaces of various widths are mnemonically mapped to:
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
    + `en` spaces of various widths, mapped to <kbd>space</kbd> with various modifiers
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
    + `en` Modifiers with <kbd>^</kbd>: split into 5 additional modifier layers (#9 <kbd>^</kbd>, #10 <kbd>^</kbd><kbd>⇧</kbd>, #11 <kbd>^</kbd><kbd>⌥</kbd>, #12 <kbd>^</kbd><kbd>⌥</kbd><kbd>⇧</kbd>, #13 <kbd>^</kbd><kbd>⌥</kbd><kbd>⌘</kbd>) to allow more assignments, e.g., to <kbd>space</kbd>

[0.1.0]: https://github.com/eugenesvk/kbdLayout-Mac/releases/tag/0.1.0
## [0.1.0]
  - __Added__
    + :sparkles: original Ilya Birman Typography Layout
    + :sparkles: Math layout
  - __Changed__
    + English layout: many various updates to the original layout
    + Russian layout: many various updates to the original layout
