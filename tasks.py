from crewai import Task
from datetime import datetime

class AINewsLetterTasks():
    def fetch_news_task(self, agent):
        return Task(
            description=f"Fetch top AI news stories from the past 24 hours. The current time is {datetime.now()}.",
            agent = agent,
            async_execution=True,
            expected_output="""A list of top AI news story titles, URLs, and a brief summary for each story from the past 24 hours.
            Example Output:
            [{
                "title":"AI takes the spotlight in the super bowl commercials",
                'url': 'https://www.example.com/ai-superbowl',
                'summary': 'AI made a splash in this year's super bowl commercials...'
            },
            {{...}}
            ]"""
        )
    
    def analyze_news_task(self, agent, context):
        return Task(
            description="Analyze each news story and ensure there are at least 5 well-formatted articles.",
            agent = agent,
            async_execution=True,
            context = context,
            expected_output="""A markdown-formatted analysis for each news story, including a rundown, detailed bullet points, and a "Why it matters" 
            section. There should be at least 5 articles, each following the proper format.
            Example Output:
            '## AI takes the spotlight in the super bowl commercials\n\n
            **The Rundown:**\n
            ** AI was featured in several high-profile commercials during the super bowl...
            **The details:**\n\n
            -Microsoft's Copilot spot showcased its AI capabilities...\n\n
            **Why it matters:**\n While AI-related ads have been rampant over the last year, its super bowl debut signals a new level of mainstream acceptance...'
            """
        )
    
    def compile_newsletter_task(self, agent, context, callback_function):
        return Task(
            description="Compile the newsletter",
            agent = agent,
            context = context,
            expected_output="""A complete newsletter in markdown format, with a consistent style and layout.
            Example Output:
            '# Top stories in AI today:\\n\\n'
            - AI takes the spotlight in the super bowl commercials\n\n
            - Altman's new AI research lab promises breakthroughs in AI ethics\n\n

            ## AI takes spotlight in the super bowl commercials\n\n
            **The Rundown:** AI made a splash in this year's super bowl commercials...\\n\\n
            **The details:**\n\n
            **why it matters:**\n AI-related ads have been rampant over the last year, its super bowl debut signals a new level of mainstream acceptance...\\n\\n            
            """,
            callback=callback_function
        )