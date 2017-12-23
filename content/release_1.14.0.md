Title: Release v1.14.0
Date: 2017-12-22
Category: Blog
Author: Thomas Roten
Tags: python, release, changelog, mysql
Slug: v1.14.0

`mycli` is a command line interface for MySQL that includes
auto-completion and syntax highlighting. [Read the install instructions]({filename}/pages/1.install.md) to find out how to get the latest version.

Mycli 1.14.0 was released on December 22, 2017 and includes these changes:

## Features

* Add a [`watch` command]({filename}/pages/commands.md#watch) to repeat a query every `N` seconds (defaults to 5)
  (Thanks: [David Caro]).
* Default to unix socket connection if host and port are unspecified. This
  simplifies authentication on some systems and matches mysql behaviour. See
  the [config documentation]({filename}/pages/config.md) for more information on
  specifying connection information.
* Add [positional parameters]({filename}/pages/favorites.md) to favorite queries (Thanks: [Scrappy Soft]).

## Bug Fixes

* Fix source command for script in current working directory. (Thanks: [Dick Marinus]).
* Fix issue where the `tee` command did not work on Python 2.7 (Thanks: [Thomas Roten]).

## Internal changes

* Drop support for Python 3.3 (Thanks: [Thomas Roten]).
* Merge `_on_completions_refreshed` and `_swap_completer_objects` functions (Thanks: [Dick Marinus]).

[Thomas Roten]: https://github.com/tsroten
[Scrappy Soft]: https://github.com/scrappysoft
[Dick Marinus]: https://github.com/meeuw
[David Caro]: https://github.com/Terseus
