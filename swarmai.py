# !pip -q install git+https://github.com/openai/swarm.git

import os
from google.colab import userdata

os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY')

from swarm import Swarm, Agent

client = Swarm()

def assess_student(student_performance):
    """Assess the student's performance based on their quiz scores or interaction history."""
    if student_performance == "low":
        return "Student is struggling with current content. They scored poorly on the last quiz."
    elif student_performance == "medium":
        return "Student is doing okay, but there are some gaps in their understanding."
    else:
        return "Student is excelling and grasping the content well."

def deliver_lesson(strategy="default"):
    """Deliver a lesson based on the current teaching strategy."""
    if strategy == "slower_pace":
        return "Delivering lesson at a slower pace with more examples and visual aids."
    elif strategy == "interactive":
        return "Delivering an interactive lesson with quizzes and activities."
    else:
        return "Delivering standard lesson based on course material."


def track_attention(attention_level):
    """Monitor student attention levels during lessons."""
    if attention_level == "low":
        return "Student's attention is waning. They seem distracted or taking longer to respond."
    elif attention_level == "medium":
        return "Student is somewhat engaged but occasionally losing focus."
    else:
        return "Student is fully engaged and actively participating."

def track_performance(student_performance):
    """Monitor student's performance based on recent quizzes or activities."""
    if student_performance == "low":
        return "Student has been struggling in the last few assessments."
    elif student_performance == "medium":
        return "Student's performance is adequate but inconsistent."
    else:
        return "Student is performing excellently and showing improvement."


def update_strategy(performance, attention_level):
    """Adjust the teaching strategy based on student's performance and attention levels."""
    if performance == "low" or attention_level == "low":
        return "slower_pace"
    elif performance == "medium" and attention_level == "medium":
        return "interactive"
    else:
        return "default"


def manage_communication(student_performance, attention_level):
    """Coordinate task handoffs and communication between agents."""
    # Step 1: Tutoring Agent delivers the lesson
    strategy = "default"
    print(f"Tutoring Agent: {deliver_lesson(strategy)}")

    # Step 2: Performance Monitoring Agent tracks attention and performance
    attention_feedback = track_attention(attention_level)
    print(f"Performance Monitoring Agent: {attention_feedback}")

    performance_feedback = track_performance(student_performance)
    print(f"Performance Monitoring Agent: {performance_feedback}")

    # Step 3: Strategy Agent updates the strategy based on feedback
    strategy = update_strategy(student_performance, attention_level)
    print(f"Strategy Agent: Switching strategy to {strategy}")

    # Step 4: Handoff back to the Tutoring Agent to deliver an updated lesson
    updated_lesson = deliver_lesson(strategy)
    print(f"Tutoring Agent (after strategy update): {updated_lesson}")

# Define the agents and their roles

# Tutoring Agent focuses on personalized learning
tutoring_agent = Agent(
    name="Tutoring Agent",
    instructions="Provide personalized lessons based on student performance.",
    functions=[
        assess_student,
        deliver_lesson
    ]
)

# Performance Monitoring Agent focuses on real-time tracking
performance_monitoring_agent = Agent(
    name="Performance Monitoring Agent",
    instructions="Monitor student progress and engagement.",
    functions=[
        track_attention,
        track_performance
    ]
)

# Strategy Agent dynamically adjusts teaching strategies
strategy_agent = Agent(
    name="Strategy Agent",
    instructions="Adapt learning strategy based on student performance and feedback.",
    functions=[
        update_strategy
    ]
)

# Collaboration Agent manages communication between agents
collaboration_agent = Agent(
    name="Collaboration Agent",
    instructions="Coordinate information between tutoring and performance monitoring agents.",
    functions=[
        manage_communication
    ]
)

# Simulate task handoff and collaboration
response = client.run(
    agent=collaboration_agent,
    messages=[
        {"role": "student", "content": "I'm struggling with math concepts."}
    ],
)

print(response.messages[-1]["content"])
