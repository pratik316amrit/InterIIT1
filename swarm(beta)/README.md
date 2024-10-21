# InterIIT

# Personalized Education System Using Swarm AI

## Overview
This project aims to create a personalized education system that adapts to students' performance and engagement levels using a multi-agent framework. The system employs various agents to monitor student progress, adjust teaching strategies, and deliver tailored lessons.

## Key Features
- **Tutoring Agent**: Delivers personalized lessons based on student performance.
- **Performance Monitoring Agent**: Tracks student engagement and performance in real-time.
- **Strategy Agent**: Adapts teaching strategies based on student feedback and performance.
- **Collaboration Agent**: Coordinates communication between tutoring and performance monitoring agents.

## Setup Instructions


1. ***Install Dependencies***
   ```bash
   !pip -q install git+https://github.com/openai/swarm.git
## How It Works

The personalized education system utilizes a multi-agent architecture to provide tailored learning experiences for students. Each agent has a specific role, and they collaborate to assess student performance, track engagement, and adjust teaching strategies. Key components include:

1. **Tutoring Agent**: 
   - **Responsibilities**: Delivers personalized lessons based on student performance.
   - **Functions**:
     - `assess_student`: Evaluates the student's performance (low, medium, high) and provides feedback.
     - `deliver_lesson`: Offers a lesson tailored to the current teaching strategy.

2. **Performance Monitoring Agent**:
   - **Responsibilities**: Monitors student engagement and performance in real-time.
   - **Functions**:
     - `track_attention`: Assesses the student's attention level during lessons (low, medium, high).
     - `track_performance`: Keeps track of the student’s recent assessments to determine performance.

3. **Strategy Agent**:
   - **Responsibilities**: Adapts teaching strategies based on student feedback and performance.
   - **Functions**:
     - `update_strategy`: Adjusts the teaching strategy based on the monitored performance and attention levels.

4. **Collaboration Agent**:
   - **Responsibilities**: Manages communication between the tutoring and performance monitoring agents.
   - **Functions**:
     - `manage_communication`: Coordinates the tasks and information flow between agents to ensure effective lesson delivery.

### Handoffs
The system's architecture facilitates seamless handoffs between agents, ensuring that each component effectively contributes to the overall learning experience. Each agent performs its function, hands off the results to the next agent, and adjusts based on continuous feedback.

## Example Workflow

Here's a step-by-step breakdown of how the agents interact in the system, highlighting the handoffs between them:

1. **Initial Lesson Delivery**:
   - The **Tutoring Agent** begins by delivering a lesson based on a default strategy.
   - **Handoff**: The Tutoring Agent's output is shared with the Performance Monitoring Agent.
   - Example Output: "Delivering standard lesson based on course material."

2. **Performance Monitoring**:
   - The **Performance Monitoring Agent** assesses the student's attention level and performance.
   - **Handoff**: This agent collects and summarizes feedback, which is then passed to the Strategy Agent.
   - Attention Feedback: "Student's attention is waning. They seem distracted or taking longer to respond."
   - Performance Feedback: "Student's performance is adequate but inconsistent."

3. **Strategy Update**:
   - The **Strategy Agent** reviews the performance and attention feedback from the Performance Monitoring Agent and updates the teaching strategy.
   - **Handoff**: The updated strategy is then communicated back to the Tutoring Agent.
   - Example Output: "Switching strategy to slower pace."

4. **Updated Lesson Delivery**:
   - The **Tutoring Agent** delivers a revised lesson according to the new strategy.
   - **Handoff**: This new lesson output is sent back to the Performance Monitoring Agent for ongoing assessment.
   - Example Output: "Delivering lesson at a slower pace with more examples and visual aids."

5. **Continuous Improvement**:
   - This cycle repeats as the system continuously monitors and adjusts based on the student's ongoing performance and attention levels. 
   - Each agent remains in communication, ensuring an adaptive learning environment tailored to the student's needs.

By coordinating their actions and effectively handing off tasks and feedback, the agents provide a comprehensive and adaptive educational experience that addresses individual student needs efficiently.
