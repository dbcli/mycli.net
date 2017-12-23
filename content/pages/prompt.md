Title: Prompt
Slug: prompt
status: hidden

Mycli provides a configurable prompt. When mycli starts up,
it will use the prompt configuration found in its
[config file]({filename}/pages/config.md). Once mycli is running
up, you can interactively change the prompt by using the
[`prompt` command]({filename}/pages/commands.md#prompt).

The default prompt looks something like this: `mysql user@localhost:db_name> `.
It is formatted using the following character sequences.
The default format string is `\t \u@\h:\d> `.

* `\D` - the full current date, e.g. `Fri Dec 20 20:51:56 2015`
* `\d` - database name
* `\h` - hostname of the server
* `\m` - minutes of the current time
* `\n` - a newline
* `\P` - AM/PM
* `\p` - the connetion port
* `\R` - the current time, in 24-hour time (0–23)
* `\r` - the current time, standard 12-hour time (1–12)
* `\s` - seconds of the current time
* `\t` - database type (e.g. Percona, MySQL, MariaDB)
* `\u` - username

## Additional Configuration

Mycli's configuration file has an additional prompt-related option
called `prompt_continuation`. This default to `-> `. This means that
when a query spans more than one line, subsequent lines start with
`->`:

```
mysql user@localhost:db > SELECT first_name, last_name, date_of_birth
                       -> FROM users
                       -> WHERE
```
