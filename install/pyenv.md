# Install instructions

1. Use the automatic installer to locally obtain `pyenv`:

```
curl https://pyenv.run | bash
```

2. Install the build dependencies to be able to build local Python binaries:

```
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

3. Register `pyenv` in your shell profile:

```
sed -Ei -e '/^([^#]|$)/ {a \
export PYENV_ROOT="$HOME/.pyenv"
a \
export PATH="$PYENV_ROOT/bin:$PATH"
a \
' -e ':a' -e '$!{n;ba};}' ~/.profile
echo 'eval "$(pyenv init --path)"' >>~/.profile

echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'export PS1="($(pyenv version-name)) "$PS1' >> ~/.bashrc
```

4. Close and reopen your WSL window, installation should be complete.


# Usage guide

`pyenv` installs separate versions of Python. To begin using it, install 1 or more versions:

```
pyenv install 3.9.12
```

You can now set the `global` version, which will be used everywhere:

```
pyenv global 3.9.12
```

If you use the `python`, or `pip`, commands now, they will refer to your pyenv's Python 3.9.10.

You can also create project specific virtual environments:

```
pyenv virtualenv my-project
```

And then use those locally in the project folder and its subdirectories:

```
mkdir my-project-folder
cd my-project-folder
pyenv local my-project
```

You can check which version is active in the current directory with `pyenv version` or which
versions exist with `pyenv versions`:

```
robin@TNG2019:~$ pyenv version
3.9.1 (set by /home/robin/.pyenv/version)

robin@TNG2019:~$ pyenv versions
  system
  2.7.18
  2.7.18/envs/nrn-dev2
  3.10.0
  3.6.9
  3.8.6
  3.8.6/envs/bwpy
  3.9.0
* 3.9.1 (set by /home/robin/.pyenv/version)
  3.9.1/envs/arb-cat
  3.9.1/envs/arb-cat-new
```
