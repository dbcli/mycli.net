Title: Pager
Slug: pager
status: hidden

Mycli outputs query results in a pager (_e.g._ `less` or `more`). This
allows you to easily view large result sets one page at a time.

## Configuring the Pager

When starting up, mycli checks the `pager` config option in `~/.myclirc`.
If it's set, then mycli uses its value as the pager. If it's blank, then mycli
will use the `$PAGER` environment variable.

Once mycli is started, you can use the `/pager` command at the REPL to change
which pager mycli uses. Or, `/nopager` to disable the pager.

```
> /pager less
PAGER set to less.
> /nopager
Pager disabled.
```

## Disable Paging

You can disable the pager by adding `enable_pager = False` to your `~/.myclirc`
file. See [Configuration](/config) for more information.

## Pager Behavior

On macOS and Linux, the pager will default to `less` for most users. `less`
sometimes has less-than-desirable behavior such as clearing the screen, cutting
off lines, _etc_.

You can configure `less` through environment variables in your shell, or by
setting the full desired command using the `pager` option in `~/.myclirc`.

Here are some common `less` options:

- `-X` leaves file contents on the screen when `less` exits.
- `-F` makes `less` quit if the entire output can be displayed on one screen.
- `-R` displays ANSI color escape sequences in "raw" form.
- `-S` disables line wrapping. Side-scroll to see long lines.

See `man less` for more information.

Configuration examples:

```ini
# This is a popular option in ~/.myclirc:
pager = 'less -XFR'

# Or, some mycli users like to disable line wrapping.
pager = 'less -SRXF'

# Here is a fancy example which may require a more recent version of "less".
pager = 'less -iRSMwF --rscroll=*d→$ --match-shift=10 --use-color -DBky$DCky$DEky$DM--$DN--$DPky$DRWk$DSky$'
```
