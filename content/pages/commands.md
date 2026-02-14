Title: Commands
Slug: commands
status: hidden

## Introduction

Mycli sends most input you enter to the MySQL server as a SQL statement. There
is also a set of commands that mycli itself will accept. To see these, type
`help` or `\?` at the prompt:

```text
mycli> help
+----------------+----------------------------+------------------------------------------------------------+
| Command        | Shortcut                   | Description                                                |
+----------------+----------------------------+------------------------------------------------------------+
| \G             | \G                         | Display current query results vertically.                  |
| \clip          | \clip                      | Copy query to the system clipboard.                        |
| \dt            | \dt[+] [table]             | List or describe tables.                                   |
| \e             | \e                         | Edit command with editor (uses $EDITOR).                   |
| \f             | \f [name [args..]]         | List or execute favorite queries.                          |
| \fd            | \fd [name]                 | Delete a favorite query.                                   |
| \fs            | \fs name query             | Save a favorite query.                                     |
| \l             | \l                         | List databases.                                            |
| \llm           | \ai                        | Interrogate an LLM.                                        |
| \once          | \o [-o] filename           | Append next result to an output file (overwrite using -o). |
| \pipe_once     | \| command                 | Send next result to a subprocess.                          |
| \timing        | \t                         | Toggle timing of commands.                                 |
| connect        | \r                         | Reconnect to the database. Optional database argument.     |
| delimiter      | <null>                     | Change SQL delimiter.                                      |
| exit           | \q                         | Exit.                                                      |
| help           | \?                         | Show this help.                                            |
| nopager        | \n                         | Disable pager, print to stdout.                            |
| notee          | notee                      | Stop writing results to an output file.                    |
| nowarnings     | \w                         | Disable automatic warnings display.                        |
| pager          | \P [command]               | Set PAGER. Print the query results via PAGER.              |
| prompt         | \R                         | Change prompt format.                                      |
| quit           | \q                         | Quit.                                                      |
| redirectformat | \Tr                        | Change the table format used to output redirected results. |
| rehash         | \#                         | Refresh auto-completions.                                  |
| source         | \. filename                | Execute commands from file.                                |
| status         | \s                         | Get status information from the server.                    |
| system         | system [command]           | Execute a system shell commmand.                           |
| tableformat    | \T                         | Change the table format used to output results.            |
| tee            | tee [-o] filename          | Append all results to an output file (overwrite using -o). |
| use            | \u                         | Change to a new database.                                  |
| warnings       | \W                         | Enable automatic warnings display.                         |
| watch          | watch [seconds] [-c] query | Executes the query every [seconds] seconds (by default 5). |
+----------------+----------------------------+------------------------------------------------------------+
```

Most commands have a long and short form. Most of the commands starting
with backslash are case sensitive. Commands may be followed by an optional
semicolon.

* <a name="g"></a> `\G`

    Send the current statement to the server and display the results vertically.
    This is used instead of a semicolon terminator, e.g. `select 1\G`.

* <a name="clip"></a> `<query>\clip`

    Send the current statement to the system clipboard.  This is used at the
    beginning or end of a statement, e.g. `select 1\clip`.

* <a name="dt"></a> `\dt`, `\dt[+] [table]`

    List the tables in the default database (when used without any parameters).
    Describe a table (when passed a parameter).

    The optional `+` verbose indicator can be used to toggle whether or not the `CREATE TABLE` statement for the table is shown.

    The `\dt` commands are equivalent to running `SHOW TABLES`, `SHOW COLUMNS FROM
    [table_name]`, and `SHOW CREATE TABLE [table_name]`.

* <a name="e"></a> `<query>\e`

    Edit the current statement with an editor (uses the environment variable `$EDITOR`).
    If this is entered without a current query, it will populate the editor
    with the previous query.  `\e` is equivalent to the keystroke sequence
    <kbd>Ctrl</kbd>-<kbd>x</kbd> <kbd>Ctrl</kbd>-<kbd>e</kbd>.

* <a name="f"></a> `\f`, `\f <name> [arg, arg, ..]`

    List or execute favorite queries. If the favorite query requires parameters,
    they can be passed to the query after the name, e.g., `\f users_by_name
    "Teddy Roosevelt"`. See [Favorite Queries]({filename}/pages/favorites.md) for more information.

* <a name="fd"></a> `\fd <name>`

    Delete a favorite query.

