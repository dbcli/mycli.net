Title: Storing Connection Configuration
Slug: credentials
status: hidden


When working with multiple servers, it is convenient to store your connection
configuration so you don't have to type it in every time you connect.  Mycli
supports three ways of storing server information and credentials:

1. Mycli's [config file]({filename}/pages/config.md) via DSN aliases.  These
   contents are in unprotected cleartext.
2. The system keyring.  These contents are encrypted.
3. The [`mysql_config_editor`](https://dev.mysql.com/doc/refman/8.4/en/mysql-config-editor.html)
   tool that ships with MySQL. It stores the authentication credentials in an
   obfuscated login-path file named `.mylogin.cnf`.  The contents are _obfuscated_,
   but not encrypted in a secure way.

The most secure and convenient way is to combine methods 1 and 2.  But users of
the vendor `mysql` client may be more familiar with method 3.

## Mycli's Config File <a name="dsn"></a>

You can store connection configurations as easy-to-remember aliases in mycli's
[configuration file]({filename}/pages/config.md).  These connection settings,
also known as [DSNs]({filename}/pages/connect.md#DSNs) (Data Source Names), can
contain the following information:

 - Hostname
 - Port
 - Database Name
 - Username
 - Password
 - SSL configuration parameters
 - Other per-connection settings such as the character set

If a password is not supplied in a given DSN, you will be prompted to enter a
password interactively. This is helpful, since you can avoid storing sensitive
data in a plaintext configuration file.

Here is an example DSN configuration in `~/.myclirc`:

```ini
[alias_dsn]
nickname = mysql://my_user@localhost:3306/test_db
```

When invoking mycli, you can use an aliased DSN by providing the `-d` flag,
or by just referring to the alias without any flag:

```bash
$ mycli nickname
```

A good practice is to set the permissions of your configuration file so that
only your user can read and write to it.  In macOS and Linux, you can do this
via `chmod`:

```bash
$ chmod 700 ~/.myclirc
```

However, the file is still stored in cleartext, so sensitive passwords are
best not stored in DSNs literally.

## The System Keyring <a name="keyring"></a>

If the following option is set in `~/.myclirc`:

```ini
use_keyring = True
```

then mycli will use your system keyring to store and retrieve passwords
transparently.

This works hand-in-hand with DSN aliases which specify everything but the password
in the DSN:

```ini
[alias_dsn]
nickname = mysql://my_user@localhost:3306/test_db
```

On the first connection to the `nickname` alias:

```bash
$ mycli nickname
```

you will be prompted for the password, and it will be stored in the keyring.

On subsequent connections, the password will be retrieved from the keyring.

To reset the saved password, use `--use-keyring=reset` on the command line:

```bash
$ mycli --use-keyring=reset nickname
```

</br>

## MySQL's `mysql_config_editor` <a name="mysql_config_editor"></a>

MySQL's login path file is a way to store connection parameters in a single
file. The login path file's obfuscation prevents plaintext credentials from
being displayed or read accidentally.  However, any attacker can decrypt the
contents given access to the file.

To set up a login path file, run the
[`mysql_config_editor`](https://dev.mysql.com/doc/refman/8.4/en/mysql-config-editor.html)
tool and set the connection parameters. Storing a password is optional.

```bash
$ mysql_config_editor set --login-path=my_server_alias --host=my.host.address --user=myusername --password
Enter password: *****
```

Then, provide the `--login-path` option when running `mycli`:

```bash
$ mycli --login-path my_server_alias my_database_name
```

If there is no password stored for a given login path, mycli will prompt for
one interactively.
