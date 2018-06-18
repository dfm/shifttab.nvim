# shifttab.nvim

Adding the Jupyter notebook's "shift-tab" functionality to Neovim.
Within a Python function, press shift-tab and see what happens!

## Installation

This plugin requires the Neovim Python API and
[Jedi](http://jedi.readthedocs.io). You can install those using pip:

```bash
pip install neovim jedi
```

Then, using [vim-plug](https://github.com/junegunn/vim-plug) (or your Neovim
plugin manager of choice) add something like the following to your
`~/.config/nvim/init.vim` file:

```viml
Plug 'dfm/shifttab.nvim', { 'do': ':UpdateRemotePlugins' }

" Map "shift-tab" to the ShiftTab function
autocmd FileType python inoremap <S-tab> <C-o>:call ShiftTab()<CR>

" Hide the mode name from the status bar so that you can see the results
autocmd FileType python setlocal noshowmode
```

(Don't forget to run `:PlugInstall` to get the new plugin installed!)

## Usage

When in insert mode, hit `Shift-Tab` when you're inside a function/method call
to see the call sequence in the status bar. For example if you type:

```python
import numpy as np
np.linspace(<Shift-Tab>
```

you will see:

```python
linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
```

in the status bar.
