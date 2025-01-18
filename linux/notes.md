## welcome 

start with this 

`echo hello world`

prints hello world


*what is cli ?*


You'll often hear the terms "terminal", "shell", "command line", "CLI", and "command prompt" used interchangeably, but often they all refer to the same thing: a program that allows you to interact with your computer in a text-based way.

*what is GUI ?*

If you don't have a technical background, you're probably used to interacting with your phone or computer using a graphical user interface (GUI). When you use a mouse to click on fancy icons, buttons, and menus, you're using a GUI.



run this in terminal 

`whoami`


install wsl if you are using windows 

`wsl --install`

*what is Terminal ?*


As we talked about, the terms "shell", "CLI", and "terminal" are often used to refer to the same thing: a program for issuing text-based commands.

But to get pedantic, the "terminal" is just one specific part of that program.
 Historically, the word "terminal" meant a physical device that you could type commands into, essentially a keyboard and a screen.

*What Is a Shell?*

So if your terminal is just a program that lets you issue text-based commands and renders the output of those commands...

...What is the program that runs those commands???

That's a shell.

Shells do a lot of things, but their main job is to interpret the commands you type and execute them.


REPL
Shells are often referred to as "REPL"s. REPL stands for

Read
Eval (evaluate)
Print
Loop
This is a fancy way of saying that shells are programs that:

Read the commands you type
Evaluate those commands, usually by running other programs on your computer
Print the output of those commands
Give you a new prompt to type another command and repeat


`expr 123456 + 7890`


## Variables


If you're using Ubuntu on WSL, you're probably running a Bash shell.
If you're using macOS, you're probably running a Zsh shell.
If you're running full Linux, I pray you already know what you're using.
The point is that you're probably using Bash or Zsh, and for the purposes of this course, they're basically the same.

Both Bash and Zsh are shells, and they also happen to be powerful programming languages. 
They have variables, functions, loops, and more. That said, only crazy people write large programs in shell languages...
 shells are optimized for running other programs and writing small scripts, not for writing large applications.


`name="Lane"`
`echo $name`

prints Lane 


## History 

When you're working in a REPL, it's really helpful to be able to see the commands you've typed in the past.
 That way you can easily re-run them, or copy and paste them into a script. To print out the history of commands 
 you've typed in your shell, you can use the history command.

 `History`


# clear

you can use ctrl + l to clear the terminal 


### chapter 2 File system 


# What is a file system 

All the data stored on your computer is organized into files and direcories. Files and directories are all stored 
into a tree like structure  called file system. 

example -> 

root
├── dir
│   ├── dir
│   │   ├── file
│   │   └── file
│   └── dir
│       └── file
├── dir
│   ├── file
│   ├── dir
│   │   └── file
│   └── file
├── dir
│   ├── file
│   └── file
├── file
└── file


Directories (or "folders" on Windows) are just containers that hold files and other directories.
Files are just a dump of raw binary data: 1's and 0's. The bytes in a file can represent anything: text, images, videos, etc.

The filesystem tree starts with a single directory called the root directory. The root directory contains files and directories,
 which can contain more files and directories, and so on.

to check current directory 

`pwd`

# ABsolute vs Relative path 
we have mostly been dealing with the relative file paths that takes your current directory in your account. for example
let's say you have following directory structure in our filesystem 

vehicles
├── cars
│   ├── fords
│   │   ├── mustang.txt
│   │   └── focus.txt



when inside the top level of vehicles dir, the relative path to the mustang.txt is 

`cars/fords/mustang.txt`

however when we are inside the cars directory path to the mustang.txt  file just 

`fords/mustang.txt`


or when we are inside fords just 

`mustang.txt`


#  Absolute paths 

An absolute path is a path that starts at the root of the filesystem. On Unix-like systems (macOS/Linux), 
the root is denoted by a forward slash /. So, if the vehicles directory is in the filesystem root, the absolute path to the mustang.txt file is

/vehicles/cars/fords/mustang.txt


# Files
You're probably familiar with the concept of files from using a GUI like Windows Explorer or Finder.

At their core, files are just blobs of data. The raw bytes in a file can represent anything: text, images, videos, etc.

*The cat Command*
The cat command is used to view the contents of a file. It's short for "concatenate", which is a fancy way of saying 
"put things together". It can feel like a confusing name if you're using the cat command to view a single file,
but it makes more sense when you're using it to view multiple files at 


`cat file1.txt`

<!-- Concatenate the contents of multiple files and print them to the terminal -->

`cat file1.txt file2.txt`


*head and tail*
Sometimes you don't want to print everything in a file. Files can be really big after all.

