Title: Configuration
Slug: config
status: hidden

The configuration file is located at `~/.myclirc` which is a hidden file in
your home folder in Linux and OS X. On Windows it is located at `C:\Users\<username>\.myclirc`.

The config file is created when mycli is launched for the very first time.
Updates to that file are not overwritten by subsequent launches of mycli or
updating the version of mycli.

Sample config file:

```
[main]

# Enables context sensitive auto-completion. If this is disabled the all
# possible completions will be listed.
smart_completion = True

# Multi-line mode allows breaking up the sql statements into multiple lines. If
# this is set to True, then the end of the statements must have a semi-colon.
# If this is set to False then sql statements can't be split into multiple
# lines. End of line (return) is considered as the end of the statement.
multi_line = False

# log_file location.
log_file = ~/.mycli.log

# Default log level. Possible values: "CRITICAL", "ERROR", "WARNING", "INFO"
# and "DEBUG".
log_level = INFO

# Timing of sql statements and table rendering.
timing = True

# Table format. Possible values: psql, plain, simple, grid, fancy_grid, pipe,
# orgtbl, rst, mediawiki, html, latex, latex_booktabs.
# Recommended: psql, fancy_grid and grid.
table_format = psql

# Syntax Style. Possible values: manni, igor, xcode, vim, autumn, vs, rrt,
# native, perldoc, borland, tango, emacs, friendly, monokai, paraiso-dark,
# colorful, murphy, bw, pastie, paraiso-light, trac, default, fruity
syntax_style = default

# Keybindings: Possible values: emacs, vi
key_bindings = emacs

# MySQL prompt
# \t - Product type (Percona, MySQL, Mariadb)
# \u - Username
# \h - Hostname of the server
# \d - Database name
prompt = '\t \u@\h:\d> '
```

All the options are thoroughly documented. 
