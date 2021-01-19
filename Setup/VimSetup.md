# Install NeoVim

1. `brew install neovim` _// Install Neovim_
2. `mkdir ~/.config/nvim` _// Make directory for your Neovim config_
3. `touch ~/.config/nvim/init.vim` _// Create an init.vim file_
4. Install vim-plug

   - `curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegun vim-plug/master/plug.vim` _// You should now have plug.vim in your autoload directory so it will load of on start_
   - `mkdir ~/.config/nvim/vim-plug` _// Make directory for plugins_
   - `touch ~/.config/nvim/vim-plug/plugins.vim` _// Make file for plugins_
   - Add the following code to your `~/.config/nvim/vim-plug/plugins.vim`

   ```vim
   if empty(glob('~/.config/nvim/autoload/plug.vim'))
     silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
       \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
     "autocmd VimEnter * PlugInstall
     "autocmd VimEnter * PlugInstall | source $MYVIMRC
   endif

   call plug#begin('~/.config/nvim/autoload/plugged')

       " Better Syntax Support
       Plug 'sheerun/vim-polyglot'
       " File Explorer
       Plug 'scrooloose/NERDTree'
       " Auto pairs for '(' '[' '{'
       Plug 'jiangmiao/auto-pairs'

   call plug#end()
   ```

   - Source the file in `~/.config/nvim/init.vim` _// Like my init.vim file_
   - Add the following code to `init.vim`

   ```vim
   source $HOME/.config/nvim/vim-plug/plugins.vim
   ```

   - Open nvim with `nvim` command
   - Click `Shift + ;` _// Open the command mode_
   - `:PlugInstall` _// Insatll all the plugins_

5. General Setings

   - `mkdir ~/.config/nvim/general` _// Make directory for general settings_
   - `touch ~/.config/nvim/general/settings.vim` _// Make file for settings_
   - Add the following code to your `~/.config/nvim/general/settings.vim`

   ```vim
   " set leader key
   let g:mapleader = "\<Space>"

   syntax enable                           " Enables syntax highlighing
   set hidden                              " Required to keep multiple buffers open multiple buffers
   set nowrap                              " Display long lines as just one line
   set encoding=utf-8                      " The encoding displayed
   set pumheight=10                        " Makes popup menu smaller
   set fileencoding=utf-8                  " The encoding written to file
   set ruler                          " Show the cursor position all the time
   set cmdheight=2                         " More space for displaying messages
   set iskeyword+=-                      " treat dash separated words as a word text object"
   set mouse=a                             " Enable your mouse
   set splitbelow                          " Horizontal splits will automatically be below
   set splitright                          " Vertical splits will automatically be to the right
   set t_Co=256                            " Support 256 colors
   set conceallevel=0                      " So that I can see `` in markdown files
   set tabstop=2                           " Insert 2 spaces for a tab
   set shiftwidth=2                        " Change the number of space characters inserted for indentation
   set smarttab                            " Makes tabbing smarter will realize you have 2 vs 4
   set expandtab                           " Converts tabs to spaces
   set smartindent                         " Makes indenting smart
   set autoindent                          " Good auto indent
   set laststatus=0                        " Always display the status line
   set number                              " Line numbers
   set cursorline                          " Enable highlighting of the current line
   set background=dark                     " tell vim what the background color looks like
   set showtabline=2                       " Always show tabs
   set noshowmode                          " We don't need to see things like -- INSERT -- anymore
   set nobackup                            " This is recommended by coc
   set nowritebackup                       " This is recommended by coc
   set updatetime=300                      " Faster completion
   set timeoutlen=500                      " By default timeoutlen is 1000 ms
   set formatoptions-=cro                  " Stop newline continution of comments
   set clipboard=unnamedplus               " Copy paste between vim and everything else
   "set autochdir                           " Your working directory will always be the same as your working directory

   au! BufWritePost $MYVIMRC source %      " auto source when writing to init.vm alternatively you can run :source $MYVIMRC

   " You can't stop me
   cmap w!! w !sudo tee %
   ```

   - Source the file in `~/.config/nvim/init.vim` _// Like my init.vim file_

