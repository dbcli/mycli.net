Title: Editor
Slug: editor
status: hidden

One of the powerful slash commands is `\e`. This will launch an editor to edit the current query. 

Here are some examples: 

```

# This will launch the default editor (read from $EDITOR env variable).
> \e 

# This will open the default editor with the current query in the buffer.
> SELECT * FROM \e

# This will open an existing file in the editor and the contents of the file will be populated into the repl once the file is saved.
> \e <filename>

```
