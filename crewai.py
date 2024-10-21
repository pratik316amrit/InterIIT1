import os

from crewai import Agent, Task, Process, Crew
from langchain_google_genai import ChatGoogleGenerativeAI

# Load gemini (this API is for free: https://makersuite.google.com/app/apikey)
api_gemini = os.environ.get("GEMINI-API-KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-pro", verbose=True, temperature=0.1, google_api_key=api_gemini
)

# Define agents
policy_expert = Agent(
    role="Policy Analyst",
    goal="Analyze the current policies of the Ministry of India and suggest improvements for better governance.",
    backstory="""You are an expert in public policy with extensive knowledge of Indian governmental structures and processes. 
        Your insights will help in understanding existing policies, identifying gaps, and proposing actionable recommendations 
        to enhance governmental efficiency and effectiveness.""",
    verbose=True,
    allow_delegation=True,
    llm=llm  # Use Gemini model
)

finance_expert = Agent(
    role="Financial Analyst",
    goal="Evaluate the budget allocation and financial strategies of the Ministry to ensure transparency and efficiency.",
    backstory="""You are a seasoned financial analyst with a focus on governmental budgets and fiscal policies. Your expertise 
        will provide insights into how funds are allocated, potential areas for cost-cutting, and recommendations for 
        financial improvements that can benefit public services.""",
    verbose=True,
    allow_delegation=True,
    llm=llm  # Use Gemini model
)

development_consultant = Agent(
    role="Development Consultant",
    goal="Create a strategic plan to enhance the socio-economic development initiatives led by the Ministry.",
    backstory="""You are a development consultant with a deep understanding of socio-economic challenges in India. Your role 
        is to design sustainable programs that address key issues, promote growth, and ensure that development initiatives are 
        aligned with the Ministry's goals.""",
    verbose=True,
    allow_delegation=True,
    llm=llm  # Use Gemini model
)

legal_advisor = Agent(
    role="Legal Advisor",
    goal="Review the regulatory framework and ensure that policies comply with existing laws and regulations.",
    backstory="""You are a legal expert with a thorough understanding of Indian laws and regulations. Your insights are 
        crucial in ensuring that governmental policies and programs adhere to legal standards and do not violate citizens' rights.""",
    verbose=True,
    allow_delegation=True,
    llm=llm  # Use Gemini model
)

public_relations_specialist = Agent(
    role="Public Relations Specialist",
    goal="Develop communication strategies to improve public perception of the Ministry and its initiatives.",
    backstory="""You are an expert in public relations with a focus on governmental communication strategies. Your role is 
        to craft messages that effectively convey the Ministry's goals and achievements to the public, enhancing transparency and trust.""",
    verbose=True,
    allow_delegation=True,
    llm=llm  # Use Gemini model
)

# Define tasks
task1 = Task(
    description="""Analyze the current policies of the Ministry of India related to economic development. 
        Write a detailed report highlighting strengths, weaknesses, and areas for improvement. The report should include 
        at least 10 bullet points on policy effectiveness and recommendations for enhancement.""",
    agent=policy_expert,
)

task2 = Task(
    description="""Evaluate the budget allocations for various programs under the Ministry of India. 
        Write a concise report with at least 10 bullet points on financial efficiency, transparency, and potential areas for 
        cost reduction.""",
    agent=finance_expert,
)

task3 = Task(
    description="""Summarize the findings from the policy and financial reports, and draft a strategic development plan 
        for the Ministry of India. The plan should include at least 10 bullet points, 5 key goals, and a timeline for achieving 
        each goal.""",
    agent=development_consultant,
)

task4 = Task(
    description="""Review the regulatory framework surrounding the Ministry's initiatives and policies. 
        Provide a report detailing compliance with existing laws and regulations, with at least 10 bullet points on legal considerations and recommendations for improvement.""",
    agent=legal_advisor,
)

task5 = Task(
    description="""Develop a comprehensive public relations strategy for the Ministry of India to improve public engagement. 
        The strategy should include at least 10 actionable points, focusing on communication channels, messaging, and outreach efforts.""",
    agent=public_relations_specialist,
)

task6 = Task(
    description="""Investigate the public's perception of the Ministry's initiatives and identify areas for improvement. 
        Write a report with at least 10 bullet points on public feedback, areas of concern, and potential strategies for enhancing public trust.""",
    agent=public_relations_specialist,
)

# Create the Crew
crew = Crew(
    agents=[policy_expert, finance_expert, development_consultant, legal_advisor, public_relations_specialist],
    tasks=[task1, task2, task3, task4, task5, task6],
    verbose=2,
    process=Process.sequential,  # Tasks will be executed sequentially
)

# Start the crew process
result = crew.kickoff()

# Output the result
print("######################")
print(result)
