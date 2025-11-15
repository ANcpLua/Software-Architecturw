# Software Architecture

> Software Engineering is about systematic, methodical creation of software.

## Foundation

Software Engineering covers the complete development process:

| Phase | Focus |
|:------|:------|
| Requirements Engineering | Understanding what needs to be built |
| Software Architecture | Designing how it should be structured |
| Design & Development | Implementing the solution |
| Testing & Evaluation | Verifying correctness and quality |
| Deployment | Bringing it to production |

## Core Principle

```
Software Engineering ≠ Advanced Programming
```

The distinction matters. Programming is execution. Engineering is decision-making.

## The Reality

| What People Think | What Actually Matters |
|:------------------|:---------------------|
| Writing code is hard | Understanding the problem is hard |
| More features = better | Right features = better |
| Latest technology | Appropriate technology |
| Individual brilliance | Systematic process |

### Source of Failure

```
100% of bugs stem from bad thinking
  └─ Most software failures are from bad decisions
      └─ Not from bad code
```

## Critical Skills

The hierarchy of what matters:

1. **Problem Analysis** - Understanding what to solve and how to solve it elegantly
2. **System Architecture** - Structuring solutions for long-term viability
3. **Requirements Engineering** - Knowing the right problem to ask
4. **Implementation** - Writing code is easy; everything above is hard

> "Good engineers write code. Great engineers make good decisions."

## Common Engineering Mistakes

| Mistake | Impact | Alternative |
|:--------|:-------|:-----------|
| Over-engineering | Complexity kills velocity | Build what you need, not what you imagine |
| Ignoring basics | Silent failures in production | Logs, monitoring, error handling are mandatory |
| Skipping tests | Users become testers | If you don't test it, your users will |
| Tight coupling | Changes require surgery | Future refactors should be straightforward |
| Chasing trends | Instability and rewrites | The right tool beats the latest tool |

## NASA Software Engineering Requirements

NASA NPR 7150.2D defines Software Engineering chapters:

```
Chapter 4: Software Engineering
├── 4.1 Software Requirements
├── 4.2 Software Architecture
├── 4.3 Software Design
├── 4.4 Software Implementation
├── 4.5 Software Testing
└── 4.6 Software Operations, Maintenance, and Retirement
```

Historical note: Apollo 11 used 30 lines of code to calculate transcendental functions for navigation.

## The Intersection with AI

### Two Dimensions

| Dimension | Description | Impact |
|:----------|:------------|:-------|
| **AI4SE** | AI as a tool in Software Engineering | Natural language interfaces, spec-driven development, automated architecture |
| **SE4AI** | Software Engineering methods for AI systems | Specific patterns for ML systems, data engineering, model lifecycle |

### The Shift

Programming languages evolution:

```
1940-1960: Assembly (Machine-first)
1960-1980: FORTRAN, COBOL (Structured)
1980-2000: C, Pascal (Procedural)
2000-2020: Java, Python (Object-oriented, readable)
2020-2040: Natural Language (Human-first)
```

Each generation became more readable to humans. The trend continues.

> "The hottest new programming language is English."

### Changed Landscape

**Traditional Role:**
- Write all code manually
- Focus on syntax and implementation
- Individual contributor

**Emerging Role:**
- Define requirements clearly
- Architect systems thoughtfully
- Decide what to build
- Manage AI coding agents
- Focus on higher-level problem solving

## Spec-Driven Development

Modern workflow with AI tooling:

```
Prompt → Requirements.md → Design.md → Tasks.md → Implementation
         (User stories,    (Technical   (Detailed    (Validated
          acceptance       architecture, tasks with    by tests,
          criteria in      sequence      discrete     generated
          EARS notation)   diagrams)     tracking)    code)
```

Each specification file becomes:
- Machine-readable for AI agents
- Human-readable for engineers
- Version-controlled artifact
- Living documentation

## The Job Market Reality

Data from 2025:

| Observation | Implication |
|:------------|:------------|
| Programmer unemployment nearly doubled | Coding-only skills insufficient |
| AI companies pay $500k+ base salaries | Fight for AI talent is intense |
| "AI will handle programming in a year" | Premature, but directionally accurate |

**What survives:**
- Understanding requirements
- System architecture decisions
- Problem decomposition
- Technical leadership
- Domain expertise

**What's challenged:**
- Pure implementation work
- Routine coding tasks
- Pattern-based development

