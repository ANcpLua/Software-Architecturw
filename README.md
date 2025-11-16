# Software Architecture Course Exercises

Comprehensive software architecture exercises covering architectural principles, quality analysis, development methods, and documentation frameworks.

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

### Evening 1: Importance of Architecture
Focus on understanding why architecture matters and the cost of architectural decisions.

- **01-architectural-decisions-hard-to-change** - Decision significance analysis, ADR templates, cost-of-change frameworks

### Evening 2: Architectural Quality
Deep dive into quality analysis using dependency matrices, interface design, and architectural principles.

- **01-architecture-real-life-story** - Real-world case study of copy-paste architecture (SRP, CCP, DIP violations)
- **01-building-block-quality-analysis** - Dependency matrix analysis and cohesion measurement
- **02-climate-model-analysis** - Stability analysis with change frequency (SDP violations)
- **02-isearchproduct-interface-specification** - O-Interface specification methodology
- **03-isearchproduct-peer-review** - Interface quality checklist (11-question framework)
- **03-mars-moons-application-core** - Application core implementation (Python)
- **04-ilist-interface-design** - ISP analysis and covariance patterns
- **06-heat-flow-analysis-tell-dont-ask** - Tell, Don't Ask principle demonstration
- **09-bigger-application-core** - Evolution scenario analysis for EarlyBird system

### Evening 3: Architecture Development
Methods for systematic architecture development from requirements.

- **01-disease-requirements-class-diagram** - Hospital management system (26 classes → 6 subsystems)
- **EarlyBirdML** - AI-driven architecture using embeddings (44 requirements → 11 components)
- **MateMate02-service-based-architecture** - SE4 method application (chess application)
- **matemate-service-elicitation-results** - Service elicitation phase results (10 services)

### Evening 4: Architecture Documentation
Industry-standard documentation frameworks and patterns.

- **architectural-frameworks** - Complete MateMate example using arc42 (7 chapters) + C4 Model (C1, C2)

---

## Key Concepts

**Architectural Principles:** SRP, OCP, LSP, ISP, DIP, CCP, CRP, SDP, SAP, ADP

**Quality Attributes:** Modifiability, testability, maintainability, scalability

**Design Patterns:** Application Core, Tell Don't Ask, Interface Segregation, Dependency Inversion

**Documentation:** arc42 template, C4 Model, Architecture Decision Records (ADR)

**Development Methods:** SE4 (Service Elicitation → Subsystem Establishment → Explanation → Evaluation), Requirements-driven architecture, AI-assisted design

---

## Repository Structure

```
Software-Architecture/
├── Evening 1 - Importance of Architecture/
│   └── 01-architectural-decisions-hard-to-change/
├── Evening 2 - Architectural Quality/
│   ├── 01-architecture-real-life-story/
│   ├── 01-building-block-quality-analysis/
│   ├── 02-climate-model-analysis/
│   ├── 02-isearchproduct-interface-specification/
│   ├── 03-isearchproduct-peer-review/
│   ├── 03-mars-moons-application-core/
│   ├── 04-ilist-interface-design/
│   ├── 06-heat-flow-analysis-tell-dont-ask/
│   └── 09-bigger-application-core/
├── Evening 3 - Architecture Development/
│   ├── 01-disease-requirements-class-diagram/
│   ├── EarlyBirdML/
│   ├── MateMate02-service-based-architecture/
│   └── matemate-service-elicitation-results/
└── Evening 4 - Architecture Documentation/
    └── architectural-frameworks/
```

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

### Mars Moons Application Core (Python)
```bash
cd "Evening 2 - Architectural Quality/03-mars-moons-application-core"
python3 mars_moon_core.py
python3 -m unittest -v
```

### EarlyBirdML (Python + Vector Database)
```bash
cd "Evening 3 - Architecture Development/EarlyBirdML"
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

---

## Repository Statistics

- 55 markdown documentation files
- 48 PNG slide images
- 15 PDF documents
- 14 complete exercises (100% coverage)
- Zero placeholders, duplicates, or technical debt

---

## Contributing

This repository is part of a software architecture course. Exercises are based on established architectural principles and industry best practices.
