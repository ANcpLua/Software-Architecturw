# Dis*Ease Hospital Management System - Architecture Analysis

**Exercise ID:** Dis*Ease01
**Type:** Requirements Class Diagram Based Architecture Development
**Domain:** Hospital Management System

---

## Exercise Overview

Design the architecture for a hospital management system based on a requirements class diagram. The architecture should
consist of **4-6 building blocks** (subsystems), with each class assigned to exactly one building block.

---

## Requirements Class Diagram Analysis

### Domain Model Classes

The class diagram shows a comprehensive hospital management system with the following key entities:

#### **Patient Management**

- **Patient** - Central entity with service episodes
- **Person** - Base class for patients and staff (title, names, birth date, contact info)
- **Clinical Document** - Medical records
- **Imaging Service Request** - Radiology/imaging procedures
- **Visit** - Patient visits to facilities
- **Service Episode** - Treatment episodes

#### **Medical Procedures**

- **Requested Procedure** - Procedures ordered
- **Scheduled Procedure Step** - Scheduled procedure steps
- **Modality Performed Procedure Step** - Actual performed steps
- **Procedure Type** - Types of procedures
- **Procedure Plan** - Treatment plans
- **Protocol Code** - Medical protocols
- **Series** - Imaging series

#### **Staff & Organization**

- **Staff** (abstract) - Base staff class with education, certification, languages
    - **Operations Staff** - Medical staff (Doctors, Nurses)
        - **Doctor** - Physicians (with specialty, locations)
        - **Nurse** - Nursing staff
        - **Surgeon** - Surgical specialists
    - **Administrative Staff** - Non-medical staff
        - **Front Desk Staff** - Reception
        - **Receptionist** - Patient intake
    - **Technical Staff** - Technical specialists
        - **Technician** - Medical technicians
        - **Technologist** - Technical specialists
        - **Surgical Technologist** - Surgery support

#### **Facilities**

- **Hospital** - Hospital entity (name, address, phone)
- **Department** - Hospital departments
- **Facility** - Physical facilities

---

## Proposed Architecture: 6 Building Blocks

### Building Block 1: **Patient Management**

**Responsibilities:**

- Patient registration and demographics
- Patient visit tracking
- Clinical documentation
- Service episode management

**Classes:**

- Patient
- Person (shared)
- Clinical Document
- Visit
- Service Episode

**Rationale:** High cohesion - all classes related to patient lifecycle and information management.

---

### Building Block 2: **Medical Procedures & Workflow**

**Responsibilities:**

- Procedure planning and scheduling
- Procedure execution tracking
- Imaging service management
- Protocol management

**Classes:**

- Requested Procedure
- Scheduled Procedure Step
- Modality Performed Procedure Step
- Procedure Type
- Procedure Plan
- Protocol Code
- Imaging Service Request
- Series

**Rationale:** Cohesive set of classes managing the complete procedure workflow from request to execution.

---

### Building Block 3: **Staff Management**

**Responsibilities:**

- Staff registration and credentials
- Staff assignments
- Staff availability and scheduling

**Classes:**

- Staff (base class)
- Operations Staff
- Administrative Staff
- Technical Staff
- Doctor
- Nurse
- Surgeon
- Front Desk Staff
- Receptionist
- Technician
- Technologist
- Surgical Technologist

**Rationale:** All staff-related entities grouped together, supporting staff lifecycle management.

---

### Building Block 4: **Organization & Facilities**

**Responsibilities:**

- Hospital and department information
- Facility management
- Organizational structure

**Classes:**

- Hospital
- Department
- Facility

**Rationale:** Organizational entities that provide context for patients and staff.

---

### Building Block 5: **Shared Domain Model**

**Responsibilities:**

- Common value objects
- Shared data types
- Cross-cutting domain concepts

**Classes:**

- Person (base class used by Patient and Staff)

**Rationale:** Foundation classes used across multiple subsystems.

---

### Building Block 6: **Imaging & Diagnostics** (Alternative Organization)

**Alternative:** Could separate imaging-specific functionality:

**Classes (if separated):**

- Imaging Service Request
- Series
- Modality Performed Procedure Step (imaging-specific)

**Rationale:** Imaging could be a specialized subsystem if the hospital has a large radiology department.

---

## Architecture Diagram (Subsystem View)

