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
⚠️ Important: first `cd` into the `symbolik/bootcamp` folder from the terminal (for example if you're using PowerShell)
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
2. <kbd>shift</kbd>+<kbd>cmd</kbd>+<kbd>P</kbd> to open command palette, search for 'Python: select interpreter'. Pick `symbolik-bootcamp`.
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
4. Use [in-context learning](https://sphere.segefjord.space/ai/intro?.=4) to improve the performance of this caveman teaching bot.
5. Provide the caveman with oddly specific knowledge about yourself. Your personal caveman 💀
<br>
<br>

___
# 🧠 Day 3 - Brain Power
Today+tomorrow we will make an AI read [40+ books in a few minutes](https://youtu.be/h-mUGj41hWA?t=87).

0. Visit Paul Graham's famous online [essays](http://www.paulgraham.com/articles.html) - they are legendary. [Paul Graham (Y Combinator → Airbnb, Dropbox, Stripe, Reddit)](http://www.paulgraham.com/bio.html) has been one of the most culturally influential people in Silicon Valley, and still is today:
	- ["What Startups Are Really Like"](http://www.paulgraham.com/really.html)
	- ["Keep Your Identity Small"](http://www.paulgraham.com/identity.html)

Before getting started today, you should [create a branch](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/making-changes-in-a-branch/managing-branches-in-github-desktop) called `san-karem` and [make commits](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop) for each day you finished in the bootcamp. ⚠️ Make sure you are on `san-karem` branch while committing and pushing. Each [commit message](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop#write-a-commit-message-and-push-your-changes) should be in the format `"✅ completed day x"` with no other text. To isolate each day from each other into separate commits, [deselect/select changes](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop#selecting-changes-to-include-in-a-commit) accordingly.

Let's install packages we need for today. Remember to activate the `(symbolik-core)` virtual environment before installing.
```
pip install pypdf
pip install tiktoken
pip install faiss-cpu
```
1. Open `Day 3/intro.ipynb` and take a look at the [LangChain PDF Document Loader](https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf). It's used in that notebook together with FAISS (simple vector DB) to generate [embeddings](https://sphere.segefjord.space/ai/intro?.=6).
	- Change the question you "ask the book" (`similarity_search`)
	- Change the book and come up with a new question
	- Try making a `PromptTemplate` where you pass your `{question}` in together with the output from the similarity search. Do some prompt engineering.
<details>
  <summary>[spoiler] (Solution): prompt engineering</summary>

```python
template = """Given the following section of a book:
{search_output}

Answer the following question:
{Question}
Answer:
"""
```

</details>

2. Watch videos on Sphere about document retrieval. Only need to watch until specified timestamps.
	- ["Building the Future with LLMs, LangChain, & Pinecone" ***(watch from 20:43 to 30:24)***](https://youtu.be/nMniwlGyX-c?t=1243)
	- [LangChain 🦜🔗 Basics Course - Video 10 (**stop at 3:35**)](https://sphere.segefjord.space/ai/langchain-basics?.=9)
	- [LangChain 🦜🔗 Basics Course - Video 11 (**stop at 7:24**)](https://sphere.segefjord.space/ai/langchain-basics?.=10)

3. Use the [documentation](https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf) on `PyPDFDirectoryLoader` to load all books at once.
4. 
<br>
<br>

___
# 🧠 Day 4 - BrainGPT ⚡️🦾
To kick off the day, read ["How To Start a Startup"](http://www.paulgraham.com/start.html) (famous Paul Graham essay) ☀️

1. Watch the advanced video on Sphere about parsing huge amounts of data into the LLM without going broke. Using `map reduce` is fine for large documents, but for ***huge*** documents like *books* it's gonna take a very long time and be way too expensive + hitting the OpenAI API calling limit (capped at $120/mo). Solution:
	- [LangChain 🦜🔗 Basics Course - Video 19 (**full video**)](https://sphere.segefjord.space/ai/langchain-basics?.=18)
			The Jupyter notebook from his video containing all code is located in:
			`./Day 3/ 5 Levels Of Summarization - Novice To Expert.ipynb`