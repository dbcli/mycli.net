Title: Favorite Queries
Slug: favorites
status: hidden

Favorite Queries are a way to save frequently used queries with a short name.

Commands:

 * `/f` - List all favorite queries.
 * `/f <name>` - Invoke a favorite query by its name.
 * `/fs <name> <query>` - Save a new favorite query called `<name>`.
 * `/fd <name>` - Delete an existing favorite query by its name.

Examples:

```text
# Save a new favorite query.
> /fs simple SELECT * FROM abc WHERE a IS NOT NULL;

# When multi-line mode is on, pressing Return twice is needed to save.
# This supports multi-statement favorites.

# List all favorite queries.
> /f
+-----------+--------------------------------------------------+
| Name      | Query                                            |
|-----------+--------------------------------------------------|
| simple    | SELECT * FROM abc WHERE a IS NOT NULL            |
| find_user | SELECT * FROM users WHERE name = '{{ kv.name }}' |
+-----------+--------------------------------------------------+

# Run a favorite query.
> /f simple
+--------+--------+
| a      | b      |
|--------+--------|
| 日本語 | 日本語   |
+--------+--------+

# Run a favorite query containing {{ kv.name }} in the template.
> /f find_user --name=henry
> /f find_user --name henry

# Run a favorite query containing positional parameter $1 in the
# template.
> /f find_user henry

# Use -- to disambiguate positional parameters such as $1, especially
# if the positional value starts with a dash.
> /f query --key=value -- positional-value
> /f query -- --positional-value-which-looks-like-a-flag--

# Delete a favorite query.
> /fd simple
simple: Deleted
```

</br>
## Positional Parameters

Favorite queries support shell-style positional parameter substitution. Save
your favorite query with positional parameters as placeholders (_e.g._ `$1`,
`$2`,`$3`, _etc._):

```sql
/fs user_by_name SELECT * FROM users WHERE name = '$1'
```

When you call a favorite query with positional parameters, just add the values
after the query's name. You can put quotes around arguments which include
spaces.

```sql
/f user_by_name "Skelly McDermott"
```

</br>
## Key/Value Parameters

Favorite queries also support key-value parameters using [Jinja](https://jinja.palletsprojects.com/en/stable/)
templates.  Save a favorite query using Jinja syntax, with the values to be
passed in `kv.`:

```sql
/fs user_by_name SELECT * FROM users WHERE name = '{{ kv.name }}'
```

Then call the query using the syntax `--key=value` to pass the values:

```sql
/f user_by_name --name=Frank
```

Unlike positional parameters, key/value parameters may be made optional, using
Jinja conditionals.

Key/value parameters will also be offered as completions.

</br>
## Shared Favorites

Favorite queries are usually saved directly to the user's `~/.myclirc`, but
the configuration value `shared_favorites_file` can also be set to a path
containing additional favorites.  This file can be shared across multiple
users.
