#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Sascha Gehlich
# Copyright (c) 2015 Sascha Gehlich
#
# License: MIT
#

"""This module exports the 9eSassLint plugin class."""

from SublimeLinter.lint import Linter, util


class NineElementsSassLint(Linter):

    """Provides an interface to 9e-sass-lint."""

    syntax = 'sass'
    cmd = '9e-sass-lint --stdin'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.0.1'
    regex = r'^.+?:(?P<line>\d+):(?P<col>\d+):(?P<message>.+)'

