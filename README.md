# LLMAgentBTCPricePredictor
CrewAI LLM agents with a custom Langchain duckduckgo search tool, conducts a financial writeup about the Bitcoin dollar price after the Bitcoin halving.
The BTC predictor utilizes three agents to write a financial writeup about the Bitcoin dollar price after the Bitcoin halving.
These agents are grouped into a crewAI crew, and each agent has access to a specific toolset and represents a distinguished role within the crew.
The crewAI framework orchestrates the tasks of the agents in a sequential manner.
The roles applicable to this project are: Journalist, Researcher and Writer.
At first journalist with the exclusive access to wikipedia defines BTC in general and provides a short introductory writeup.
The Researcher investigates the topic of Bitcoin halving, providing a bullet list summarizing the most important financial aspects by searching through news articles on Yahoo Financial News 
and by scraping the web using a customized langchain DuckDuckGo search tool.
Finally the LLM agent Writer, with access to the same toolset as the Journalist, provides the final financial writeup, including the predicted BTC price in dollar.<br>
<p align="center">
   <img src="https://github.com/BierschneiderEmanuel/LLMAgentBTCPricePredictor/blob/16fea7f7d9887002ad8fcfa9883a61c81144614b/p9_0.jpg" alt="p9_2">
</p>
<p align="center">
   <img src="https://github.com/BierschneiderEmanuel/LLMAgentBTCPricePredictor/blob/16fea7f7d9887002ad8fcfa9883a61c81144614b/p9_1.JPG" alt="p9_1">
</p>
To run the BTC price predictor, the Windows linux virtualization environment and the Ollama model please refer to the following steps:<br>
Win-R <br>
cmd <br>
wsl.exe --install <br>
user newUserName pwd newUserNamePassword <br>
wsl.exe --user root -d ubuntu <br>
apt-get update <br>
apt-get upgrade <br>
curl https://ollama.ai/install.sh | sh <br>
ollama run openhermes <br>

To install the requirements of crewAI: <br>
pip install -r Requirements.txt <br>
Run the BTC price predictor script: <br>
To start the BTC price prediction run the python script: <br>
Win-R <br>
cmd <br>
python llm_agent_BTC_price_predictor.py <br> 
