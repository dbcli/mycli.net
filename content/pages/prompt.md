Title: Prompt
Slug: prompt
status: hidden

Mycli provides a configurable prompt. When mycli starts up,
it will use the prompt configuration found in its
[config file]({filename}/pages/config.md). Once mycli is running,
you can interactively change the prompt by using the
[`/prompt` command]({filename}/pages/commands.md#prompt).

The prompt is generated using the following format sequences:

 * `\D` - full current date, _e.g._ `Sat Feb 14 15:55:48 2026`
 * `\R` - current hour in 24-hour time (00–23)
 * `\r` - current hour in 12-hour time (01–12)
 * `\m` - minutes of the current time
 * `\s` - seconds of the current time
 * `\P` - AM/PM
 * `\d` - selected database/schema
 * `\h` - hostname of the server
 * `\H` - shortened hostname of the server
 * `\p` - connection port
 * `\j` - connection socket basename
 * `\J` - full connection socket path
 * `\k` - connection socket basename OR the port
 * `\K` - full connection socket path OR the port
 * `\T` - connection SSL/TLS version
 * `\t` - database vendor (Percona, MySQL, MariaDB, TiDB, Doris)
 * `\u` - username
 * `\w` - number of warnings, or "(none)" (requires frequent trips to the server)
 * `\W` - number of warnings, or the empty string (requires frequent trips to the server)
 * `\y` - uptime in seconds (requires frequent trips to the server)
 * `\Y` - uptime in words (requires frequent trips to the server)
 * `\A` - DSN alias if any
 * `\n` - a newline
 * `\_` - a space
 * `\\` - a literal backslash
 * `\x1b[...m` - an ANSI escape sequence (can style with color or attributes)
   ANSI color example: `prompt = '\x1b[31mroot\x1b[0m@localhost:\d> '`
 * `\<html>` - a leading sequence indicating that the rest of the prompt be styled like HTML.
   See https://python-prompt-toolkit.readthedocs.io/en/stable/pages/printing_text.html#html .
   Characters such as "&" or literal "<" and ">" must be HTML-escaped in this mode.
   HTML styles cannot be combined with ANSI sequences.  HTML mode takes precedence.
   HTML color example: `prompt = '\<html><red><u>root</u></red>@localhost:\d&gt; '`.

The default prompt looks something like this in use: `mysql user@localhost:db_name> `.

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

`prompt_continuation` can also be set to the empty string: `''` for no
indentation.