```
┌─────────────────────────────────────────────────────────────┐
│              Dis*Ease Hospital Management System             │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────────┐         ┌──────────────────┐          │
│  │  Patient         │         │  Medical         │          │
│  │  Management      │◄───────►│  Procedures      │          │
│  │                  │         │  & Workflow      │          │
│  └────────┬─────────┘         └────────┬─────────┘          │
│           │                            │                     │
│           │                            │                     │
│           ▼                            ▼                     │
│  ┌──────────────────┐         ┌──────────────────┐          │
│  │  Organization    │         │  Staff           │          │
│  │  & Facilities    │◄───────►│  Management      │          │
│  │                  │         │                  │          │
│  └──────────────────┘         └──────────────────┘          │
│           │                            │                     │
│           │                            │                     │
│           └────────────┬───────────────┘                     │
│                        ▼                                     │
│              ┌──────────────────┐                            │
│              │  Shared Domain   │                            │
│              │  Model           │                            │
│              └──────────────────┘                            │
└─────────────────────────────────────────────────────────────┘
```

---

## Dependency Analysis

### Key Dependencies

**Patient Management → Medical Procedures**

- Patients have requested procedures
- Service episodes link to procedure steps

**Patient Management → Organization & Facilities**

- Patients visit facilities
- Patients are treated at hospitals

**Medical Procedures → Staff Management**

- Procedures are performed by operations staff
- Doctors and nurses execute procedure steps

**Staff Management → Organization & Facilities**

- Staff belong to departments
- Staff work at facilities

**All Subsystems → Shared Domain Model**

- All use Person base class
- Common value objects

---

## Alternative: 4-Subsystem Architecture

For a more coarse-grained design:

### 1. **Clinical Core** (Patient + Medical Procedures)

- Patient management
- Procedure workflow
- Clinical documentation
- Imaging services

### 2. **Human Resources** (Staff Management)

- Staff credentials
- Staff scheduling
- Staff assignments

### 3. **Infrastructure** (Organization & Facilities)

- Hospital/department structure
- Facility management
- Organizational hierarchy

### 4. **Shared Kernel** (Common Domain)

- Person entity
- Shared value objects
- Cross-cutting concerns

---

## Design Principles Applied

### 1. **Single Responsibility Principle (SRP)**

Each building block has one clear responsibility:

- Patient Management → Patient lifecycle
- Medical Procedures → Procedure workflow
- Staff Management → Staff administration
- Organization → Hospital structure

### 2. **Stable Dependencies Principle (SDP)**

- Shared Domain Model is most stable (no dependencies)
- Organization & Facilities are stable (infrastructure)
- Staff Management depends on stable Organization
- Patient Management depends on stable subsystems

### 3. **Common Closure Principle (CCP)**

Classes that change together are packaged together:

- Imaging-related classes in Medical Procedures
- Staff hierarchy in Staff Management
- Patient visit/episode in Patient Management

### 4. **Acyclic Dependencies Principle (ADP)**

No circular dependencies between subsystems:

```
Patient Mgmt → Medical Procedures → Staff Mgmt → Organization → Shared
     ↓              ↓                    ↓              ↓
     └──────────────┴────────────────────┴──────────────┘
                    ↓
              Shared Domain Model
```

---

## Class-to-Subsystem Mapping

| Class                             | Building Block            | Rationale                 |
|-----------------------------------|---------------------------|---------------------------|
| Patient                           | Patient Management        | Core patient entity       |
| Person                            | Shared Domain Model       | Used by Patient and Staff |
| Clinical Document                 | Patient Management        | Patient medical records   |
| Imaging Service Request           | Medical Procedures        | Procedure workflow        |
| Visit                             | Patient Management        | Patient visit tracking    |
| Service Episode                   | Patient Management        | Treatment episodes        |
| Requested Procedure               | Medical Procedures        | Procedure planning        |
| Scheduled Procedure Step          | Medical Procedures        | Procedure scheduling      |
| Modality Performed Procedure Step | Medical Procedures        | Procedure execution       |
| Procedure Type                    | Medical Procedures        | Procedure metadata        |
| Procedure Plan                    | Medical Procedures        | Treatment planning        |
| Protocol Code                     | Medical Procedures        | Medical protocols         |
| Series                            | Medical Procedures        | Imaging series            |
| Facility                          | Organization & Facilities | Physical locations        |
| Hospital                          | Organization & Facilities | Hospital entity           |
| Department                        | Organization & Facilities | Organizational units      |
| Staff                             | Staff Management          | Base staff class          |
| Operations Staff                  | Staff Management          | Medical staff             |
| Administrative Staff              | Staff Management          | Admin staff               |
| Technical Staff                   | Staff Management          | Technical staff           |
| Doctor                            | Staff Management          | Physicians                |
| Nurse                             | Staff Management          | Nurses                    |
| Surgeon                           | Staff Management          | Surgeons                  |
| Front Desk Staff                  | Staff Management          | Reception                 |
| Receptionist                      | Staff Management          | Patient intake            |
| Technician                        | Staff Management          | Technicians               |
| Technologist                      | Staff Management          | Technologists             |
| Surgical Technologist             | Staff Management          | Surgery support           |

