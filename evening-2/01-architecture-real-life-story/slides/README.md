# Exercise Slides - ArchitecturalQuality10

This folder contains the exercise slide for **ArchitecturalQuality10: Architecture - A Real-Life Story**.

## Slide Images

Place the following slide image here:

1. `slide_architecturalquality10.png` - Class Group Exercise: Architecture - A Real-Life Story
   - Shows Product1 and Product2 architecture evolution
   - Common Core with Charts functionality duplication
   - Demonstrates principle violations through copy-paste architecture

## Exercise Context

**Exercise ID:** ArchitecturalQuality10
**Evening:** 2
**Type:** Group
**PDF:** Page 217 in Architectural Quality slides

**Task:** Which architectural principles (most but not all have three letters) from this document were violated here?

**Scenario:**
1. Product1 needed chart functionality (bar chart, pie chart, etc.)
2. Common Core was extended to include chart functionality
3. Product2 needed charts too - sources were copied into Charts2 component
4. Charts2 is massively enhanced with new mandatory attributes
5. At this point, the architect is involved for the first time

**Question:** You should be able to present your results.

**Violated Principles to Identify:**
- SRP (Single Responsibility Principle)
- OCP (Open-Closed Principle)
- DIP (Dependency Inversion Principle)
- CCP (Common Closure Principle)
- CRP (Common Reuse Principle)
- SDP (Stable Dependencies Principle)
- SAP (Stable Abstractions Principle)

**Key Insight:** This demonstrates the dangers of copy-paste architecture and lack of early architectural involvement.
