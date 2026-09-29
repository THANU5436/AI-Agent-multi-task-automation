# 🤖 Multi-Agent Task Automation System with Code Executor

** Project Overview**

**Multi-Agent Task Automation System with Code Executor** is an AI-powered system that uses multiple specialized AI agents to automate coding and task-solving activities.

The system accepts a user's task, understands the requirement, generates the required code, reviews the generated code, executes it automatically, and displays the output or errors.

If an error occurs during execution, the system can analyze the error, modify the code, and execute it again.

The main goal of this project is to **reduce manual coding, testing, and debugging effort** by allowing multiple AI agents to work together.

---

## 🎯 Objectives

* Automate coding-related tasks using AI agents.
* Divide complex tasks among specialized agents.
* Generate code automatically from user requirements.
* Review and validate generated code.
* Execute generated code automatically.
* Detect and handle execution errors.
* Reduce manual debugging and testing.
* Provide an easy-to-use interface for users.

---

# Key Features

* 🤖 **Multi-Agent Architecture**
* 🧠 **AI-based Task Understanding**
* 🔍 **Research and Information Gathering**
* 💻 **Automatic Code Generation**
* 📝 **Code Review and Validation**
* ▶️ **Automatic Code Execution**
* 🐛 **Error Detection and Correction**
* 🔄 **Automatic Re-execution**
* 📊 **Output and Error Display**
* 🖥️ **Streamlit Web Interface**
* 🔐 **Code Execution Safety Considerations**

---

🏗️ System Architecture

The system consists of multiple AI agents that communicate with each other to complete a user's task.

### Main Workflow

```text
                    ┌───────────────────┐
                    │       User        │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Coordinator Agent │
                    └─────────┬─────────┘
                              │
              ┌───────────────┼────────────────┐
              ▼               ▼                ▼
       ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
       │  Researcher │ │    Writer   │ │   Reviewer  │
       │    Agent    │ │    Agent    │ │    Agent    │
       └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
              │               │                │
              └───────────────┼────────────────┘
                              ▼
                    ┌───────────────────┐
                    │  Code Executor    │
                    │      Agent        │
                    └─────────┬─────────┘
                              │
                     ┌────────┴────────┐
                     ▼                 ▼
                  Output             Error
                                       │
                                       ▼
                              ┌─────────────────┐
                              │ Error Correction│
                              └────────┬────────┘
                                       │
                                       ▼
                                Re-execution
```

---

## 🤖 AI Agents

### 1. Coordinator Agent

The **Coordinator Agent** manages the overall workflow.

Responsibilities:

* Understand the user's request.
* Divide the task into smaller activities.
* Assign tasks to appropriate agents.
* Coordinate communication between agents.
* Manage the overall execution flow.

---

### 2. Researcher Agent

The **Researcher Agent** gathers the required information for completing the task.

Responsibilities:

* Analyze the task.
* Identify required information.
* Provide relevant technical details.
* Support the code generation process.

---

### 3. Writer / Code Generator Agent

The **Writer Agent** generates the required code based on the user's requirements and information provided by other agents.

Responsibilities:

* Understand the programming requirement.
* Generate source code.
* Follow the requested programming language.
* Modify code when required.

---

### 4. Reviewer Agent

The **Reviewer Agent** checks the generated code before execution.

Responsibilities:

* Check syntax and logic.
* Identify possible errors.
* Review code quality.
* Suggest corrections.
* Decide whether the code is ready for execution.

---

### 5. Code Executor Agent

The **Code Executor Agent** executes the generated code and returns the result.

Responsibilities:

* Receive reviewed code.
* Execute the code.
* Capture output.
* Capture errors.
* Send execution results back to the system.

If an error occurs, the workflow can return to the code generation/review stage for correction and re-execution.

---

## 🔄 Working Process

The system follows these steps:

### Step 1 — User Input

The user enters a task or coding requirement through the Streamlit interface.

Example:

```text
Create a Python program to find the largest number in an array.
```

### Step 2 — Task Understanding

The Coordinator Agent analyzes the user's request and determines the required workflow.

### Step 3 — Research

The Researcher Agent provides the required technical information or approach.

### Step 4 — Code Generation

The Writer/Code Generator Agent generates the required program.

### Step 5 — Code Review

The Reviewer Agent checks the generated code for possible errors.

### Step 6 — Code Execution

The Code Executor executes the reviewed code.

### Step 7 — Result

The system displays the execution output to the user.

### Step 8 — Error Handlin
