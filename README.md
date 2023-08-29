# 🚀 5-Day Bootcamp

From zero to hero with LangChain 🦜⛓

___
# 🌴 Day 1 - setup
Today will be slightly boring/frustrating (to be honest), but important. You got this! 🙌
At the end of the day you will run your first LangChain code! 🎉

1. Install [GitHub Desktop](https://desktop.github.com/) and create a [GitHub](https://github.com/) account.

2. Learn about Git if you're not familiar (important):
	- [(YouTube) Git in 100 seconds](https://www.youtube.com/watch?v=hwP7WQkmECE)
	- Video 1-4 on [(Sphere playlist) Git and GitHub for Poets](https://sphere.segefjord.space/tech/git)

3. Create a folder anywhere you'd like called `symbolik`. Personally I have a folder called `dev` in my ***user folder*** that I use for all development projects. I put `symbolik` into that one. All repositories from the Symbolik organization is then cloned into `dev/symbolik`.
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
- **❖ Windows:** `.\symbolik-bootcamp\Scripts\activate`
- **  Mac:** `pyenv activate symbolik-bootcamp`

<br>
<br>

### LangChain installation
With the `symbolik-bootcamp` activated, proceed to install LangChain using `pip`. Don't worry, you already have `pip` installed as it ships with your python installation from the previous step.

1. Make sure the `virtualenv (symbolik-bootcamp)` is activated and that you're `cd`'ed into the `symbolik` folder.
2. Use the official release and install just the bare minimum requirements.

https://python.langchain.com/docs/get_started/installation
<br>

### Your first code!
After cloning this repository at the beginning of the day, open the repo in `vscode` (open folder).
Install the [python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extensions.

1. open `./Day 1/quickstart.py`
2. <kbd>shift</kbd>+<kbd>cmd</kbd>+<kbd>P</kbd> to open command palette, search for 'select interpreter' (python). Select `symbolik-bootcamp`.
3. Duplicate the `example.env` file and rename to just `.env`
4. Obtain an API key from OpenAI: [guide](https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt)
5. Paste the key in the new `.env` file
6. Install [python-dotenv](https://pypi.org/project/python-dotenv/) to store the API key safely
	- [(YouTube) About .env files](https://www.youtube.com/watch?v=17UVejOw3zA)

7. Run the `quickstart.py` code using the `vscode` button (top right)
8. Play around with the notebook version! (`quickstart.ipynb`)
	- notice how the outputs are automatically printed instead of using `print()`
9. Follow the [Quickstart Guide](https://python.langchain.com/docs/get_started/quickstart) from LangChain to complete the code in either `quickstart.ipynb` or `quickstart.py`.

Well done! 🙌 🚀 Setup can be daunting, but you got through it and can focus on the code from now on 🌴
<br>
<br>

___
# 🗿 Day 2 - CaveGPT
Today you will create a ChatGPT clone, but where the AI talks in simple caveman language and uses lots of 🔥🦴🦶 emojis.

1. Refresh your knowledge on prompt templates in LangChain using the [Quickstart](https://python.langchain.com/docs/get_started/quickstart) if needed. Also check out the diagram on the [Model I/O](https://python.langchain.com/docs/modules/model_io/) page. Design a few random templates. Use `templates.py`
	- Remember to use the `print` statement to see output, as the `.py` file is not a notebook
	- You can change the filetype to `.ipynb` if you prefer notebooks
2. Learn about the simple memory types in LangChain. Use `memory.py`
	- [Conversation buffer memory](https://python.langchain.com/docs/modules/memory/types/buffer)
	- [Conversation buffer window memory](https://python.langchain.com/docs/modules/memory/types/buffer_window)
		ChatGPT (the app) likely uses a simple technique similar to `ConversationBufferWindowMemory`.

3. Combine your newfound knowledge about prompt templates and memory in LangChain to create the prototype app in `CaveGPT.ipynb` using the [LLMChain with memory](https://python.langchain.com/docs/modules/memory/adding_memory).

**Tip:** use the  [Chat Model](https://python.langchain.com/docs/modules/model_io/models/chat/) version of the OpenAI models, rather than the base-model as is used per the LangChain documentation (29/8/23). Sometimes the documentation in LangChain isn't up to date, because so much is changing in this space, and LangChain is just open source software. It's only as good as it's contributors.
```python
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI()
# instead of LangChain documentation (29/8/23):
from langchain.llms import OpenAI
llm = OpenAI()
```

**Tip 2:** they use "Chatbot:" in their example code `template`, but it should be "AI:"
This is again just a case of outdated documentation.

The key to solving this is just reading the documentation links provided in step 3, and then applying some prompt engineering to make the chatbot talk like a caveman. Here is my proposed solution. Try solving yourself. It might take a lot of trial and error, but you will learn from that.
<details>
  <summary>[spoiler] (Solution): prompt engineering</summary>
  
	This is the prompt template I came up with, seems to work pretty well:
	
	```python
	template = """You (AI) are a funny teacher who teaches any subject always using caveman language and emojis to educate. You (AI) provide short explanations of subjects as an overview, but always highlight important words that you can expand upon. Explain to me (human) like I'm a caveman (but assume knowledge about the modern world, I'm not really a caveman). Prefer emojis (or even simple math symbols) rather than text. Your grammar needs to be a little caveman-broken. You always explain your answers.
	
	{chat_history}
	Human: {human_input}
	AI:"""
	```

</details>

Even though my solution works quite well most of the time, there's room for improvement.
4. Use [in-context learning](https://thegradient.pub/in-context-learning-in-context/) to improve the performance of this caveman teaching bot.
5. Provide the caveman with oddly specific knowledge about yourself. Your personal caveman 💀