## Industry Experience Domains

Real-world software engineering spans:

```
Banking                  Insurance               Healthcare
Logistics                Mobile Telephony        Event Management
Public Transport         Data Forensics          Waterway Management
Military Systems         CRM Systems             Sales Platforms
```

Project characteristics:
- Timeline: Days to decades
- Scale: Small to 1000+ person-years
- Type: Greenfield and maintenance
- Technologies: Evolving continuously

## Practical Wisdom

### On Requirements

| Without | With |
|:--------|:-----|
| Building the wrong thing correctly | Building the right thing |
| Rework and waste | Clear direction |
| Stakeholder conflict | Stakeholder alignment |

### On Architecture

| Without | With |
|:--------|:-----|
| Tangled dependencies | Clear boundaries |
| Difficult changes | Accommodating change |
| Scaling problems | Scalable design |

### On Testing

| Without | With |
|:--------|:-----|
| Production surprises | Controlled validation |
| Fear of changes | Confidence in refactoring |
| Unknown quality | Measured quality |

## The Continuous Learning Requirement

Technology patterns (historical):

| Technology | Initial Reception | Actual Impact |
|:-----------|:-----------------|:-------------|
| Personal Computer | "Will drop towards zero" | Ubiquitous |
| Internet | "Won't be mass medium" | Foundation of modern life |
| Smartphones | "Nokia has a billion customers" | Complete transformation |
| Large Language Models | "Impossible to build" | Rapidly advancing |

**Pattern:** Underestimating transformative technologies is consistent.

**Implication:** Continuous learning is not optional. It's survival.

## Knowledge Hierarchy

```
Level 0: Knowing syntax
Level 1: Knowing patterns
Level 2: Knowing when to apply patterns
Level 3: Knowing what problem to solve
Level 4: Knowing how to make decisions under uncertainty
```

This course focuses on Levels 3-4.

## Blended Learning Model

### Time Allocation

**2 ECTS Course:**
- Total: 50 hours (1 hour = 60 minutes)
- In-class: 10 units × 45 min = 7.5 hours (15%)
- Self-study: 42.5 hours (85%)

**3 ECTS Course:**
- Total: 75 hours
- In-class: 14 units × 45 min = 10.5 hours (14%)
- Self-study: 64.5 hours (86%)

### Responsibilities

**At Home:**
- Study materials (PDFs with structured content)
- Complete exercises
- Deep understanding

**In Class:**
- Active participation
- Group exercises
- Individual exercises
- Knowledge verification

## Assessment Model

### No Final Exam

Instead: Continuous assessment through individual exercises

**Rationale:**
- Information fresh in memory
- Immediate application
- Allows open-book for appropriate content
- Tests understanding, not memorization

### Passing Criteria

```
Required: ≥60% points across all individual exercises
+
Active participation measured in hours

Grade Calculation (if ≥60% achieved):
├── ≥90% participation → Grade 1
├── ≥80% participation → Grade 2
├── ≥70% participation → Grade 3
├── ≥60% participation → Grade 4
└── <60% participation → Grade 5
```

**Philosophy:** Theory (60%) establishes baseline. Practice determines excellence.

## AI Usage Policy

### Encouraged

- Home exercises: Use AI freely
- Learning: Experiment with tools
- Exploration: Understand capabilities

### Required Documentation

When using AI:
```
Prompt: [exact prompt used]
Model: [specific model and version]
Output: [what was generated]
Modifications: [how you adapted it]
```

### Responsibility

```
AI suggests → You decide → You own the result
```

End-to-end accountability remains with the engineer.

## Knowledge Distribution

> "True knowledge is knowing that we know nothing."

This repository preserves and shares what has been learned. The content reflects:
- Industry experience across domains
- Academic rigor in teaching
- Practical application in real systems
- Evolution of software engineering practice

## Structure Philosophy

```
Simplicity
  └─ Does not mean simplistic
      └─ Means essential complexity only
          └─ Means understandable at a glance
              └─ Means tables when structure matters
                  └─ Means prose when flow matters
```

Inspired by precision. Guided by clarity. Structured for transmission.

---

**Foundation:** Based on teaching materials by Dr. Martin Hasitschka
**Purpose:** Preserve and transmit software engineering wisdom
**Audience:** Those who take craft seriously
**Maintenance:** Living document, evolving with practice

