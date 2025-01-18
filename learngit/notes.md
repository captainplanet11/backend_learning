<!-- linus the GOAT  -->
<!-- boot.dev -> https://www.boot.dev/lessons/41af0d0d-9805-4dd0-b7f8-6526a6d42ec8 -->
### chapter1.1 

**setup** 

download git and check with git --version


**RFTM** 

One of the best parts of using Git is that all the documentation is fantastic 

how to read git docs - > git help 

## PORCELAIN AND PLUMBING 

In Git commands are divided into high level(procelain) commands and lowlevel (plumbing) commands. The procelain commands 
are the ones that you will  use most often as a developer to interact with your code. some procelain commands are 

- git status 
- git add
- git commit
- git push
- git pull
- git log
  

examples of plumbing commands

- git apply
- git commit-tree
- git hash-object

we will focus on the high-level commands because that's what you use 99% of 
the  time as a developer, but we will dipo down into the low-level commands ocassionally 
to really understand how git works


**Quick config**

we need to configure git to contain your information. whenever code changes, Git tracks who made change. to
ensure you get proper credit for the code you wrote, you need to set you name and email 

Git comes with a configuration both at global level and repo project level. Most of the time 
you will just use global config.

# check if your user.name and user.email are already set

`git config --get user.name`
`git config --get user.email`

# if they are not set i recommend using Github username and passwordd

`git config --add --global user.name "githubusername"`
`git config --add --global user.email "user@email.com"`

finally lets set a default branch 

`git config --global init.defaultBranch master`

# Make sure it worked
`cat ~/.gitconfig`



### chapter 1.2 Repositories

# config 

The very first step of any project is to create a repo. A Git Repository or "Repo" represents a single
project. you will typically have one repo for each project you work on.
A repo is essentially just a directory that contains a project. The only difference is that it also contains a hidden .git 
directory. That hidden directory is where Git stores all of its internal tracking and versioning for the project.

# Webflyx

In this course, we'll be managing content for "Webflyx", an imaginary self-hosted video streaming application. Webflyx serves 
content directly from a Git repo!.

# Assingment
Navigate to somewhere on your filesystem where you'd like to store your project. Once you're there create a new directory
called Webflyx and cd into it.

`mkdir webflyx
cd webflyx`

once inside the directory, create a mew Git repo

`git init`

the ls command does not show hidden files and directories. you can use

`ls -a`

# status

A file can be in one of the several states in a Git repo. 

- Untracked: Not being tracked by git
- staged: Marked for inclusion in the next commit
- committed: Saved to repo's history 


`git status`  command shows you the current state of your project.

# create a file in the root of your webflyx dir called contents.md and add the following text 
`# contents`

save the file then run 
`git status`

# Staging 

The contents.md file is created but we see saw it is untracked. we need to stage it (add it to the index) with git add 
command before commiting it later.

without staging, every file in the repo would be included in every commit, but that's not often you want.

`git add <path-to-file> |pattern `

1. Now add contents.md to the statging area
2. Run git status again 


# commit  
After staging a file, we can commit it.

A commit is a sanpshot of the repository at a given point in time. It's a way to save the state of the repo, and its how Git keeps
tracks of changes to the project. A commit comes with  a message that describes that changes made in commit.

`git commit -m"your message here`

commit the contents.md file with the message A: add contents.md

Run git status again, and you should see that the file is no longer staged

# GIT LOG 

A Git repo is long list of commits, where each commit represents the full state of the repo at a given time.
The git log commands show a history of the commits in a repo.

`git log`




### chapter 1.3 Internals 

My latest git commit hash was: 15e6919d78a71c55c81bdb58e997bf33e076901a

you may have noticed that even though different people may have same contents in repo, they have different commit hashes.
while commit hashes are dreived from their content changes, there are some other stuff that affects the end hash

for example:

- The commit message 
- the author's name and email
- the date and time 
- Parent(previous) commit hashes

All this to say that hashes are almost always unique, and because they're generated automatically for you,
you don't need to worry too much about what goes into them right now.


**NOTE = SHA**

# THE PLUMBING 

so far we've been using Git in a "procelain" manner. But to state our insatiable curiosity, let's take a lok at some plumbing.

All the data in the git repo is stored directly in the hidden .git directory. That includes all the commits, branches, tags, etc.


# THE OBJECT FILE 

.git is just a folder

