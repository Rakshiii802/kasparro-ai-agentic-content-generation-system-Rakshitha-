# Multi-Agent Content Generation System  
(Project Documentation)

---

## 1. Purpose of the System

The purpose of this system is to automatically generate multiple structured content artifacts from a given product dataset using **autonomous agents**.

The focus of the assignment is not on content quality or UI rendering, but on designing a system that demonstrates:
- agent independence
- dynamic coordination
- separation of responsibilities
- non-static execution flow

The system generates machine-readable outputs that can be consumed by downstream applications.

---

## 2. Design Motivation

A traditional step-by-step script or pipeline is not suitable for this problem because it tightly couples execution order with logic.

Instead, this system is designed as a **multi-agent architecture**, where:
- each agent is responsible for exactly one concern
- agents do not directly invoke each other
- coordination happens indirectly through shared state

This allows the system to scale, evolve, and remain modular without rewriting orchestration logic.

---

## 3. Core Architectural Components

The system consists of three core components:

### Agents
Independent units that perform a single task and publish their results.

### MessageBus
A shared state mechanism that enables indirect communication between agents.

### Orchestrator
A lightweight scheduler that repeatedly evaluates which agents are ready to act.

The orchestrator does **not** contain domain logic and does **not** enforce execution order.

---

## 4. Agent Autonomy Model

Each agent implements the same conceptual contract:

- **can_act(bus)**  
  Determines whether the agent has sufficient data available to perform its task.

- **act(bus)**  
  Executes the agent’s responsibility and publishes its output to the MessageBus.

Agents decide **independently** when they can act.  
No agent has knowledge of other agents or their internal logic.

---

## 5. Agent Responsibilities

### ProductParserAgent
- **Consumes:** RAW_PRODUCT  
- **Produces:** PARSED_PRODUCT  
- **Responsibility:** Normalize and structure raw product input for downstream use.

---

### QuestionGeneratorAgent
- **Consumes:** PARSED_PRODUCT  
- **Produces:** QUESTIONS  
- **Responsibility:** Generate user-style informational questions from product data.

---

### FAQAgent
- **Consumes:** PARSED_PRODUCT, QUESTIONS  
- **Produces:** FAQ_PAGE  
- **Responsibility:** Assemble structured FAQ content in JSON format.

---

### ProductPageAgent
- **Consumes:** PARSED_PRODUCT  
- **Produces:** PRODUCT_PAGE  
- **Responsibility:** Generate a structured product description page.

---

### ComparisonAgent
- **Consumes:** PARSED_PRODUCT  
- **Produces:** COMPARISON_PAGE  
- **Responsibility:** Generate a comparison between the main product and a fictional alternative.

Each agent owns exactly one output and does not modify outputs owned by other agents.

---

## 6. Message-Based Coordination

All coordination between agents occurs through a shared **MessageBus**.

- Agents publish outputs as named artifacts
- Other agents react when required artifacts become available
- There is no direct agent-to-agent communication

This design ensures:
- loose coupling
- modularity
- easy extensibility
- true agent independence

---

## 7. Orchestrator Behavior

The orchestrator acts as a **generic scheduler**.

Its responsibilities are limited to:
- iterating over registered agents
- allowing an agent to execute when `can_act()` returns true
- continuing until no agent can make further progress

The orchestrator:
- does not know what agents produce
- does not manage dependencies manually
- does not enforce a predefined execution sequence

Execution order **emerges dynamically** based on data availability.

---

## 8. Execution Model (Emergent Flow)

The system does not follow a fixed, step-based pipeline.

Instead:
- agents continuously evaluate shared state
- new outputs enable other agents to act
- multiple agents may become ready in different orders depending on system state

This results in **dynamic, condition-driven execution** rather than static control flow.

---

## 9. Outputs

The system produces deterministic, machine-readable JSON outputs:

- `faq.json`
- `product_page.json`
- `comparison_page.json`

These outputs are intentionally separated from presentation or UI concerns.

---

## 10. Summary

This system demonstrates:

- clear separation of agent responsibilities
- autonomous agent behavior
- dynamic coordination through shared state
- orchestration without embedded business logic

The architecture reflects the intended definition of a **true multi-agent system**, avoiding static pipelines or manually wired execution flow.


