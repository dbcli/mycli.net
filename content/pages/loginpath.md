Title: Storing Server Configuration
Slug: loginpath
status: hidden


When working with multiple servers, it is convenient to store your host and login
configuration so you don't have to type it in every time you connect to a
database server. Mycli supports two ways of storing server and authentication credentials.

1. The [`mysql_config_editor`](https://dev.mysql.com/doc/refman/5.7/en/mysql-config-editor.html)
  tool that ships with MySQL. It stores the authentication credentials in an
  encrypted login path file named `.mylogin.cnf`. Mycli can read and use those
  credentials. This method is recommended by MySQL.
2. Mycli's [config file]({filename}/pages/config.md) via DSN aliases.

## MySQL's `mysql_config_editor` <a name="mysql_config_editor"></a>

MySQL's login path file is a convenient way to store your authentication
credentials in an encrypted file. The login path file encryption prevents
plaintext credentials from being displayed on the screen or in an editor,
however if an attacker has access to the file, they can easily decrypt
it.

To set up a login path, first, run the
[`mysql_config_editor`](https://dev.mysql.com/doc/refman/5.7/en/mysql-config-editor.html)
tool and enter the credentials. Storing a password is optional. If there is no
password stored for a login path and mycli cannot connect, it will ask for one.

```
$ mysql_config_editor set --login-path=my_server_alias --host=my.host.address --user=myusername --password
Enter password: *****
```

Then, provide the `--login-path` option when running `mycli`:

```
$ mycli --login-path my_server_alias my_database_name
```

## Mycli's Config File <a name="dsn"></a>

You can store server connections as easy-to-remember aliases in mycli's
[configuration file]({filename}/pages/config.md). These connection settings,
also known as DSNs (Data Source Names), can contain the following information:

- Alias
- Host Name
- Port
- Database Name
- Username
- Password

If a password is not supplied and mycli cannot connect to the server, it will
prompt you to enter one. This is helpful so you do not have to store your
password in a plaintext configuration file.

Here is an example DSN configuration:

```
[alias_dsn]
test = mysql://my_user:password@localhost:3306/test_db
```

When starting up mycli, you can use a DSN by providing the `-d` flag:

```
$ mycli -d test
```

You should set the permissions of your configuration file so that only your
user can read and write to it. In macOS and Linux, you can do this via `chmod`:

```
$ chmod 700 ~/.myclirc
```