try cat into the folder

`cat ./git/objects/15/e6919d78a71c55c81bdb58e997bf33e076901a`

i got -> x□□M
□0@□□s□□$□□QAJ□2&Q&□_□□□[|/□R□□□%gJ□g□□-H□f□3□□<[□
□B왆Y□^߲□¹;□$□0□□□□u□□w-□□.□□□□#mɍ□□□j□□g,□Bq□Z□T□□JT?□␦?□

what you will recieve is a mess. The contents have been compressed to raw bytes! Let's try again with xxd 

00000000: 7801 a5cd 4d0a 8330 1040 e1ae 738a d917  x...M..0.@..s...
00000010: 2493 9f51 414a af32 2651 0326 111d ef5f  $..QAJ.2&Q.&..._
00000020: efd0 ed5b 7c2f b452 b200 8eee 2567 4ae0  ...[|/.R....%gJ.
00000030: 6783 d12d 48ec 66dd 3385 983c 5be3 0c0e  g..-H.f.3..<[...
00000040: fd42 ec99 8659 935e 14df b2b5 1302 1fc2  .B...Y.^........
00000050: b91e 3bd7 2488 3095 1cb6 fbca 75dd fc77  ..;.$.0.....u..w
00000060: 2d9c f72e b4f2 01ec ad23 6dc9 8df0 d6de  -........#m.....
00000070: 6af5 d467 2ce9 0f42 718c 105a 9554 e5ea  j..g,..Bq..Z.T..
00000080: 4a54 3fbf 1a3f f9                        JT?..?.


so in your commits there is a tree which is like a directory  tree has a blob. 

A -
    ------- tree 
                 --------- blob 
                                -------- contents.md 



# TREES AND BLOBS

> tree: git's way of storing a directory 
> blob: git's way of stpring a file 


# Storing data 

Git stores an entire snapshot of files on a pre-commited level. This was a surprise to me! 
I always assumed each commit only stored the changes made in that commit.

**OPTIMIZATION**

While it's true that git stores an entire snapsots, it does have some performance optimizations so that your .git 
does not get too unbearably large.

* Git comresses and packs files to store them efficiently
* Git deduplicates files that are the same across different commits. if a file does not change between commits, Git 
 will only store it once.


blob - > d29facf3a9f003c38489cb324cfc9a6189b6b7f5 


# GET

We have used --list to see all the configuration values, but the --get flag is useful for getting a single value.

`git config --get <key>`

keys are in the format <section>,<keyname>
for example 
* user.name
* webflyx.ceo 

example 
`git config --get webflyx.valuation`


# unset

the --unset flag is used to remove a configuration value.

`git config --unset <key>`


# remove section 

`git config --remove-section section`


## BRANCH 
#   What is a branch

A Git branch allows you to keep track of different changes separately.
For example, let's say you have a big web project and you want to experiment with changing the color scheme.
Instead of changing the entire project directly.

Branch is jsut a pointer to a commit, they are lightweight and "cheap" resource wise to create. When you create 10 branches, you are not
creating 10 copies of your project.


# Default branch 

We have been using Git's default branch master branch. Intrestingly Github recently changed its master branch form master to main 
As a general rule use main as your default branch 

How to rename a branch 

`git branch -m oldname newname`

# visualizing branch

text to represent branches

A-B-C main 

means a branch called main with 3 commits. C is the most recent commit, B is the previous commit, and A is the commit before that.
To represent multiple branch

      D- E other_branch
    /
A- B- C main


# New Branch

`git branch my new branch`

switch -c switches to new branch

`git switch -c my new branch`

one cool thing both branch points to the same thing right 
to prove check this 

`cat .git/refs/heads/add_classics`

this gives you -> 002e935019c3f8c62778b790a272877f1734c775

`cat .git/refs/heads/main`

this also gives -> 002e935019c3f8c62778b790a272877f1734c775


we will use the add_classics branch to add a commit to project without affecting the mian branch

As you know, git log shows you the history of commits in your repo. There are a few flags I like to use from time to time to make the output easier to read.

The first is --decorate. It can be one of:

short (the default)
full (shows the full ref name)
no (no decoration)
Run git log --decorate=full. You should see that instead of just using your branch name, it will show the full ref name. A ref is just a pointer to a commit. All branches are refs, but not all refs are branches.

Run git log --decorate=no. You should see that the branch names are no longer shown at all.

The second is --oneline. This flag will show you a more compact view of the log. I use this one all the time, it just makes it so much easier to see what's going on.



`git log --oneline`


# Merge 

What's the point of having multiple branches?" you might ask. They're most often used to safely make changes without
affecting your (or your team's) primary branch. However, once you're happy with your changes, 
you'll want to merge them back into the main branch so that they make their way into the final product.

# merge commits 

Let's say we start with this:


A - B - C    main
   \
    D - E    vimchadsonly

And we merge vimchadsonly into main by running this while on main:

`git merge vimchadsonly`


The merge will:

> Find the "merge base" commit, or "best common ancestor" of the two branches. In this case, A.
> Replays the changes from main, starting from the best common ancestor, into a new commit.
> Replays the changes from vimchadsonly onto main, starting from the best common ancestor.
> Records the result as a new commit, in our case, F.
> F is special because it has two parents, C and E.

After merge 

A - B - C - F    main
   \     /
    D - E        vimchadsonly


run this after the merge to see check the graph 

`git log --oneline --decorate --graph --parents`


# Merge Log


Your output from git log --oneline --decorate --graph --parents (aside from the hashes) should look something like:


*   89629a9 d234104 b8dfd64 (HEAD -> main) F: Merge branch 'add_classics'
|\
| * b8dfd64 fba0999 (tag: 5.8, add_classics) D: add classics
* | d234104 fba0999 (tag: 6.1) E: update contents
|/
* fba0999 1381199 (tag: 3.8, origin/master, origin/main, master) C: add quotes
* 1381199 a21228f (tag: 3.7) B: add titles.md
* a21228f A: add contents.md



Each asterisk * represents a commit in the repository. There are multiple commit hashes on each line because the --parents flag logs the parent hash(es) as well.

The first line, with these three hashes: 89629a9 d234104 b8dfd64 is our recent merge commit. The first hash, 89629a9 is the merge commit's hash, and the other two are the parent commits.
The next section is a visual representation of the branch structure. It shows the commits on the add_classics branch and the main branch before the merge. Notice that they both share a common parent.
The next three lines are just "normal" commits, each pointing to their parent.
The last line is the initial commit and therefore has no parent.


# Fast Forward Merge

The simplest type of merge is a fast-forward merge. Let's say we start with this:

      C     delete_vscode
     /
A - B       main


And we run this while on main:

`git merge delete_vscode`

Because delete_vscode has all the commits that main has, Git automatically does a fast-forward merge. It just moves the pointer of the "base" branch to the tip of the "feature" branch:

            delete_vscode
A - B - C   main


Notice that with a fast-forward merge, no merge commit is created.

This is a common workflow when working with Git on a team of developers:

Create a branch for a new change
Make the change
Merge the branch back into main (or whatever branch your team dubs the "default" branch)
Remove the branch
Repeat

# Rebase


"Rebase vs Merge" is one of the most hotly debated topics in the Git world. A lot of the discussions 
you'll see online come down to the fact that many developers (yes, even professionals) 
don't understand the purpose of rebase and use it incorrectly, causing a bunch of Git havoc,
and then blame the rebase command.


# Visualizing Rebase

Say we have this commit history:

A - B - C    main
   \
    D - E    feature_branch



We're working on feature_branch, and want to bring in the changes our team added to main so we're not working with a stale branch.
We could merge main into feature_branch, but that would create an additional merge commit.
Rebase avoids a merge commit by replaying the commits from feature_branch on top of main.
After a rebase, the history will look like this:


A - B - C         main
         \
          D - E   feature_branch


# Run rebase 


To use rebase to bring changes from main onto a current branch 
(let's pretend we're on one called jdsl), we would run this while on the jdsl branch:

`git rebase main`


This will do the following:

Checkout the latest commit from main into a temporary location
Replay each commit from jdsl one at a time onto this temporary location
Update the jdsl branch to point to the last replayed commit in the temporary location, making this the new permanent jdsl.
The rebase does not affect the main branch; jdsl now includes all changes from main.


# When to rebase 

git rebase and git merge are different tools.

An advantage of merge is that it preserves the true history of the project. It shows when branches were merged and where. One disadvantage is that it can create a lot of merge commits, which can make the history harder to read and understand.

A linear history is generally easier to read, understand, and work with. Some teams enforce the usage of one or the other on their main branch, but generally speaking, you'll be able to do whatever you want with your own branches.



### Reset 
# undoing changes


One of the major benefits of using Git is the ability to undo changes. There are a lot of different ways to do this, but first, we'll start by going back in the commit history without discarding changes.


# Git Reset soft 

The git reset command can be used to undo the last commit(s) or any changes in the index (staged but not committed changes) and the worktree (unstaged and not committed changes).


`git reset --soft COMMITHASH`

The --soft option is useful if you just want to go back to a previous commit, but keep all of your changes. 
Committed changes will be uncommitted and staged, while uncommitted changes will remain staged or unstaged as before.


# Git reset hard 

In the last lesson, we undid a commit but kept the changes. We don't want to keep the changes to titles.md, here's how to reset those changes.

`git reset --hard COMMITHASH`

# Danger 

I want to stress how dangerous this command can be. If you were to simply delete a committed file, it would be trivially easy to recover because it is tracked in Git. However, if you used git reset --hard to undo committing that file, it would be deleted for good.

Always be careful when using git reset --hard. It's a powerful tool, but it's also a dangerous one.

If you want to reset back to a specific commit, you can use the git reset --hard command and provide a commit hash. For example:

`git reset --hard a1b2c3d`


### Git Remote 

Often our frenemies (read: coworkers) make code changes that we need to begrudgingly accept into our pristine bug-free repos. /s

This is where the "distributed" in "distributed version control system" comes from. We can have "remotes", which are just external repos with mostly the same Git history as our local repo.

When it comes to Git (the CLI tool), there really isn't a "central" repo. GitHub is just someone else's repo. Only by convention and convenience have we, as developers, started to use GitHub as a "source of truth" for our code.



# Adding a remote

`git remote add <name> <uri>`

# Fetch 

Adding a remote to our Git repo does not mean that we automagically have all the contents of the remote. First, we need to fetch the contents (but not yet!).


`git fetch`


This downloads copies of all the contents of the .git/objects directory (and other book-keeping information) from the remote repository into your current one.

# Not fetched 

Just because we fetched all of the metadata from the remote webflyx repo doesn't mean we have all of the files.

# Log remote 

The git log command isn't only useful for your local repo. You can log the commits of a remote repo as well!

`git log remote/branch_name`

# Merge
Just as we merged branches within a single local repo, we can also merge branches between local and remote repos.

`git merge remote/branch`

For example, if you wanted to merge the primeagen branch of the remote origin into your local main branch, you would run this inside the local repo while on the main branch:

`git merge origin/primeagen`


# Github repo 

Just like we created a webflyx-local repo and used webflyx as a remote,
 GitHub makes it easy to create "remote" repos that are hosted on their servers.

`git remote add origin https`

# Git push 

`git push origin main`

or 

`git push origin <localbranch>:<remotebranch>`


# pull 

Fetching is nice, but most of the time we want the actual file changes from a remote repo, not just the metadata.

Command Syntax
git pull [<remote>/<branch>]

The [...] syntax means that the bracketed remote and branch are optional. If you execute git pull without anything specified it will pull your current branch from the remote repo.


# pull requests

On GitHub, a pull request is a way to propose changes, typically to the rest of your team, or to the maintainer of a project you're contributing to.

Pull requests allow team members to see what changes are being proposed and to discuss them before they are merged into the main codebase.

# Merge Pull Request

In a typical team workflow, you would ask a team mate to review your pull request. If they approve of the changes, they would approve the pull request, and you'd be clear to merge.

We're the dictators of our own repo however, so no need to wait for approval!


### GItignore 


As you've seen, it's pretty normal to use the following workflow from the top level of your repo:

git add .
git commit -m "some message here"
git push origin main


A problem arises when we want to put files in our project's directory, but we don't want to track them with Git. A .gitignore file solves this. For example, if you work with Python, you probably want to ignore automatically generated files like .pyc and __pycache__. If you are building a server, you probably want to ignore .env files that might hold private keys. If you (I'm sorry) work with JavaScript, you might want to ignore the node_modules directory.


Here's an example .gitignore file, which exists at the root of a repo:

`node_modules`


This will ignore every path containing node_modules as a "section" (directory name or file name). It ignores:

> node_modules/code.js
> src/node_modules/code.js
> src/node_modules
> It does not ignore:

> src/node_modules_2/code.js
> env/node_modules_3


