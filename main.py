from crewai import Crew, Process
from agent import AINewsLetterAgents
from tasks import AINewsLetterTasks
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from file_io import saveMarkdownFile

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openAI = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4-turbo-2024-04-09")

#We need to start by adding all of our agents and tasks which are defined as a class
agents = AINewsLetterAgents()
tasks = AINewsLetterTasks()

#Setting up agent
editor = agents.editor_agent()
news_fetcher = agents.news_fetcher_agent()
news_analyzer = agents.news_analyzer_agent()
newsletter_compiler = agents.newsletter_compiler_agent()

#Setting up tasks
fetch_news_task = tasks.fetch_news_task(news_fetcher)
analyze_news_task = tasks.analyze_news_task(news_analyzer, [fetch_news_task]) #For context since we can pass multiple items. Hence, we need to pass it in as an array
compile_newsletter_task = tasks.compile_newsletter_task(newsletter_compiler, [analyze_news_task], callback_function=saveMarkdownFile)

#Setting up tools - Setup is done in the tools folder and is called in the agents file

#Building the crew that ties everything together
crew = Crew(
    agents = [editor, news_fetcher, news_analyzer, newsletter_compiler],
    tasks = [fetch_news_task, analyze_news_task, compile_newsletter_task],
    process = Process.hierarchical, #This allows to run processes parallely rather than sequentially
    manager_llm = openAI
)

#Run the crew
results = crew.kickoff()

print(f"Crew work results:\n {results}")