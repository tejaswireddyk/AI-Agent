from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo


websearch_agent=Agent(
    name="Web search agent",
    role="Search the web for information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
)

## Financial agent

finance_agent=Agent(
    name="Finance AI agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    show_tool_calls=True,
    instructions=["Use tables to dispaly the data"],
    
)

multi_ai_agent=Agent(
    model=Groq(id="llama-3.1-70b-versatile"),
    team=[websearch_agent,finance_agent],
    instructions=["Always include sources","Use tables to dispaly the data"],
    show_tool_calls=True,
    
)

multi_ai_agent.print_response("Summarize analyst recommentation and share the latest news for NVDA",stream=True)