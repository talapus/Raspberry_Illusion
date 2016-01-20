How to use this project on windows:

1. Install chocolatey packages (choco)[https://chocolatey.org/]
1. Open a command window with Administrator privileges. In that window, install git with the command ``choco install -y git``
1. When that completes, open another command window. It doesn't need to have special privileges.
1. Navigate to your repositories directory and type the command ``git clone https://github.com/talapus/Raspberry_Illusion.git``

Some things to note

1. After installing choco and git, open your file manager and navigate to Program Files\Git and find the 'git-bash.exe' file. Double click it, then pin it to your toolbar. That's bash, and a small set of the common gnu tools. Tiny UNIX on your desktop!

Python

1. Install python with the command ``choco install -y python``

Real UNIX

1. If you want a real unix shell on windows, install virtualbox and vagrant
1. make a directory
1. Open the 'git-bash' terminal. Navigate into your Vagrant directory and type this command ``vagrant init ubuntu/trusty64`` to initialize it. You don't need to do this again unless you are creating a new box (which will have to be in another directory - one box per directory).
1. Start up the virtual machine with the command ``vagrant up``. It stays running until you ``vagrant halt``.
1. Now type the command ``vagrant ssh`` to log into your shiny new Ubuntu box.
