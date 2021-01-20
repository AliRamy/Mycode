# Customize ZShell Layout

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
2. `code agnoster.zsh-theme` _#Open agnoster theme_
3. Delet all code and add the following code

```bash
# vim:ft=zsh ts=2 sw=2 sts=2
#
# agnoster's Theme - https://gist.github.com/3712874
# A Powerline-inspired theme for ZSH
#
# # README
#
# In order for this theme to render correctly, you will need a
# [Powerline-patched font](https://github.com/Lokaltog/powerline-fonts).
# Make sure you have a recent version: the code points that Powerline
# uses changed in 2012, and older versions will display incorrectly,
# in confusing ways.
#
# In addition, I recommend the
# [Solarized theme](https://github.com/altercation/solarized/) and, if you're
# using it on Mac OS X, [iTerm 2](https://iterm2.com/) over Terminal.app -
# it has significantly better color fidelity.
#
# If using with "light" variant of the Solarized color schema, set
# SOLARIZED_THEME variable to "light". If you don't specify, we'll assume
# you're using the "dark" variant.
#
# # Goals
#
# The aim of this theme is to only show you *relevant* information. Like most
# prompts, it will only show git information when in a git working directory.
# However, it goes a step further: everything from the current user and
# hostname to whether the last call exited with an error to whether background
# jobs are running in this shell will all be displayed automatically when
# appropriate.

### Segment drawing
# A few utility functions to make it easy and re-usable to draw segmented prompts

CURRENT_BG='NONE'

case ${SOLARIZED_THEME:-dark} in
    light) CURRENT_FG='white';;
    *)     CURRENT_FG='black';;
esac

# Special Powerline characters

() {
  local LC_ALL="" LC_CTYPE="en_US.UTF-8"
  # NOTE: This segment separator character is correct.  In 2012, Powerline changed
  # the code points they use for their special characters. This is the new code point.
  # If this is not working for you, you probably have an old version of the
  # Powerline-patched fonts installed. Download and install the new version.
  # Do not submit PRs to change this unless you have reviewed the Powerline code point
  # history and have new information.
  # This is defined using a Unicode escape sequence so it is unambiguously readable, regardless of
  # what font the user is viewing this source code in. Do not replace the
  # escape sequence with a single literal character.
  # Do not change this! Do not make it '\u2b80'; that is the old, wrong code point.
  SEGMENT_SEPARATOR=$'\ue0b0'
}

# Begin a segment
# Takes two arguments, background and foreground. Both can be omitted,
# rendering default background/foreground.
prompt_segment() {
  local bg fg
  [[ -n $1 ]] && bg="%K{$1}" || bg="%k"
  [[ -n $2 ]] && fg="%F{$2}" || fg="%f"
  if [[ $CURRENT_BG != 'NONE' && $1 != $CURRENT_BG ]]; then
    echo -n " %{$bg%F{$CURRENT_BG}%}$SEGMENT_SEPARATOR%{$fg%} "
  else
    echo -n "%{$bg%}%{$fg%} "
  fi
  CURRENT_BG=$1
  [[ -n $3 ]] && echo -n $3
}

# End the prompt, closing any open segments
prompt_end() {
  if [[ -n $CURRENT_BG ]]; then
    echo -n " %{{$CURRENT_BG}%}$SEGMENT_SEPARATOR"
  else
    echo -n "%{%k%}"
  fi
  echo -n "%{%f%}"
  CURRENT_BG=''
}

### Prompt components
# Each component will draw itself, and hide itself if no information needs to be shown

# Context: user@hostname (who am I and where am I)
prompt_context() {
  if [[ "$USER" != "$DEFAULT_USER" || -n "$SSH_CLIENT" ]]; then
    prompt_segment black default "%(!.%{%F{yellow}%}.) %n@%m"
  fi
}

# Git: branch/detached head, dirty status
prompt_git() {
  (( $+commands[git] )) || return
  if [[ "$(git config --get oh-my-zsh.hide-status 2>/dev/null)" = 1 ]]; then
    return
  fi
  local PL_BRANCH_CHAR
  () {
    local LC_ALL="" LC_CTYPE="en_US.UTF-8"
    PL_BRANCH_CHAR="  "         # 
  }
  local ref dirty mode repo_path

   if [[ "$(git rev-parse --is-inside-work-tree 2>/dev/null)" = "true" ]]; then
    repo_path=$(git rev-parse --git-dir 2>/dev/null)
    dirty=$(parse_git_dirty)
    ref=$(git symbolic-ref HEAD 2> /dev/null) || ref=" $(git rev-parse --short HEAD 2> /dev/null)"
    if [[ -n $dirty ]]; then
      prompt_segment yellow black
    else
      prompt_segment green $CURRENT_FG
    fi

    if [[ -e "${repo_path}/BISECT_LOG" ]]; then
      mode=" <B>"
    elif [[ -e "${repo_path}/MERGE_HEAD" ]]; then
      mode=" >M<"
    elif [[ -e "${repo_path}/rebase" || -e "${repo_path}/rebase-apply" || -e "${repo_path}/rebase-merge" || -e "${repo_path}/../.dotest" ]]; then
      mode=" >R>"
    fi

    setopt promptsubst
    autoload -Uz vcs_info

    zstyle ':vcs_info:*' enable git
    zstyle ':vcs_info:*' get-revision true
    zstyle ':vcs_info:*' check-for-changes true
    zstyle ':vcs_info:*' stagedstr ''
    zstyle ':vcs_info:*' unstagedstr ''
    zstyle ':vcs_info:*' formats ' %u%c'
    zstyle ':vcs_info:*' actionformats ' %u%c'
    vcs_info
    echo -n "${ref/refs\/heads\//$PL_BRANCH_CHAR }${vcs_info_msg_0_%% }${mode}"
  fi
}

prompt_bzr() {
  (( $+commands[bzr] )) || return

  # Test if bzr repository in directory hierarchy
  local dir="$PWD"
  while [[ ! -d "$dir/.bzr" ]]; do
    [[ "$dir" = "/" ]] && return
    dir="${dir:h}"
  done

  local bzr_status status_mod status_all revision
  if bzr_status=$(bzr status 2>&1); then
    status_mod=$(echo -n "$bzr_status" | head -n1 | grep "modified" | wc -m)
    status_all=$(echo -n "$bzr_status" | head -n1 | wc -m)
    revision=$(bzr log -r-1 --log-format line | cut -d: -f1)
    if [[ $status_mod -gt 0 ]] ; then
      prompt_segment yellow black "bzr@$revision ✚"
    else
      if [[ $status_all -gt 0 ]] ; then
        prompt_segment yellow black "bzr@$revision"
      else
        prompt_segment green black "bzr@$revision"
      fi
    fi
  fi
}

prompt_hg() {
  (( $+commands[hg] )) || return
  local rev st branch
  if $(hg id >/dev/null 2>&1); then
    if $(hg prompt >/dev/null 2>&1); then
      if [[ $(hg prompt "{status|unknown}") = "?" ]]; then
        # if files are not added
        prompt_segment red white
        st='±'
      elif [[ -n $(hg prompt "{status|modified}") ]]; then
        # if any modification
        prompt_segment yellow black
        st='±'
      else
        # if working copy is clean
        prompt_segment green $CURRENT_FG
      fi
      echo -n $(hg prompt "☿ {rev}@{branch}") $st
    else
      st=""
      rev=$(hg id -n 2>/dev/null | sed 's/[^-0-9]//g')
      branch=$(hg id -b 2>/dev/null)
      if `hg st | grep -q "^\?"`; then
        prompt_segment red black
        st='±'
      elif `hg st | grep -q "^[MA]"`; then
        prompt_segment yellow black
        st='±'
      else
        prompt_segment green $CURRENT_FG
      fi
      echo -n "☿ $rev@$branch" $st
    fi
  fi
}

# Dir: current working directory
prompt_dir() {
  prompt_segment blue $CURRENT_FG '  %~'
}

# Virtualenv: current working virtualenv
prompt_virtualenv() {
  local virtualenv_path="$VIRTUAL_ENV"
  if [[ -n $virtualenv_path && -n $VIRTUAL_ENV_DISABLE_PROMPT ]]; then
    prompt_segment blue black "(`basename $virtualenv_path`)"
  fi
}

# Status:
# - was there an error
# - am I root
# - are there background jobs?
prompt_status() {
  local -a symbols

  [[ $RETVAL -ne 0 ]] && symbols+="%{%F{red}%}"
  [[ $UID -eq 0 ]] && symbols+="%{%F{yellow}%}"
  [[ $(jobs -l | wc -l) -gt 0 ]] && symbols+="%{%F{cyan}%}漣"

  [[ -n "$symbols" ]] && prompt_segment black default "$symbols"
}

#AWS Profile:
# - display current AWS_PROFILE name
# - displays yellow on red if profile name contains 'production' or
#   ends in '-prod'
# - displays black on green otherwise
prompt_aws() {
  [[ -z "$AWS_PROFILE" || "$SHOW_AWS_PROMPT" = false ]] && return
  case "$AWS_PROFILE" in
    *-prod|*production*) prompt_segment red yellow  "AWS: $AWS_PROFILE" ;;
    *) prompt_segment green black "AWS: $AWS_PROFILE" ;;
  esac
}

## Main prompt
build_prompt() {
  RETVAL=$?
  prompt_status
  prompt_virtualenv
  prompt_aws
  prompt_context
  prompt_dir
  prompt_git
  prompt_bzr
  prompt_hg
  prompt_end
}

PROMPT='%{%f%b%k%}$(build_prompt) '
```

