This guide covers how to set up your computer to be able to write code!

# Operating System

If you use a Linux distribution, you're in luck, your OS is open-source and the whole
neuroscience software landscape is built around it!

## MacOS

Completely out of luck! You're also a UNIX system so technically you could do everything a
Linux distribution can, but Apple has  lots of proprietary hardware and software
components and subtle changes will usually prevent you from running things out of the box.

However, you can install [Docker](https://docs.docker.com/desktop/mac/install/), and run
things in a Linux container!

## Windows

Also out of luck, but you get a fancier integration than Docker using
[WSL](https://docs.microsoft.com/en-us/windows/wsl/install).

# IDEs/editors

Integrated Development Environments integrate the code editor with the development
environment and help you run and analyse code while you write it.

Get yourself one of the following:

* Atom (https://atom.io/ free lean editor easily extendable by installing packages)
* VSCode (https://code.visualstudio.com/ free IDE, also extendable by packages but comes with more fleshed out interface by default)
* PyCharm (proprietary JetBrains IDE, see if you have a license)

## Software stack

A software stack is the collection of tools you'll need to run your neuroscience
experiments. In our laboratory this comprises:

* Python
* NEURON
* NEST
* MPI
* BSB
