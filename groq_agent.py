from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.googlesearch import GoogleSearch
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

finance_agent = Agent(
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price=True,stock_fundamentals=True,analyst_recommendations=True)],
    show_tool_calls= True,
    debug_mode=True,
    markdown=True,
    instructions=["Use tables to display data"]
)

search_agent = Agent(
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [GoogleSearch()],
    show_tool_calls=True,
    debug_mode=True,
    markdown=True,
    instructions=["Always include sources"]
)

agent = Agent(
    team = [finance_agent, search_agent],
    model = Groq(id = "llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True
)

agent.print_response("Summarize and compare analyst recommendations and stock fundamentals for top 5 US tech stocks")
