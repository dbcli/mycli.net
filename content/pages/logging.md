Title: Logging
Slug: logging
status: hidden

There are two types of logging for the REPL:

1. Operational logs are on by default and stored in the home folder as `~/.mycli.log`. This is useful for debugging or developing mycli. But not very useful for end users.  This feature can be configured using `log_file` and `log_level` in `~/.myclirc`.

2. Audit logs can be optionally turned on using the command line option `-l`/`--logfile`. This will log every command and its output with a timestamp. This is useful for keeping track of all that happened in the CLI during a session.  This can be configured using `audit_log` in `~/.myclirc`.

In `--batch` mode,

1. `-l`/`--logfile` is also respected, and

2. `--checkpoint` can be used to log only successful query statements (not output).  A checkpoint file can be used to resume an interrupted script.
