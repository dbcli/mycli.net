Title: Editor
Slug: editor
status: hidden

# Introduction

One of the most useful mycli commands is `/edit` or `\edit`. This can be used
to launch an editor to edit the current query (or previous query, if the
current line is otherwise blank).

When used at the end-of-line, we must use the alternate backslash form `\edit`
to avoid ambiguity with valid SQL.

</br>
# Examples

```text
# /edit alone will launch the default editor (read from the $EDITOR or $VISUAL
# environment variables).  It will put the _previous_ query in the editor,
# and the query will be populated back into the prompt once the edit session
# is exited.
mysql> /edit
```

</br>

```text
# \edit at end-of-line will open the editor with the query-so-far in the editor.
mysql> SELECT * FROM \edit
```

</br>

```text
# /edit followed by an argument refers to a file.  This will open an existing
# file in the editor.
> /edit <filename>
```

</br>
# Setup

Mycli reads the choice of editor from the `$VISUAL` or `$EDITOR` environment
variable, which the user must set, usually in `~/.bash_profile`.

Example:  if VS Code is installed, and its CLI tool `code` is on your `$PATH`,
then this will allow editing mycli queries in VS Code with `/edit`:

```bash
export VISUAL='code --wait'
```
