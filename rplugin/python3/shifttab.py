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
        line = self.vim.call('line', '.')
        column = self.vim.call('col', '.')
        path = self.vim.current.buffer.name
        source = "\n".join(self.vim.current.buffer)
        script = jedi.Script(source=source, line=line, column=column,
                             path=path)
        sigs = script.call_signatures()
        if len(sigs):
            # print(sigs[0].docstring())
            self.vim.command('echo "{0}"'.format(
                sigs[0].docstring().splitlines()[0].replace("\"", "\\\"")
            ))
        else:
            self.vim.command('echo "nothing"')
