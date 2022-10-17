# CLI(Command Line Interface)-2
---
### Standard Output
- By default, standard output is screen.
- "**>**" : You can redirect output to create and save the output in a file
-  "**cat**" : Displays the content of a text file.
-  "**>>**" : Appends output to an extising file (if it already exitsts),
or create and write to a new file if it doesn’t exist.
### Standard Input
- By default, standard input is from keyboard.
- "**<**" : You can redirecct input from a file.
- "**<**" and "**>**" : You cna mix both in a single line.
### Pipelines
- "**|**" : Feeds output of previous command to input of next command.
### Expansion
- Special characters expand its meaning when given to shell commands.
### Backslash
- Can be used to ignore line change in command (“enter”),
to enter a long command in multiple lines.
### Permissions
- Linux is a multi-user system.
- Files and directories have a permission assigned differently to owner / group / others.
![ex1](https://linuxcommand.org/images/file_permissions.png)
- Changing : “**chmod**”
 -Change the permission of a file “word.txt” that only the owner (you) can read and write,
but all the others (including others in the group) can only read it. No execution is needed
for all users.