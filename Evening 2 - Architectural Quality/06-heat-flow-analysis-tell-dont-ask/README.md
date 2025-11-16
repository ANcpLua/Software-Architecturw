# Self Check Exercise: Heat Flow Calculator

## Exercise Context

**Exercise ID:** ArchitecturalQuality09
**Type:** Self-Check
**Topic:** Architectural Quality Analysis

## Problem

Analyze the architectural weaknesses in a heat flow regulation system.

The `Room` class knows its desired and actual temperatures. At regular intervals, the `HeatFlowRegulator` calls:

- `get_desired_temp()`
- `get_actual_temp()`

And compares the results. If the desired temperature is higher than actual, `HeatFlowRegulator` calls the `Furnace`
class to heat up the room.

**Question:** Do you see any weaknesses in this architecture?

## Architecture Components

- **Room** - Stores desired temperature, actual temperature, and occupancy
- **HeatFlowRegulator** - Polls temperatures and controls furnace
- **Furnace** - Heats the room when instructed

## What You'll Learn

- Tell, Don't Ask principle
- Information hiding violations
- Procedural vs object-oriented design
- How polling architectures create tight coupling

## Source

Arthur J. Riel, Object-Oriented Design Heuristics, Addison Wesley, 1996

## Slides

- [slide_architecturalquality09.png](slides/slide_architecturalquality09.png)
