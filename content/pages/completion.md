Title: Auto-Completion
Slug: completion
status: hidden

# AutoCompletion

Auto-completion is on by default. The REPL will pop up a suggestion menu as
soon as you start typing. The suggestions are context-sensitive based on the
position of the cursor. _Eg_ only tables are suggested after the `FROM` keyword;
only column names are suggested after the `WHERE` clause.

## Smart Completion

We call this context-sensitive completion _smart completion_. Here are a few examples of smart completion.

### Tables

Only table names from the current database are suggested after the `FROM` keyword.

<img src="images/docs/table.png" width=750 align="center">

### Columns

Column names from the current table are suggested after the `WHERE` clause.

<img src="images/docs/column.png" width=750 align="center">

### Inserts

`INSERT` statement will suggest the column names.

<img src="images/docs/insert.png" width=750 align="center">

### Aliases

Aliases in the query are resolved and the columns from the table aliases are suggested.

<img src="images/docs/alias.png" width=750 align="center">

## Fuzzy Matching

The completions are matched using a [built-in fuzzy algorithm](http://blog.amjith.com/fuzzyfinder-in-10-lines-of-python) and [rapidfuzz](https://github.com/rapidfuzz/RapidFuzz).

For example typing 'djmi' will match the table 'django_migrations' because 'djmi' has parts of matching substrings. Here's an example:

<img src="images/docs/fuzzy.png" width=750 align="center">
