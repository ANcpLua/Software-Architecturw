# Exercise: Requirements Class Diagram Based Architecture Development

**Exercise ID:** Dis*Ease01
**Source:** 1_Architecture_Development_V702.pdf, Page 95
**Type:** Exercise

## Overview

This exercise demonstrates how to develop a software architecture starting from a requirements class diagram. The Dis*
Ease system serves as a case study for understanding the transition from requirements modeling to architectural design.

## Exercise Description

**Task:** Design the architecture for the hospital management system (Dis*Ease).

**Constraints:**

- The architecture should consist of **4-6 building blocks**
- Each class from the requirements class diagram should be assigned to **exactly one building block**
- Building blocks should be cohesive and follow architectural principles

**Time:** Group exercise (45-60 minutes)

## Learning Objectives

- Transforming requirements class diagrams into architectural components
- Identifying architectural building blocks from requirements
- Mapping domain concepts to architectural elements
- Understanding the relationship between requirements and architecture
- Applying systematic architecture development methods

## The Dis*Ease System

The Dis*Ease system is a comprehensive hospital management system that handles:

- **Patient Management** - Patient records, admissions, personal information
- **Medical Procedures** - Procedure planning, scheduling, execution, and tracking
- **Staff Management** - Hospital personnel (doctors, nurses, technicians, administrative staff)
- **Facility Management** - Hospital departments, rooms, and resources
- **Imaging Services** - Medical imaging requests and procedures
- **Clinical Documentation** - Service episodes, visits, and clinical records

### Requirements Class Diagram

The system's domain model includes:

**Patient & Person Management:**

- `Person` - Base class with personal information (name, birthdate, gender, contact details)
- `Patient` - Extends Person, represents hospital patients
- `Hospital` - Hospital information and location
- `Department` - Hospital departments
- `Staff` - Hospital personnel (Operations, Administrative, Technical)
    - `Doctor`, `Nurse`, `Surgeon` (Operations Staff)
    - `Front Desk Staff`, `Receptionist` (Administrative Staff)
    - `Technician`, `Technologist`, `Surgical Technologist` (Technical Staff)

**Medical Procedures:**

- `Procedure Plan` - Planned medical procedures
- `Requested Procedure` - Procedures requested by physicians
- `Scheduled Procedure Step` - Scheduled steps in a procedure
- `Procedure Type` - Types of medical procedures
- `Modality Performed Procedure Step` - Executed procedure steps
- `Protocol Code` - Procedure protocols
- `Series` - Imaging series data

**Service & Episodes:**

- `Service Episode` - Patient care episodes
- `Visit` - Patient visits to hospital
- `Facility` - Hospital facilities

**Clinical Documents:**

- `Clinical Document` - Medical documentation
- `Imaging Service Request` - Requests for imaging services

### Key Relationships

- Patients have service episodes and visits
- Visits include requested procedures
- Staff members perform procedures
- Procedures are scheduled in facilities
- Imaging requests specify procedures and modalities

## Methodology

This exercise likely follows a systematic approach:

1. **Requirements Analysis** - Understanding the class diagram
2. **Component Identification** - Deriving architectural components
3. **Interface Design** - Defining component interfaces
4. **Architecture Validation** - Ensuring requirements coverage

## Files

- `README.md` - This file
- `architecture-analysis.md` - ✅ Complete architecture analysis
- `slides/slide_disease_exercise.png` - Exercise specification with class diagram
- `slides/` - Exercise slides and diagrams

## Solution Overview

The analysis proposes a **6-subsystem architecture**:

1. **Patient Management** - Patient lifecycle, visits, clinical documents (8 classes)
2. **Medical Procedures & Workflow** - Procedure planning, scheduling, execution (8 classes)
3. **Staff Management** - All staff types: Operations, Administrative, Technical (13 classes)
4. **Organization & Facilities** - Hospital, departments, facilities (3 classes)
5. **Shared Domain Model** - Person base class and common entities (1 class)
6. **Alternative: Imaging & Diagnostics** - Could be separated if needed

**Alternative:** 4-subsystem coarse-grained architecture also provided.

**Key Principles Applied:**

- Single Responsibility Principle (SRP)
- Stable Dependencies Principle (SDP)
- Common Closure Principle (CCP)
- Acyclic Dependencies Principle (ADP)

See [architecture-analysis.md](architecture-analysis.md) for:

- Complete subsystem design with architecture diagram
- Class-to-subsystem mapping (all 26 classes)
- Dependency analysis and rationale
- Evolution scenarios (telemedicine, insurance, multi-hospital)
- Implementation recommendations (layered architecture, tech stack)
- Security and compliance considerations (HIPAA, HL7 FHIR)

## Related Exercises

- [Service Based Architecture Development](../05-matemate-service-based-architecture/) (MateMate02)
- [Using AI to Develop an Architecture](../02-ai-driven-requirement-clustering/) (ArchitectureDevelopment02)
