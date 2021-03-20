# Git

## Creating Snapshots

### Initializing a Repository

`git init`

### Git Configuration

`git config --global user.name "Ali Ramy"` _# Define the user name_

`git config --global user.email aliramy772004@gmail.com` _# Define the user email_

`git config --global core.editor "code --wait"` _# Define thre default editor_

`git config --global -e` _# Open the config file_

`git config --global core.autocrlf input`

### Staging Files

`git add file1.js` _# Stages a single file_

`git add file1.js` file2.js _# Stages multiple files_

`git add *.js` _# Stages with a pattern_

`git add .` _# Stages the current directory and all its content_

### Viewing The Status

`git status` _# Full status_

`git status -s` _# Short status_

### Committing The Staged Files

`git commit -m “Message”` _# Commits with a one-line message_

`git commit` _# Opens the default editor to type a long message_

### Skipping The Staging Area

`git commit -am “Message”`

### Removing Files

`git rm file1.js` _# Removes from working directory and staging area_

`git rm --cached file1.js` _# Removes from staging area only_

### Renaming or Moving Files

`git mv file1.js file1.txt`

### Viewing The Staged/Unstaged Changes

`git diff` _# Shows unstaged changes_

`git diff --staged` _# Shows staged changes_

`git diff --cached` _# Shows staged changes_

### Viewing The History

`git log` _# Full history_

`git log --oneline` _# Summary_

`git log --reverse` _# Lists the commits from the oldest to the newest_

### Viewing a Commit

`git show [CommitName]` _# Shows the given commit_

### Unstaging Files _(Undoing `git add`)_

`git restore --staged file.js` _# Copies the last version of file.js from repo to index_

### Discarding Local Changes

`git restore file.js` _# Copies file.js from index to working directory_

`git restore file1.js file2.js` _# Restores multiple files in working directory_

`git restore .` _# Discards all local changes (except untracked files)_

`git clean -fd` _# Removes all untracked files_

### Restoring an Earlier Version of a File

`git restore --source=HEAD~2 file.js`

## Browsing History

### Viewing the History

`git log --stat` _# Shows the list of modified files_

`git log --patch` _# Shows the actual changes (patches)_

### Creating an Alias

`git config --global alias.lg “log --oneline"` _# Make lg alias for log --online_

### Finding Contributors

`git shortlog`

### Viewing The History of a File

`git log file.txt` _# Shows the commits that touched file.txt_

`git log --stat file.txt` _# Shows statistics (the number of changes) for file.txt_

`git log --patch file.txt` _# Shows the patches (changes) applied to file.txt_

### Finding The Author of Lines

`git blame file.txt` _# Shows the author of each line in file.txt_

### Tagging

`git tag v1.0` _# Tags the last commit as v1.0_

`git tag v1.0 5e7a828` _# Tags an earlier commit_

`git tag` _# Lists all the tags_

`git tag -d v1.0` _# Deletes the given tag_

## Branching & Merging

### Managing Branches

`git branch [Branch Name]` _# Creates a new branch_

`git checkout [Branch Name]` _# Switches to a branch_

`git switch [Branch Name]` _# Switches to a branch_

`git switch -C [Branch Name]` _# Creates and switches_

`git branch -d [Branch Name]` _# Deletes a branch_

### Comparing Branches

`git log master..bugfix` _# Lists the commits in the bugfix branch not in master_

`git diff master..bugfix` _# Shows the summary of changes_

### Stashing

`git stash push -m “New tax rules” list` _# Creates a new stash_

`git stash list` _# Lists all the stashes_

`git stash show stash@{1}` _# Shows the given stash_

`git stash show 1` _# shortcut for stash@{1}_

`git stash apply 1` _# Applies the given stash to the working dir_

`git stash drop 1` _# Deletes the given stash_

`git stash clear` _# Deletes all the stashes_

### Merging

`git merge example` _# Merges the example branch into the current branch_

`git merge --no-ff example` _# Creates a merge commit even if FF is possible_

`git merge --squash bugfix` _# Performs a squash merge_

`git merge --abort` _# Aborts the merge_

### Viewing the merged branches

`git branch --merged` _# Shows the merged branches_

`git branch --no-merged` _# Shows the unmerged branches_

### Rebasing

`git rebase master` _# Changes the base of the current branch_

### Cherry picking

`git cherry-pick dad47ed` _# Applies the given commit on the current branch_

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
