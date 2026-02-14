Title: Logging
Slug: logging
status: hidden

There are two types of logging.

1. Operational logs are on by default and stored in the home folder as `~/.mycli.log`. This is useful for debugging or developing mycli. But not very useful for end users.  This feature can be configured using `log_file` and `log_level` in `~/.myclirc`.

2. Audit logs can be optionally turned on using the command line option `-l`. This will log every command and its output with a timestamp. This is useful for keeping track of all that happened in the CLI during a session.  This can be configured using `audit_log` in `~/.myclirc`.
