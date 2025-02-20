# from agno.agent import Agent
# from agno.model.openai import OpenAIChat
# from agno.storage.agent.sqlite import SqlAgentStorage
# from agno.tools.duckduckgo import DuckDuckGo
# from agno.tools.yfinance import YFinanceTools
# from agno.playground import Playground, serve_playground_app

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app
from agno.storage.agent.sqlite import SqliteAgentStorage
# from agno.storage.agent.sqlite import SqlAgentStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

web_agent = Agent(
    name="Web Agent",
    agent_id="weg_agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
    storage=SqliteAgentStorage(table_name="web_agent_session", db_file="agents.db"),
    #add_history_to_messages=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    agent_id="finance_agent",
    role="Get Financeial Data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Always use tables to display data"],
    storage=SqliteAgentStorage(table_name="finance_agent_session", db_file="agents.db"),
    #add_history_to_messages=True,
    markdown=True,
)

news_agent = Agent(
    name="News Agent",
    agent_id="news_agent",
    role="Get breaking news",
    model=OpenAIChat(id="gpt-4o"),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    instructions=["Always include sources"],
    storage=SqliteAgentStorage(table_name="news_agent_session", db_file="agents.db"),
    markdown=True
)

team_agent = Agent(
    name="Team Agent",
    agent_id="team_agent",
    team=[web_agent, finance_agent, news_agent],
    storage=SqliteAgentStorage(table_name="team_agent_session", db_file="agents.db"),
    markdown=True,
)

#app = Playground(agents=[finance_agent, web_agent, team_agent]).get_app()
app = Playground(agents=[web_agent, finance_agent, news_agent, team_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("team:app", reload=True)
 