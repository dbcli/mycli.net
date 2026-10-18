Title: Commands
Slug: commands
status: hidden

## Introduction

Mycli sends most input you enter directly to the MySQL server as a SQL
statement. There is also a set of commands that mycli itself will accept
locally.  To see these commands, type `/help` or `/?` at the prompt:

```text
mycli> /help
┌─────────────────┬────────┬──────────────────────────────┬──────────────────────────────────────────────────┐
│ Command         │ Alias  │ Usage                        │ Description                                      │
├─────────────────┼────────┼──────────────────────────────┼──────────────────────────────────────────────────┤
│ /bug            │ <null> │ /bug                         │ File bug on GitHub.                              │
│ /clip           │ <null> │ /clip | <query>\clip         │ Copy query to system clipboard.                  │
│ /config         │ <null> │ /config <command> [key]      │ Inspect config file settings (/config help).     │
│ /connect        │ /r     │ /connect [database]          │ Reconnect to server, optionally switching dbs.   │
│ /delimiter      │ <null> │ /delimiter <string>          │ Set end-of-statement delimiter.                  │
│ /dsn            │ <null> │ /dsn <command>               │ Manage saved DSNs (/dsn help).                   │
│ /dt             │ <null> │ /dt[+] [table]               │ List or describe tables.                         │
│ /edit           │ /e     │ /edit <file> | <query>\edit  │ Edit query with editor (via $VISUAL/$EDITOR).    │
│ /exit           │ /q     │ /exit                        │ Exit.                                            │
│ /f              │ <null> │ /f [name [args] [--key=val]] │ Run favorite query shortcut.                     │
│ /favorite       │ <null> │ /favorite <command>          │ Manage favorite queries (/favorite help).        │
│ /fd             │ <null> │ /fd <name>                   │ Delete favorite query shortcut.                  │
│ /fs             │ <null> │ /fs <name> <query>           │ Save favorite query shortcut.                    │
│ \g              │ <null> │ <query>\g                    │ Display results (mnemonic: go).                  │
│ \G              │ <null> │ <query>\G                    │ Display results vertically.                      │
│ /help           │ /?     │ /help [term]                 │ Show this table, or search for help on term.     │
│ /l              │ <null> │ /l                           │ List databases.                                  │
│ /llm            │ /ai    │ /llm [arguments]             │ Interrogate LLM (/llm help).                     │
│ /nopager        │ /n     │ /nopager                     │ Disable pager; print to stdout.                  │
│ /notee          │ <null> │ /notee                       │ Stop writing all results to tee file.            │
│ /nowarnings     │ /w     │ /nowarnings                  │ Disable automatic warnings display.              │
│ /once           │ /o     │ /once [-o] <file>            │ Append next result to a file (-o to overwrite).  │
│ /pager          │ /P     │ /pager [command]             │ Set pager to [command]; print results via pager. │
│ /ping           │ <null> │ /ping                        │ Check connection.                                │
│ /pipe_once      │ /|     │ /pipe_once <command>         │ Send next result to subprocess.                  │
│ /prompt         │ /R     │ /prompt [string]             │ Set or show prompt format.                       │
│ /quit           │ /q     │ /quit                        │ Quit.                                            │
│ /redirectformat │ /Tr    │ /redirectformat <format>     │ Set table format used for redirected results.    │
│ /rehash         │ /#     │ /rehash                      │ Refresh completions.                             │
│ /source         │ /.     │ /source [options] <file>     │ Execute queries from file.                       │
│ /status         │ /s     │ /status                      │ Get status information from server.              │
│ /system         │ <null> │ /system [-r] <command>       │ Execute shell command (-r for raw mode).         │
│ /tableformat    │ /T     │ /tableformat <format>        │ Set table format used for interactive results.   │
│ /tee            │ <null> │ /tee [-o] <file>             │ Append all results to file (-o to overwrite).    │
│ /timing         │ /t     │ /timing                      │ Toggle query timing.                             │
│ /use            │ /u     │ /use <database>              │ Change to a new database.                        │
│ /warnings       │ /W     │ /warnings                    │ Enable automatic warnings display.               │
│ /watch          │ <null> │ /watch [sec] [-c] <query>    │ Execute query every [sec] seconds (default 5).   │
│ \x              │ <null> │ <query>\x                    │ Display results in an interactive explorer.      │
└─────────────────┴────────┴──────────────────────────────┴──────────────────────────────────────────────────┘
Use \backslash forms when at end-of-line.
Docs index — https://mycli.net/docs
```