6. Mapping new keys

   - `mkdir ~/.config/nvim/keys` _// Make directory for mapping keys_
   - `touch ~/.config/nvim/keys/mappings.vim` _// Make file for mapping_
   - Add the following code to your `~/.config/nvim/keys/mapping.vim`

   ```vim
   " Better nav for omnicomplete
   inoremap <expr> <c-j> ("\<C-n>")
   inoremap <expr> <c-k> ("\<C-p>")

   " Use alt + hjkl to resize windows
   nnoremap <M-j>    :resize -2<CR>
   nnoremap <M-k>    :resize +2<CR>
   nnoremap <M-h>    :vertical resize -2<CR>
   nnoremap <M-l>    :vertical resize +2<CR>

   " I hate escape more than anything else
   inoremap jk <Esc>
   inoremap kj <Esc>

   " Easy CAPS
   inoremap <c-u> <ESC>viwUi
   nnoremap <c-u> viwU<Esc>

   " TAB in general mode will move to text buffer
   nnoremap <TAB> :bnext<CR>
   " SHIFT-TAB will go back
   nnoremap <S-TAB> :bprevious<CR>

   " Alternate way to save
   nnoremap <C-s> :w<CR>
   " Alternate way to quit
   nnoremap <C-Q> :wq!<CR>
   " Use control-c instead of escape
   nnoremap <C-c> <Esc>
   " <TAB>: completion.
   inoremap <expr><TAB> pumvisible() ? "\<C-n>" : "\<TAB>"

   " Better tabbing
   vnoremap < <gv
   vnoremap > >gv

   " Better window navigation
   nnoremap <C-h> <C-w>h
   nnoremap <C-j> <C-w>j
   nnoremap <C-k> <C-w>k
   nnoremap <C-l> <C-w>l

   nnoremap <Leader>o o<Esc>^Da
   nnoremap <Leader>O O<Esc>^Da
   ```

   - Source the file in `~/.config/nvim/init.vim` _// Like my init.vim file_

7. Get healthy

   - Open nvim with `nvim` command
   - Click `Shift + ;` _// Open the command mode_
   - `:checkhealth` _// o see copy/paste and python and node setup_
   - On mac `pbcopy` should be builtin _// Support for copy/paste_
   - On Ubuntu
     - `sudo apt install xsel`
   - On Arch Linux
     - `sudo pacman -S xsel`
   - Neovim python support
     - `pip install pynvim`
   - Neovim node support
     - `npm i -g neovim`
   - `touch ~/.config/nvim/general/paths.vim` _// Make file for paths_
   - Add the following code to your `~/.config/nvim/general/paths.vim`

   ```vim
   "let g:python3_host_prog = expand("<path to python with pynvim installed>")
   let g:python3_host_prog = expand("/usr/local/bin/python3") " <- example
   "let g:node_host_prog = expand("<path to node with neovim installed>")
   let g:node_host_prog = expand("~/.nvm/versions/node/v15.0.1/bin/node") " <- example
   ```

8. Adding a theme

   - Add the following code to your `vim-plug/plugins.vim`

   ```vim
   "Themes
   Plug 'joshdick/onedark.vim'
   ```

   - Make sure to run `:PlugInstall` after add any plug
   - `mkdir ~/.config/nvim/themes` _// Make themes directory_
   - `touch ~/.config/nvim/themes/onedark.vim` _// Make file for theme_
   - Add the following code to your `~/.config/nvim/themes/onedark.vim`

   ```vim
   " onedark.vim override: Don't set a background color when running in a terminal;
   if (has("autocmd") && !has("gui_running"))
   augroup colorset
       autocmd!
       let s:white = { "gui": "#ABB2BF", "cterm": "145", "cterm16" : "7" }
       autocmd ColorScheme * call onedark#set_highlight("Normal", { "fg": s:white }) " `bg` will not be styled since there is no `bg` setting
   augroup END
   endif

   hi Comment cterm=italic
   let g:onedark_hide_endofbuffer=1
   let g:onedark_terminal_italics=1
   let g:onedark_termcolors=256

   syntax on
   colorscheme onedark


   " checks if your terminal has 24-bit color support
   if (has("termguicolors"))
       set termguicolors
       hi LineNr ctermbg=NONE guibg=NONE
   endif
   ```

   - Source the file in `~/.config/nvim/init.vim` _// Like my init.vim file_

