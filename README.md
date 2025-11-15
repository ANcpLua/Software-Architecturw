# Software Architecture Course - Exercise Repository

**Foundation:** Empirically-validated software engineering principles (1968-2025)
**Course Structure:** 4 evenings, 21 exercises
**Learning Mode:** Remote-friendly with group and home exercises

## Quick Navigation

| Evening | Focus | Exercises | Supporting Materials |
|---------|-------|-----------|---------------------|
| **[Evening 1](#evening-1-importance-of-architecture)** | Importance of Architecture | 2 exercises | Course introduction |
| **[Evening 2](#evening-2-architectural-quality)** | Interface Design & Quality | 7 exercises | Case Study: EarlyBird |
| **[Evening 3](#evening-3-architecture-development)** | Architecture Development | 5 exercises | Case Studies: Mars, EarlyBird, Dis*Ease |
| **[Evening 4](#evening-4-architecture-documentation)** | Documentation & Synthesis | 2 exercises | Review all prior work |

**Related Repositories:**
- [Mars](https://github.com/ANcpLua/Mars) - Mars moons calculator and architecture analysis exercises
- [EarlyBird](https://github.com/ANcpLua/EarlyBird) - Interface design and application core exercises
- [MateMate](https://github.com/ANcpLua/MateMate) - Mermaid diagram tooling
- [earlybird-sdd](https://github.com/ANcpLua/earlybird-sdd) - Hub repository with documentation
- [EarlyBirdAI](https://github.com/ANcpLua/EarlyBirdAI) - AI components

---

## Evening 1: Importance of Architecture

**PDF:** `1_The_Importance_of_Architecture_V702.pdf`
**Theme:** Why architecture matters - decisions with long-term impact

### Exercises

| ExID | Exercise | Type | Page | Description |
|------|----------|------|------|-------------|
| - | What Decisions Are Hard to Change? | Group | 13 | Identify architectural decisions, their influenced non-functional aspects (security, efficiency, changeability), and determine which "-ility" appears most frequently. |
| - | Tools Corner | Optional | - | Present tools for developing/documenting architectures (e.g., Structurizr, C4, arc42). |

---

## Evening 2: Architectural Quality

**PDF:** `1_Architectural_Quality_V701.pdf`
**Theme:** Cohesion, coupling, interface quality, peer review

### Exercises

| ExID | Exercise | Type | Page | Repository | Description |
|------|----------|------|------|------------|-------------|
| **ArchitecturalQuality01** | Quality of Building Blocks | Group | 8 | - | Analyze internal quality (cohesion) of a building block using dependency matrix. |
| **ArchitecturalQuality03** | An A-Interface of EarlyBird | Group | 71 | [EarlyBird](https://github.com/ANcpLua/EarlyBird) | Specify `ISearchProduct` interface for EarlyBird's ProductManager component. |
| **ArchitecturalQuality04** | ISearchProduct Specification | Group | 73 | [EarlyBird](https://github.com/ANcpLua/EarlyBird) | Extend interface specification checklist and peer-review ArchitecturalQuality03. |
| **ArchitecturalQuality05** | Specification of a 0-Interface | Group | 74 | [EarlyBird](https://github.com/ANcpLua/EarlyBird) | Design and document generic `IList` interface. |
| **ArchitecturalQuality07** | List Interface Specification | Group | 75 | [EarlyBird](https://github.com/ANcpLua/EarlyBird) | Peer-review partner group's `IList` specification from ArchitecturalQuality05. |
| **ArchitecturalQuality08** | Climate Model | Group | 125 | [Mars](https://github.com/ANcpLua/Mars) | Analyze climate model subsystems dependencies and identify architectural weaknesses. |
| **ArchitecturalQuality09** | Heat Flow Calculator | Self-Check | 83 | - | Identify coupling weaknesses and "Tell Don't Ask" violations. |
| **ArchitecturalQuality10** | Architecture - A Real-Life Story | Group | 124 | [Mars](https://github.com/ANcpLua/Mars) | Analyze Charts/Products architecture evolution and identify violated principles. |

**Case Study Required:** `2_Case Study Early Bird Requirements V150.pdf` (for ArchitecturalQuality03, ArchitecturalQuality04)

---

## Evening 3: Architecture Development

**PDF:** `1_Architecture_Development_V702.pdf`
**Theme:** From requirements to architecture - service-based, domain-driven, AI-assisted

### Exercises

| ExID | Exercise | Type | Page | Repository | Description |
|------|----------|------|------|------------|-------------|
| **MateMate02** | Service-Based Architecture Development | Group | 34 | [MateMate](https://github.com/ANcpLua/MateMate) | For MateMate chess app: establish subsystems, determine blood types (A/T/0), create allowed-to-use specification. |
| **Mars02** | A Very Small Application Core | Home | 126-128 | [Mars](https://github.com/ANcpLua/Mars) | Design 4-component architecture for Mars moons visibility calculator. |
| **EarlyBird12** | A Bigger Application Core | Home | 129 | [EarlyBird](https://github.com/ANcpLua/EarlyBird) | Design EarlyBird application core with change impact analysis. |
| **Dis\*Ease01** | Requirements Class-Diagram-Based Architecture | Group | 50 | - | Design DIS*EASE hospital system architecture from domain class diagram (4-6 building blocks). |
| **ArchitectureDevelopment02** | AI Architecture Development (Embedding Approach) | Home | 71 | [EarlyBirdAI](https://github.com/ANcpLua/EarlyBirdAI) | Use vector embeddings to cluster EarlyBird requirements into architecture components. |

**Case Studies Required:**
- `3_Case_Study_Mars_V161.pdf` (for Mars02)
- `2_Case Study Early Bird Requirements V150.pdf` (for EarlyBird12, ArchitectureDevelopment02)

---

## Evening 4: Architecture Documentation

**PDF:** `1_Architecture_Documentation_V701.pdf`
**Theme:** Presentation, discussion, synthesis

### Exercises

| ExID | Exercise | Type | Page | Description |
|------|----------|------|------|-------------|
| - | Presentation & Discussion | Group | 2 | Present and discuss architecture documentation from prior exercises (ArchitecturalQuality03-07, MateMate02, Mars02, EarlyBird12). |
| - | Architectural Frameworks | Home | 92 | Design an architectural framework better than existing ones. |

---

## Exercise Categories

### By Type

**Group Exercises (In-Class):** ArchitecturalQuality01, ArchitecturalQuality03, ArchitecturalQuality04, ArchitecturalQuality05, ArchitecturalQuality07, ArchitecturalQuality08, ArchitecturalQuality10, MateMate02, Dis*Ease01

**Home Exercises (Asynchronous):** Mars02, EarlyBird12, ArchitectureDevelopment02, Architectural Frameworks

**Self-Check (Individual):** ArchitecturalQuality09

**Optional:** Tools Corner

### By Skill Focus

| Skill | Exercises |
|-------|-----------|
| **Interface Design** | ArchitecturalQuality03, ArchitecturalQuality04, ArchitecturalQuality05, ArchitecturalQuality07 |
| **Architecture Analysis** | ArchitecturalQuality01, ArchitecturalQuality08, ArchitecturalQuality09, ArchitecturalQuality10 |
| **Architecture Design** | MateMate02, Mars02, EarlyBird12, Dis*Ease01 |
| **AI-Assisted Architecture** | ArchitectureDevelopment02 |
| **Documentation & Tooling** | Architectural Frameworks, Tools Corner |

---

## Repository Map

### Exercise Locations

```
Software-Architecture (this repo - central index)
├── Mars/
│   ├── ArchitecturalQuality08 - Climate Model Analysis
│   ├── ArchitecturalQuality10 - Charts/Products Architecture
│   └── Mars02 - Mars Moons Application Core
│
├── EarlyBird/
│   ├── ArchitecturalQuality03 - ISearchProduct Interface
│   ├── ArchitecturalQuality04 - Interface Quality Checklist
│   ├── ArchitecturalQuality05 - IList Interface Design
│   ├── ArchitecturalQuality07 - Interface Review
│   └── EarlyBird12 - Application Core Architecture
│
├── MateMate/
│   └── MateMate02 - Service-Based Architecture
│
└── EarlyBirdAI/
    └── ArchitectureDevelopment02 - AI Architecture Development
```

---

## Learning Strategies

### For Remote Learners

1. **Follow evening sequence** - Each builds on prior knowledge
2. **Do group exercises solo** - Present to yourself (Feynman technique)
3. **Complete Mars02 before EarlyBird12** - Small application core principles apply to large systems
4. **Document AI usage** - Note prompts and models when using AI assistants

### For In-Person Students

1. **Bring digital copies** - Keep exercise solutions accessible for presentations
2. **Peer review seriously** - ArchitecturalQuality04 and ArchitecturalQuality07 are critical learning moments
3. **Participate actively** - Be ready to present any home exercise

### General Tips

- **ArchitecturalQuality03 → ArchitecturalQuality04 → ArchitecturalQuality05 → ArchitecturalQuality07** - This is a mini-course on interface quality
- **All exercises trace to principles** - Every decision has empirical evidence

---

## Principles Reference

All exercises apply empirically-validated software engineering principles:

| Principle | Applied In |
|-----------|-----------|
| **SRP** - Single Responsibility | All design exercises |
| **OCP** - Open-Closed | ArchitecturalQuality10, EarlyBird12 |
| **DIP** - Dependency Inversion | ArchitecturalQuality10, EarlyBird12 |
| **ISP** - Interface Segregation | ArchitecturalQuality08 |
| **CCP** - Common Closure | ArchitecturalQuality08, ArchitecturalQuality10 |
| **CRP** - Common Reuse | ArchitecturalQuality10 |
| **SDP** - Stable Dependencies | ArchitecturalQuality08, ArchitecturalQuality10 |
| **SAP** - Stable Abstractions | ArchitecturalQuality10 |
| **ADP** - Acyclic Dependencies | Mars02 |
| **Blood Type Separation (A/T/0)** | MateMate02, EarlyBird12 |
| **Tell Don't Ask** | ArchitecturalQuality09 |

---

## Quality Standards

All documentation in this repository follows:

1. **Empirical Evidence:** Every architectural decision cites research or case studies
2. **Professional Diagrams:** GitHub-compatible Mermaid syntax
3. **No Emojis:** Clean, professional markdown
4. **Cognitive Load Optimization:** Information chunking, progressive disclosure
5. **Traceability:** Requirements → Components → Principles → Evidence

---

## Course Philosophy

> "Good engineers write code. Great engineers make good decisions."
>
> — Raul Junco (@RaulJuncoV)

**Key Principles:**
1. Build what you need, not what you imagine
2. Logs, monitoring, and error handling aren't optional
3. Test your code before your users do
4. The right tool > the latest tool

---

**Course Completion:** All 21 exercises
**Total Time Investment:** ~40 hours (4 evenings × 4 hours + ~24 hours homework)
**Prerequisite Knowledge:** Software development experience, basic OOP

**Course:** Software Architecture (Blended Learning)
**ECTS:** 2-3 ECTS (50-75 hours total workload)
**Format:** 4 evenings (2+4+4+4 hours each)

**Maintained By:** Course instructors and AI teaching assistants
