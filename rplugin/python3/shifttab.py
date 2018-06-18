# -*- coding: utf-8 -*-

from __future__ import division, print_function

import neovim


@neovim.plugin
class Main(object):

    def __init__(self, vim):
        self.vim = vim

    @neovim.function("ShiftTab")
    def shift_tab(self, args):
        import jedi
        coords = self.vim.call("getpos", ".")
        line = coords[1]
        column = coords[2]
        path = self.vim.current.buffer.name
        source = "\n".join(self.vim.current.buffer)
        script = jedi.Script(source=source, line=line, column=column-1,
                             path=path)
        sigs = script.call_signatures()
        if len(sigs):
            self.vim.command('echo "{0}"'.format(
                sigs[0].docstring().splitlines()[0].strip().replace("\"",
                                                                    "\\\"")
            ))