9. Conquerer of Completion COC

   - Add the following code to your `vim-plug/plugins.vim`

   ```vim
   " Stable version of coc
   Plug 'neoclide/coc.nvim', {'branch': 'release'}
   ```

   - Make sure to run `:PlugInstall` after add any plug
   - `mkdir ~/.config/nvim/plug-config` _// make plug-config directory_
   - `touch ~/.config/nvim/plug-config/coc.vim` _// make file for coc_
   - Add the following code to your `~/.config/nvim/plug-config/coc.vim`

   ```vim
   " TextEdit might fail if hidden is not set.
   set hidden

   " Some servers have issues with backup files, see #649.
   set nobackup
   set nowritebackup

   " Give more space for displaying messages.
   set cmdheight=2

   " Having longer updatetime (default is 4000 ms = 4 s) leads to noticeable
   " delays and poor user experience.
   set updatetime=300

   " Don't pass messages to |ins-completion-menu|.
   set shortmess+=c

   " Always show the signcolumn, otherwise it would shift the text each time
   " diagnostics appear/become resolved.
   if has("patch-8.1.1564")
   " Recently vim can merge signcolumn and number column into one
   set signcolumn=number
   else
   set signcolumn=yes
   endif

   " Use tab for trigger completion with characters ahead and navigate.
   " NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
   " other plugin before putting this into your config.
   inoremap <silent><expr> <TAB>
       \ pumvisible() ? "\<C-n>" :
       \ <SID>check_back_space() ? "\<TAB>" :
       \ coc#refresh()
   inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

   function! s:check_back_space() abort
   let col = col('.') - 1
   return !col || getline('.')[col - 1]  =~# '\s'
   endfunction

   " Use <c-space> to trigger completion.
   if has('nvim')
   inoremap <silent><expr> <c-space> coc#refresh()
   else
   inoremap <silent><expr> <c-@> coc#refresh()
   endif

   " Make <CR> auto-select the first completion item and notify coc.nvim to
   " format on enter, <cr> could be remapped by other vim plugin
   inoremap <silent><expr> <cr> pumvisible() ? coc#_select_confirm()
                               \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

   " Use `[g` and `]g` to navigate diagnostics
   " Use `:CocDiagnostics` to get all diagnostics of current buffer in location list.
   nmap <silent> [g <Plug>(coc-diagnostic-prev)
   nmap <silent> ]g <Plug>(coc-diagnostic-next)

   " GoTo code navigation.
   nmap <silent> gd <Plug>(coc-definition)
   nmap <silent> gy <Plug>(coc-type-definition)
   nmap <silent> gi <Plug>(coc-implementation)
   nmap <silent> gr <Plug>(coc-references)

   " Use K to show documentation in preview window.
   nnoremap <silent> K :call <SID>show_documentation()<CR>

   function! s:show_documentation()
   if (index(['vim','help'], &filetype) >= 0)
       execute 'h '.expand('<cword>')
   elseif (coc#rpc#ready())
       call CocActionAsync('doHover')
   else
       execute '!' . &keywordprg . " " . expand('<cword>')
   endif
   endfunction

   " Highlight the symbol and its references when holding the cursor.
   autocmd CursorHold * silent call CocActionAsync('highlight')

   " Symbol renaming.
   nmap <leader>rn <Plug>(coc-rename)

   " Formatting selected code.
   xmap <leader>f  <Plug>(coc-format-selected)
   nmap <leader>f  <Plug>(coc-format-selected)

   augroup mygroup
   autocmd!
   " Setup formatexpr specified filetype(s).
   autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
   " Update signature help on jump placeholder.
   autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
   augroup end

   " Applying codeAction to the selected region.
   " Example: `<leader>aap` for current paragraph
   xmap <leader>a  <Plug>(coc-codeaction-selected)
   nmap <leader>a  <Plug>(coc-codeaction-selected)

   " Remap keys for applying codeAction to the current buffer.
   nmap <leader>ac  <Plug>(coc-codeaction)
   " Apply AutoFix to problem on the current line.
   nmap <leader>qf  <Plug>(coc-fix-current)

   " Map function and class text objects
   " NOTE: Requires 'textDocument.documentSymbol' support from the language server.
   xmap if <Plug>(coc-funcobj-i)
   omap if <Plug>(coc-funcobj-i)
   xmap af <Plug>(coc-funcobj-a)
   omap af <Plug>(coc-funcobj-a)
   xmap ic <Plug>(coc-classobj-i)
   omap ic <Plug>(coc-classobj-i)
   xmap ac <Plug>(coc-classobj-a)
   omap ac <Plug>(coc-classobj-a)

   " Remap <C-f> and <C-b> for scroll float windows/popups.
   if has('nvim-0.4.0') || has('patch-8.2.0750')
   nnoremap <silent><nowait><expr> <C-f> coc#float#has_scroll() ? coc#float#scroll(1) : "\<C-f>"
   nnoremap <silent><nowait><expr> <C-b> coc#float#has_scroll() ? coc#float#scroll(0) : "\<C-b>"
   inoremap <silent><nowait><expr> <C-f> coc#float#has_scroll() ? "\<c-r>=coc#float#scroll(1)\<cr>" : "\<Right>"
   inoremap <silent><nowait><expr> <C-b> coc#float#has_scroll() ? "\<c-r>=coc#float#scroll(0)\<cr>" : "\<Left>"
   vnoremap <silent><nowait><expr> <C-f> coc#float#has_scroll() ? coc#float#scroll(1) : "\<C-f>"
   vnoremap <silent><nowait><expr> <C-b> coc#float#has_scroll() ? coc#float#scroll(0) : "\<C-b>"
   endif

   " Use CTRL-S for selections ranges.
   " Requires 'textDocument/selectionRange' support of language server.
   nmap <silent> <C-s> <Plug>(coc-range-select)
   xmap <silent> <C-s> <Plug>(coc-range-select)

   " Add `:Format` command to format current buffer.
   command! -nargs=0 Format :call CocAction('format')

   " Add `:Fold` command to fold current buffer.
   command! -nargs=? Fold :call     CocAction('fold', <f-args>)

   " Add `:OR` command for organize imports of the current buffer.
   command! -nargs=0 OR   :call     CocAction('runCommand', 'editor.action.organizeImport')

   " Add (Neo)Vim's native statusline support.
   " NOTE: Please see `:h coc-status` for integrations with external plugins that
   " provide custom statusline: lightline.vim, vim-airline.
   set statusline^=%{coc#status()}%{get(b:,'coc_current_function','')}

   " Mappings for CoCList
   " Show all diagnostics.
   nnoremap <silent><nowait> <space>a  :<C-u>CocList diagnostics<cr>
   " Manage extensions.
   nnoremap <silent><nowait> <space>e  :<C-u>CocList extensions<cr>
   " Show commands.
   nnoremap <silent><nowait> <space>c  :<C-u>CocList commands<cr>
   " Find symbol of current document.
   nnoremap <silent><nowait> <space>o  :<C-u>CocList outline<cr>
   " Search workspace symbols.
   nnoremap <silent><nowait> <space>s  :<C-u>CocList -I symbols<cr>
   " Do default action for next item.
   nnoremap <silent><nowait> <space>j  :<C-u>CocNext<CR>
   " Do default action for previous item.
   nnoremap <silent><nowait> <space>k  :<C-u>CocPrev<CR>
   " Resume latest coc list.
   nnoremap <silent><nowait> <space>p  :<C-u>CocListResume<CR>
   ```

   - Source the file in `~/.config/nvim/init.vim` _// Like my init.vim file_
   - Open nvim with `nvim` command
   - Click `Shift + ;` _// Open the command mode_
   - `:CocInstall` coc-angular coc-clangd coc-css coc-flutter coc-git coc-go coc-html coc-java coc-python coc-omnisharp coc-rome coc-sql coc-svg coc-xml coc-marketplace
   - [Coc extensions](https://github.com/neoclide/coc.nvim/wiki/Using-coc-extensions)
   - `:CocConfig` will open `~/.config/nvim/coc-settings.json`
   - Add the following code to your `~/.config/nvim/coc-settings.json`

   ```json
   {
     "coc.preferences.formatOnSaveFiletypes": [
       "css",
       "markdown",
       "javascript",
       "graphql",
       "html",
       "yaml",
       "json",
       "python"
     ],

     "python.linting.enabled": true,
     "python.linting.pylintEnabled": true,
     "snippets.ultisnips.directories": [
       "UltiSnips",
       "~/.config/nvim/utils/snips"
     ]
   }
   ```

   - for more info on configuring your settings checkout [this page](https://github.com/neoclide/coc.nvim/wiki/Using-coc-extensions)

10. Installing Nerd Fonts

    - [Nerd Font Repo](https://github.com/ryanoasis/nerd-fonts)
    - [Nerd Font Website](https://www.nerdfonts.com/)

11. Airline

    - Add the following code to `~/.config/nvim/vim-plug/plugins.vim`

    ```vim
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
    ```

    - `touch ~/.config/nvim/themes/airline.vim` _// Make file for airline_
    - Add the following code to `~/.config/nvim/themes/arline.vim`

    ```vim
    " enable tabline
    let g:airline#extensions#tabline#enabled = 1
    let g:airline#extensions#tabline#left_sep = ''
    let g:airline#extensions#tabline#left_alt_sep = ''
    let g:airline#extensions#tabline#right_sep = ''
    let g:airline#extensions#tabline#right_alt_sep = ''

    " enable powerline fonts
    let g:airline_powerline_fonts = 1
    let g:airline_left_sep = ''
    let g:airline_right_sep = ''

    " Switch to your current theme
    let g:airline_theme = 'onedark'

    " Always show tabs
    set showtabline=2

    " We don't need to see things like -- INSERT -- anymore
    set noshowmode
    ```

    - Source the file in `~/.config/nvim/init.vim` _// Like my init.vim file_

12. Install coc-explorer

    - Open nvim with `nvim` command
    - Click `Shift + ;` _// Open the command mode_
    - `:CocInstall` coc-explorer
    - `:CocConfig` will open `~/.config/nvim/coc-settings.json`
    - Add the following code to your `~/.config/nvim/coc-settings.json`

    ```json
    "explorer.width": 30,
    "explorer.icon.enableNerdfont": true,
    "explorer.previewAction.onHover": false,
    "explorer.keyMappings.global": {
    "<cr>": ["expandable?", "expand", "open"],
    "v": "open:vsplit"
    }
    ```

    - Add the following code to `~/.config/nvim/plug-config/coc.vim`

    ```vim
    " Explorer
    let g:coc_explorer_global_presets = {
    \   '.vim': {
    \     'root-uri': '~/.vim',
    \   },
    \   'tab': {
    \     'position': 'tab',
    \     'quit-on-open': v:true,
    \   },
    \   'floating': {
    \     'position': 'floating',
    \     'open-action-strategy': 'sourceWindow',
    \   },
    \   'floatingTop': {
    \     'position': 'floating',
    \     'floating-position': 'center-top',
    \     'open-action-strategy': 'sourceWindow',
    \   },
    \   'floatingLeftside': {
    \     'position': 'floating',
    \     'floating-position': 'left-center',
    \     'floating-width': 50,
    \     'open-action-strategy': 'sourceWindow',
    \   },
    \   'floatingRightside': {
    \     'position': 'floating',
    \     'floating-position': 'right-center',
    \     'floating-width': 50,
    \     'open-action-strategy': 'sourceWindow',
    \   },
    \   'simplify': {
    \     'file-child-template': '[selection | clip | 1] [indent][icon | 1] [filename omitCenter 1]'
    \   }
    \ }

    nmap <space>e :CocCommand explorer<CR>
    nmap <space>f :CocCommand explorer --preset floating<CR>
    autocmd BufEnter * if (winnr("$") == 1 && &filetype == 'coc-explorer') | q | endif
    ```
