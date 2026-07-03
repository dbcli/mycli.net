Title: Environment Variables
Slug: environment
status: hidden

</br>
# Variables Affecting Mycli

</br>
## $FZF_DEFAULT_OPTS

`$FZF_DEFAULT_OPTS` does not directly affect mycli sessions, but if set, can
affect the external program [fzf] which is executed for fuzzy history search.
See `man fzf` for more.

</br>
## $MYCLI_HISTFILE

`$MYCLI_HISTFILE` sets the location of the history file, which is `~/.mycli-history`
by default.  See also the `history_file` setting in [`~/.myclirc`]({filename}/pages/config.md).

</br>
## $MYCLI_LLM_OFF

`$MYCLI_LLM_OFF` suppresses loading of LLM libraries, making the `/llm`
feature unavailable.  If you don't use the `/llm` feature, setting this
variable may improve startup time.

</br>
## $MYSQL_DSN

`$MYSQL_DSN` sets a DSN to use for [connecting to a server]({filename}/pages/connect.md).

</br>
## $MYSQL_HOST

`$MYSQL_HIST` sets a hostname to use for [connecting to a server]({filename}/pages/connect.md).

</br>
## $MYSQL_PWD

`$MYSQL_PWD` sets a password to use for [connecting to a server]({filename}/pages/connect.md).

</br>
## $MYSQL_TCP_PORT

`$MYSQL_TCP_PORT` sets a TCP port to use for [connecting to a server]({filename}/pages/connect.md).

</br>
## $MYSQL_UNIX_SOCKET

`$MYSQL_UNIX_SOCKET` sets a Unix Domain Socket to use for [connecting to a server]({filename}/pages/connect.md).

</br>
## $MYSQL_USER

`$MYSQL_USER` sets a username to use for [connecting to a server]({filename}/pages/connect.md).

</br>
## $PAGER

`$PAGER` controls the pager for mycli output in the case that `pager` is not set in
[`~/.myclirc`]({filename}/pages/config.md).

</br>
## $LESS

`$LESS` does not directly affect mycli sessions, but if set, can affect the behavior
of the`less` executable, commonly used as the mycli output [pager]({filename}/pages/pager.md).
See `man less` for more.

</br>
## $VISUAL/$EDITOR

`$VISUAL` and `$EDITOR` do not directly affect mycli sessions, but are used by the
[prompt-toolkit] dependency to invoke the editor triggered by the mycli `/edit`
command or the <kbd>control</kbd>-<kbd>x</kbd>, <kbd>control</kbd>-<kbd>e</kbd> key sequence.

`$VISUAL` is preferred.

See the [editor docs]({filename}/pages/editor.md) for more.

</br>
## $XDG_CONFIG_HOME

For users of the XDG Base Directory Specification, mycli will search `$XDG_CONFIG_HOME`
for its configuration file before checking the `$HOME` directory.

[fzf]: https://github.com/junegunn/fzf
[prompt-toolkit]: https://github.com/jonathanslenders/python-prompt-toolkit