*The head Command*
The head command prints the first n lines of a file, where n is a number you specify.

`head -n 10 file1.txt`

The tail command prints the last n lines of a file, where n is a number you specify.

`tail -n 10 file1.txt`

# More and less

The more and less commands let you view the contents of a file, one page (or line) at a time.
As the adage goes, less is more.

In the context of these commands, less is literally more. The less command does everything that the more command does
 but also has more features. As a general rule, you should use less instead of more.

You would only use more if you're on a system that doesn't have less installed.

# Touch 

The touch command updates the access and modification timestamps of a file. By default, if the specified file does not exist, touch will create an empty file with the given filename.
Because of this side-effect, you’ll often see this command used to quickly create new empty files.


`touch new_file.txt`

you can also craete multiple files at once by listing them 

`touch some_file.txt some_other_file.txt`


# Directories

As we mentioned before, a directory is just a location in a filesystem that can contain files and other directories. 
On some systems, directories are called "folders", but it's the same thing.


`mkdir my_directory`

# Move

The move command moves a file or directory from one location to another. You can use it to rename a 
file or to move it to a different directory altogether. Your working directory can't be the directory you're moving.


Renaming a file:

`mv some_file.txt some_other_name.txt`

Moving a file from the current directory to another nested directory:

`mv some_file.txt some_directory/some_file.txt`

Moving a file from the current directory, to the parent directory:

`mv some_file.txt ../some_file.txt`

If you don't want to rename the file and you're just moving it to a different directory, you can omit the filename:

`mv some_file.txt some_directory/`



# Remove 

The remove command deletes a file or empty directory:

`rm some_file.txt`

You can optionally add a -r flag to tell the rm command to delete a directory and all of its contents recursively.
 "Recursively" is just a fancy way of saying "do it again on all of the subdirectories and their contents".

`rm -r some_directory`




# copy 

The copy command does what you would (hopefully) expect: it copies a file from one location to another.


`cp source_file.txt destination/`

You can also copy a directory and all of its contents recursively by adding the -R flag:

`cp -R my_dir new_dir`


# Home 

In a Unix-like operating system, a user's home directory is the directory where their personal files are stored. 
It is also the directory that a user starts in when logging into the system.
recommend doing all of your development work in your home directory. For example, I like to create a workspace
directory in my home directory, and all my programming projects live in subdirectories there.


# Danger

Your home directory is where you want to spend most of your time. Many of the other directories on your machine are 
critical to the operating system or other programs. Be careful when working in other directories like /bin, /etc, /var, etc.


# ~ ALias

My home directory (on Mac) is located at /Users/wagslane. The ~ character is an alias for your home directory.
So when I want to go home, I don't have to type out cd /Users/wagslane, I can just type:

`cd ~`


## GREP 

you might be used to nice graphical interfaces that allow you to serach for text in files, usually with ctrl + f or cmd + f.
But what about when you are working on a terminal ?

As it turns out, once you're used to it, searching for text in files on a CLI can be much faster than using a GUI.

# The Grep Command 

The grep command allows you to search for text in files. It has a ton of capability, 
and we'll only be scratching the surface of its true power.

# Basic usage 

The most basic use for grep is to search for a string in a file. For example, if we wanted to search for the word "hello" in the file words.txt,
we could run:

`grep "hello" words.txt`

This will print out every line in words.txt that contains the word "hello". It's a case-sensitive search,
so it will only match "hello", not "Hello" or "HELLO".


#   other grep uses

> Case-Insensitive Search  `grep -i "error" file.txt`
> Search Recursively in Directories `grep -r "search_term" /path/to/directory`
> Display Line Numbers  `grep -n "error" file.txt`
> Show Only Matching Parts  `grep -o "error" file.txt`
> Use Regular Expressions `grep -E "pattern1|pattern2" file.txt`
> Count Matches  `grep -c "error" file.txt`
> Highlight Matches `grep --color "error" file.txt`
> Search for Whole Words `grep -w "error" file.txt`


# Find 

the find command is a powerful too for finding files and directories by name, not by their comments.

* Find a File by name 

Let's say you're looking for a file named hello.txt somewhere in your home directory. You can use the find command to search for exactly that title:Let's say you're looking for a file named hello.txt somewhere in your home directory.
You can use the find command to search for exactly that title: 

`find some_directory -name hello.txt`

* pattern search  

The find command can also search for files that match a pattern. For example,
if you wanted to find all files that end in .txt, you could run:

`find some_directory -name "*.txt"`

The * character is a wildcard that matches anything. If you're trying to find filenames that contain a specific word,
you can use the * character to match the rest of the filename:

