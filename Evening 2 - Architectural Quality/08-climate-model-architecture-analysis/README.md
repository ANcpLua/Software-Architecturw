# Climate Model Architecture Analysis

**Exercise ID:** ArchitecturalQuality08
**Type:** Group Exercise
**Evening:** 2 - Architectural Quality

---

## Overview

Analyze the architectural weaknesses of a climate model system with 9 subsystems. This exercise focuses on identifying violations of the Stable Dependencies Principle (SDP) and understanding the impact of change frequency on system stability.

---

## Exercise Question

**Scenario:**
You are developing part of a climate model with the subsystems shown in the table. The "uses" column shows the subsystems used by each subsystem (e.g., DYN uses APPG).

**Question:** What are the weaknesses of this architecture?

---

## The Climate Model Subsystems

| Subsystem | Description | Changes/Year | Uses |
|-----------|-------------|--------------|------|
| **APPG** | Keeps air pressure and population growth data | 5x | DE, CHK |
| **APC** | Checks air pressure data for plausibility and converts to JSON | 5x | APPG |
| **DE** | Solves differential equations | 1x | DE1 |
| **DE1** | Solves first order differential equations | 1x | none |
| **STL** | Statistics library | 1x | none |
| **DYN** | Models the laws of aerodynamics | 1x | APPG |
| **NNW** | Neural network for forecasting | 12x | none |
| **FCA** | Performs forecasts | **150x** | APPG, DYN, STL, NNW |
| **CHK** | Checks plausibility of forecasts | 5x | FCA |

---

## Key Observation

**Critical Issue:** FCA changes **150 times per year** - 30x more than most other components!

This extreme volatility creates cascading stability problems throughout the architecture.

---

## Files

- [climate-model-analysis.md](climate-model-analysis.md) - Complete architectural weakness analysis
- `slides/slide_climate_model_subsystems.png` - Exercise slide with subsystem table

---

## Principles to Apply

**Focus Areas:**
- **SDP (Stable Dependencies Principle)** - Depend in the direction of stability
- **CCP (Common Closure Principle)** - Classes that change together should be packaged together
- **Change Impact Analysis** - Understanding ripple effects of changes

---

## Key Learning

**The Problem:**
- Stable components (DYN: 1x/year) depend on volatile ones (APPG: 5x/year)
- Very stable components (CHK: 5x/year) depend on extremely volatile ones (FCA: 150x/year)
- High-volatility component (FCA) has many dependencies

**The Consequence:**
- Changes propagate unpredictably
- Stable code becomes unstable
- Testing burden increases exponentially

**The Solution:**
- Invert dependencies using abstractions
- Isolate volatile components
- Apply Dependency Inversion Principle (DIP)

---

## Analysis Framework

Use these questions when analyzing:

1. **Identify volatility:** Which components change most frequently?
2. **Map dependencies:** Who depends on whom?
3. **Find violations:** Do stable components depend on volatile ones?
4. **Calculate impact:** How many components affected by a change?
5. **Propose fixes:** Where should abstractions be introduced?

---

## See Also

- [Charts/Products Analysis](../07-charts-products-architecture-story/) - Another principle violation case study
- [Building Block Quality](../01-building-block-quality-analysis/) - Cohesion analysis methodology
- [Heat Flow Analysis](../06-heat-flow-analysis-tell-dont-ask/) - Tell, Don't Ask principle
