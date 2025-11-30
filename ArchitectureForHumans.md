# Software Architecture Strategies

A comprehensive guide to software architecture principles, development methods, and documentation frameworks.

---

## Table of Contents

- [Core Architecture Competencies](#core-architecture-competencies)
- [Software Blood Types](#software-blood-types---fundamental-separation)
- [Architectural Quality Principles](#architectural-quality-principles)
- [Interface Design Principles](#interface-design-principles)
- [Architecture Development Methods](#architecture-development-methods)
- [Architecture Documentation](#architecture-documentation-approaches)
- [Architecture Evaluation](#architecture-evaluation-methods)
- [Case Studies](#case-studies-with-architectural-lessons)
- [Practical Recommendations](#practical-recommendations-for-architects)

---

## Core Architecture Competencies

A software architect must master four key areas:

| Competency | Description |
|------------|-------------|
| **Importance** | Understanding what architecture is and why it matters |
| **Quality** | Recognizing good architecture |
| **Development** | Methods to create good architectures |
| **Documentation** | Effectively communicating architecture decisions |

> [!IMPORTANT]
> **Core Definition:** Architecture = the technical decisions that are hard to change

*"Big design up front is dumb. No design up front is even dumber."* — Dave Thomas

---

## Software Blood Types - Fundamental Separation

The most critical architectural principle: **separate application logic from technology concerns.**

<table>
<tr>
<th>TYPE A (Application)</th>
<th>TYPE T (Technology)</th>
<th>TYPE 0 (Universal)</th>
</tr>
<tr>
<td>

**Implements:** Functional requirements

**Constraints:** Should NOT know about OS, web frameworks, databases, UI

**Examples:**
- Order validation
- Price calculation
- Business rules

**Color:** Purple

</td>
<td>

**Implements:** Non-functional requirements

**Handles:** Databases, web servers, message queues, OS interaction

**Examples:**
- HTTP handlers
- Database adapters
- Logging infrastructure

**Color:** Blue

</td>
<td>

**Definition:** "Eternal truths of computer science"

**Examples:**
- String manipulation
- Math libraries
- Differential equation solvers

**Change Rate:** Minimal

**Color:** Orange

</td>
</tr>
</table>

> [!CAUTION]
> **Critical Rule:** Building blocks must be A OR T, never both!

### Application Core Pattern

| Layer | Content | Behavior |
|-------|---------|----------|
| **Core** | A-software only | Grows with functional scope |
| **Ring** | T-software around core | Size stays constant |

This is the foundation of Clean Architecture and Domain-Driven Design.

> [!NOTE]
> **Microservices Principle:** Microservices are A-services, not T-services. "Built around business capabilities" — Martin Fowler

---

## Architectural Quality Principles

<details open>
<summary><b>1. Cohesion Principles</b></summary>

### Single Responsibility Principle (SRP)

| Aspect | Description |
|--------|-------------|
| **Rule** | Each building block does ONE job only |
| **Test** | Can describe in simple sentence without "and" or "or" |
| **Quote** | "Responsible to one and only one actor" — Robert C. Martin |

### Separation of Concerns (SOC)

Each building block has one concern. Applies to:

<table>
<tr>
<td>Components</td>
<td>If-statements</td>
<td>Branches</td>
</tr>
<tr>
<td>Databases</td>
<td>Sprints</td>
<td>Prompts</td>
</tr>
</table>

### Don't Repeat Yourself (DRY)

- Each job implemented only once
- "Designs without duplication tend to be easy to change" — Kent Beck

### Cohesion Applied Everywhere

| Domain | Application |
|--------|-------------|
| **Code** | Extract till you drop - small functions with one purpose |
| **Git Branches** | Use Gitflow - one feature per branch |
| **Databases** | Normalize - eliminate redundancy |
| **Sprints** | One sprint goal, coherent work |
| **Prompts** | Chain prompting - one task per prompt |

</details>

<details open>
<summary><b>2. Coupling Principles</b></summary>

### Low Coupling Goal

| Source | Quote |
|--------|-------|
| Siedersleben | "Check and minimize dependencies. Each avoided dependency is a victory" |
| Ian Cooper | "Coupling is what kills all software" |
| Kent Beck | "The bulk of software design is managing dependencies" |

### Ripple Effect Management

- Changes propagate along dependencies ("Lawineneffekt")
- Use dependency firewalls to block propagation
- Perform impact analysis before changes

> [!TIP]
> **Good Architecture = Weakly Coupled + Strongly Cohesive**
> - Many local dependencies (within components)
> - Few non-local dependencies (between components)

</details>

<details open>
<summary><b>3. Acyclic Dependencies Principle (ADP)</b></summary>

> [!WARNING]
> No cycles allowed in architecture!

Cycles mean components must be:

| Constraint | Impact |
|------------|--------|
| Understood together | Increased cognitive load |
| Changed together | No independent evolution |
| Tested together | Complex test setup |
| Deployed together | Monolithic deployment |

**Detection:** Use dependency analysis tools to find and break cycles

</details>

<details open>
<summary><b>4. Common Closure Principle (CCP)</b></summary>

| Aspect | Description |
|--------|-------------|
| **Definition** | "Things that change together should be in the same module" |
| **Original** | "A change that affects a package affects all the classes in that package" — Robert C. Martin |
| **Extended** | Typical change request should affect FEW building blocks, not many |
| **Key Insight** | Put code with same change rate in same building block |

</details>

<details open>
<summary><b>5. Common Reuse Principle (CRP)</b></summary>

| Aspect | Description |
|--------|-------------|
| **Principle** | Put frequently reused-together items in one building block |
| **Benefit** | Splitting reduces impact analysis scope |
| **Example** | Don't bundle rarely-used utilities with frequently-used core logic |

</details>

<details open>
<summary><b>6. Tell Don't Ask (TDA)</b></summary>

**Core OOP Principle:** Move behavior close to data

**Bad (Ask):**

```python
temperature = sensor.getTemperature()
if temperature > threshold:
    regulator.turnOn()
```

**Good (Tell):**

```python
sensor.regulate(threshold, regulator)
```

**Result:** Data doesn't travel through system. Compute at source.

</details>

---

## Interface Design Principles

### Decoupling Through Interfaces

> [!NOTE]
> **Greatest Invention in Computer Science:**
> - Split into: interface (what others need) + implementation (hidden)
> - Information hiding
> - Enables independent evolution

**Change Management Value:**

| Scenario | Impact |
|----------|--------|
| New consumer | No provider change needed |
| New provider | No consumer change needed |
| Result | Firewalls against change propagation |

### Interface Quality Criteria

<table>
<tr>
<th>Not Underspecified</th>
<th>Not Overspecified (Minimal)</th>
</tr>
<tr>
<td>

Specify everything needed for cooperation:
- Syntax
- Semantics
- Error handling
- Performance

</td>
<td>

- Need-to-know principle only
- Allow maximum freedom to evolve
- Can be under- AND over-specified simultaneously!

</td>
</tr>
</table>

> [!IMPORTANT]
> "Easy to use correctly, hard to use incorrectly" — Scott Meyers

### Interface Changes

> [!CAUTION]
> **Avoid Interface Changes!**
> - Trigger big ripple effects
> - Backward compatibility is "guiding principle" (Kent Beck)
> - No changes to existing promises, only additions
> - Common practice in microservices

### Interface Segregation Principle (ISP)

**Prefer several small interfaces over one big interface**

| Advantage | Description |
|-----------|-------------|
| 1. Deployment | Independent deployment, smaller deployments |
| 2. Access Rights | Independent access rights per interface |
| 3. Testability | Better testability |

**Applications:**
- Separate admin from operation interfaces
- Separate test-only interfaces
- Limited Access Principle (LAP): Each client accesses only needed services

### Interface Blood Types

| Type | Description | Examples |
|------|-------------|----------|
| **A-Interface** (Good) | Uses domain language, business concepts, technology-free | promoteToVIP, blacklist |
| **T-Interface** (Bad for A) | Technology-specific, couples A to T | writeToDB2, saveToRedis |
| **0-Interface** (Universal) | Technology-free abstractions, safe for A-components | persist, save |

> [!NOTE]
> **Rule:** A-components depend on A-interfaces and 0-interfaces, NOT T-interfaces

**Dependency Inversion:** Introduce abstractions to reverse dependencies on concrete implementations

---

## Architecture Development Methods

<details open>
<summary><b>1. Use Case Driven Development</b></summary>

| Use Case Type | Description | Example |
|---------------|-------------|---------|
| **Primary** | Services to external actors | Transfer Funds |
| **Secondary** | Services between building blocks | Identify Card |

**Service Elicitation from Requirements:**

```text
Requirement: "Order OK if <=100 items and no alcohol for minors"

Secondary Services:
  - CheckOrder(Order)
  - ContainsAlcohol(Product)
  - IsAdult(Customer)
```

**Packaging Goal:** Minimize arrows between packages (arrows need interfaces)

</details>

<details open>
<summary><b>2. Domain Driven Design (DDD)</b></summary>

**Three Core Principles:**

| # | Principle |
|---|-----------|
| 1 | Focus on the core domain |
| 2 | Collaborate with domain practitioners |
| 3 | Speak ubiquitous language within bounded context |

**Bounded Contexts:** Linguistically defined boundaries

> [!TIP]
> **Example:** "Customer" means different things in Marketing vs. Delivery contexts

**Finding Aggregates via:**
- Existence dependence/compositions
- Global search patterns
- Transactional business rules
- Navigable relationships

**Aggregate Canvas:** Document A-components with name, description, lifecycle, business rules, services, events

</details>

<details open>
<summary><b>3. CRUD Matrix Approach</b></summary>

**Steps:**

| Step | Action |
|------|--------|
| 1 | Create matrix: services (rows) x classes (columns) |
| 2 | Mark CRUD operations (Create, Read, Update, Delete) |
| 3 | Exchange rows/columns to move filled cells near diagonal |
| 4 | Define components as diagonal squares |
| 5 | Maximize letters inside squares (cohesion), minimize outside (coupling) |

**Quality Metric:** Cohesion / Coupling ratio

**Example:** 12 intra-component cells / 3 inter-component cells = 4.0 (good)

</details>

<details open>
<summary><b>4. Evolutionary Coupling Refactoring</b></summary>

| Aspect | Description |
|--------|-------------|
| **Measure** | Which components changed together in past? |
| **Example** | Components "ord" and "gos" changed together 96% of time |

**Refactoring Strategies:**
- Split building blocks with different change rates
- Merge blocks with strong evolutionary coupling
- Requires good change management system

</details>

<details open>
<summary><b>5. AI/Embedding Approach</b></summary>

**Modern Method:**

| Step | Action |
|------|--------|
| 1 | Feed functional requirement embeddings into vector database |
| 2 | Cluster requirements automatically |
| 3 | Each cluster = one component |
| 4 | LLM generates cluster names |

</details>

---

## Architecture Documentation Approaches

### The Four Standard Views

| View | Purpose | Diagram Type |
|------|---------|--------------|
| **Meta View** | Types of parts | Class diagram, metamodel |
| **Structure View** | Parts and connections | Component/class diagram |
| **Behavior View** | Runtime cooperation | Sequence/activity diagram |
| **Network View** | Distribution on network | Deployment diagram |

> [!IMPORTANT]
> **Metamodel Importance:** "Common vocabulary to describe software architecture" — Simon Brown

Define consistently: Component, System, Layer, Module

### C4 Model (Simon Brown)

**Four Levels of Abstraction:**

| Level | Name | Content |
|-------|------|---------|
| 1 | **Context** | System and its interfaces to external actors |
| 2 | **Container** | Big T-building blocks (web server, database, message queue) |
| 3 | **Component** | Big A-building blocks (business components) |
| 4 | **Class** | Detailed design within components |

**Plus:** Communication diagrams for dynamic behavior

**Principle:** Each level zooms into the previous level

### arc42 Framework

Free template at http://www.arc42.org/

<details>
<summary><b>12 Essential Sections</b></summary>

| # | Section | Content |
|---|---------|---------|
| 1 | **Functional Requirements** | Use cases |
| 2 | **Constraints** | Technical, organizational, legal limitations |
| 3 | **Business Context** | External interfaces and partners |
| 4 | **Solution Strategy** | Key decisions and patterns |
| 5 | **Building Block View** | Blackbox/Whitebox decomposition |
| 6 | **Runtime View** | Cooperation scenarios |
| 7 | **Deployment View** | Infrastructure mapping |
| 8 | **Cross-Cutting Concepts** | Recurring patterns (logging, security, error handling) |
| 9 | **Architecture Decisions** | ADRs (Architecture Decision Records) |
| 10 | **Quality Scenarios** | Test cases including non-functional requirements |
| 11 | **Risks** | Technical debt, known issues |
| 12 | **Glossary** | Ubiquitous language |

</details>

**Architecture Decision Records (ADR) Format:**
- Context and problem statement
- Options considered with pros/cons
- Decision made
- Rationale and consequences

### Documentation Best Practices (Simon Brown)

| Practice | Description |
|----------|-------------|
| Consistent notation | Same symbols mean same things |
| Similar abstraction levels | Within each diagram |
| Explain all notation | Legend for readers |
| Color/shape complement | Don't replace labels |
| Unidirectional lines | With annotations |
| Narrative complements diagram | Doesn't just explain it |
| Icons supplement text | Visual recognition |
| Documentation evolves | Not write-once |

---

## Architecture Evaluation Methods

### Initial Reviews (Design Time)

| Method | Description | Requires |
|--------|-------------|----------|
| **Checklist-Based** | Verify architectural quality principles (SRP, ADP, CCP, blood types) | Component diagram with A/T information |
| **Scenario-Based** | Walk through use cases step-by-step, verify components can perform use case | Use case diagram/list + component diagram |
| **CRUD Analysis** | Evaluate ratio: CRUD-cells within components / CRUD-cells between | CRUD matrix |
| **Reusability Test** | "What can be sold separately?" | Component boundaries |
| **ATAM** | Architecture Tradeoff Analysis Method - evaluate quality attribute tradeoffs | Quality scenarios + stakeholders |
| **Risk Assessment** | Identify and prioritize architectural risks and technical debt | Architecture documentation |

### Continuous Reviews (Runtime)

| Method | Description | Requires |
|--------|-------------|----------|
| **Compliance Checking** | Automated scripts find allowed-to-use violations | Documented allowed-to-use specification |
| **Metrics Monitoring** | Track coupling/cohesion metrics, dependency depth, cyclomatic complexity | Static analysis tools |
| **Fitness Functions** | Automated tests verifying architectural characteristics continuously | CI/CD pipeline integration |

> [!TIP]
> **Resolution for violations:** Move logic between components, introduce interfaces, or update allowed-to-use specification

---

## Communication Styles

**Key Decisions for Interfaces:**

| Decision | Options |
|----------|---------|
| Wait or continue? | Synchronous / Asynchronous |
| Session bundling? | Stateful / Stateless |
| Transaction support? | Transactional / Not transactional |
| Work per call? | Fine-grained / Coarse-grained |
| Location? | Local / Network |

**Coupling Impact:**

| More Coupled | Less Coupled |
|--------------|--------------|
| Synchronous | Asynchronous |
| Stateful | Stateless |
| Transactional | Not transactional |
| Fine-grained | Coarse-grained |
| Local | Network |

> [!TIP]
> **Performance Tip:** Use coarse-grained interfaces for network calls

---

## Allowed-to-Use Specification

**Definition:** Information about allowed/forbidden dependencies between components

**Enforcement:**

| Type | Description |
|------|-------------|
| **Ex ante** | Permission requests before coding |
| **Ex post** | Source code scanning tools |

### Common Patterns

| Pattern            | Rule                                    | Example                           |
|--------------------|-----------------------------------------|-----------------------------------|
| **Layered**        | Block n cannot use lower-numbered blocks| Book(1), Librarian(2), BookShelf(3)|
| **Strictly Layered**| Block n only uses n-1                  | Each layer talks only to adjacent |

### Benefits

| Benefit                     | Description                           |
|-----------------------------|---------------------------------------|
| Better testability          | Fewer stubs/drivers needed            |
| Controlled dependencies     | Clear dependency management           |
| Easier impact analysis      | Predictable change propagation        |

---

## Key Anti-Patterns to Avoid

> [!WARNING]
> Violating these principles leads to architectural erosion and technical debt.

| Anti-Pattern | Description |
|--------------|-------------|
| **Mixing A and T** | A-component knowing about databases, web frameworks |
| **A-person receiving T-messages** | Error codes instead of user-friendly messages |
| **CRUD language in A-software** | "Create Employee" instead of "Hire Employee" |
| **Cyclic dependencies** | Components tightly bound together |
| **Conway's Law inversion** | Let orgchart determine architecture |
| **Underspecified interfaces** | Missing necessary cooperation information |
| **Overspecified interfaces** | Too much detail, prevents evolution |

---

## Additional Critical Principles

| Principle | Description | Example/Note |
|-----------|-------------|--------------|
| **Stable Dependencies (SDP)** | Depend on low-change-rate blocks over high-change-rate | Requires stability classification |
| **Stable Abstractions (SAP)** | Abstract blocks should change less than concrete ones | "Person" changes less than "Patient" |
| **Separate Normal/Exception** | Don't mix normal behavior and exception handling | Include (normal) vs. Extend (exceptional) |
| **Interface-Implementation Imbalance** | Interface much smaller/simpler than implementation | Hide complexity behind simple API |
| **Building Block Balance** | Avoid one big block + many small blocks | Aim for similar-sized components |
| **Ubiquitous Language** | A-architecture uses requirement terminology exactly | Foundation of DDD |
| **Environmental Impact** | Good architectures need less energy | Bjorna Kalaja, 2024 |

---

## Command Query Separation Patterns

### CQS (Command Query Separation) - Method Level

Each method either:

| Type | Behavior |
|------|----------|
| **Query** | Reads attributes and returns value |
| **Command** | Changes state and returns nothing |

> [!CAUTION]
> Never both!

### CQRS (Command Query Responsibility Segregation) - Building Block Level

Separate building blocks for:

| Type | Purpose | Benefits |
|------|---------|----------|
| **Commands** | Write operations | Independent scaling |
| **Queries** | Read operations | Independent optimization |

---

## Case Studies with Architectural Lessons

<details open>
<summary><b>EarlyBird: Breakfast Delivery System</b></summary>

**Business Context:** A food delivery company guaranteeing breakfast delivery in <25 minutes.

**Evolution Challenge:** Originally phone-based ordering with manual processing. Now moving to web-based automation with SMS ordering capability.

**Key Lessons:**

| Lesson | Description |
|--------|-------------|
| **A/T Separation** | A-Components (Order, Product, Customer) stay stable when T-Components (Web, SMS) change |
| **Interface Segregation** | ISearchProduct interface used by both web UI and phone system |
| **DDD Aggregates** | Order Aggregate enforces business rules at boundaries |
| **External Integration** | Use coarse-grained interfaces with minimal data |
| **Evolution Without Breaking** | Good architecture enables gradual migration |

> [!TIP]
> When phone clerks are eliminated, only T-layer changes. A-layer remains unchanged.

</details>

<details open>
<summary><b>Mars: Moon Visibility Calculator</b></summary>

**Business Context:** NASA Mars mission calculating time-overlap when both moons are visible.

**Key Lessons:**

| Lesson | Description |
|--------|-------------|
| **Pure Application Core** | Interval calculation completely technology-free |
| **Separation of Core from Interface** | Same A-component works in production and testing |
| **Type 0 (Universal Truth)** | Time interval overlap is universal mathematics |
| **Edge Case Handling** | "Twilight rule" is an A-requirement in A-layer |
| **Testability** | Clean interface enables different T-adapters |

> [!NOTE]
> Mars demonstrates the ultimate goal: application core so pure it works anywhere with any interface.

</details>

<details open>
<summary><b>MateMate: Chess Application Evolution</b></summary>

**Business Context:** Chess software playing against humans, calculating optimal moves.

**Key Lessons:**

| Lesson | Description |
|--------|-------------|
| **Service Elicitation** | 20 secondary services identified from chess rules |
| **Software 1.0 to 2.0** | Swap evaluation implementations without touching other components |
| **SE4 Method** | Service -> Subsystem -> Evaluation systematic approach |
| **Reusability Test** | Chess engine separable from game history tracking |

> [!TIP]
> When AlphaZero beats Stockfish, it's just swapping one IPositionEvaluator implementation for another.

</details>

<details>
<summary><b>Industry Anti-Pattern: Charts Component Duplication</b></summary>

**What Happened:**
1. Common Core contained financial calculations for Product1 and Product2
2. Charts functionality added for Product1
3. Product2 needs charts - sources COPIED into Charts2
4. Charts2 massively enhanced - interface changed
5. Product1 can't use new charts without rewriting

**Principles Violated:**

| Principle | Violation |
|-----------|-----------|
| DRY | Chart logic duplicated |
| CRP | Chart features not packaged together |
| ISP | One big interface forced breaking changes |
| Backward Compatibility | Breaking old interface |

</details>

<details>
<summary><b>Vienna Transit Boards: ISP Violation</b></summary>

**What Happened:** Apps parsing destination data suddenly showed "Save the Climate" as train destinations.

**Root Cause:** Display interface bundled destination data with promotional messages.

**Solution:** Separate IDestinationProvider from IPublicMessageProvider

</details>

---

## What Case Studies Teach

| Case Study | Lesson |
|------------|--------|
| **EarlyBird** | A/T separation enables technology migration without touching business logic |
| **Mars** | Pure application cores work anywhere with any interface |
| **MateMate** | Unstable algorithms behind stable interfaces enable evolution |
| **Vienna Transit** | ISP violations cause production failures in unexpected places |
| **Evolutionary Coupling** | Design intent != change reality. Measure actual coupling. |
| **Compliance Violations** | Architecture erosion is invisible without automated governance |

---

## Practical Recommendations for Architects

| # | Recommendation | Key Actions |
|---|----------------|-------------|
| 1 | **Always Separate A and T** | First question: Is this A or T? Never mix in same component |
| 2 | **Design for Change** | Use CCP (change together = belong together), CRP (reuse together = belong together), classify by stability |
| 3 | **Minimize Dependencies** | Each avoided dependency is a victory; use dependency inversion; keep allowed-to-use spec |
| 4 | **Document Multiple Views** | C4 (Context, Container, Component, Class); Structure, Behavior, Network views |
| 5 | **Review Systematically** | Checklist-based, scenario-based, CRUD analysis, automated compliance checking |
| 6 | **Use Ubiquitous Language** | A-interfaces use domain terms only; avoid CRUD in business layer; maintain glossary |
| 7 | **Embrace Modern Methods** | AI/embeddings for clustering; evolutionary coupling analysis; automated validation |
| 8 | **Record Decisions** | Use ADRs; document options, decision, rationale; maintain in version control |
| 9 | **Focus on the Core** | Application core (A) grows with features; Technical ring (T) stays constant |
| 10 | **Think Long-Term** | Architecture = framework for change; Maintenance = 75% of cost; Good architecture = high changeability |

---

## Timeless Wisdom

> *"The rules of software architecture are universal and changeless. They have been the same since Alan Turing wrote the first code in 1946."* — Robert C. Martin

> *"On the Criteria to be Used in Decomposing Systems into Modules" (David Parnas, 1972) - still relevant today*

> *"Architecture = the technical decisions that are hard to change"*

> *"The code doesn't tell the whole story."* — Simon Brown

---

## Further Reading

### Essential Books

| Author | Title |
|--------|-------|
| Eric Evans | Domain-Driven Design (2003) |
| Robert C. Martin | Clean Architecture |
| Simon Brown | Software Architecture for Developers |
| Vaughn Vernon | Implementing Domain-Driven Design |
| John Ousterhout | A Philosophy of Software Design |
| Johannes Siedersleben | Moderne Software-Architektur |
| Nicolai Josuttis | SOA in Practice |

### Key Articles

| Author | Article | Source |
|--------|---------|--------|
| Martin Fowler | [Microservices](https://martinfowler.com/articles/microservices.html) | martinfowler.com |
| Cesare Pautasso et al. | Microservices in Practice | IEEE Software 2017 |

### Frameworks & Templates

| Resource | URL | Description |
|----------|-----|-------------|
| arc42 | [arc42.org](https://arc42.org) | Free architecture documentation template |
| C4 Model | [c4model.com](https://c4model.com) | Visualizing software architecture |
| iSAQB | [isaqb.org](https://isaqb.org) | International Software Architecture Qualification Board |
