# Class Group Exercise: What Decisions Are Hard to Change?

**Source:** 1_The_Importance_of_Architecture_V702.pdf, Page 22
**Type:** Class Group Exercise

## Overview

This foundational exercise explores the critical concept of architectural decisions and their impact on software
systems. Understanding which decisions are difficult to change helps architects make better choices early in the
development process.

## Exercise Description

Group discussion exercise exploring which architectural decisions are most costly to change and why. Students analyze
decision categories, evaluate their reversibility, and develop strategies for identifying high-impact decisions early in
projects.

## Learning Objectives

- Identifying architectural decisions vs. design decisions
- Understanding the cost of change for different decisions
- Recognizing dependencies that make decisions hard to reverse
- Evaluating decision impact across the software lifecycle
- Applying the concept of "architectural significance"

## Key Concepts

### What Makes a Decision "Hard to Change"?

Decisions become difficult to reverse due to:

1. **Extensive Dependencies**
    - Many components rely on the decision
    - Cross-cutting concerns affected
    - Integration points established

2. **Infrastructure Investment**
    - Hardware procurement
    - License costs
    - Development tool setup

3. **Team Knowledge and Skills**
    - Training investments
    - Expertise built around chosen technology
    - Team reorganization required for change

4. **External Commitments**
    - API contracts with external parties
    - Regulatory compliance
    - Customer expectations

5. **Technical Debt Accumulation**
    - Code written assuming the decision
    - Test suites built around it
    - Documentation and training materials

## Exercise Activities

- Analyze example architectural decisions from real projects
- Categorize decisions by difficulty of change
- Calculate estimated cost of reversing specific decisions
- Identify early warning signs that a decision will be hard to change
- Create decision frameworks for future projects

## Related Content

- [Architectural Decisions slide](../slides/architectural-decisions-analysis-slide-p13.png) - Page 13 reference
- Evening 2: Architecture Quality - Building on these concepts
- Evening 3: Architecture Development - Applying decision-making

## Files

- `README.md` - This file
- `architectural-decisions-analysis.md` - Complete analysis with ADR templates and frameworks
- `slides/` - Exercise slides and diagrams

## Reflection Questions

Consider for discussion:

1. What decisions in your current/past projects were hardest to change?
2. How could early identification of "hard to change" decisions improve planning?
3. What strategies can reduce the cost of changing key decisions?
4. How do you balance flexibility with commitment in architecture?

## Examples of Hard-to-Change Decisions

Common examples include:

- Programming language choice
- Database technology selection
- Communication protocols
- Authentication/authorization mechanisms
- Deployment architecture
- Data storage formats
- External service dependencies

## Notes

This exercise is foundational - understanding what makes architectural decisions significant is the first step in
becoming an effective software architect.
