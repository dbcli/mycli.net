Title: Connecting to a database
Slug: connect
status: hidden

Mycli requires you to have a MySQL compatible server to connect with, reachable
using TCP/IP or a UNIX Domain Socket (local computer only).  You'll also need
the right credentials (a username, and optionally a password).

Please note the hostname is part of the credentials for MySQL!

The following default values are used to connect:

* `user` — your current local username
* `password` — none (depends on settings)
* `hostname` — `localhost`
* `socket` — `/var/run/mysqld/mysqld.sock`
* `port` — 3306

These can be overruled by your configuration files and command-line
arguments (command-line arguments take precedence over configuration files).

The database name can be changed at runtime using the REPL (`use` or `connect`
commands).

It's also possible to supply some of these arguments using environment variables:

* `$MYSQL_HOST` — hostname
* `$MYSQL_TCP_PORT` — port
* `$MYSQL_UNIX_PORT` — UNIX domain socket
* `$MYSQL_PWD` — password (please note this might not be secure on some multi user systems!)

The following configuration files can be used to configure your connection:

* [`~/.myclirc`]({filename}/pages/config.md) — mycli configuration file (see `[connection]` and `[alias_dsn]` sections).
* **DEPRECATED**: `/etc/my.cnf` and `~/.my.cnf` — MySQL compatible configuration files

</br>

## Primary Connection Command-line Arguments

### `database`

The database name or DSN can be given alone as a positional argument.

DSNs are usually in the form `mysql://user:password@hostname:port/databasename`;
see [DSNs](#DSNs) below for more detail.

### `-h TEXT`, `--host TEXT`

Hostname of the server, as a name or IP address.  Not needed when using a socket
to connect.

### `-P INTEGER`, `--port INTEGER`

Port number to use on the host.  Not needed when using a socket to connect.

### `-u TEXT`, `--user TEXT`

User name to connect to the server.

### `-S PATH`, `--socket PATH`

A Unix Domain Socket file to use for the connection, instead of a host/port
combination.

### `-p TEXT`, `--pass TEXT`, `--password TEXT`

Password to connect to the sever.  If given in the last position on the command
line without an argument, this means "prompt for the password" (which may be
the default anyway).

### `-D TEXT`, `--database TEXT`

Optional database name to use when connected, or a DSN to use specifying all
of the connection parameters.

### `-d TEXT`, `--dsn TEXT`

Use a DSN by alias, as configured in the `[alias_dsn]` section of [`~/.myclirc`]({filename}/pages/config.md).

See the alias choices by running `mycli --list-dsn`.

## SSL Command-line Arguments

(See especially the `[connection]` section in [`~/.myclirc`]({filename}/pages/config.md) for SSL defaults.)

### ` --ssl-mode <auto|on|off>`

Set desired SSL behavior. `auto` is preferred.  `on` means "forced to be on for this connection";
`off` means "forced to be off for this connection".

### ` --ssl-ca PATH`

CA file in PEM format.

### ` --ssl-capath PATH`

CA directory.

### ` --ssl-cert PATH`

X509 certificate in PEM format.

### ` --ssl-key PATH`

X509 key in PEM format.

### ` --ssl-cipher TEXT`

SSL cipher to use.

### ` --tls-version TEXT`

One of `tlsv1`, `tlsv1.1`, `tlsv1.2`, or `tlsv1.3`

### ` --ssl-verify-server-cert`

Verify server's "Common Name" in its certificate.  Default is off.

## Other Command-line Arguments Affecting Connections

### `--charset`

The character set to negotiate for the connection, defaulting to `utf8mb4`.

### `--local-infile BOOLEAN`

Enable/disable `LOAD DATA LOCAL INFILE`.

### `--defaults-file PATH`

**DEPRECATED**: Only read MySQL options from the given pathname, ignoring `/etc/my.cnf` and `~/.my.cnf`.

### `--myclirc PATH`

Only read mycli options from the given pathname, ignoring [`~/.myclirc`]({filename}/pages/config.md).

<a name="DSNs"></a>
## DSNs

DSNs are usually in the form `mysql://user:password@hostname:port/databasename`, but many
parts are optional.  For example, if the password part is omitted, you will be prompted
for the password.

In addition, other values may be passed in the form of URL-style parameters,
especially SSL settings.  For example:

```bash
$ mycli 'mysql://user:password@hostname:port/databasename?ssl_key=%2Fpath%2Fto%2Ffile'
```

```bash
$ mycli 'mysql://user:password@hostname:port/databasename?tls_version=tlsv1'
```

Note that because of the question mark character `?`, most shells will require
quotation marks around the DSN if URL-style parameters are included.

The following URL-style parameters are recognized:

 * `ssl` — corresponds to CLI option `--ssl`
 * `ssl_ca` — corresponds to CLI option `--ssl-ca`
 * `ssl_capath` — corresponds to CLI option `--ssl-capath`
 * `ssl_cert` — corresponds to CLI option `--ssl-cert`
 * `ssl_key` — corresponds to CLI option `--ssl-key`
 * `ssl_cipher` — corresponds to CLI option `--ssl-cipher`
 * `tls_version` — corresponds to CLI option `--tls-version`
 * `ssl_verify_server_cert` — corresponds to CLI option `--ssl-verify-server-cert`

</br>

## Connection Examples

Connect using a database name:

```bash
$ mycli my_database
```

Connect using a username, hostname and database name:

```bash
$ mycli -u my_user -h my_host.com my_database
```

Connect using a DSN:

```bash
$ mycli mysql://my_user@my_host.com:3306/my_database
```

Connect using a DSN alias:

```bash
$ mycli --dsn server1
```
