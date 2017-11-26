Title: Favorite Queries
Slug: favorites
status: hidden

Favorite Queries are a way to save frequently used queries
with a short name.

`\f` - list all favorite queries.

`\f <name>` - Invoke a favorite query by its name.

`\fs <name> <query>` - Save a new favorite query called 'name'.

`\fd <name>` - Delete an existing favorite query by its name.

Examples:

```
    # Save a new favorite query.
    > \fs simple select * from abc where a is not Null;

    # List all favorite queries.
    > \f
    +--------+---------------------------------------+
    | Name   | Query                                 |
    |--------+---------------------------------------|
    | simple | SELECT * FROM abc where a is not NULL |
    +--------+---------------------------------------+

    # Run a favorite query.
    > \f simple
    +--------+--------+
    | a      | b      |
    |--------+--------|
    | 日本語 | 日本語   |
    +--------+--------+

    # Delete a favorite query.
    > \fd simple
    simple: Deleted
```

## Positional Parameters

Favorite queries support shell-style parameter substitution. Save your favorite
query with parameters as placeholders (e.g. `$1`, `$2`,
`$3`, etc.):

```
\fs user_by_name select * from users where name = '$1'
```

When you call a favorite query with parameters, just add the parameters after
the query's name. You can put quotes around arguments that include spaces.

```
\f user_by_name "Skelly McDermott"
```
