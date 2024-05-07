#This will allow us to save our final newsletter as a markdown file.
from datetime import datetime

def saveMarkdownFile(task_output):
    #Get today's date formated YYYY-MM-DD
    todays_date = datetime.now().strftime('%Y-%m-%d')
    #Set file name to include today's date
    filename = f"AI_Newsletter_{todays_date}.md"
    #Write the output to a markdown file
    with open(filename, 'w') as file:
        file.write(task_output)
    print(f"Newsletter saved as {filename}")