# Evening 4 - Architecture Documentation

**Focus:** Architecture Frameworks (arc42 + C4 Model)
**Type:** Documentation Examples & Exercises

---

## Overview

Evening 4 demonstrates comprehensive architectural documentation using industry-standard frameworks. You'll learn how to
document system architecture using arc42 and C4 Model, and understand when to use each framework.

---

## Exercises

### 1. Architectural Frameworks (MateMate Example)

**Location:** [02-custom-architecture-frameworks/matemate/](02-custom-architecture-frameworks/matemate/)

**Description:** Complete architectural documentation example using MateMate (Desktop Chess Application) as the case
study.

**What's Included:**

- **C4 Model** (2 levels)
    - C1: System Context
    - C2: Container View
- **arc42** (7 chapters)
    - Chapter 1: Introduction & Goals
    - Chapter 3: Context & Scope
    - Chapter 5: Building Blocks
    - Chapter 6: Runtime View
    - Chapter 8: Cross-Cutting Concepts
    - Chapter 9: Design Decisions
    - Chapter 10: Quality Requirements
- **Extended Concepts**
    - Allowed-to-Use Matrix
    - Change Impact Heatmap
    - FinOps & Cost Governance
    - Sustainability Analysis

Complete documentation example.

---

### 2. Optional Home Exercise: Tools Corner

**Location:** [01-tools-corner/](01-tools-corner/)

**Description:** Kiro IDE Orchestrator architecture presentations

**Files:**

- Kiro_IDE_Orchestrator_NEW_FH.pptx
- Kiro_IDE_Orchestrator_Old_FH.pptx
- README (3).md

Presentation files for tools corner discussion.

---

## Learning Objectives

1. **Understand arc42 framework**
    - Know which chapters to use and when
    - Learn how to structure architectural documentation

2. **Master C4 Model**
    - System Context vs. Container View
    - When to stop (no need for C3/C4 in most cases)

3. **Combine frameworks effectively**
    - Use C4 for visual diagrams
    - Use arc42 for comprehensive documentation
    - Add governance views (FinOps, sustainability)

4. **Create practical documentation**
    - Focus on what stakeholders need
    - Avoid documentation for documentation's sake
    - Maintain living documentation

---

## Key Concepts

### arc42 Template

Lightweight architecture documentation template with 12 chapters (we use 7)

### C4 Model

Hierarchical diagram approach: Context → Containers → Components → Code (we use first 2)

### Extended Framework

Combines arc42 + C4 + governance views for complete picture

### Architecture Decision Records (ADRs)

Document why decisions were made, not just what was decided

---

## Files

- `02-custom-architecture-frameworks/` - Complete MateMate documentation example
- `01-tools-corner/` - Tools Corner presentations
- `slides/` - Evening 4 slide deck and exercise slides

---

## See Also

- [MateMate README](02-custom-architecture-frameworks/matemate/README.md) - Framework overview
- [arc42 Template](https://arc42.org/) - Official arc42 documentation
- [C4 Model](https://c4model.com/) - Official C4 Model documentation

---
