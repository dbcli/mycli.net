Title: Keybindings
Slug: keybindings
status: hidden

There are two editing modes available: Emacs mode and Vi mode. The modes can
be changed via `key_bindings` property in the config file (`~/.myclirc`) or
toggled via the F4 key.

Emacs mode is the default. In Emacs mode you can type <kbd>Ctrl</kbd>-<kbd>a</kbd> to go to the
beginning of a line and <kbd>Ctrl</kbd>-<kbd>e</kbd> to go to the end of a line and many more,
similar to the defaults of the `readline` library.

When Vi mode is enabled you can use modal editing features offered by Vim in
the REPL.

Mycli also adds some [custom keybindings](https://github.com/dbcli/mycli/blob/main/mycli/key_bindings.py)
which are summarized here along with completion navigation:

 * <kbd>f2</kbd> — toggle smart completions
 * <kbd>f3</kbd> — toggle multi-line mode
 * <kbd>f4</kbd> — toggle Vi/Emacs editing mode
 * <kbd>control</kbd>-<kbd>space</kbd> — summon completions
 * <kbd>tab</kbd> — summon completions + advance in completions
 * <kbd>enter</kbd> — choose a completion candidate
 * <kbd>escape</kbd> — cancel completions popup
 * <kbd>control</kbd>-<kbd>g</kbd> — cancel completions popup
 * <kbd>control</kbd>-<kbd>r</kbd> — search history with [fzf](https://github.com/junegunn/fzf) if available
 * <kbd>alt</kbd>-<kbd>enter</kbd> — add a line break in multi-line mode (or <kbd>escape</kbd>-<kbd>enter</kbd>)
 * arrows — completion navigation

In Emacs mode only (with comma showing a sequence of multiple keystrokes):

 * <kbd>control</kbd>-<kbd>x</kbd>, <kbd>p</kbd> — prettify a multi-line query
 * <kbd>control</kbd>-<kbd>x</kbd>, <kbd>u</kbd> — unprettify a query
 * <kbd>control</kbd>-<kbd>o</kbd>, <kbd>d</kbd> — insert the current date
 * <kbd>control</kbd>-<kbd>o</kbd>, <kbd>t</kbd> — insert the current datetime
 * <kbd>control</kbd>-<kbd>o</kbd>, <kbd>control</kbd>-<kbd>d</kbd> — insert the quoted current date
 * <kbd>control</kbd>-<kbd>o</kbd>, <kbd>control</kbd>-<kbd>>t</kbd> — insert the quoted current datetime
 * <kbd>alt</kbd>-<kbd>r</kbd> — search history with [fzf](https://github.com/junegunn/fzf) even if `~/.myclirc` is configured not to use it
