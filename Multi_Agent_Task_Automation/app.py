import asyncio
import streamlit as st
from dotenv import load_dotenv

from agents import create_agents
from code_executor import execute_python_code

load_dotenv()

# -----------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------

st.set_page_config(
    page_title="Multi-Agent Task Automation",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Multi-Agent Task Automation System")

st.write(
    "Enter a task and let multiple AI agents "
    "work together to complete it."
)

# -----------------------------------------
# USER INPUT
# -----------------------------------------

task = st.text_area(
    "Enter your task:",
    placeholder="Example: Create a report about AI-based cybersecurity",
    height=150
)


# -----------------------------------------
# AGENT EXECUTION FUNCTION
# -----------------------------------------

async def run_agents():

    (
        coordinator,
        researcher,
        writer,
        reviewer,
        model_client
    ) = create_agents()

    try:

        # =====================================
        # 1. COORDINATOR
        # =====================================

        st.info("🧠 Coordinator Agent is working...")

        plan_result = await coordinator.run(
            task=f"""
Analyze the following user task.

USER TASK:
{task}

Create a clear step-by-step plan
for completing this task.
"""
        )

        plan = plan_result.messages[-1].content

        # =====================================
        # 2. RESEARCHER
        # =====================================

        st.info("🔍 Research Agent is working...")

        research_result = await researcher.run(
            task=f"""
USER TASK:
{task}

COORDINATOR PLAN:
{plan}

Perform the required research.

Provide:
- Important concepts
- Important information
- Applications
- Advantages
- Limitations
- Future scope

Include only information relevant
to the user's task.
"""
        )

        research = research_result.messages[-1].content

        # =====================================
        # 3. WRITER
        # =====================================

        st.info("✍️ Writer Agent is working...")

        writer_result = await writer.run(
            task=f"""
USER TASK:
{task}

COORDINATOR PLAN:
{plan}

RESEARCH:
{research}

Create a complete answer.

If the user's task is a CODING TASK:

- Generate working Python code.
- Put the complete executable code
  inside ONE Python code block.
- Do not put explanations inside the
  Python code block.
- Keep the code simple and beginner-friendly.
- If the program requires user input,
  use input() normally.
- Do not ask the user for input inside
  the AI response.

If the user's task is NOT a coding task:

- Answer normally.
- Use simple English.
- Use clear headings and bullet points
  when appropriate.

Do not mention the internal agents.
"""
        )

        draft = writer_result.messages[-1].content

        # =====================================
        # 4. REVIEWER
        # =====================================

        st.info("✅ Reviewer Agent is checking the answer...")

        review_result = await reviewer.run(
            task=f"""
USER TASK:
{task}

DRAFT ANSWER:
{draft}

Review the draft.

Check for:
1. Missing information
2. Incorrect information
3. Repetition
4. Grammar
5. Structure
6. Clarity

If this is a coding task:

- Check whether the Python code is
  syntactically correct.
- Keep the code executable.
- Preserve input() if the program
  requires user input.
- Do not remove the Python code block.

Then provide the corrected final answer.

Return ONLY the final answer.
Do not mention the review process
or the internal agents.
"""
        )

        final_answer = review_result.messages[-1].content

        return (
            plan,
            research,
            draft,
            final_answer
        )

    finally:

        await model_client.close()


# -----------------------------------------
# RUN BUTTON
# -----------------------------------------

if st.button("🚀 Run Task"):

    if not task.strip():

        st.warning("⚠️ Please enter a task.")

    else:

        try:

            with st.spinner(
                "🤖 AI agents are working..."
            ):

                (
                    plan,
                    research,
                    draft,
                    final_answer
                ) = asyncio.run(run_agents())

            st.success(
                "✅ Task completed successfully!"
            )

            # =================================
            # DISPLAY RESULTS
            # =================================

            st.subheader("🧠 Coordinator Plan")
            st.write(plan)

            st.subheader("🔍 Research Agent")
            st.write(research)

            st.subheader("✍️ Writer Agent")
            st.write(draft)

            st.subheader("🎯 Final Output")

            # =================================
            # CODE GENERATOR
            # =================================

            if "```python" in final_answer:

                st.subheader("💻 Code Generator")

                code = (
                    final_answer
                    .split("```python", 1)[1]
                    .split("```", 1)[0]
                    .strip()
                )

                st.code(
                    code,
                    language="python"
                )

                # =================================
                # USER INPUT
                # =================================

                if "input(" in code:

                    st.subheader("📝 Program Input")

                    user_input = st.text_area(
                        "Enter input values "
                        "(one value per line):",
                        placeholder="Example:\n10\n20",
                        height=120
                    )

                else:

                    user_input = ""

                # =================================
                # EXECUTE CODE
                # =================================

                if st.button("▶️ Execute Code"):

                    st.subheader("📤 Execution Output")

                    result = execute_python_code(
                        code,
                        user_input
                    )

                    if result["success"]:

                        st.success(
                            "✅ Code executed successfully!"
                        )

                        st.code(
                            result["output"]
                        )

                    else:

                        st.error(
                            "❌ Code execution failed!"
                        )

                        st.code(
                            result["error"]
                        )

            else:

                st.write(final_answer)

        except Exception as e:

            st.error(
                "❌ Something went wrong."
            )

            st.code(str(e))