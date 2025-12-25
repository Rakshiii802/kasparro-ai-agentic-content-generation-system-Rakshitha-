# Multi-Agent Content Generation System

This project implements a multi-agent automation system that generates
structured content pages (FAQ, Product Page, Comparison Page) from a fixed
product dataset.

The focus of this assignment is system design, agent boundaries, and
automation flow rather than UI or domain expertise.

## How It Works

The system is built as a step-based pipeline controlled by a central
orchestrator.

Flow:
Product Data → Parser Agent → Question Agent → FAQ Agent →
Product Page Agent → Comparison Agent → JSON Outputs

## Key Design Decisions

- Each agent has a single responsibility
- Reusable logic is implemented as stateless logic blocks
- Page structure is defined using explicit templates
- All outputs are machine-readable JSON
- A centralized orchestrator controls execution

## How to Run

```bash
python3 orchestrator.py
