<p align="center">
English and Russian keyboard layouts for macOS
<br>
with easier access to various typographical, mathematical, and Greek symbols
</p>

<p align="center">  
(Math and Greek are embedded, Math is also available as a separate layout) 
</p>

## Introduction

- Unlocked <kbd>^</kbd>[^4] to enable default macOS layers 
- Extensive diacritics
- Math layer embedded ...
- Greek layer embedded behind a <kbd>🕱</kbd>, mapped to  `Greek` macOS layers (base, <kbd>⇧</kbd>, <kbd>⌥</kbd>, <kbd>⇧</kbd><kbd>⌥</kbd>), <kbd>🕱</kbd>`Greek` (mapped to <kbd>^</kbd><kbd>g</kbd>), and (in <kbd>🕱</kbd>`Greek`):
        * <kbd>🕱</kbd>`greek-tonos` (mapped to <kbd>;</kbd>)
        * <kbd>🕱</kbd>`diaeresis-greek` (mapped to <kbd>⇧</kbd><kbd>;</kbd>)
        * <kbd>🕱</kbd>`greek-dialytika-tonos` (mapped to <kbd>⇧</kbd><kbd>w</kbd> / <kbd>⌥</kbd><kbd>;</kbd>)
[^4]: <kbd>⇧</kbd> is <kbd>Shift</kbd>, <kbd>^</kbd> is <kbd>Control</kbd>, <kbd>⌥</kbd> is <kbd>Alt</kbd>, <kbd>🕱</kbd> is dead key


## Installation

- Copy `TypES Layout.bundle` to `~/Library/Keyboard Layouts`
- Open `System Preferences` → `Keyboard` → `Input Sources` → `+` to add:
    + `English — TypES`
    + `Russian — TypES`
    + `English — Math` (though it is also embedded in the English/Russian layouts)
- (_optionally_) Delete the [default layout](https://apple.stackexchange.com/questions/44921/how-to-remove-or-disable-a-default-keyboard-layout#60521). For macOS `10.9` and later:
    + Change the current input source to your custom keyboard layout added above
    + Backup then open `~/Library/Preferences/com.apple.HIToolbox.plist` (you can convert the plist to XML with `plutil -convert xml1`)
    + Remove the input source you want to disable from the `AppleEnabledInputSources` dictionary
    + Remove the `AppleDefaultAsciiInputSource` key if it exists
    + Restart

## Usage


To allow entering all the extra symbols these keyboard layouts rely heavily on <kbd>🕱</kbd>s (or dead keys), which are keys that don't print anything by themselves, but instead enter into a new keyboard layer with extra symbols. For example[^3] <kbd>⌥</kbd><kbd>c</kbd> is a <kbd>🕱</kbd> dead key `Copyright`, pressing it enables to enter the following 3 symbols, each with just a single key:

  1. `©` with <kbd>c</kbd>
  2. `®` with <kbd>r</kbd>
  3. `™` with <kbd>t</kbd>

[^3]: Most examples are using the English layout, though most of the keybinds are identical in the Russian layout as well (<kbd>⌥</kbd><kbd>o</kbd>≡<kbd>⌥</kbd><kbd>щ</kbd>)

How to find how to insert a symbol?

- Open the [SymbolsAll-En](./helper/SymbolsAll-En.md) or [SymbolsAll-Ru](./helper/SymbolsAll-Ru.md) files for the English/Russian layouts, find a symbol and look at its row/column re. which modifier+key combo produces it
- (certain, but tedious alternative): find a symbol in the keyboard layout file (e.g. `English — TypES.keylayout`) and note the `key code` and `keyMap index` tha produce it, lookup the values in Ukelele


### Details on various keybinds

### Additional tips

#### Insert English <kbd>⇧</kbd><kbd>1</kbd>–<kbd>0</kbd> symbols in the Russian layout

Russian layout has somehwat different <kbd>⇧</kbd><kbd>1</kbd>–<kbd>0</kbd> symbols:<br>
<kbd>2</kbd><kbd>3</kbd><kbd>4</kbd><kbd>6</kbd><kbd>7</kbd><br>
`"`⁠`№`⁠`;`⁠`:`⁠`?` `Russian — TypES`<br>
`@`⁠`#`⁠`$`⁠`^`⁠`&` `English — TypES`<br>
which in the system layout is resolved by mapping <kbd>⌥</kbd><kbd>1</kbd>–<kbd>0</kbd> to the symbols from the English layout. However, these `TypES` layouts have identical <kbd>⌥</kbd> layers, so there are two alternatives to enter the English symbols with the number keys:

  1. Use <kbd>^</kbd><kbd>⌥</kbd> that copies the <kbd>⌥</kbd> layer of the `Russian - PC` layout  
  2. Use `Karabiner-Elements` to remap <kbd>right⇧</kbd> to insert English characters in the Russian layout (unfortunately, `Ukelele` can't differentiate between left and right keys):
    + copy this [config file](./helper/ru-RShift=en-LShift.json) to `~/.config/karabiner/assets/complex_modifications`
    + in `Karabiner-Elements`→`Complex modifications`→`Add rule` add the rule named `"  Ru RShift+1–4,6–7 to En: r⇧1–4,6–7 ⟶ ⌃⌥1–4,6–7 (in 'Russian — TypES' mapped to en⇧)"` under the group `es-8) ruR⇧≈enL⇧`


## Known issues

## Credits
  - [Ilya Birman Typography Layout](https://ilyabirman.ru/projects/typography-layout/faq/), 3.7
  - [English Math](https://tex.stackexchange.com/questions/110042/entering-unicode-math-symbols-into-latex-direct-from-keyboard-on-a-mac/110043#110043) layout
  - [Ukelele](https://github.com/sillsdev/Ukelele) keyboard layout editing app
