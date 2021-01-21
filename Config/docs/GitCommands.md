# Git Commands

## Initializing a Repository

- `git init`

## Staging Files

- `git add <File-Name>`
- `git add .`

## Viewing The Status

- `git status`
- `git status -s`

## Committing The Staged Files

- `git commit -m "Message"`
- `git commit -a -m "Message"`
- `git commmit`

## Removing Files

- `git rm <File-Name>`
- `git rm --cached <File-Name>` _// Removes from staging area only_
- `git rm <Folder-Name> -r`
- `git rm <Folder-Name> -r` _// Removes from staging area only_

## Renaming or Moving Files

- `git mv <Old-File-Name> <New-File-Name>`

## Viewing The Staged / Unstaged Changes

- `git diff` _**// Shows unstaged changes**_
- `git diff --staged` _// Shows unstaged changes_
- `git diff --cached` _// Shows unstaged changes_

## Viewing The History

- `git log` _// Full History_
- `git log --oneline` _// Summary History_
- `git log --reverse` _// Lists the commits from the oldest to the newest_

## Unstaging Files (Undoing git add)

- `git restore --staged <File-Name>` _// Copies the last version of file.js from repo to index_

## Generating a New SSH key

- `mkdir ~/.ssh`
- `touch ~/.ssh/config`
- `ssh-keygen -t ed25519 -C "email"`
  _// Note: If you are using a legacy system that doesn't support the Ed25519 algorithm, use:_
- `ssh-keygen -t rsa -b 4096 -C "email"`
- Add the Following Code to config file _// Note: If you chose not to add a passphrase to your key, you should omit the UseKeychain line_

```config
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/<Name-of-private-keyfile>
```

- `ssh-add -K ~/.ssh/<Name-of-Private-Keyfile>`

## Adding a new SSH key to your GitHub account

- `pbcopy < ~/.ssh/<Name-of-Private-Keyfile>.pub`
- In the upper-right corner of any page, click your profile photo, then click Settings.

![Settings](/Config/images/Settings.png)

- In the user settings sidebar, click SSH and GPG keys.

![Settings](/Config/images/ssh-keys.png)

- Click New SSH key or Add SSH key.

![Settings](/Config/images/add-ssh-key.png)

- In the "Title" field, add a descriptive label for the new key. For example, if you're using a personal Mac, you might call this key "Personal MacBook Air".
- Paste your key into the "Key" field.

![Settings](/Config/images/ssh-key-paste.png)

- Click Add SSH key.

![Settings](/Config/images/ssh-add-key.png)

- If prompted, confirm your GitHub password.

![Settings](/Config/images/sudo_mode_popup.png)

## Create a new repository on github

- In the upper-right corner of any page, use the drop-down menu, and select New repository.

![Settings](/Config/images/repo-create.png)

- Type a short, memorable name for your repository. For example, "hello-world".

![Settings](/Config/images/create-repository-name.png)

- Optionally, add a description of your repository. For example, "My first repository on GitHub."

![Settings](/Config/images/create-repository-desc.png)

- Choose a repository visibility. For more information, see "About repository visibility."

![Settings](/Config/images/create-repository-public-private.png)

- Click Create repository.

![Settings](/Config/images/create-repository-button.png)

- Copy the ssh address

![Settings](/Config/images/git.png)

- `git remote add origin git@github.com:AliRamy/hello-world.git`
- `git push origin master`

## Create a new repository on the command line

- `echo "# Repository_Name" >> README.md`
- `git init`
- `git add README.md`
- `git commit -m "first commit"`
- `git branch -M main` or `git branch -M master`
- `git remote add origin git@github.com:username/Repository_Name.git`
- `git push -u origin main` or `git push origin master`
