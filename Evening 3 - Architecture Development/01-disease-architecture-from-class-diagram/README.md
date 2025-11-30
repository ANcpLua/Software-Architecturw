# Dis*Ease Hospital Management System

**Exercise ID:** Dis*Ease01
**Title:** Requirements Class Diagram Based Architecture Development

Design a software architecture for a hospital management system starting from a requirements class diagram.

---

## Exercise Overview

This exercise demonstrates how to develop a software architecture starting from a **requirements class diagram**. The
Dis*Ease system serves as a case study for understanding the transition from requirements modeling to architectural
design.

### The Exercise Task

Design the architecture for the hospital management system (Dis*Ease) based on the requirements class diagram.

**Constraints:**

- The architecture should consist of **4-6 building blocks**
- Each class from the requirements class diagram should be assigned to **exactly one building block**
- Building blocks should be cohesive and follow architectural principles

**Expected Result:** A subsystem architecture where each building block groups cohesive domain classes.

---

## Approach

1. **Requirements Analysis:** Understand the domain model classes and relationships
2. **Component Identification:** Group classes into cohesive building blocks
3. **Dependency Analysis:** Define relationships between subsystems
4. **Architecture Validation:** Ensure all classes mapped, principles applied

---

## Result

**6 subsystems** for 26 domain classes (~4 classes per subsystem)

- **Design Principles:** SRP, SDP, CCP, ADP applied
- **Alternative:** 4-subsystem coarse-grained architecture also provided
- **Evolution Scenarios:** Validated with telemedicine, insurance, multi-hospital

See [**architecture-analysis.md**](architecture-analysis.md) for full analysis.

---

## Architecture

See [**architecture-analysis.md**](architecture-analysis.md) for subsystem descriptions:

- Subsystem 1: Patient Management (8 classes)
- Subsystem 2: Medical Procedures & Workflow (8 classes)
- Subsystem 3: Staff Management (13 classes)
- Subsystem 4: Organization & Facilities (3 classes)
- Subsystem 5: Shared Domain Model (1 class)
- Alternative: Imaging & Diagnostics (could be separated)

---

## Files

### Documentation

- **README.md** - This file
- **architecture-analysis.md** - Complete architecture analysis

### Reference Materials

- **slides/** - Exercise slides and diagrams
- **slides/slide_disease_exercise.png** - Exercise specification with class diagram

---

## The Dis*Ease System

The Dis*Ease system is a comprehensive hospital management system:

**Patient Management:**
- Patient records, admissions, personal information
- Service episodes and clinical documentation

**Medical Procedures:**
- Procedure planning, scheduling, execution
- Imaging service requests and protocols

**Staff Management:**
- Hospital personnel (doctors, nurses, technicians)
- Administrative and technical staff

**Facility Management:**
- Hospital departments, rooms, resources
- Organizational structure

---

## Learning Outcomes

This exercise demonstrates:

1. **Requirements-to-Architecture:** Transforming class diagrams into components
2. **Component Identification:** Deriving building blocks from domain concepts
3. **Dependency Management:** Managing subsystem relationships
4. **Architecture Principles:** Applying SRP, SDP, CCP, ADP
5. **Architecture Validation:** Ensuring requirements coverage

---

## Related Materials

See [**architecture-analysis.md**](architecture-analysis.md) for:

- Complete subsystem design with architecture diagram
- Class-to-subsystem mapping (all 26 classes)
- Dependency analysis and rationale
- Evolution scenarios validation
- Implementation recommendations
- Security and compliance considerations (HIPAA, HL7 FHIR)

---

## Related Exercises

- [Using AI to Develop an Architecture](../02-ai-driven-requirement-clustering/) (ArchitectureDevelopment02)
- [Service Based Architecture Development](../05-matemate-service-based-architecture/) (MateMate02)

---
