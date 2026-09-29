import os
from dotenv import load_dotenv

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()


def create_agents():

    model_client = OpenAIChatCompletionClient(
        model="openai/gpt-oss-20b",
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "structured_output": True,
            "family": "unknown"
        }
    )

    # -----------------------------------------
    # COORDINATOR
    # -----------------------------------------

    coordinator = AssistantAgent(
        name="coordinator",
        model_client=model_client,
        system_message="""
You are the Coordinator Agent.

Understand the user's task.
Break the task into smaller steps.
Create a clear plan.
Coordinate the work of the other agents.
"""
    )

    # -----------------------------------------
    # RESEARCHER
    # -----------------------------------------

    researcher = AssistantAgent(
        name="researcher",
        model_client=model_client,
        system_message="""
You are the Research Agent.

Analyze the given task.
Identify important information,
concepts, facts, applications,
advantages, limitations and future scope
when appropriate.

Provide useful information for the Writer Agent.
"""
    )

    # -----------------------------------------
    # WRITER
    # -----------------------------------------

    writer = AssistantAgent(
        name="writer",
        model_client=model_client,
        system_message="""
You are the Writer Agent.

Use the coordinator plan and research
to create a clear and well-structured answer.

IMPORTANT:

If the user's task is a CODING TASK:
- Generate working Python code.
- Put the complete executable code inside ONE
  Python code block.
- Do not put explanations inside the code block.
- Keep the code simple and beginner-friendly.
- Make sure the code can be executed directly.

If the user's task is NOT a coding task:
- Answer normally.
- Use simple English.
- Use suitable headings and bullet points.

Do not mention the internal agents.
- Do NOT use input() because the code will be
  automatically executed by the system.
- Use sample values directly in the code when
  input values are required.
- Make sure the program can run automatically
  without waiting for keyboard input.
"""
    )

    # -----------------------------------------
    # REVIEWER
    # -----------------------------------------

    reviewer = AssistantAgent(
        name="reviewer",
        model_client=model_client,
        system_message="""
You are the Reviewer Agent.

Check the answer for:
- Missing information
- Incorrect information
- Repetition
- Poor structure
- Grammar
- Clarity

Correct important problems and produce
a polished final answer.
"""
    )

    return (
        coordinator,
        researcher,
        writer,
        reviewer,
        model_client
    )