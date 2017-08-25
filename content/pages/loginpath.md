Title: Storing server configuration
Slug: loginpath
status: hidden


When working with multiple servers, it is advisable to use the
[`mysql_config_editor`](https://dev.mysql.com/doc/refman/5.7/en/mysql-config-editor.html)
tool that ships with MySQL to store the authentication credentials in an encrypted file called
`.mylogin.cnf`. Then, `mycli` can read and use those credentials.

First, run the `mysql_config_editor` tool and enter the credentials:

```
$ mysql_config_editor set --login-path=my_server_alias --host=my.host.address --user=myusername --password
Enter password: *****
```

Then, provide the `--login-path` option when running `mycli`:

```
$ mycli --login-path my_server_alias my_database_name
```
