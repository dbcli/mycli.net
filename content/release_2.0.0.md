Title: Release v2.0.0
Date: 2026-07-03
Category: Blog
Author: Roland Walker
Tags: python, release, changelog, mysql
Slug: v2.0.0

`mycli` is a command line interface for MySQL which includes
auto-completion and syntax highlighting.

[Read the install instructions]({filename}/pages/1.install.md) to find out how to get the latest version.

Mycli v2.0.0 has [breaking changes](https://github.com/dbcli/mycli/blob/v2.0.0/changelog.md#breaking-changes)!

Major features added in recent months include

 * powerful fuzzy history search with [fzf](https://github.com/junegunn/fzf) (thanks [lazmond3]!)
 * integrated LLMs with the `/llm` command
 * shell-like query-result redirection with trailing `$|` and `$>` operators
 * system keyring support for saving passwords
 * improved batch execution with checkpoint/resume and progress/eta indicator
 * _many_ completion improvements, such as leveraging foreign keys (thanks [scottnemes]!)
 * fuzzy completion/correction with [RapidFuzz](https://github.com/rapidfuzz/RapidFuzz)
 * SSL modernization (thanks [scottnemes]!)

[lazmond3]: https://github.com/lazmond3
[scottnemes]: https://github.com/scottnemes
