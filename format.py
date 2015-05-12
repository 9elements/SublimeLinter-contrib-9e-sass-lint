#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Sascha Gehlich
# Copyright (c) 2015 Sascha Gehlich
#
# License: MIT
#

"""This module exports the SassFormatCommand class."""

import sublime
import sublime_plugin
from SublimeLinter.lint import util


class SassFormatCommand(sublime_plugin.TextCommand):

    """Provides an interface to standard-format."""

    def run(self, edit):
        """Command to run when sass_format is executed."""
        v = self.view
        regions = []
        sel = v.sel()

        for region in sel:
            if not region.empty():
                regions.append(region)

        if len(regions) < 1:
            # No selected regions, so format the whole file.
            allreg = sublime.Region(0, v.size())
            regions.append(allreg)

        for region in regions:
            self.doFormat(edit, region, v)

    def doFormat(self, edit, region, v):
        """Format a region of text using 9e-sass-lint --fix command."""
        cmd = []
        cmd.append(util.which("9e-sass-lint"))
        cmd.append("--stdin")
        cmd.append("--fix")

        if not region.empty():
                s = v.substr(region)
                s = util.communicate(cmd, code=s)
                if len(s) > 0:
                    v.replace(edit, region, s)
                else:
                    args = cmd, code = s, output_stream = util.STREAM_STDERR
                    error = util.communicate(args)
                    sublime.error_message(error)
