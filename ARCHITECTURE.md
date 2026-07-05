# Kubepilot Architecture v2.0

Status: FROZEN

Date: 2026-07-02

## Core Principle

The core architecture is frozen.

New functionality must extend the architecture instead of modifying it.

Only the following changes are allowed:

- Bug fixes
- Performance improvements
- Security improvements
- Refactoring without changing responsibilities

Changing component responsibilities requires a major version (v3).

---

## Core Components

- Workflow Engine
- Adaptive Investigation Planner
- Adaptive Pipeline
- Resource Discovery
- Capability Router
- Agent Registry
- Agent Bus
- Specialist Agents
- Specialist AI
- Aggregator
- Incremental Analyzer
- AI Analyzer
- AI Verification
- Memory Engine
- Knowledge Engine
- Learning Engine
- Report Generator
- Remediation Engine

---

## Extension Points

New features must be added as plugins/modules through:

- Connectors
- Specialist Agents
- AI Specialists
- Memory
- Knowledge
- Learning
- Remediation
- UI

Never bypass these layers.

---

Architecture Version

v2.0

Status

Frozen
