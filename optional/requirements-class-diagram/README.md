# Exercise: Requirements Class Diagram Based Architecture Development

## Exercise Context

**Exercise ID:** Dis*Ease01
**Type:** Exercise
**Topic:** Class Diagram to Architecture Mapping

## Task

Design the architecture for the hospital management system **Dis*Ease**.

The architecture should consist of **4-6 building blocks**.

**Each class should be in exactly one of them.**

## The Class Diagram

The provided class diagram shows the domain model for a hospital management system with:

**Patient Management:**
- Patient (Person attributes: name, gender, address, etc.)
- Clinical Document
- Service Episode
- Visit

**Medical Procedures:**
- Imaging Service Request
- Requested Procedure
- Procedure Plan
- Protocol Code
- Scheduled Procedure Step
- Modality Performed Procedure Step
- Series

**Hospital Organization:**
- Hospital
- Department
- Staff (with subtypes: Operations Staff, Administrative Staff, Technical Staff)
  - Doctor, Nurse (Operations)
  - Front Desk Staff, Receptionist (Administrative)
  - Technician, Technologist, Surgical Technologist (Technical)
- Facility
- Procedure Type

## What You'll Learn

- Mapping domain models to architectural building blocks
- Identifying cohesive component boundaries from class relationships
- Balancing granularity (4-6 components, not too many, not too few)
- The relationship between domain-driven design and architecture

## Challenge

How do you group these 25+ classes into 4-6 cohesive architectural components?

## Slides

- [slide_disease01.png](slides/slide_disease01.png)
