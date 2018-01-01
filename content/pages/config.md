Title: Configuration
Slug: config
status: hidden

## Introduction

Most of mycli's user settings are configured via the file located at
`~/.myclirc`, which is a hidden file in your home folder in Linux and macOS.
On Windows it is located at `C:\Users\<username>\.myclirc`.

The config file is created when mycli is launched for the very first time.
Updates to that file are not overwritten by subsequent launches of mycli or
updating the version of mycli.

Mycli also reads the `[client]` section of MySQL's option file, `~/.my.cnf`
(on Windows: `C:\Users\<username>\.my.cnf`). See the example file at the bottom of this
page for more information.

**NOTE:** Mycli does not read the `[mysql]` section of MySQL's option files. It
only reads the `[client]` section.

Mycli supports two methods of storing server credentials. See the
[server configuration documentation]({filename}/pages/loginpath.md)
for more information.


## Sample Mycli Config File

```
[main]

# Enables context sensitive auto-completion. If this is disabled then all
# possible completions will be listed.
smart_completion = True

# Multi-line mode allows breaking up the sql statements into multiple lines. If
# this is set to True, then the end of the statements must have a semi-colon.
# If this is set to False then sql statements can't be split into multiple
# lines. End of line (return) is considered as the end of the statement.
multi_line = False

# Destructive warning mode will alert you before executing a sql statement
# that may cause harm to the database such as "drop table", "drop database"
# or "shutdown".
destructive_warning = True

# log_file location.
log_file = ~/.mycli.log

# Default log level. Possible values: "CRITICAL", "ERROR", "WARNING", "INFO"
# and "DEBUG".
log_level = INFO

# Log every query and its results to a file. Enable this by uncommenting the
# line below.
# audit_log = ~/.mycli-audit.log

# Timing of sql statments and table rendering.
timing = True

# Table format. Possible values: ascii, double, github,
# psql, plain, simple, grid, fancy_grid, pipe, orgtbl, rst, mediawiki, html,
# latex, latex_booktabs, textile, moinmoin, jira, vertical, tsv, csv.
# Recommended: ascii
table_format = ascii

# Syntax Style. Possible values: manni, igor, xcode, vim, autumn, vs, rrt,
# native, perldoc, borland, tango, emacs, friendly, monokai, paraiso-dark,
# colorful, murphy, bw, pastie, paraiso-light, trac, default, fruity
syntax_style = default

# Keybindings: Possible values: emacs, vi.
# Emacs mode: Ctrl-A is home, Ctrl-E is end. All emacs keybindings are available in the REPL.
# When Vi mode is enabled you can use modal editing features offered by Vi in the REPL.
key_bindings = emacs

# Enabling this option will show the suggestions in a wider menu. Thus more items are suggested.
wider_completion_menu = False

# MySQL prompt
# \t - Product type (Percona, MySQL, Mariadb)
# \u - Username
# \h - Hostname of the server
# \d - Database name
# \n - Newline
prompt = '\t \u@\h:\d> '

# Skip intro info on startup and outro info on exit
less_chatty = False

# Use alias from --login-path instead of host name in prompt
login_path_as_host = False

# Cause result sets to be displayed vertically if they are too wide for the current window,
# and using normal tabular format otherwise. (This applies to statements terminated by ; or \G.)
auto_vertical_output = False

# Custom colors for the completion menu, toolbar, etc.
[colors]
# Completion menus.
Token.Menu.Completions.Completion.Current = 'bg:#00aaaa #000000'
Token.Menu.Completions.Completion = 'bg:#008888 #ffffff'
Token.Menu.Completions.MultiColumnMeta = 'bg:#aaffff #000000'
Token.Menu.Completions.ProgressButton = 'bg:#003333'
Token.Menu.Completions.ProgressBar = 'bg:#00aaaa'

# Selected text.
Token.SelectedText = '#ffffff bg:#6666aa'

# Search matches. (reverse-i-search)
Token.SearchMatch = '#ffffff bg:#4444aa'
Token.SearchMatch.Current = '#ffffff bg:#44aa44'

# The bottom toolbar.
Token.Toolbar = 'bg:#222222 #aaaaaa'
Token.Toolbar.Off = 'bg:#222222 #888888'
Token.Toolbar.On = 'bg:#222222 #ffffff'

# Search/arg/system toolbars.
Token.Toolbar.Search = 'noinherit bold'
Token.Toolbar.Search.Text = 'nobold'
Token.Toolbar.System = 'noinherit bold'
Token.Toolbar.Arg = 'noinherit bold'
Token.Toolbar.Arg.Text = 'nobold'

# Favorite queries.
[favorite_queries]

# Use the -d option to reference a DSN.
[alias_dsn]
# example_dsn = mysql://[user[:password]@][host][:port][/dbname]
```

## Sample MySQL Option File

```
[client]
# The client section is read by mycli and all MySQL applications.

# Default connection information
user = thor
password = hammer
host = localhost
database = asgard
port = 3306

# Connect via a socket.
# socket = '/tmp/mysql.sock'

# Use the UTF-8 character set
default-character-set = utf-8

# SSL options - see the MySQL documentation for more information.
# https://dev.mysql.com/doc/refman/5.7/en/secure-connection-options.html#option_general_ssl-ca
# ssl-ca
# ssl-cert
# ssl-key
# ssl-cipher
# ssl-verify-server-cert

# Turn on the LOAD DATA INFILE statement
local-infile = on

# Another local infile alias.
# Use it if the previous one clashes with other MySQL tools.
loose-local-infile = on

# Configure the pager
pager = 'vim -'

# Disable the pager
# skip-pager = on
```