---

## Quality Attributes Addressed

### 1. **Modifiability**

- Clear subsystem boundaries allow independent changes
- Staff hierarchy can evolve without affecting patient management
- Procedure workflow can be enhanced independently

### 2. **Testability**

- Each subsystem can be tested independently
- Mock interfaces between subsystems for unit testing
- Integration tests focus on subsystem interactions

### 3. **Maintainability**

- Developers can focus on one subsystem at a time
- Clear ownership boundaries (Patient team, Procedure team, etc.)
- Reduced cognitive load

### 4. **Scalability**

- Subsystems can be deployed independently (microservices)
- Different teams can work on different subsystems
- Database can be partitioned by subsystem

---

## Evolution Scenarios

### Scenario 1: Add Telemedicine Support

**Impact:**

- Patient Management: Add virtual visits
- Medical Procedures: Add remote procedure consultations
- Staff Management: Add telemedicine credentials

**Isolation:** Changes contained to 3 subsystems, no impact on Organization

### Scenario 2: Integrate with Insurance Systems

**Impact:**

- Patient Management: Add insurance information
- Medical Procedures: Add billing codes to procedures

**Isolation:** Limited to 2 subsystems

### Scenario 3: Multi-Hospital Support

**Impact:**

- Organization & Facilities: Extend hospital hierarchy
- All subsystems: Add hospital context to queries

**Isolation:** Core domain model unchanged, mostly configuration

---

## Implementation Recommendations

### Layer Architecture per Subsystem

Each subsystem should follow layered architecture:

```
┌─────────────────────────────────┐
│  REST API / User Interface      │  (Presentation)
├─────────────────────────────────┤
│  Application Services           │  (Use Cases)
├─────────────────────────────────┤
│  Domain Model (Classes)         │  (Business Logic)
├─────────────────────────────────┤
│  Data Access / Persistence      │  (Infrastructure)
└─────────────────────────────────┘
```

### Technology Stack Suggestions

**Backend:**

- Java/Spring Boot or C#/.NET for each subsystem
- JPA/Hibernate or Entity Framework for ORM
- REST APIs for inter-subsystem communication

**Database:**

- PostgreSQL or SQL Server
- One schema per subsystem (or separate databases)
- Shared schema for Shared Domain Model

**Integration:**

- Message bus (RabbitMQ/Kafka) for asynchronous events
- REST for synchronous queries
- Event-driven architecture for procedure workflow

---

## Security Considerations

### Access Control by Subsystem

**Patient Management:**

- Doctors: Read/Write patient records
- Nurses: Read/Write vital signs, limited demographics
- Admin: Read-only access to demographics

**Medical Procedures:**

- Doctors: Order procedures, view results
- Nurses: Execute procedure steps
- Technologists: Perform imaging procedures

**Staff Management:**

- HR Admin: Full access
- Department heads: Read-only for their department
- Staff: Read-only for their own record

**Organization & Facilities:**

- Admin: Full access
- All staff: Read-only access

---

## Compliance Considerations

### HIPAA Compliance

- Patient Management: Audit logging required
- Medical Procedures: Procedure tracking for compliance
- Staff Management: Access control enforcement
- All subsystems: Encryption at rest and in transit

### HL7 FHIR Integration

- Patient Management: Patient resource
- Medical Procedures: Procedure, DiagnosticReport resources
- Staff Management: Practitioner, PractitionerRole resources
- Organization: Organization, Location resources

---

## Conclusion

The proposed 6-subsystem architecture (or 4-subsystem alternative) provides:

✅ **Clear separation of concerns**
✅ **Independent deployability**
✅ **Team autonomy**
✅ **Scalability for growth**
✅ **Compliance-ready structure**
✅ **Technology flexibility**

Each class from the requirements diagram is assigned to exactly one subsystem, meeting the exercise constraint while
maintaining architectural quality.

---

## Exercise Deliverables

1. **Architecture Diagram** - Subsystem view with dependencies
2. **Class-to-Subsystem Mapping Table** - All classes assigned
3. **Dependency Analysis** - Justification for subsystem relationships
4. **Evolution Scenarios** - Validate architecture with change scenarios
5. **Design Principles** - SRP, SDP, CCP, ADP application

---

**Subsystems Identified:** 6 (or 4 for coarse-grained alternative)
**Classes Mapped:** 26 classes across all subsystems
