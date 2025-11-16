# Class Group Exercise: Service Based Architecture Development

**Exercise ID:** MateMate02
**Source:** 1_Architecture_Development_V702.pdf, Page 73
**Type:** Class Group Exercise

## Overview

This exercise guides you through the development of a service-based architecture for the MateMate system. Service-based architecture is a crucial architectural pattern that helps organize complex systems into manageable, loosely-coupled services.

## Exercise Description

This exercise continues the MateMate architecture development using the **SE4 method** (Service Elicitation → Subsystem Establishment → System Explanation → System Evaluation). Service Elicitation has been completed (see related exercise). This exercise focuses on the remaining phases:

**Phase 2: Subsystem Establishment**
- Create list of subsystems
- Map services to subsystems
- Define good names for each subsystem
- Specify "blood type" (stability/volatility) of each subsystem
- Create allowed-to-use specification

**Phase 3: System Explanation**
- Document architecture views
- Create component diagrams
- Define interfaces between subsystems

**Phase 4: System Evaluation**
- Validate architecture against requirements
- Review quality attributes
- Create architecture proposal

**Deliverable:** Digital documentation of architecture proposal from your group.

## Learning Objectives

- Understanding service-based architecture principles
- Identifying service boundaries
- Designing service interfaces
- Managing service dependencies
- Applying service decomposition strategies

## Related Content

- [MateMate Service Elicitation Results](../matemate-service-elicitation-results/) - Results and analysis
- [Bigger Application Core](../04-bigger-application-core/) (EarlyBird12)

## MateMate System

MateMate is a desktop chess application developed by Queen&King Inc.

### System Description

- Plays chess against a human opponent who makes moves via mouse/keyboard
- Thinks ahead several moves and evaluates possible future positions
- Calculates numerical scores for each future position
- Selects and displays the optimal move by moving the chess piece
- Implements standard chess rules and validates legal moves

### Architecture Development Status

**Phase 1: Service Elicitation** - COMPLETE
- 10 services identified (see [service elicitation results](../matemate-service-elicitation-results/))

**Phase 2-4: This Exercise** - IN PROGRESS
- Subsystem establishment
- System explanation
- System evaluation

## Files

- `README.md` - This file
- `slides/` - Exercise slides showing SE4 method phases
  - `slide_matemate02_01.png` - SE4 workflow and deliverables
  - `slide_matemate02_02.png` - MateMate system description
  - `MateMate02-service-based-architecture.pdf` - Complete exercise slides

## Deliverables

Groups should produce:
1. List of subsystems with rationale
2. Service-to-subsystem mapping table
3. Subsystem names and descriptions
4. Blood type specification (stability levels)
5. Allowed-to-use matrix
6. Architecture diagram
7. Quality evaluation
