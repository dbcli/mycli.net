Title: Development
Slug: develop
status: hidden

This is a guide for developers who would like to contribute to this project.

First of all I'm flattered that you're interested in contributing. Second, my
heart felt thanks for contributing.

## GitHub Workflow

The source code is hosted by Github: <https://github.com/dbcli/mycli>

If you already know how to fork a project and send pull requests to it using
github, you can safely skip this section.

Github help has a pretty detailed documentation on how to use Github to fork
and send pull requests to a repository.
<https://help.github.com/articles/fork-a-repo/>

The basic steps are:

1. Fork the mycli project via the github UI.

1. Clone your fork to your local machine.

```
    git clone git@github.com:<your-username>/mycli.git
```

1. Setup a remote called upstream that points to the original mycli repo. This
   is to keep your fork in sync with the mainline.

```
    git remote add upstream git@github.com:dbcli/mycli.git
```

1. Make the necessary changes in your local machine. Commit and push to your
   fork.

```
       $ git commit

       $ git push origin
```

1. Create a pull request from your fork to the mainline repo using Github UI.

1. Sync with the main mycli repo.


```
       $ git pull upstream master   # Pull from the main repo to local copy.

       $ git push origin master     # Pushes from local copy to your fork.
```

## Local Development Setup

It is highly recommended to use virtualenv for development. If you don't know
what a virtualenv is, this [guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtual-environments)
will help you get started.

Create a virtualenv (let's call it mycli-dev). Once the virtualenv is activated
`cd` into the local clone of mycli folder and install mycli using pip as
follows:

```
    $ pip install --editable .
```

This will install the necessary dependencies as well as install mycli from the
working folder into the virtualenv. By installing it using `pip install -e`
we've linked the mycli installation with the working copy. So any changes made
to the code is immediately available in the installed version of mycli. This
makes it easy to change something in the code, launch mycli and check the
effects of your change.

## Tests

The tests are located in the `tests` directory in the mycli project root.

Tests are written using `py.test` testing framework. Install `py.test` by
using `pip install pytest` in the virtualenv. Then execute the tests by
calling `py.test` from the root of the project folder.

A test runner called `tox` is used to run the tests in Python 2.7 and 3.3+.
You can do `pip install tox` and call `tox` from the
project root to run the tests in all supported python versions.

If you'd like to run just one of the test files (say test_sqlcompletion.py)
then `cd` into the tests folder and execute `py.test test_sqlcompletion.py`
to run just the tests from that file or `tox test_sqlcompletion.py` to run
the tests in that file in all three Python versions.

The tests are also run via [Travis CI](https://travis-ci.org/dbcli/mycli) when
a new Pull Request is opened. If you have a change and it happens to be failing
on one of the Python versions, don't worry about it. Just open a pull request
and I can help you get it fixed before merging.

