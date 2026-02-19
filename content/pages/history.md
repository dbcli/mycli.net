Title: History and Search
Slug: history
status: hidden

Mycli keeps track of the queries entered in the REPL.  The history is
persistent across sessions, and has no limit.

The <kbd>Up</kbd>/<kbd>Down</kbd> arrow keys can be used to navigate the
recent history.

</br>

## Incremental Search

Pressing <kbd>control</kbd>-<kbd>r</kbd> will enable incremental history
search across your entire query history.  If you press
<kbd>control</kbd>-<kbd>r</kbd> and then start typing your search term, you
will see all past queries narrowed down by that search term.  You can cycle
through the matches by pressing <kbd>control</kbd>-<kbd>r</kbd> again.

## fzf

If [fzf](https://github.com/junegunn/fzf) is installed on your system, the
<kbd>control</kbd>-<kbd>r</kbd> incremental search will leverage fzf to
provide fuzzy search throughout your entire query history.

The interface provided by the fzf search is completely different than
"vanilla" incremental search, but it is powerful, and recommended.  For
example, fzf will allow you to use _multiple_ space-separated search terms to
narrow the search, with the terms given in any order, operating as a logical
`AND`.  Many more advanced searches are possible, such as the use of negated
terms by preceding the term with `!` (documented at the
[fzf project](https://github.com/junegunn/fzf); see also the manual at `man fzf`
and `fzf --help`).

When in the fzf interface, repeating <kbd>control</kbd>-<kbd>r</kbd> still
cycles through past matches, and the arrow keys can also be used
to navigate the matches.  Press <kbd>Enter</kbd> to accept a match, and
<kbd>Escape</kbd> or <kbd>control</kbd>-<kbd>g</kbd> to exit the search.

Mycli sets up a full-screen interface for fzf searches, in which

* the top half of the screen shows a fragment of all matching candidates from the history, with highlighted search terms
* the middle line shows the interactive search prompt and search terms
* the bottom half of the screen shows a fuller preview of the current candidate which would be accepted with <kbd>Enter</kbd>

Example:

<img src="images/history/fzf_screen_split.png" width=750 align="center">

The fzf search is truly "fuzzy" and tolerates spelling errors.

### Key Bindings

If you have fzf installed but do not wish to use the fancy fzf interface for
history search, set the following in [`~/.myclirc`]({filename}/pages/config.md):

```ini
[keys]
# possible values: auto, fzf, reverse_isearch
control_r = reverse_isearch
```
