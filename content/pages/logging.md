Title: Logging
Slug: logging
status: hidden

There are two types of logging. 

1. Operational logs are on by default and stored in the home folder as ~/.mycli.log. This is useful for debugging mycli. It is useful if you're developing mycli, but not so useful for end users.

2. Audit logs can be optionally turned on using a command line option `-l`. This will log every command and it's output with a timestamp. This is useful for record-keeping or audit-logs.