`# Find all filenames that contain the word "chad"
find some_directory -name "*chad*"`


### Chapter 3 (Permission)

## users 

Unix-like systems (like the one you're using) support multiple users. Each user has their own home directory, their own files, and their own permissions.
If you're like most people these days, you're the only user on your machine. It used to be more common for multiple people
to share a single computer, or for multiple people to do their work on the same computer over a network.


# sudo  

The sudo keyword lets you run a command as a "superuser". It's short for "superuser do". To use it,
you'll need a password with superuser privileges, which you should already have if you're the only user of your machine.

**Note: sudo grants unrestricted access and can risk system damage if you don't know what you're doing.
All commands in this course are safe, but other commands should be reviewed before running with sudo.**


## Permissions 

In a Unix-like operating system, permissions control who can do what to which files and directories.
The permissions of an individual file or directory are visually represented as a 10-character string:


`drwxrwxrwx`


Let's break down each character. The first one just tells you whether you're looking at a file or a directory:

-: Regular file (e.g. -rwxrwxrwx)
d: Directory (e.g. drwxrwxrwx)
The next 9 characters are broken up into 3 sets of rwx and represent the permissions themselves for the "owner",
"group", and "others", in order. Each group of 3 represents the permissions for reading, writing, and executing, in order.
So, for example:

rwx: All permissions

rw-: Read and write, but not execute

r-x: Read and execute, but not write


* The first 3 characters are "owner" permissions. The "owner" is usually just the user who created the file or directory, but it can be manually changed.

* The next 3 characters are "group" permissions. Unix-like systems support groups of users and a file or directory can be assigned to a single group. To be honest, unless you're a system administrator, you won't often worry about groups.

* The last 3 characters are "others" permissions. This is everyone else

In my experience, when you're doing programming work on your own local machine, you mostly just care about the "owner"
permissions because that's usually you. Here are some full examples:

*-rwxrwxrwx: A file where everyone can do everything*
*-rwxr-xr-x: A file where everyone can read and execute, but only the owner can write*
*drwxr-xr-x: A directory where everyone can read (ls the contents) and execute (cd into it), but only the owner can write (modify the contents)*
*drwx------: A directory where only the owner can read, write and execute*



## Changing permissions 


The chmod command lets you change the permissions of a file or directory. It's short for "change mode" 
(I wish it was called "change permissions", but alas).

`chmod -R u=rwx,g=,o= DIRECTORY`


## Executables

You're familiar with the idea of reading and writing data into files. But what about executing them? Executable files are just files 
where the data stored inside is a program that you can run on your computer.

Files with a .sh extension are shell scripts. They're just text files that contain shell commands. 
You can run a file in your shell by typing its filepath:

`mydir/program.sh`


Interestingly, if the program is in the current directory (in this example, the mydir directory),
you need to prefix it with ./ to run it:


`./program.sh`


As far as file paths go, ./program.sh and program.sh are the same. The dot (.) is an alias for the current directory.
We need the prefix when running executables so that the shell knows we're trying to run a file from a file path,
not an installed command like ls, mkdir, chmod, etc.

# Root user 

The "root" user is a superuser. It has access to everything on the system and can do anything. 
When you use the sudo command, you're running as the root user (as long as your system hasn't been configured differently).

The sudo keyword is convenient because it quickly gives you elevated permissions to run a single command.


However, it can also be dangerous because it gives you access to everything. If you run a command with sudo that 
you don't understand, you could do serious damage to your system.

For example, rm with the r and f flags run on the root directory (/), will delete all the files on your system. Don't do that.
The r flag is for "recursive" (delete everything inside) and the f flag is for "force". Most systems will prevent you from doing this,
but if you run it with sudo, you've just turned your computer into a very expensive paperweight.

Some modern systems will actually prevent you from deleting everything by default as a safeguard unless you use 
--no-preserve-root, but it's still a very bad idea.

### chapter 4 (Programs)

## compiled vs interpreted 

A program is just a set of instructions that a computer can execute, and an "executable" is just a file that contains a program.
The words "program" and "executable" are often used interchangeably. Broadly speaking, there are two types of programs:

> Compiled programs
> Interpreted programs


# compiled programs 

A compiled program is a program that has been converted from human-readable source code into machine code (binary).
Machine code is a set of instructions that a computer can execute directly: your computer's CPU is hardware that's
been designed to execute machine code.

# Interpreted programs 

An interpreted program is a program that is executed by another program. The program that executes the interpreted program is called an interpreter.
 The interpreter reads the source code of the interpreted program and executes it.