Most commands have a long and short form. Many of the commands starting with
backslash are case sensitive.  Most command lines may be followed by an optional
semicolon.

* <a name="bug"></a> `/bug`

    Open a browser window to GitHub Issues to report a bug with mycli.

* <a name="clip"></a> `<query>\clip`

    Send the current statement to the system clipboard.  This is used at the
    beginning or end of a statement, _e.g._ `SELECT 1\clip`.  At the end of
    a statement, the backslash form `\clip` must be used to avoid a SQL
    ambiguity.

* <a name="config"></a> `/config search pager`

    Inspect configuration settings.  See `/config help`.  It is not yet possible
    to save settings via this interface.

* <a name="connect"></a> `/connect [database]`, `/r [database]`

    Reconnect to the server.  You can optionally supply a database name which
    will be set as the default database for your connection.

* <a name="delimiter"></a> `/delimiter <string>`

    Set the SQL end-of-statement delimiter, which is `;` by default.  Some
    mycli functionality may depend on the delimiter being `;`.

* <a name="dsn"></a> `/dsn show`, `/dsn save <alias>`

    Manage saved DSNs, including saving the current connection under an alias.
    See `/dsn help`.

* <a name="dt"></a> `/dt`, `/dt[+] [table]`

    List the tables in the default database (when used without any parameters).
    Describe a table (when a parameter is passed).

    The optional `+` verbose indicator can be used to toggle whether or not the `CREATE TABLE` statement for the table is shown.

    The `/dt` commands are equivalent to running `SHOW TABLES`, `SHOW COLUMNS FROM
    [table_name]`, and `SHOW CREATE TABLE [table_name]`.

* <a name="e"></a> `/edit <filename>`, `<query>\edit`

    Edit the current statement with an editor (uses the environment variables `$EDITOR`
    or `$VISUAL`), or open a file.  If this is entered with an empty line, it will
    populate the editor with the previous query.  At the end of a statement, the backslash
    form `\edit` must be used to avoid a SQL ambiguity.  `/edit` is generally equivalent to
    the keystroke sequence <kbd>control</kbd>-<kbd>x</kbd> <kbd>control</kbd>-<kbd>e</kbd>.

* <a name="f"></a> `/f`, `/f <name> [arg, arg, ..]`

    List or execute named favorite queries.  If the favorite query requires parameters,
    they can be passed to the query after the name, _e.g._, `/f users_by_name
    "Teddy Roosevelt"`. See [Favorite Queries]({filename}/pages/favorites.md) for more information.

* <a name="favorite"></a> `/favorite run <query>`

    Alternative interface for favorite queries, with additional functionality such as
    `/favorite eval`.  See `/favorite help`.

* <a name="fd"></a> `/fd <name>`

    Delete a favorite query.

* <a name="fs"></a> `/fs <name> <query>`

    Save a favorite query.  Favorite queries support shell-style parameter
    substitution. See [Favorite Queries]({filename}/pages/favorites.md) for more information.

* <a name="g"></a> `\g`

    Send the current statement to the server and display the results in the
    default format.  This is used instead of a semicolon terminator, _e.g._
    `SELECT 1\g`.

* <a name="G"></a> `\G`

    Send the current statement to the server and display the results vertically.
    This is used instead of a semicolon terminator, _e.g._ `SELECT 1\G`.

* <a name="help"></a> `/help [name]`, `/? [name]`

    Display a help message listing mycli's commands.  If optional `name` is
    given and it is a mycli `/command`, display help on command.  If `name`
    is not a mycli `/command` earch for help for `name` on the _server_.

* <a name="l"></a> `/l`

    List the databases on the MySQL server host. This is equivalent to running
    `SHOW DATABASES`.

