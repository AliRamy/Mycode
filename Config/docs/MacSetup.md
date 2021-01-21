# How To Setup Your Mac For Code

## Change Shell to ZSH

1. `chsh -s /bin/zsh` _// Changing The Shell Type_
2. `which $SHELL` _// It should prompt /bin/zsh_

## Install XCode Tools

`sudo xcode-select --install` _// Then you have to install Xcode Feom AppStore_

## Install Homebrew

1. `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
   [Homebrew Website](https://brew.sh/)
2. `brew update` _// This updates Homebrew_

## Install Git

`brew install git`

## Install Google Chrome

`brew cask install google-chrome`

## Install Chrome Extensions

Notion Web clipper
Google Translate
Hover Zoom
Adblock Plus
Google Keep
Bitdefender Anti-Tracker
Chrome Remote Desktop
Grammarly
Social Blade
Quran Tab
Picture in Picture

## Install Iterm2

1. `brew cask install iterm2`
2. Go to Prefrences > Appearance > General > Theme > Minimal

## Install VSCode

`brew cask install visual-studio-code`

## Install Kite

`brew cask install kite`

## Install Alfred 4

`brew cask install alfred`

## Install Spectacle

`brew cask install spectacle`

## Install VSCode Extensions

1. .Net Deevlopment

   - .NET Install Tool for Extension Authors
   - C# for Visual Studio Code

2. C And C++ Development

   - C/C++ Extension Pack

3. Data Storage

   - Azure Tools
   - SQL Server (mssql)

4. Themes and Icons

   - Community Material Theme
   - Material Icon Theme
   - Material Theme
   - One Dark Pro
   - Dark+ Pro

5. Java

   - Java Extension Pack
   - Spring Boot Tools
   - Spring Initializer Java Support
   - Spring Boot Dashboard

6. Web And Mobile

   - HTML Snippets
   - LiveServer
   - CSS Peek
   - JavaScript
   - TypeScript
   - React Extension Pack
   - React Native Tools
   - Dart
   - Flutter

7. Python

   - Python
   - Pylance
   - Jupyter

8. PHP

   - PHP Extension Pack

9. Components Management

   - Docker
   - Kubernetes
   - Gardener Kubernetes Service

10. Sharing And Streaming

    - LiveShare
    - Remote-SSH
    - Remote - SSH: Editing Configuration Files
    - Remote - Containers

11. Formmat Code

    - Prettier

12. Git

    - GitHub Pull Requests and Issues
    - GitLens — Git supercharged

13. Write Code Fast

    - Kite AI Code AutoComplete

14. General

    - markdownlint

15. Vim

    - Vim
    - VimL

16. Node

    - Search node_modules
    - npm
    - npm Intellisense

## Install Cowsay

`brew install cowsay`

## Install Python3 and pip3

1. `brew install python3`
2. `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
3. `python3 get-pip.py`
4. `pip3 install python-dev-tools`

## Installing Virtualenv & Virtualenvwrapper

1. `sudo pip3 install virtualenvwrapper`
2. `sudo pip3 install virtualenv`
3. `python3.8 -m pip install pipenv`
4. `pip freeze | grep virtualenv` _// to know virtualenvwrapper version_

## Exporting Python Interpreter

```bash
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
```

## Exporting Python Virtualenv and Virtualenvwrapper

```bash
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Mycode
export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
source /usr/local/bin/virtualenvwrapper_lazy.sh
```

## Alias Python

```bash
alias python=python3
alias pip=pip3
```

## Install Java

1. `brew cask install java`
2. `wget https://download.java.net/java/GA/jdk14.0.1/664493ef4a6946b186ff29eb326336a2/7/GPL/openjdk-14.0.1_osx-x64_bin.tar.gz`
3. `tar -xf openjdk-14.0.1_osx-x64_bin.tar.gz`
4. `/usr/libexec/java_home -v 1.8` _// this is how to know wher java installed_
5. `brew install maven`

## Exporting Java

```bash
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-15.0.1.jdk/Contents/Home
export PATH=$JAVA_HOME/bin:$PATH
```

## Install Dart

1. `brew tap dart-lang/dart`
2. `brew install dart`

## Exporting Dart

```bash
export PATH="$PATH":"$HOME/usr/local/opt/dart/libexec"
```

## Install NVM/Node

1. `brew install node`
2. `curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash`

## Exporting Node and NVM

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
export PATH="/usr/local/bin/npm:/usr/local/bin/node:/usr/local/bin:$PATH"
```

## Install TypeScript

1. `npm install -g typescript`
2. `tsc` _// type script compilier_

## Install Flutter

1. `git clone https://github.com/flutter/flutter.git -b stable`
2. `flutter doctor`
3. `flutter precache`
4. For more details to install IOS Simulator and Andriod Emulator go to [Flutter Docs](https://flutter.dev/docs/get-started/install/macos)

## Exporting Flutter

```bash
export PATH="$PATH:/Users/aliramy/flutter/bin"
```

## Install CS50 Library on Mac

1. Download the latest release from [CS50 Github](https://github.com/cs50/libcs50/releases)
2. Extract libcs50-_._
3. `cd libcs50-*`
4. `sudo make install`

## Exporting CS50

```bash
export LIBRARY_PATH=/usr/local/lib
export C_INCLUDE_PATH=/usr/local/include
export LD_LIBRARY_PATH=/usr/local/lib
```

## Install Notion

`brew cask install notion`
[Notion Website](https://www.notion.so/desktop)