Programming languages like Python, Ruby, and JavaScript, are typically interpreted as they run, which means your computer needs to have the interpreter installed to run the program.
Another example is the .sh shell script files we talked about. Those are interpreted by the shell program.


## Shebang 

As we talked about before, you can run any executable file by typing its file path into your shell. For example:

`bin/genids.sh`

That works out-of-the-box for files that are compiled executables. But what about scripts that need to be 
interpreted by another program? The computer needs to be told what program to use to interpret the file.

A "shebang" is a special line at the top of a script that tells your shell which program to use to execute the file.


The format of a shebang is:

`#! interpreter [optional-arg]`

For example, if your script is a Python script and you want to use Python 3, your shebang might look like this:

`!/usr/bin/python3`


# Bourne Shell 


As we talked about before:

- If you're using Ubuntu on WSL, you're probably running a Bash shell.
- If you're using macOS, you're probably running a Zsh shell.
- If you're running a raw Linux installation, I pray you already know what you're using.

To get hand-wavy about it, I want to explain the difference between the 3 shells you're likely to encounter:

- sh: The Bourne shell. This is the original Unix shell and is POSIX-compliant. It's very basic and doesn't have many quality-of-life features.
- bash: The Bourne Again shell. This is the most popular shell on Linux. It builds on sh, but also has a lot of extra features.
- zsh: The Z shell. This is the most popular shell on macOS. Like bash, it does what sh can do, but also has a lot of extra features.

Both zsh and bash are "sh-compatible" shells, meaning they can run .sh scripts, but they also have extra features that 
generally make them more pleasant to use. For your purposes, the differences between zsh and bash are not super significant.
Everything we do in this course will work in both shells.


## Shell Configuration 


Bash and Zsh both have configuration files that run automatically each time you start a new shell session. 
These files are used to set up your shell environment. They can be used to set up aliases, functions, and environment variables.

These files are located in your home directory (~) and are hidden by default. The ls command has a -a flag that will show hidden files:


`ls -a ~`

> If you're using Bash, .bashrc is probably the file you want to edit.
> If you're using Zsh, .zshrc is probably the file you want to edit or create if it doesn't yet exist.


# ENVIROMENT Variables

We talked about how you can create and use local variables in your shell:

`name="Lane" echo $name # Lane`


There is another type of variable called an environment variable. They are available to all programs that you run in your shell.

You can view all of the environment variables that are currently set in your shell with the env command.

To set a variable in your shell, use the export command:


`export NAME="Lane"`

You can then use the variable in your shell, just as before:

`echo $NAME # Lane`

The interesting part is that programs and scripts you run in your shell can also use that variable:

For example, we can create a file called introduce.sh with the following contents:

`#!/bin/sh echo "Hi I'm $NAME"`

then we run it  

`chmod +x ./introduce.sh

./introduce.sh # Hi I'm Lane`


## PATH 

This is one of the most important lessons in this entire course! Listen up.

There are environment variables that are sort of "built-in" to your shell.
By "built-in" I just mean that different programs and parts of your system know about them and use them.
The PATH variable is one of those.


# Why do we care about the Path ?

If it weren't for the PATH, you'd have to remember the filesystem path of every executable you wanted to run in your shell.
Instead of just running ls, you'd have to run /bin/ls (or whatever the location of the ls executable is on your system). That's not very convenient.

The PATH variable is a list of directories that your shell will look into when you try to run a command.
If you type ls, your shell will look in each directory listed in your PATH variable for an executable called ls. 
If it finds one, it will just run it. If it doesn't, it will give you a error like: "command not found".

# What is path Variables ?

Take a look at your current PATH variable:

`echo $PATH`

### Chapter(5) Input/ Output 


## MAN 

The man command is short for "manual". It's a program that displays the manual for other programs.

I know that manuals and documentation can feel intimidating, heck, that's why there are courses like this one to give you a gentler introduction.
That said, manuals and documentation will become more useful to you as you become a more experienced developer.
They're not as scary as they seem when you actually take the time to read them

# USing man 

The man command will only work for programs that it has a manual for, but most built-in commands and Unix programs are supported. You just pass the name of the command as an argument.
The most intuitive place to start, of course, is reading the manual's manual:

*open the man pages for the 'man' command

`man man`

# searching 

Most people don't just read man pages for fun. More often, the manual is used as a reference to quickly look up usage or special flags.

You can search for text in the manual by pressing the / key and typing your search, then pressing enter.
Let's try to look up what the -r flag does for the ls command:

` man ls
# type '/-r' to start searching

# press 'n' to jump to the next result

# press 'N' to go back if you went too far     
`


## Flags 


As you've already seen in this course, some commands accept flags. Flags are options that you can pass to a command 
to change its behavior.

For example, the ls command can take a -l flag to show a "long" listing of files:

`ls -l`

Or the -a flag to show "all" files, including hidden files:

`ls -a`

#   conventions 

Whether or not a command takes flags, and what those flags are, is up to the developer of the command. That said there are some common conventions:

Single-character flags are prefixed with a single dash (.e.g -a)
Multi-character flags are prefixed with two dashes (e.g. --help)
Sometimes the same flag can be used with a single dash or two dashes (e.g. -h or --help)

# positional arguments

Programming languages have functions, and functions take arguments.
For example, this Python function takes two arguments: xp and level:


`def print_player(xp, level):
    print("Player has", xp, "xp and is level", level)`

It can then be called with two arguments:

`print_player(100, 2)`


In a shell, commands (programs) can also take arguments. For example, the cd command takes a single argument
(the directory to change to):


`cd /home/wagslane`

Other commands might take multiple arguments. For example, the mv command takes two arguments: the file to move,
and the destination to move it to:

`mv file.txt newfile.txt`


## Help 

By convention, most production-ready CLI tools have a "help" option that prints information about how to use the tool. It's usually accessed with one of the following:

--help (flag)
-h (flag)
help (first positional argument)
The "help" output is often easier to parse than a full man page. It's usually more of a quick start guide than a full manual.

# Standard output 
You might not even know it yet, but you're already a pro at using standard output. You've been using it since you started the first exercise in this course.

"Standard Output", usually called "standard out" or "stdout", is the default place where programs print their output. It's just a stream of data that prints to your terminal, but we'll talk later about how it can be redirected to other places.

All programming languages have a simple way to print to stdout. In Python, it's the print function:

# Standard Error 

"Standard Error", usually called "stderr", is a data stream just like standard output, but is intended to be used for error messages.

It's a separate stream so that you can redirect it to a different place if need be, but by default, it prints to your terminal just like stdout.

# Redirecting stream 

You can redirect stdout and stderr to different places using the > and 2> operators. > redirects stdout, and 2> redirects stderr.

`echo "Hello world" > hello.txt
cat hello.txt`


# standard In  

If there's a standard output, there must be a standard input, right?

"Standard Input", usually called "standard in" or "stdin", is the default place where programs read their input.
It's just a stream of data that programs can read from as they run.

All major programming languages provide a simple way to read from stdin. In Python, it's the input function:

`name = input("What is your name? ")
print("Hello,", name)`


## piping

One of the most beautiful things about the shell is that you can pipe the output of one program into the input of another program.
With this one simple concept, you can run incredibly powerful automation tasks.

# pipe

The pipe operator is |. It's the character that looks like a vertical line. It's usually on the same key as the backslash (\) above the enter key.
The pipe operator takes the stdout of the program on the left and "pipes" it into the stdin of the program on the right.

`echo "Have you heard the tragedy of Darth Plagueis the Wise?" | wc -w` # this outputs 10 


## Interrupt 

Sometimes a program will get stuck and you'll want to stop it. Common reasons for this are:

You made a typo in the command and it's not doing what you want
It's trying to access the internet but you're not connected
It's processing too much data and you don't want to wait for it to finish
There is a bug in the program causing it to hang

In these cases, you can stop the program by pressing ctrl + c. This sends a "SIGINT" signal to the program, which tells it to stop.


## kill 

Sometimes a program is in such a bad state (or is so malicious) that it doesn't respond to the SIGINT, in which case the best option is to use another
shell session (new terminal window) to manually kill the program.

`KILL PID` 

PID stands for "process ID". Every process that's running on your machine has a unique ID. The ps, "process status"
command can be used to list the processes running on your machine, and their IDs:


`ps aux`

The "aux" options just mean "show all processes, including those owned by other users, and show extra information about each process".


### Package managers 


Package Managers
A package manager is a software tool that helps you install other software. Its primary functions include:

Downloading software from official sources
Installing software
Updating software
Removing software
Managing dependencies
As a developer, you'll frequently use package managers to get access to the software you need to get your work done.

# APT 

APT, or "Advanced Package Tool", is the primary package manager for Ubuntu. To be fair, you can use other package managers 
on Ubuntu, but APT is the default and most common.

If you're on WSL and Ubuntu, you'll be using APT. If you're on another Linux setup, I pray you already know what package
manager you're using. If you're on WSL or Ubuntu, check to make sure you have APT installed by running the following command:


