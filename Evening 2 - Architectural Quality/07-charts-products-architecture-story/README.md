# Architecture Real-Life Story: Charts/Products Analysis

**Exercise ID:** ArchitecturalQuality10
**Type:** Group Exercise
**Evening:** 2 - Architectural Quality

---

## Overview

Analyze a real-world architecture evolution story where copy-paste architecture led to violation of fundamental architectural principles. This exercise demonstrates the consequences of poor architectural decisions and highlights the importance of early architect involvement.

---

## Exercise Task

**Scenario:**
1. Product1 needed chart functionality (bar charts, pie charts, etc.)
2. Common Core was extended to include chart functionality
3. Product2 needed charts - sources were copied to create Charts2 component
4. Charts2 was massively enhanced with new mandatory attributes
5. Architect gets involved for the first time at this point

**Question:** Which architectural principles were violated here? You should be able to present your results.

---

## Files

- [architectural-principles-analysis.md](architectural-principles-analysis.md) - Complete analysis of violated principles
- `slides/` - Exercise slides showing the architecture evolution

---

## Principles to Consider

This exercise tests knowledge of:
- **SRP** (Single Responsibility Principle)
- **OCP** (Open-Closed Principle)
- **DIP** (Dependency Inversion Principle)
- **CCP** (Common Closure Principle)
- **CRP** (Common Reuse Principle)
- **SDP** (Stable Dependencies Principle)
- **SAP** (Stable Abstractions Principle)

---

## Key Learning

**The Problem:** Copy-paste architecture creates:
- Code duplication
- Inconsistent bug fixes
- Maintenance nightmares
- Violated architectural principles

**The Solution:** Early architect involvement to:
- Identify shared abstractions
- Prevent code duplication
- Ensure proper separation of concerns
- Apply dependency inversion

---

## See Also

- [Climate Model Analysis](../08-climate-model-architecture-analysis/) - Another architectural quality exercise
- [Building Block Quality](../01-building-block-quality-analysis/) - Quality assessment methodology
