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
            # Adapted from deoplete-jedi
            comp = sigs[0]
            if comp.type not in ("function", "class"):
                return

            params = []
            for i, p in enumerate(comp.params):
                desc = p.description.strip()
                if i == 0 and desc == 'self':
                    continue
                if '\\n' in desc:
                    desc = desc.replace('\\n', '\\x0A')
                desc.replace("\"", "\\\"")
                # Note: Hack for jedi param bugs
                if desc.startswith('param ') or desc == 'param':
                    desc = desc[5:].strip()
                if desc:
                    params.append(desc)

            # width = self.vim.call("columns")
            text = "{0}({1})".format(comp.name, ", ".join(params))
            width = max(0, self.vim.eval("&columns")-14)
            if len(text) > width:
                width = max(0, width - 3)
                text = text[:width] + "..."
            self.vim.command('echo "{0}"'.format(text))
