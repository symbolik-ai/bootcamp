# 🚀 5-Day Bootcamp

From zero to hero with LangChain 🦜⛓

___
# 🌴 Day 1 - setup
Today will be slightly boring/frustrating (to be honest), but important. You got this! 🙌
At the end of the day you will run your first LangChain code! 🎉

1. Install [GitHub Desktop](https://desktop.github.com/) and create a [GitHub](https://github.com/) account.

2. Learn about Git if you're not familiar (important):
	+ [(YouTube) Git in 100 seconds](https://www.youtube.com/watch?v=hwP7WQkmECE)
	+ Video 1-4 on [(Sphere playlist) Git and GitHub for Poets](https://sphere.segefjord.space/tech/git)

3. Create a folder anywhere you'd like called `symbolik`. Personally I have a folder called `dev` in my ***user folder*** that I use for all development projects. I put `symbolik` into that one. All repositories from the Symbolik organization is then cloned into that folder.
4. Clone this repository to your `symbolik` folder: [(YouTube) Clone a repository with GitHub Desktop](https://www.youtube.com/watch?v=PoZNIbs_wx8).

### Python installation
Symbolik uses `pyenv` + `virtualenv` for managing python version and virtual environments at the same time. Don't worry if you're [not familiar with these terms](https://realpython.com/intro-to-pyenv/).

<br>

**  Mac:** [(Brew)](https://brew.sh/) → `brew install pyenv pyenv-virtualenv`

Add this code to your `~/.zshrc` (that's mac os default shells configuration file)
```
nano ~/.zshrc
```

```shell
# pyenv
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Restart your terminal.

Then `pyenv install 3.11.0` and create a virtual environment for this bootcamp:
```
pyenv virtualenv 3.11.0 symbolik-bootcamp
pyenv activate symbolik-bootcamp
```
<br>

**❖ Windows:** [if you already installed python previously](https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#python-pip), otherwise [install via PowerShell](https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#powershell). 
Then do `pyenv install 3.11.0` followed by `pyenv global 3.11.0`

***Copy*** the path returned from this command:
```
pyenv which python
```
(Should look something like `C:\Users\USER FOLDER\.pyenv-win ... \python.exe`)

Create a virtual environment for this bootcamp.
⚠️ Important: first `cd` into the `symbolik` folder from the terminal (for example if you're using PowerShell)
```
pip install virtualenv
virtualenv --python PASTE-PATH-HERE symbolik-bootcamp
.\symbolik-bootcamp\Scripts\activate
```

<br>

Every time you make a new terminal session, you will need to reactivate the `virtualenv` using:
**❖ Windows:** `.\symbolik-bootcamp\Scripts\activate`
**  Mac:** `pyenv activate symbolik-bootcamp`

### LangChain installation
With the `symbolik-bootcamp` activated, proceed to install LangChain using `pip`. Don't worry, you already have `pip` installed as it ships with your python installation from the previous step.

1. Make sure the `virtualenv (symbolik-bootcamp)` is activated and that you're `cd`'ed into the `symbolik` folder.
2. Use the official release and install all integrations.

https://python.langchain.com/docs/get_started/installation
<br>
### Your first code!
After cloning this repository at the beginning of the day, open the repo in `vscode` (open folder).
Install the [python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extensions.

