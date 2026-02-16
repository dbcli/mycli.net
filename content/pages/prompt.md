Title: Prompt
Slug: prompt
status: hidden

Mycli provides a configurable prompt. When mycli starts up,
it will use the prompt configuration found in its
[config file]({filename}/pages/config.md). Once mycli is running,
you can interactively change the prompt by using the
[`prompt` command]({filename}/pages/commands.md#prompt).

The prompt is generated using the following format sequences:

 * `\D` - full current date, _e.g._ `Sat Feb 14 15:55:48 2026`
 * `\R` - current hour in 24-hour time (00–23)
 * `\r` - current hour in 12-hour time (01–12)
 * `\m` - minutes of the current time
 * `\s` - seconds of the current time
 * `\P` - AM/PM
 * `\d` - selected database/schema
 * `\h` - hostname of the server
 * `\p` - connection port
 * `\j` - connection socket basename
 * `\J` - full connection socket path
 * `\k` - connection socket basename OR the port
 * `\K` - full connection socket path OR the port
 * `\t` - database vendor (Percona, MySQL, MariaDB, TiDB)
 * `\u` - username
 * `\A` - DSN alias if any
 * `\n` - a newline
 * `\_` - a space
 * `\x1b[...m` - an ANSI escape sequence (can style with color)

The default prompt looks something like this: `mysql user@localhost:db_name> `.

The default format string is `\t \u@\h:\d> `.

## Additional Configuration

Mycli's configuration file has an additional prompt-related option
called `prompt_continuation`. This defaults to `-> `. This means that
when a query spans more than one line, subsequent lines start with
`-> `:

```
mysql user@localhost:db > SELECT first_name, last_name, date_of_birth
                       -> FROM users
                       -> WHERE
```

`prompt_continuation` can also be set to the empty string: `''`.
