vim
===

setting(.vimrc)
---------------
autocmd FileType cpp noremap <F7> :wa <CR>: make -j4<CR>
autocmd FileType cpp noremap <F5> :wa <CR>: !make run <CR>
autocmd FileType cpp noremap <F12> :cw <CR> : /error<CR>


shortcut
--------
delete

-dt/df 'c' --- not include c/include c
- db 
- de
- d$
- c w: delete word and insert mode
- Ctrl + w: delelte previous word in insert mode
- shift+c: delete till end and insert

move_

- A: move to end then edit
- b --- word begining
- e --- word ending
- w --- next word

.. _move: https://stackoverflow.com/questions/1737163/traversing-text-in-insert-mode#1737259 

completion_

    ctrl+n
    ctrl+p

.. _completion: http://vim.wikia.com/wiki/Any_word_completion 


cmd
---
%s

:%s/.*\n.*\n.*\n/\0\r/g (link2_)
& ---- repeat replace

.. _repeat_replace : https://stackoverflow.com/questions/382155/how-to-repeat-a-command-with-substitution-in-vim#17725288
.. _link2: https://stackoverflow.com/questions/10413906/how-to-add-a-line-after-every-few-lines-in-vim#10414058

search
------
:grep --- search text

/\c --- insensive match

shift+v --- for full lines

quickfix
 - :copen  open quickfix
 - autocmd QuickFixCmdPost *grep* cwindow  
 - autocmd QuickFixCmdPost [^l]* nested cwindow

g then ctrl+g --- count (link0_)

.. _link0: https://unix.stackexchange.com/questions/145289/how-can-i-count-the-number-of-words-in-a-file-whilst-editing-the-file-in-vim#145293

^/0(zero) --- You can use ^ or 0 (Zero) in normal mode to move to the beginning of a line.

@: --- To repeat a command-line command (link1_)

.. _link1: https://stackoverflow.com/questions/4789811/how-do-i-repeat-any-command-in-vim-like-c-x-z-in-emacs


Plugins
-------

nerdtree
- ?
- B: open bookmark
- cd: change path to    

fugutive
- Gstatus --- then '-' add/reset
- Gcommt -am "messages"
- Gpush origin branch
    

ctags
-----
ctags -R . --c++-kinds=+pf --extra=+q

or

Make a directory, for example ~/.vim/tags that will hold your ctags.

ctags -R --sort=yes --c++-kinds=+p --fields=+iaS --extra=+q --language-force=C++ -f qt5 /home/fossy/apps/qt5/5.15.0/gcc_64/include

set tags+=~/.vim/tags/qt5

**Shortcut**

g ] / ctrl+]

gf got header file

**Reference**

ctags_

.. _ctags: https://vim.fandom.com/wiki/C%2B%2B_code_completion


