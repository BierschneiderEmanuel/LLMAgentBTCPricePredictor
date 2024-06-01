from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew, Process
from crewai_tools import tool
import wikipediaapi
from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain_community.tools import DuckDuckGoSearchRun
import asyncio
ollama_openhermes = Ollama(model="openhermes")
#ollama_openhermes = Ollama(model="myllama3")

def get_wiki_content(key_word):
    try:
        #  Wikipedia API ready
        wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')
        page = wiki_wiki.page(key_word)
        if page.exists(): # Page - Exists: True
            print("Page - Title:", page.title)
            print("Page - Summary:", page.summary)
            return page.summary
        else:
            print("Page not found.")
        return page.summary
    except Exception as error:
        # handle the exception
        print("An exception occurred:", error)
    return ""

web_search_tool = DuckDuckGoSearchRun()

async def web_duck_search(question):
    return web_search_tool.run(question)

def web_search(search_input):
    """
    Web search tool

    Args:
        search_input (str): Input to be searched for

    Returns:
        web_results (str): Web search results
    """

    # Web search
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        web_results = loop.run_until_complete(web_duck_search(search_input))
    finally:
        asyncio.set_event_loop(None)
        loop.close()

    return web_results

@tool ("duckduck go search tool")
def duck_duck_go_search_tool(argument: str) -> str:
    """Use this tool to search new information using duckduckgo, if you do need additional information."""
    return web_search(argument)

@tool("wikipedia search tool")
def wikipedia_search_tool(argument: str) -> str:
    """Use this tool to search a single keyword on wikipedia, if you do not know the answer to a question."""
    return get_wiki_content(argument)

def run_crew():
    journalist = Agent(
        role='Journalist',
        goal='Bitcoin',
        backstory="""You write about Bitcoin""",
        verbose=True,
        allow_delegation=False,
        tools=[wikipedia_search_tool, YahooFinanceNewsTool()],
        llm=ollama_openhermes
    )
    researcher = Agent(
        role='Researcher',
        goal='Predict new Bitcoin prices',
        backstory="""You are an Bitcoin trader in a bank""",
        verbose=True,
        allow_delegation=False,
        tools=[duck_duck_go_search_tool, YahooFinanceNewsTool()],
        llm=ollama_openhermes
    )
    writer = Agent(
        role='Writer',
        goal='Write compelling and engaging blog posts about Bitcoin',
        backstory="""You are an Bitcoin blog post writer who specializes in writing Bitcoin blog posts""",
        verbose=True,
        allow_delegation=False,
        tools=[duck_duck_go_search_tool, YahooFinanceNewsTool()],
        llm=ollama_openhermes
    )

    task1=Task(description='Define Bitcon',expected_output= 'Introductory writeup on Bitcoin topic', agent=journalist)
    task2=Task(description='Investigate the next Bitcoin halving',expected_output= 'A bullet list summary of the top 5 most important Bitcoin halving financial aspects', agent=researcher)
    task3=Task(description='Write a compelling blog post about Bitcoin',expected_output='Write an exceptionally interesting financial writeup about the price of Bitcoin, including an explicit dollar value, after the halving.', agent=writer)
    crew = Crew(
        agents=[journalist, researcher, writer],
        tasks=[task1, task2, task3],
        verbose=2,
        process=Process.sequential
    )
    result = crew.kickoff()

if __name__ == "__main__":
    run_crew()

