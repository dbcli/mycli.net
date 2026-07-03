Title: Editor
Slug: editor
status: hidden

One of the most useful slash commands is `/edit` or `\edit`. This can be used
to launch an editor to edit the current query (or previous query, if the
current line is otherwise blank).

When used at the end-of-line, we must use the backslash form `\edit` to
avoid ambiguity with valid SQL.

Here are some examples:

```ini
# /edit alone will launch the default editor (read from the $EDITOR or $VISUAL
# environment variables).  It will put the _previous_ query in the editor,
# and the query will be populated back into the prompt once the edit session
# is exited.
> /edit

# \edit at end-of-line will open the default editor with the query-so-far
# in the editor.
> SELECT * FROM \edit

# /edit followed by an argument refers to a file.  This will open an existing
# file in the editor.
> /edit <filename>
```
