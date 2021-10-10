# Changelog
All notable changes to this project will be documented in this file

[unreleased]: https://github.com/eugenesvk/kbdLayout-Mac/compare/0.2.0...HEAD
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
