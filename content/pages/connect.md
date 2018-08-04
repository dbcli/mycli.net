Title: Connect to database
Slug: connect
status: hidden

MyCli requires you to have a MySQL compatible server on your local computer
or on a remote server reachable using TCP/IP (a SSH tunnel is commonly used
for this purpose) or a UNIX domain socket (local computer only).
You'll also need the right credentials (username and optionally a password).

Please note the hostname is part of the credentials for MySQL!

The following default values are used to connect:

* `user` - your current username
* `password` - none (empty)
* `hostname` - localhost
* `socket` - /var/run/mysqld/mysqld.sock
* `port` - 3306

These can be overruled by your configuration files and command line
arguments (command line arguments take preference over configuration files.

The database name can be changed at runtime using the interactive command line
interface (`use` or `connect` command).

It's also possible to supply some of these arguments using environment variables:
* `MYSQL_HOST` - hostname
* `MYSQL_TCP_PORT` - port
* `MYSQL_UNIX_PORT` - UNIX domain socket
* `MYSQL_PWD` - password (please note this might not be secure on some multi user systems!)

The following configuration files can be used to configure your connection:

* /etc/my.cnf / ~/.my.cnf - MySQL compatible configuration file
* ~/.myclirc - MyCli configuration file (see `[alias_dsn]` section.

## Command line arguments

* `database` - database name or DSN (mysql://user:password@hostname:port/databasename)
* `-h`, `--host TEXT` - Host address of the database.
* `-P`, `--port INTEGER` - Port number to use for connection.
* `-u`, `--user TEXT` - User name to connect to the database.
* `-S`, `--socket TEXT` - The socket file to use for connection.
* `-p`, `--password TEXT` - Password to connect to the database.
* `--pass` `TEXT` - Password to connect to the database (please note this will be visible for other users!).
* `-D`, `--database TEXT` - Database to use.
* `-d`, `--dsn TEXT` - Use DSN configured into the `[alias_dsn]` section of myclirc file.
* `--defaults-file PATH` Only read MySQL options from the given file.
* `--myclirc PATH` Location of myclirc file.

## Examples

Connect using a database name:
`$ mycli my_database`

Connect using a username, hostname and database name:
`$ mycli -u my_user -h my_host.com my_database`

Connect using a DSN:
`$ mycli mysql://my_user@my_host.com:3306/my_database`

Connect using a SSH tunnel:
```
$ ssh remote -L 3306:localhost:3306 -f sleep 60
$ mycli
```
Connect using a DSN alias:
`$ mycli --dsn server1`
