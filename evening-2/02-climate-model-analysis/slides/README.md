# Exercise Slides - ArchitecturalQuality08

This folder contains the exercise slide for **ArchitecturalQuality08: Climate Model**.

## Slide Images

Place the following slide image here:

1. `slide_architecturalquality08.png` - Class Group Exercise: Climate Model
   - Shows climate model subsystems dependency table
   - 9 subsystems: APPG, APC, DE, DE1, STL, DYN, NNW, FCA, CHK
   - "uses" column shows dependencies
   - "changes per year" column shows stability (1x to 150x)

## Exercise Context

**Exercise ID:** ArchitecturalQuality08
**Evening:** 2
**Type:** Group
**PDF:** Page 219 in Architectural Quality slides

**Task:** Analyze the architectural weaknesses of this climate model.

**Key Question:** What are the weaknesses of this architecture?

**Focus Areas:**
- Stable Dependencies Principle (SDP) violations
- Components with high change frequency (FCA changes 150x/year)
- Unstable dependencies (stable components depending on volatile ones)
- Change impact analysis

**Subsystems:**
- APPG: Keeps air pressure and population growth data (5x changes/year)
- APC: Checks air pressure data and converts to JSON (5x changes/year)
- DE: Solves differential equations (1x changes/year)
- DE1: Solves first order differential equations (1x changes/year)
- STL: Statistics library (1x changes/year)
- DYN: Models laws of aerodynamics (1x changes/year)
- NNW: Neural network for forecasting (12x changes/year)
- FCA: Performs forecasts (150x changes/year) - HIGH VOLATILITY
- CHK: Checks plausibility of forecasts (5x changes/year)
