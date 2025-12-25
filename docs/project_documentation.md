# Multi-Agent Content Generation System

## Problem Statement

The objective of this assignment is to design and implement a modular, agent-based automation system that can take a fixed product dataset as input and automatically generate structured, machine-readable content pages.

The system must:
- operate only on the given product data
- avoid external research or manual content writing
- generate reusable, scalable content using automation
- demonstrate clear agent boundaries and orchestration

This project focuses on system design, automation logic, and agent coordination rather than domain expertise or UI development.

---

## Solution Overview

The solution is implemented as a multi-agent content generation pipeline. Each agent is responsible for a single, well-defined task, and an orchestrator controls the execution flow.

The system processes a product dataset and automatically generates:
- a FAQ page
- a Product Description page
- a Comparison page (against a fictional product)

All outputs are generated in clean, structured JSON format, making them suitable for downstream machine consumption.

---

## Scope & Assumptions

### Scope
- The system operates strictly on the provided product dataset.
- All generated content is derived from the input data using rule-based logic.
- The system is designed to be extensible for additional products or page types.

### Assumptions
- No external data sources or APIs are used.
- The fictional comparison product is intentionally simple and structured.
- Content quality is secondary to system design and automation correctness.

---

## System Design

## System Design

The system is designed as a modular, multi-agent automation pipeline that converts a structured product dataset into multiple machine-readable content pages.

Instead of implementing all logic in a single script, the system is decomposed into independent agents, each responsible for a specific stage of content generation. A central orchestrator manages execution order and data flow between agents.

This design ensures clarity, reusability, and easy extensibility.

---

### Architecture Overview

The architecture consists of the following components:

- A single product data source
- Multiple specialized agents
- A centralized orchestrator
- JSON-based output files

Each agent operates independently and communicates only through structured inputs and outputs.

---

### Agent Responsibilities

**ProductParserAgent**  
Responsible for receiving the raw product dataset and converting it into a clean internal representation. This abstraction allows future validation or preprocessing without affecting downstream agents.

**QuestionGeneratorAgent**  
Generates categorized user questions (informational, usage, safety, purchase, etc.) based on the product data. This separates user intent generation from content generation.

**FAQAgent**  
Consumes the generated questions and product data to produce a structured FAQ page. All FAQ-related formatting and logic are encapsulated within this agent.

**ProductPageAgent**  
Generates the product description page using only product-level information such as ingredients, benefits, usage, and price.

**ComparisonAgent**  
Creates a comparison page between the main product and a fictional alternative. This agent isolates comparative logic from single-product content generation.

---

### Orchestration Flow

A centralized orchestrator controls the execution flow of the system. Agents are executed in a fixed, deterministic order, and outputs from one agent are passed as inputs to the next where required.

The execution flow is as follows:

1. Load product data
2. Parse product data
3. Generate user questions
4. Generate FAQ page
5. Generate product page
6. Generate comparison page
7. Persist all outputs as JSON files

This step-based pipeline ensures predictable execution and avoids tight coupling between agents.

---

### Design Characteristics

- **Single Responsibility**: Each agent performs exactly one task.
- **Loose Coupling**: Agents do not depend on each other’s internal logic.
- **Centralized Control**: All execution is managed by the orchestrator.
- **Deterministic Output**: The same input always produces the same output.
- **Extensible Architecture**: New agents or page types can be added without modifying existing agents.

This design closely resembles real-world automation and content generation pipelines used in production systems.

---

## Agent Responsibilities

### ProductParserAgent
- Input: raw product data
- Output: cleaned internal product representation
- Responsibility: prepare data for downstream agents

### QuestionGeneratorAgent
- Input: parsed product data
- Output: categorized user questions
- Responsibility: simulate user intent generation

### FAQAgent
- Input: questions + product data
- Output: FAQ page JSON
- Responsibility: generate structured Q&A content

### ProductPageAgent
- Input: product data
- Output: product description JSON
- Responsibility: assemble product-level information

### ComparisonAgent
- Input: product data
- Output: comparison page JSON
- Responsibility: compare the product against a fictional alternative

---

## Automation Flow

1. The orchestrator loads the product dataset.
2. ProductParserAgent processes the raw data.
3. QuestionGeneratorAgent creates categorized questions.
4. FAQAgent generates the FAQ page.
5. ProductPageAgent generates the product page.
6. ComparisonAgent generates the comparison page.
7. The orchestrator saves all outputs as JSON files.

This flow represents a directed, step-based automation pipeline.

---

## Output Structure

The system generates three machine-readable JSON files:

- faq.json  
- product_page.json  
- comparison_page.json  

Each file follows a consistent, structured schema and can be consumed by other systems without further processing.

The output directory serves as the final interface between the agentic system and downstream applications.

