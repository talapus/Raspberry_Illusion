How to use this project on windows:

1. Install chocolatey packages https://chocolatey.org/
1. Open a command window with Administrator privileges. In that window, install git with the following command
1. ``> choco install -y git``
1. When that completes, open another command window. It doesn't need to have special privileges.
1. Navigate to your repositories directory and clone the repository with the command 
1. ``> git clone https://github.com/talapus/Raspberry_Illusion.git``

Some things to note

1. After installing choco and git, open your file manager and navigate to Program Files\Git and find the 'git-bash.exe' file. 
2. Double click it, then pin the running application to your toolbar. 
3. That's bash, and the core gnu tools. Tiny UNIX on your desktop! Almost anyway. Depending on how you use it, you'll find issues around the terminal type, and windows filesystem. As long as you don't want to change the shell, use really long file names, or install anything new, this should work fine. 
4. If the limited nature of this shell becomes an obstacle and you want to stick with windows, the next level is to build a command line development image in virtualbox and vagrant then: ``$ vagrant init ubuntu/trusty32`` then ``$ vagrant up`` and then `$ `vagrant ssh`` in a git-bash/MINGW64 window. Use ``$ vagrant halt`` to stop the VM when you are done. 

Python

1. ``> choco install -y python``

Atom Editor

1. I highly recommend this free editor for working on your python projects. Install it with ``choco install -y atom``
1. It's a full windows GUI application, like a beefed up notepad.
1. It has built-in syntax error checkers and color themes which are both useful time savers. 
