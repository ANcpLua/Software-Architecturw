# Software Architecture Course Exercises

This repository contains my exercise solutions, personal notes, and interpretations from Dr. Martin Hasitschka's Software Architecture course in my Master's program. I maintain this collection as a study guide and reference for architectural principles, quality analysis, development methods, and documentation frameworks.

---

## Quick Links

**Architecture Guides:**

- [ArchitectureForHumans.md](ArchitectureForHumans.md) - Human-readable architecture documentation guide
- [ArchitectureForAIs.md](ArchitectureForAIs.md) - AI-optimized architecture documentation guide

**Related Repositories:**

- [EarlyBird](https://github.com/ANcpLua/EarlyBird) - Breakfast delivery system (main implementation)
- [EarlyBirdAI](https://github.com/ANcpLua/EarlyBirdAI) - AI-driven architecture (requirements clustering)
- [earlybird-sdd](https://github.com/ANcpLua/earlybird-sdd) - Software design document
- [Mars](https://github.com/ANcpLua/Mars) - Mars moons visibility calculator
- [MateMate](https://github.com/ANcpLua/MateMate) - Chess application architecture
- [Tools Corner](https://github.com/ANcpLua/Optional-Home-Exercise-Tools-Corner) - Kiro IDE orchestrator

---

## Course Structure

> [!NOTE]
> **Course Format:** 4 evenings (2+4+4+4 hours) | **Total:** ~40 hours with homework

### Evening 1: Importance of Architecture
> Understanding why architecture matters and the cost of decisions

<details open>
<summary><b>1 Exercise</b></summary>

- **[01-architectural-decisions-hard-to-change](Evening%201%20-%20Importance%20of%20Architecture/01-architectural-decisions-hard-to-change)** - Decision significance analysis, ADR templates, cost-of-change frameworks

</details>

### Evening 2: Architectural Quality
> Quality analysis using dependency matrices, interface design, and architectural principles

<details open>
<summary><b>8 Exercises</b></summary>

- **[01-building-block-quality-analysis](Evening%202%20-%20Architectural%20Quality/01-building-block-quality-analysis)** - Dependency matrix analysis and cohesion measurement
- **[02-isearchproduct-interface-specification](Evening%202%20-%20Architectural%20Quality/02-isearchproduct-interface-specification)** - O-Interface specification methodology
- **[03-isearchproduct-peer-review](Evening%202%20-%20Architectural%20Quality/03-isearchproduct-peer-review)** - Interface quality checklist (11-question framework)
- **[04-ilist-interface-design](Evening%202%20-%20Architectural%20Quality/04-ilist-interface-design)** - Generic IList interface design
- **[05-ilist-peer-review](Evening%202%20-%20Architectural%20Quality/05-ilist-peer-review)** - Peer review of IList specification
- **[06-heat-flow-analysis-tell-dont-ask](Evening%202%20-%20Architectural%20Quality/06-heat-flow-analysis-tell-dont-ask)** - Tell, Don't Ask principle demonstration
- **[07-charts-products-architecture-story](Evening%202%20-%20Architectural%20Quality/07-charts-products-architecture-story)** - Real-world copy-paste architecture case study (SRP, CCP, DIP violations)
- **[08-climate-model-architecture-analysis](Evening%202%20-%20Architectural%20Quality/08-climate-model-architecture-analysis)** - Stability analysis with change frequency (SDP violations)

</details>

### Evening 3: Architecture Development
> Systematic architecture development from requirements

<details open>
<summary><b>6 Exercises</b></summary>

- **[01-disease-architecture-from-class-diagram](Evening%203%20-%20Architecture%20Development/01-disease-architecture-from-class-diagram)** - Hospital management system (26 classes → 6 subsystems)
- **[02-ai-driven-requirement-clustering](Evening%203%20-%20Architecture%20Development/02-ai-driven-requirement-clustering)** - AI-driven architecture using embeddings (44 requirements → 11 components)
- **[03-mars-application-core](Evening%203%20-%20Architecture%20Development/03-mars-application-core)** - Pure application core implementation (Python)
- **[04-earlybird-application-core](Evening%203%20-%20Architecture%20Development/04-earlybird-application-core)** - Evolution scenario analysis for EarlyBird system
- **[05-matemate-service-based-architecture](Evening%203%20-%20Architecture%20Development/05-matemate-service-based-architecture)** - SE4 method application (chess application)
- **[matemate-service-elicitation-results](Evening%203%20-%20Architecture%20Development/matemate-service-elicitation-results)** - Service elicitation phase results (10 services)

</details>

> [!TIP]
> Complete **Mars02** before **EarlyBird12** - small application core principles apply to larger systems.

### Evening 4: Architecture Documentation
> Industry-standard documentation frameworks and patterns

<details open>
<summary><b>2 Exercises</b></summary>

- **[01-tools-corner](Evening%204%20-%20Architecture%20Documentation/01-tools-corner)** - Kiro IDE orchestrator (optional home exercise)
- **[02-custom-architecture-frameworks](Evening%204%20-%20Architecture%20Documentation/02-custom-architecture-frameworks)** - Complete MateMate example using arc42 (7 chapters) + C4 Model (C1, C2)

</details>

---

## Key Concepts

<table>
<tr><td>

**Architectural Principles**

SRP, OCP, LSP, ISP, DIP, CCP, CRP, SDP, SAP, ADP

</td><td>

**Quality Attributes**

Modifiability, testability, maintainability, scalability

</td></tr>
<tr><td>

**Design Patterns**

Application Core, Tell Don't Ask, Interface Segregation, Dependency Inversion

</td><td>

**Documentation**

arc42 template, C4 Model, Architecture Decision Records (ADR)

</td></tr>
</table>

**Development Methods**

SE4 (Service Elicitation → Subsystem Establishment → Explanation → Evaluation), Requirements-driven architecture, AI-assisted design

---

## Repository Structure

<details open>
<summary><b>Evening 1 - Importance of Architecture</b></summary>

- 01-architectural-decisions-hard-to-change

</details>

<details open>
<summary><b>Evening 2 - Architectural Quality</b></summary>

- 01-building-block-quality-analysis
- 02-isearchproduct-interface-specification
- 03-isearchproduct-peer-review
- 04-ilist-interface-design
- 05-ilist-peer-review
- 06-heat-flow-analysis-tell-dont-ask
- 07-charts-products-architecture-story
- 08-climate-model-architecture-analysis

</details>

<details open>
<summary><b>Evening 3 - Architecture Development</b></summary>

- 01-disease-architecture-from-class-diagram
- 02-ai-driven-requirement-clustering
- 03-mars-application-core
- 04-earlybird-application-core
- 05-matemate-service-based-architecture
- matemate-service-elicitation-results

</details>

<details open>
<summary><b>Evening 4 - Architecture Documentation</b></summary>

- 01-tools-corner
- 02-custom-architecture-frameworks

</details>

---

## Learning Path

**Foundations** (Evening 1)
Start with understanding why architecture matters and the cost of decisions.

**Quality Analysis** (Evening 2)
Learn to analyze existing architectures using principles and metrics.

**Development** (Evening 3)
Apply systematic methods to develop architectures from requirements.

**Documentation** (Evening 4)
Master professional documentation using arc42 and C4 Model.

---

## Exercise Standards

Each exercise includes:

- README with learning objectives and task description
- Analysis or solution document with comprehensive content
- Slides with visual diagrams and specifications
- Cross-references to related exercises

---

## Technologies

**Languages:** Python, C#, Java
**Frameworks:** .NET, Spring Boot
**Tools:** Mermaid (diagrams), PlantUML, Qdrant (vector database)
**Documentation:** Markdown, arc42, C4 Model

---

## Running Code Exercises

### Mars Application Core (Python)

```bash
cd "Evening 3 - Architecture Development/03-mars-application-core"
python3 mars_moon_core.py
python3 -m unittest -v
```

### AI-Driven Requirement Clustering (Python + Vector Database)

```bash
cd "Evening 3 - Architecture Development/02-ai-driven-requirement-clustering"
python3 main.py  # Run clustering experiment
docker run -p 6333:6333 qdrant/qdrant  # Start vector database
python3 qdrant_ingest.py  # Load results
```

---

## References

- [arc42 Documentation Template](https://arc42.org/)
- [C4 Model for Software Architecture](https://c4model.com/)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Package Principles (Martin)](https://en.wikipedia.org/wiki/Package_principles)

