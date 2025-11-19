# Bigger Application Core: EarlyBird Architecture

**Exercise ID:** EarlyBird12
**Type:** Home Exercise
**Evening:** 3 (but placed in Evening 2 for organization)

---

## Overview

Design a bigger application core for the EarlyBird breakfast delivery system, applying the principles learned from the
Mars Moons exercise. This exercise demonstrates how to separate stable business logic from volatile technology concerns
in a larger, more realistic system.

---

## Exercise Task

**Scenario:**
Build upon the small application core principles from Mars02 to design a comprehensive application core for EarlyBird
that:

1. Separates business logic from infrastructure
2. Identifies stable vs. volatile components
3. Applies change impact analysis for evolution scenarios

**Question:** How should the application core be structured to minimize the impact of technology changes?

---

## Files

- [application-core-design.md](application-core-design.md) - Complete architecture design with 3 evolution scenarios
- [earlybird-requirements-v150.pdf](earlybird-requirements-v150.pdf) - Full system requirements
- `slides/slide_earlybird12.png` - Exercise slide

---

## Key Concepts

**Application Core:**

- Contains stable business logic
- Independent of frameworks and databases
- Protected from technology volatility

**Hexagonal Architecture:**

- Business logic in the center
- Adapters on the outside
- Dependencies point inward

---

## Evolution Scenarios

The design document analyzes three realistic change scenarios:

1. **Database Migration** (PostgreSQL → MongoDB)
    - Impact analysis
    - Components affected
    - Isolation strategy

2. **API Framework Change** (REST → GraphQL)
    - Surface area analysis
    - Adapter redesign
    - Core protection

3. **New Delivery Channel** (Mobile App)
    - Reusability assessment
    - Integration points
    - Shared core benefits

---

## See Also

**Related Exercises:**

- [Mars Application Core](../03-mars-application-core/) - Small application core example
- [ISearchProduct Interface](../../Evening%202%20-%20Architectural%20Quality/02-isearchproduct-interface-specification/) - O-Interface design
- [Building Block Quality](../../Evening%202%20-%20Architectural%20Quality/01-building-block-quality-analysis/) - Cohesion measurement

**Finished EarlyBird Projects:**

- [EarlyBird - Application Core Architecture](https://github.com/ANcpLua/EarlyBird/blob/main/EarlyBird/04-application-core-architecture/application-core-design.md) - Complete implementation and design document
- [EarlyBird SDD - Software Design Document](https://github.com/ANcpLua/earlybird-sdd) - Full software design documentation

---

## Prerequisite

**Important:** Complete Mars02 (Mars Moon Calculator) before this exercise. The small application core principles apply
directly to larger systems.
