Title: Multi-line Mode
Slug: multi-line
status: hidden

The default behavior of `mycli` is to execute a query as soon as the Enter key
is pressed. This might come as a surprise to seasoned MySQL users who always
enter a semicolon to denote the end of the query.

To emulate the vendor client behavior you can enable multi-line mode, which
will require a semicolon to be present at the end of the statement. This enables
writing multi-line queries.

You can toggle multi-line mode by pressing the `<F3>` key or set it persistently
via the `multi_line` option in [`~/.myclirc`]({filename}/pages/config.md).
