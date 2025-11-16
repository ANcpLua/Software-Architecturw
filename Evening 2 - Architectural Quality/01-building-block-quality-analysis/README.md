# Class Group Exercise: Quality of Building Blocks

## Exercise Context

**Exercise ID:** ArchitecturalQuality01
**Evening:** 2
**Type:** Class Group Exercise
**Topic:** Internal Quality (Cohesion) Analysis

## Problem

Analyze the internal quality (cohesion) of a building block using a dependency matrix.

**The Building Block:** مکان نکهش (Location Display - appears to be in Persian/Arabic)

**Task:** Ignore the arrows for now. What can you say about the quality of the building block مکان نکهش just by looking
at the matrix?

## The Dependency Matrix

The slide shows:

- A central building block (مکان نکهش)
- Multiple dependent components (shown with dashed green arrows)
- A dependency matrix showing relationships between components
- Components labeled with Persian/Arabic text

## What You'll Learn

- **Cohesion measurement** - Using dependency matrices to measure internal coupling
- **Building block quality** - How to assess if a component has good internal structure
- **Dependency patterns** - Recognizing cohesive vs. scattered dependencies
- **Matrix analysis** - Reading dependency matrices to spot architectural issues

## Key Concepts

### Cohesion

How closely related the responsibilities within a building block are. High cohesion = good quality.

### Dependency Matrix

A table showing which components depend on which other components:

- Rows and columns represent components
- Dots (•) indicate dependencies
- Empty cells mean no dependency

### Analysis Questions

1. Are the dependencies clustered (high cohesion)?
2. Are they scattered across the matrix (low cohesion)?
3. Do components have many dependencies on each other?
4. Are there isolated components?

## Discussion Format

This is an **in-class group exercise** - analyze the matrix together and discuss findings.

**Key Question:** Based on the dependency pattern in the matrix, is this building block well-designed or does it need
refactoring?

## Related Principles

- **SRP (Single Responsibility Principle)** - Each building block should have one reason to change
- **CCP (Common Closure Principle)** - Things that change together should be packaged together
- **Cohesion metrics** - Measuring internal coupling strength

## Slides

- [slide_architecturalquality01.png](slides/slide_architecturalquality01.png)

## Source

**PDF:** Architectural_Quality_V701.pdf
**Page:** Approximately page 15 (Class Group Exercise section)
