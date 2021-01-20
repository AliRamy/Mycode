# Customize Zsh Layout

1. `sh -c "\$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"` _// Download Oh My Zsh_

2. Installing FiraMono Nerd Font From GitHub

   - [Nerd Font Repo](https://github.com/ryanoasis/nerd-fonts)
   - [Nerd Font Website](https://www.nerdfonts.com/)

3. Install Powerline Fonts

   - `git clone https://github.com/powerline/fonts.git`
   - `cd fonts`
   - `./install.sh`

4. Download Iterm Themes:

   - `git clone https://github.com/mbadolato/iTerm2-Color-Schemes.git`

5. Change Themes

   - Open iTerm2 > Profiles > Edit Profiles > Colors > Color Presets Drop Down > Import.
   - In the import window, navigate to the “Schemes” folder _// from step 2_.
   - Select all the files so you can import all the color schemes at once.
   - Simply select whichever color scheme you like.

6. Change Font:

   - Open iTerm2 > Profiles > Edit Profiles > Text > Font Drop Down.
   - Select FiraMono Nerd Fonts

7. Install Syntax Highlighting Plugin and AutoSuggestion Plugin

   - `git clone https://github.com/zsh-users/zsh-syntax-highlighting.git \${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting`
   - `git clone https://github.com/zsh-users/zsh-autosuggestions \$ZSH_CUSTOM/plugins/zsh-autosuggestions`

8. Add the following code to .zshrc

```bash
# If you come from bash you might have to change your $PATH.
export PATH=$HOME/bin:/usr/local/bin:$PATH

# Exporting Path to oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

# Setting ZSH_THEME
ZSH_THEME="agnoster"
#ZSH_THEME="duellj"
#ZSH_THEME="cloud"
#ZSH_THEME="edvardm"
#ZSH_THEME="apple"
#ZSH_THEME="jonathan"
#ZSH_THEME="intheloop"
figlet "Let's Code"
cowsay -f tux "Hello World!"

#Exporting Node and NVM
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
export PATH="/usr/local/bin/npm:/usr/local/bin/node:/usr/local/bin:$PATH"

#Exporting Java
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-15.0.1.jdk/Contents/Home
export PATH=$JAVA_HOME/bin:$PATH

#Exporting Dart
export PATH="$PATH":"$HOME/usr/local/opt/dart/libexec"

#Exporting Flutter
export PATH="$PATH:/Users/aliramy/flutter/bin"

#Exporting Python Interpreter
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv

#Exporting Python Virtualenv and Virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Mycode
export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
source /usr/local/bin/virtualenvwrapper_lazy.sh

#Exporting CS50 library
export LIBRARY_PATH=/usr/local/lib
export C_INCLUDE_PATH=/usr/local/include
export LD_LIBRARY_PATH=/usr/local/lib

#Alias Python
alias python=python3
alias pip=pip3
alias cl=clear
alias vim=nvim

# Setting Plugins
plugins=(
    git
    zsh-syntax-highlighting
    zsh-autosuggestions
    virtualenvwrapper
)

source $ZSH/oh-my-zsh.sh
```

## Making Some Changes on oh-my-zsh themes

1. `cd .oh-my-zsh/themes/`
2. `code agnoster.zsh-theme` _// Open agnoster theme_
3. Delet all code and add the following code
4. [Agnoster Theme File](/AwesomeZsh/themes/agnoster.zsh-theme)

5. `code cloud.zsh-theme`
6. Delete all the code and add the following code
7. [Cloud Theme File](/AwesomeZsh/themes/cloud.zsh-theme)

8. `code edvardm.zsh-theme`
9. Delete all the code and add the following code
10. [Edvardm Theme File](/AwesomeZsh/themes/evardm.zsh-theme)

11. `code jonathan.zsh-theme`
12. Delete all the code and add the following code
13. [Jonathan Theme File](/AwesomeZsh/themes/jonathan.zsh-theme)

14. `code intheloop.zsh-theme`
15. Delete all the code and add the following code
16. [Intheloop Theme File](/AwesomeZsh/themes/intheloop.zsh-theme)