1. `code cloud.zsh-theme`
2. Delete all the code and add the following code

```bash
if [[ -z $ZSH_THEME_CLOUD_PREFIX ]]; then
    ZSH_THEME_CLOUD_PREFIX='☁'
fi

PROMPT='%{$fg_bold[cyan]%}$ZSH_THEME_CLOUD_PREFIX %{$fg_bold[green]%} %{$fg[green]%}%c %{$fg_bold[cyan]%}$(git_prompt_info)%{$fg_bold[blue]%} % %{$reset_color%}'

ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg[green]%}[%{$fg[cyan]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[green]%}] %{$fg[yellow]%} %{$reset_color%}"
ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg[green]%}]"
```

1. `code edvardm.zsh-theme`
2. Delete all the code and add the following code

```bash
PROMPT='%{$fg_bold[red]%} %{$fg_bold[green]%} %{$fg_bold[white]%}%c %{$fg_bold[blue]%}$(git_prompt_info)%{$fg_bold[blue]%} % %{$reset_color%}'

ZSH_THEME_GIT_PROMPT_PREFIX="  %{$fg[red]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[blue]%} %{$fg[yellow]%}%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg[blue]%}"
```

1. `code jonathan.zsh-theme`
2. Delete all the code and add the following code

```bash
functions rbenv_prompt_info >& /dev/null || rbenv_prompt_info(){}

function theme_precmd {
    local TERMWIDTH
    (( TERMWIDTH = ${COLUMNS} - 1 ))


    ###
    # Truncate the path if it's too long.

    PR_FILLBAR=""
    PR_PWDLEN=""

    local promptsize=${#${(%):---(%n@%m:%l)---()--}}
    local rubyprompt=`rvm_prompt_info || rbenv_prompt_info`
    local rubypromptsize=${#${rubyprompt}}
    local pwdsize=${#${(%):-%~}}

    if [[ "$promptsize + $rubypromptsize + $pwdsize" -gt $TERMWIDTH ]]; then
      ((PR_PWDLEN=$TERMWIDTH - $promptsize))
    else
      PR_FILLBAR="\${(l.(($TERMWIDTH - ($promptsize + $rubypromptsize + $pwdsize)))..${PR_HBAR}.)}"
    fi

}


setopt extended_glob
theme_preexec () {
    if [[ "$TERM" == "screen" ]]; then
    local CMD=${1[(wr)^(*=*|sudo|-*)]}
    echo -n "\ek$CMD\e\\"
    fi
}


setprompt () {
    ###
    # Need this so the prompt will work.

    setopt prompt_subst


    ###
    # See if we can use colors.

    autoload zsh/terminfo
    for color in RED GREEN YELLOW BLUE MAGENTA CYAN WHITE GREY; do
    eval PR_$color='%{$terminfo[bold]$fg[${(L)color}]%}'
    eval PR_LIGHT_$color='%{$fg[${(L)color}]%}'
    (( count = $count + 1 ))
    done
    PR_NO_COLOUR="%{$terminfo[sgr0]%}"

    ###
    # Modify Git prompt
    ZSH_THEME_GIT_PROMPT_PREFIX=" on %{$fg[green]%}"
    ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}"
    ZSH_THEME_GIT_PROMPT_DIRTY=""
    ZSH_THEME_GIT_PROMPT_CLEAN=""

    ZSH_THEME_GIT_PROMPT_ADDED="%{$fg[green]%} ✚"
    ZSH_THEME_GIT_PROMPT_MODIFIED="%{$fg[blue]%} "
    ZSH_THEME_GIT_PROMPT_DELETED="%{$fg[red]%} ✖"
    ZSH_THEME_GIT_PROMPT_RENAMED="%{$fg[magenta]%} "
    ZSH_THEME_GIT_PROMPT_UNMERGED="%{$fg[yellow]%} ═"
    ZSH_THEME_GIT_PROMPT_UNTRACKED="%{$fg[cyan]%} ﯙ "

    ###
    # See if we can use extended characters to look nicer.
    # UTF-8 Fixed

    if [[ $(locale charmap) == "UTF-8" ]]; then
    PR_SET_CHARSET=""
    PR_SHIFT_IN=""
    PR_SHIFT_OUT=""
    PR_HBAR="─"
        PR_ULCORNER="┌"
        PR_LLCORNER="└"
        PR_LRCORNER="┘"
        PR_URCORNER="┐"
    else
        typeset -A altchar
        set -A altchar ${(s..)terminfo[acsc]}
        # Some stuff to help us draw nice lines
        PR_SET_CHARSET="%{$terminfo[enacs]%}"
        PR_SHIFT_IN="%{$terminfo[smacs]%}"
        PR_SHIFT_OUT="%{$terminfo[rmacs]%}"
        PR_HBAR='$PR_SHIFT_IN${altchar[q]:--}$PR_SHIFT_OUT'
        PR_ULCORNER='$PR_SHIFT_IN${altchar[l]:--}$PR_SHIFT_OUT'
        PR_LLCORNER='$PR_SHIFT_IN${altchar[m]:--}$PR_SHIFT_OUT'
        PR_LRCORNER='$PR_SHIFT_IN${altchar[j]:--}$PR_SHIFT_OUT'
        PR_URCORNER='$PR_SHIFT_IN${altchar[k]:--}$PR_SHIFT_OUT'
     fi


    ###
    # Decide if we need to set titlebar text.

    case $TERM in
    xterm*)
        PR_TITLEBAR=$'%{\e]0;%(!.-=*[ROOT]*=- | .)%n@%m:%~ | ${COLUMNS}x${LINES} | %y\a%}'
        ;;
    screen)
        PR_TITLEBAR=$'%{\e_screen \005 (\005t) | %(!.-=[ROOT]=- | .)%n@%m:%~ | ${COLUMNS}x${LINES} | %y\e\\%}'
        ;;
    *)
        PR_TITLEBAR=''
        ;;
    esac


    ###
    # Decide whether to set a screen title
    if [[ "$TERM" == "screen" ]]; then
    PR_STITLE=$'%{\ekzsh\e\\%}'
    else
    PR_STITLE=''
    fi


    ###
    # Finally, the prompt.

    PROMPT='$PR_SET_CHARSET$PR_STITLE${(e)PR_TITLEBAR}\
$PR_CYAN$PR_ULCORNER$PR_HBAR$PR_GREY(\
$PR_GREEN%$PR_PWDLEN<...<%~%<<\
$PR_GREY)`rvm_prompt_info || rbenv_prompt_info`$PR_CYAN$PR_HBAR$PR_HBAR${(e)PR_FILLBAR}$PR_HBAR$PR_GREY(\
$PR_CYAN%(!.%SROOT%s.%n)$PR_GREY@$PR_GREEN%m:%l\
$PR_GREY)$PR_CYAN$PR_HBAR$PR_URCORNER\

$PR_CYAN$PR_LLCORNER$PR_BLUE$PR_HBAR(\
$PR_YELLOW%D{%H:%M:%S}\
$PR_LIGHT_BLUE%{$reset_color%}`git_prompt_info``git_prompt_status`$PR_BLUE)$PR_CYAN$PR_HBAR\
$PR_HBAR\
>$PR_NO_COLOUR '

    # display exitcode on the right when >0
    return_code="%(?..%{$fg[red]%}%? ↵ %{$reset_color%})"
    RPROMPT=' $return_code$PR_CYAN$PR_HBAR$PR_BLUE$PR_HBAR\
($PR_YELLOW%D{%a,%b%d}$PR_BLUE)$PR_HBAR$PR_CYAN$PR_LRCORNER$PR_NO_COLOUR'

    PS2='$PR_CYAN$PR_HBAR\
$PR_BLUE$PR_HBAR(\
$PR_LIGHT_GREEN%_$PR_BLUE)$PR_HBAR\
$PR_CYAN$PR_HBAR$PR_NO_COLOUR '
}

setprompt

autoload -U add-zsh-hook
add-zsh-hook precmd  theme_precmd
add-zsh-hook preexec theme_preexec
```

1. `code intheloop.zsh-theme`
2. Delete all the code and add the following code

```bash
# A multiline prompt with username, hostname, full path, return status, git branch, git dirty status, git remote status

local return_status="%{$fg[red]%}%(?..⏎)%{$reset_color%}"

local host_color="green"
if [ -n "$SSH_CLIENT" ]; then
  local host_color="red"
fi

PROMPT='
%{$fg_bold[grey]%}[%{$reset_color%}%{$fg_bold[${host_color}]%}%n@%m%{$reset_color%}%{$fg_bold[grey]%}]%{$reset_color%} %{$fg_bold[blue]%}%10c%{$reset_color%} $(git_prompt_info) $(git_remote_status)
%{$fg_bold[cyan]%}❯%{$reset_color%} '


RPROMPT='${return_status}%{$reset_color%}'

ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg[grey]%}(%{$fg[red]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[grey]%}) %{$fg[yellow]%}%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg[grey]%})"
ZSH_THEME_GIT_PROMPT_BEHIND_REMOTE="%{$fg_bold[magenta]%}↓%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_AHEAD_REMOTE="%{$fg_bold[magenta]%}↑%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIVERGED_REMOTE="%{$fg_bold[magenta]%}↕%{$reset_color%}"
```
