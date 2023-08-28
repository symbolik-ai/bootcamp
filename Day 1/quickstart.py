from dotenv import load_dotenv
load_dotenv()
# This has the same effect as loading variables into the
# terminal session every time with export OPENAI_API_KEY="..."
# ---------------------

from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()
print(chat_model.predict("hi!"))
