from crewai import Agent
from tools.search_tools import SearchTools

class AINewsLetterAgents():
    def editor_agent(self):
        return Agent(
            role="Editor",
            goal="Oversee the creation of the AI Newsletter",
            backstory="""With a keen eye for detail and a passion for storytelling, you ensure that the newsletter not only informs, but also
            engages and inspires readers. You work closely with the writers and designers to bring the newsletter to life.""",
            allow_delegation=True,
            verbose=True,
            max_iter = 15
        )

    def news_fetcher_agent(self):
        return Agent(
            role="News Fetcher",
            goal="Fetch the top AI news stories for the day",
            backstory= """As a digital sleuth, you scour the internet for the latest and most impactful developments in the world of AI, ensuring
            that our readers are always up to date. You have a knack for finding hidden gems and a keen sense of what will resonate with our audience.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
        )
    
    def news_analyzer_agent(self):
        return Agent(
            role="News Analyzer",
            goal="Analyze each news story and generate a detailed markdown summary.",
            backstory="""With a critical eye and a knack for distilling complex information, you provide a summary analysis of AI news stories, making them accessible
            and engaging for our audience.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
        )
    
    def newsletter_compiler_agent(self):
        return Agent(
            role="Newsletter Compiler",
            goal="Compile the analyzed news stories into the final newsletter format.",
            backstory="""As the final architect of the newsletter, you meticulously arrange and format the news stories, ensuring a coherant and visually appealing
            presentation that captivates our readers and keeps them coming back for more. Maintain a consistent format and throughput.""",
            verbose=True,
        )