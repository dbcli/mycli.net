Title: Pager
Slug: pager
status: hidden

Mycli outputs query results in a pager (e.g. `less`, `more`). This
allows you to easily view large result sets one page at a time.

## Configuring the Pager

When starting up, mycli checks the `pager` config option in MySQL's option
files. If it's set, then mycli uses its value as the pager. If it's blank,
then mycli will use the `PAGER` environment variable's value.

Once mycli is started, you can use the `pager` command to change which pager
mycli uses. Or, `nopager` will disable the pager.

```
> pager less
PAGER set to less.
> nopager
Pager disabled.
```

## Disable Paging

You can disable the pager by adding `enable_pager = False` to your mycli config
file. See [Configuration](/config) for more information.

## Pager Behavior

On macOS and Linux, the pager will default to `less` for most users. `less`
sometimes has less-than-desirable behavior like clearing the screen, cutting
lines off, etc. You can configure `less` through environment variables in your
shell configuration files. Here are some common `less` options and
configuration examples:

- `-X` leaves file contents on the screen when less exits.
- `-F` makes `less` quit if the entire output can be displayed on one
  screen.
- `-R` displays ANSI color escape sequences in "raw" form.
- `-S` disables line wrapping. Side-scroll to see long lines.

```
# This is a popular option among mycli users.
export LESS="-XFR"

# Some mycli users like to disable line wrapping.
export LESS="-SRXF"
```
