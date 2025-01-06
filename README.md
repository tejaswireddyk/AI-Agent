# AI-Agent
Financial Agent with Phidata

Initially create a virtual environment venv for your project. 
$conda create -p venv python==3.10
$activate

create the requirements.txt file and run it. It installs all the necessary libraries and packages mentioned in the file.
create financial_agent.py 
- It has websearch_agent(searches the web and gets all the info of the stock using DuckDuckGo tool) and
- finance_agent(It will get uptodate info from the news using YFinance tool)
- these 2 agents will be combined and given to multi_ai_agent and we provide prompts to this.
  when executed, we get the stock price of the stock requested and the related info and news.

Then, create playground.py. It represents the above code as a application on phidata.
when executed we get localhost url. To view the chatbot agent, go to phidata --> playground --> activate/connect the url to phidata