* <a name="llm"></a> `/llm <question>`

    Interact with an LLM using natural language.  See [Using the /llm Command]({filename}/pages/llm.md).

* <a name="nopager"></a> `/nopager`, `/n`

    Disable the use of an external pager for outputting query results. For more
    information see the [pager section]({filename}/pages/pager.md) of the
    web documentation.

* <a name="notee"></a> `/notee`

    Disable output to a tee file. For more information, see the
    [`/tee` command](#tee).

* <a name="nowarnings"></a> `/nowarnings`, `/w`

    Disable automatic display of MySQL warnings from the server. For more
    information, see the [`/warnings` command](#warnings).

* <a name="once"></a> `/once <filename>`, `/o [-o] <filename>`

    Output the next query's results to an output file. Defaults to
    append mode. Use `-o` to overwrite any existing file content.
    Also consider using shell-style redirects `$> <filename>` or
    `$>> <filename>` after your SQL statement.

* <a name="pager"></a> `/pager [command]`, `/P [command]`

    Enable the use of a pager for outputting query results, by default `less`.
    Optionally, specify a different command that will be used as the pager. For
    more information see the [pager section]({filename}/pages/pager.md) of the
    web documentation.  The default pager may be set in your `~/.myclirc` file.

* <a name="ping"></a> `/ping`

    Check whether the connection to the server is live, without running a
    query.

* <a name="pipe_once"></a> `/pipe_once <command>`, `/| <command>`

    Output the next query's results to a shell command.  Also
    consider using the shell-style redirect `$| <command` after
    your SQL statement, as in `SELECT 1 $| wc;`.

* <a name="prompt"></a> `/prompt`, `/R [format]`

    Change the prompt format. The default is `\t \u@\h:\d> `. See the
    [prompt]({filename}/pages/prompt.md) documentation for more information.

* <a name="quit"></a> `/quit`, `/exit`, `/q`

    Exit mycli.

* <a name="redirectformat"></a> `/redirecformat [format]`, `/Tr [format]`

    Change the output format for shell-style redirections.  Run the command
    without specifying a format to see the possible values.  The default is
    `csv`.

* <a name="rehash"></a> `/rehash`, `/#`

    Refresh the cached auto-completion data. (This is the list of databases,
    tables, columns that auto-complete when you are typing.)

* <a name="source"></a> `/source <filename>`, `/. <filename>`

    Execute the SQL commands from `<filename>`.

* <a name="status"></a> `/status`, `/s`

    Display status information about the client machine, server, and
    connection you are using.

* <a name="system"></a> `/system [-r] <command>`

    Execute a shell command and output the results.  `-r` requests raw mode,
    in which output is passed through without formatting.

    A few commands are special-cased.

    If the command is in the form `/system cd <directory>`, change the working
    directory for mycli.

    If the command is `/system clear`, do not show timings after the command.

    The following commands are assumed to be in raw mode: `vim`, `vi`, `bash`,
    and `zsh`.

* <a name="tableformat"></a> `/tableformat [format]`, `/T [format]`

    Change the interactive tabular output format.  Run the command without
    specifying a format to see the possible values.

* <a name="tee"></a> `/tee [-o] <filename>`

    Log all queries/commands and their output to `filename`. Defaults to
    append mode. Use `-o` to overwrite any existing file content. To disable,
    see the [`/notee` command](#notee).

* <a name="timing"></a> `/timing`, `/t`

    Toggle whether or not the time it takes to execute a statement is displayed
    below the results.

* <a name="use"></a> `/use <db_name>`, `/u <db_name>`

    Use `db_name` as the default database.

* <a name="warnings"></a> `/warnings`, `/W`

    Enable automatic display of MySQL warnings from the server.  This is the
    equivalent of running `SHOW WARNINGS` after every statement.

* <a name="watch"></a> `/watch [seconds] [-c] query`

    Repeatedly execute a query every `n` seconds. The default interval is 5
    seconds. `-c` can be used to clear the screen after each iteration.

* <a name="x"></a> `\x`

    Send the current statement to the server and display the results in an
    interactive explorer rather than the default pager.  This is used instead of
    a semicolon terminator, _e.g._
    `SELECT * FROM employees\x`.