* <a name="fs"></a> `\fs <name> <query>`

    Save a favorite query. Favorite queries support shell-style parameter
    substitution. See [Favorite Queries]({filename}/pages/favorites.md) for more information.

* <a name="l"></a> `\l`

    List the databases on the MySQL server host. This is equivalent to running
    `SHOW DATABASES`.

* <a name="llm"></a> `\llm <question>`

    Interact with an LLM using natural language.  See [Using the \llm Command]({filename}/pages/llm.md).

* <a name="once"></a> `once <filename>`, `\o [-o] <filename>`

    Output the next query's results to an output file. Defaults to
    append mode. Use `-o` to overwrite any existing file content.
    Also consider using shell-style redirects `$> <filename>` or
    `$>> <filename>` after your SQL statement.

* <a name="pipe_once"></a> `pipe_once <command>`, `\| <command>`

    Output the next query's results to a shell command.  Also
    consider using the shell-style redirect `$| <command` after
    your SQL statement, as in `SELECT 1 $| wc;`.

* <a name="timing"></a> `timing`, `\t`

    Toggle whether or not the time it takes to execute a statement is displayed
    below the results.

* <a name="connect"></a> `connect [database]`, `\r [database]`

    Reconnect to the server. You can optionally supply a database name that
    will be set as the default database for your connection.

* <a name="delimiter"></a> `delimiter <string>`

    Set the SQL end-of-statement delimiter, which is `;` by default.  Some
    mycli functionality may depend on the delimiter being `;`.

* <a name="quit"></a> `quit`, `exit`, `\q`

    Exit mycli.

* <a name="help"></a> `help [name]`, `\? [name]`, `? [name]`

    Display a help message listing mycli's commands.  As a special case, if
    optional `name` is given, search for help for `name` on the _server_.

* <a name="nopager"></a> `nopager`, `\n`

    Disable the use of pager software for outputting query results. For more
    information see the [pager section]({filename}/pages/pager.md) of the
    web documentation.

* <a name="notee"></a> `notee`

    Disable output to the tee file. For more information, see the
    [`tee` command](#tee).

* <a name="nowarnings"></a> `nowarnings`, `\w`

    Disable automatic display of MySQL warnings from the server. For more
    information, see the [`warnings` command](#warnings).

* <a name="pager"></a> `pager [command]`, `\P [command]`

    Enable the use of a pager for outputting query results, by default `less`.
    Optionally, specify a different command that will be used as the pager. For
    more information see the [pager section]({filename}/pages/pager.md) of the
    web documentation.  The default pager may be set in your `~/.myclirc` file.

* <a name="prompt"></a> `prompt`, `\R [format]`

    Change the prompt format. The default is `\t \u@\h:\d> `. See the
    [prompt]({filename}/pages/prompt.md) documentation for more information.

* <a name="redirectformat"></a> `redirecformat [format]`, `\Tr [format]`

    Change the output format for shell-style redirections.  Run the command
    without specifying a format to see the possible values.  The default is
    `csv`.

* <a name="rehash"></a> `rehash`, `\#`

    Refresh the cached auto-completion data. (This is the list of databases,
    tables, columns that auto-complete when you are typing.)

* <a name="source"></a> `source <filename>`, `\. <filename>`

    Execute the SQL commands from the named file.

* <a name="status"></a> `status`, `\s`

    Display status information about the client machine, server, and
    connection you are using.

* <a name="system"></a> `system <command>`

    Execute a shell command and outputs the results.

* <a name="tableformat"></a> `tableformat [format]`, `\T [format]`

    Change the interactive tabular output format. Run the command without
    specifying a format to see the possible values.

* <a name="tee"></a> `tee [-o] <filename>`

    Log all queries/commands and their output to `filename`. Defaults to
    append mode. Use `-o` to overwrite any existing file content. To disable
    this, see the [`notee` command](#notee).

* <a name="use"></a> `use <db_name>`, `\u <db_name>`

    Use `db_name` as the default database.

* <a name="warnings"></a> `warnings`, `\W`

    Enable automatic display of MySQL warnings from the server.  This is the
    equivalent of running `SHOW WARNINGS` after every statement.

* <a name="watch"></a> `watch [seconds] [-c] query`

    Repeatedly execute a query every `n` seconds. The default interval is `5`
    seconds. `-c` can be used to clear the screen after every iteration.
