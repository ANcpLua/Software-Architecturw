# Climate Model Architecture Analysis

**Exercise ID:** ArchitecturalQuality08

**Related Exercises:**

- [Charts/Products Architecture Analysis][exercise1]
- [Mars Moons Application Core][exercise3]
- [Case Study PDF][case-study]

---

## Subsystems Table

| Subsystem | Description                                | Changes/Year | Uses                |
|-----------|--------------------------------------------|--------------|---------------------|
| APPG      | Air pressure & population data             | 5x           | DE, CHK             |
| APC       | Checks air pressure data, converts to JSON | 5x           | APPG                |
| DE        | Solves differential equations              | 1x           | DE1                 |
| DE1       | Solves first-order differential equations  | 1x           | none                |
| STL       | Statistics library                         | 1x           | none                |
| DYN       | Models aerodynamics laws                   | 1x           | APPG                |
| NNW       | Neural network for forecasting             | 12x          | none                |
| FCA       | Performs forecasts                         | 150x         | APPG, DYN, STL, NNW |
| CHK       | Checks forecast plausibility               | 5x           | FCA                 |

---

## Structural Weaknesses

### 1. SDP (Stable Dependencies Principle) Violations

**CHK → FCA dependency:**

- CHK changes 5x/year (relatively stable)
- FCA changes 150x/year (extremely unstable)
- **Problem:**
  Stable component depends on component that changes 30x more frequently
- Every FCA change risks breaking CHK,
  forcing regression testing and potential code changes
- CHK cannot be stable when its primary dependency is highly volatile

**DYN → APPG dependency:**

- DYN changes 1x/year (very stable - core physics)
- APPG changes 5x/year (data source, 5x more volatile)
- **Problem:**
  Stable aerodynamics model forced to adapt to data format changes
- Physics algorithms shouldn't depend on data representation

---

### 2. CCP (Common Closure Principle) Issue

**FCA change frequency mismatch:**

- FCA: 150 changes/year
- Its dependencies: APPG (5x), DYN (1x), STL (1x), NNW (12x)
- **Problem:**
  FCA changes far more frequently than its dependencies
- Suggests FCA has internal responsibilities unrelated to its dependencies
- Should be split:
  algorithm changes vs. data adapter changes vs. orchestration

---

### 3. High Fan-In Risk: APPG Bottleneck

**APPG used by:** APC, DYN, FCA (indirectly CHK)

- **Problem:**
  Changes to APPG data format affect 3-4 components
- No abstraction layer isolates consumers from data source changes
- 5 changes/year × 3-4 consumers = 15-20 component updates/year

---

### 4. ISP (Interface Segregation) Potential Violation

**APPG provides:** "Air pressure AND population growth data"

- **FCA likely needs:** Only air pressure for weather forecasts
- **Problem:**
  If FCA doesn't use population data,
  it's forced to depend on unnecessary functionality
- Changes to population data methods affect FCA even though it doesn't use them

---

### 5. NNW Isolation Waste

- NNW changes 12x/year but only used by FCA
- If it's a general neural network library,
  should be stable (~1x/year)
- High change rate suggests it's tightly coupled to FCA's forecasting logic
- Should split:
  general NN library (stable) vs. forecast-specific adapter (volatile)

---

## Architecture Diagram (C4 Component View)

**What this diagram shows:**

This C4 Component diagram illustrates the climate model system's architecture with all 9 subsystems and their
dependencies.
Each component is annotated with its change frequency (changes per year) and stability classification,
making it easy to identify architectural weaknesses where stable components depend on volatile ones.

**Why this diagram exists:**

To support the exercise goal of identifying architectural weaknesses based on dependency direction and change frequency.
The diagram makes SDP violations immediately visible:
CHK (stable, 5x/year) depending on FCA (volatile, 150x/year),
and DYN (very stable, 1x/year) depending on APPG (moderate, 5x/year).

**Principles illustrated:**

- **SDP (Stable Dependencies Principle):** Dependencies should flow toward stability - violated by CHK→FCA and DYN→APPG
- **CCP (Common Closure Principle):** FCA's high change rate (150x/year) suggests mixed responsibilities
- **ISP (Interface Segregation):** APPG provides both air pressure and population data, forcing unnecessary dependencies
- **ADP (Acyclic Dependencies):** The dependency graph is acyclic, which is good
- **High Fan-In Risk:** APPG is used by multiple components (bottleneck risk)

**Arrow Legend:**

- **Dark Blue solid arrows** → Normal dependencies (required code flow)
- **Orange dashed arrows** → Violations highlighted (architectural problems - SDP violations)

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#e3f2fd','primaryTextColor':'#0d47a1','primaryBorderColor':'#1976d2','lineColor':'#1565C0','secondaryColor':'#fff3e0','tertiaryColor':'#f3e5f5', 'fontSize':'18px', 'edgeLabelBackground':'#ffffff'}}}%%
graph TB
    subgraph stable["⚙️ STABLE COMPONENTS (1x/year)"]
        DE["<b>🔷 DE</b><br/><br/>Differential Equations<br/><br/>Solves differential equations<br/>1x/year • stable"]
        DE1["<b>🔷 DE1</b><br/><br/>First-Order DE<br/><br/>Solves first-order DEs<br/>1x/year • stable"]
        STL["<b>🔷 STL</b><br/><br/>Statistics Library<br/><br/>Statistical functions<br/>1x/year • stable"]
        DYN["<b>🔷 DYN</b><br/><br/>Aerodynamics<br/><br/>Models aerodynamics laws<br/>1x/year • stable"]
    end

    subgraph moderate["🔄 MODERATE COMPONENTS (5-12x/year)"]
        APPG["<b>🟡 APPG</b><br/><br/>Data Provider<br/><br/>Air pressure & population data<br/>5x/year • moderate"]
        APC["<b>🟡 APC</b><br/><br/>Data Checker<br/><br/>Checks air pressure, converts to JSON<br/>5x/year • moderate"]
        CHK["<b>🟡 CHK</b><br/><br/>Forecast Checker<br/><br/>Checks forecast plausibility<br/>5x/year • moderate"]
        NNW["<b>🟡 NNW</b><br/><br/>Neural Network<br/><br/>Neural network forecasting<br/>12x/year • moderate"]
    end

    subgraph volatile["🔥 VOLATILE COMPONENTS (150x/year)"]
        FCA["<b>🔴 FCA</b><br/><br/>Forecast Calculator<br/><br/>Performs forecasts<br/>150x/year • volatile"]
    end

    Legend["<b>📋 ARROW LEGEND</b><br/><br/>━━ Dark Blue solid<br/>→ Normal dependencies<br/><br/>╌╌ Orange dashed<br/>→ Violations (SDP)"]

    DE -->|uses| DE1
    APC -->|reads| APPG
    DYN -->|reads ⚠️| APPG
    FCA -->|reads| APPG
    FCA -->|uses| DYN
    FCA -->|uses| STL
    FCA -->|uses| NNW
    CHK -->|validates ⚠️| FCA

    DYNNote["<b>⚠️ SDP VIOLATION</b><br/><br/>DYN (1x/year stable)<br/>depends on<br/>APPG (5x/year moderate)<br/><br/>Physics algorithms shouldn't<br/>depend on data format changes"]
    APPGNote["<b>⚠️ HIGH FAN-IN RISK</b><br/><br/>Used by APC, DYN, FCA<br/><br/><b>⚠️ ISP VIOLATION</b><br/><br/>Provides air pressure AND<br/>population data<br/>(FCA may not need population)"]
    CHKNote["<b>⚠️ SDP VIOLATION</b><br/><br/>CHK (5x/year moderate)<br/>depends on<br/>FCA (150x/year volatile)<br/><br/>Every FCA change risks<br/>breaking CHK"]
    FCANote["<b>⚠️ CCP VIOLATION</b><br/><br/>FCA changes 150x/year<br/>while dependencies change<br/>only 1-12x/year<br/><br/>Suggests mixed responsibilities<br/>needing component split"]

    DYN -.-> DYNNote
    APPG -.-> APPGNote
    CHK -.-> CHKNote
    FCA -.-> FCANote

    style DE fill:#85BBF0,stroke:#1976d2,stroke-width:3px,color:#000
    style DE1 fill:#85BBF0,stroke:#1976d2,stroke-width:3px,color:#000
    style STL fill:#85BBF0,stroke:#1976d2,stroke-width:3px,color:#000
    style DYN fill:#85BBF0,stroke:#1976d2,stroke-width:3px,color:#000
    style APPG fill:#FFE082,stroke:#F57C00,stroke-width:3px,color:#000
    style APC fill:#FFE082,stroke:#F57C00,stroke-width:3px,color:#000
    style CHK fill:#FFE082,stroke:#F57C00,stroke-width:3px,color:#000
    style NNW fill:#FFE082,stroke:#F57C00,stroke-width:3px,color:#000
    style FCA fill:#FFCDD2,stroke:#C62828,stroke-width:3px,color:#000
    style DYNNote fill:#FFF9C4,stroke:#F57F17,stroke-width:3px,color:#000
    style APPGNote fill:#FFF9C4,stroke:#F57F17,stroke-width:3px,color:#000
    style CHKNote fill:#FFF9C4,stroke:#F57F17,stroke-width:3px,color:#000
    style FCANote fill:#FFF9C4,stroke:#F57F17,stroke-width:3px,color:#000
    style Legend fill:#E8F5E9,stroke:#2e7d32,stroke-width:3px,color:#000

    linkStyle 0 stroke:#0D47A1,stroke-width:4px
    linkStyle 1 stroke:#0D47A1,stroke-width:4px
    linkStyle 2 stroke:#0D47A1,stroke-width:4px
    linkStyle 3 stroke:#0D47A1,stroke-width:4px
    linkStyle 4 stroke:#0D47A1,stroke-width:4px
    linkStyle 5 stroke:#0D47A1,stroke-width:4px
    linkStyle 6 stroke:#0D47A1,stroke-width:4px
    linkStyle 7 stroke:#0D47A1,stroke-width:4px
    linkStyle 8 stroke:#FF8C00,stroke-width:4px,stroke-dasharray:5
    linkStyle 9 stroke:#FF8C00,stroke-width:4px,stroke-dasharray:5
    linkStyle 10 stroke:#FF8C00,stroke-width:4px,stroke-dasharray:5
    linkStyle 11 stroke:#FF8C00,stroke-width:4px,stroke-dasharray:5
```

---

## Expensive Change Scenarios

### 1. Modify APPG Data Format

**Example:** Change from CSV to JSON format

**Impact:**

- **Direct:**
  APC, DYN, FCA all must adapt to new format
- **Indirect:**
  CHK must revalidate (depends on FCA which uses APPG)
- **Total affected:**
  4 components
- **Why expensive:**
  No abstraction layer means all consumers directly coupled to format
- **Cost:**
  Every APPG change (5x/year) propagates to 3-4 components

---

### 2. Update FCA Forecasting Algorithm

**Example:** Replace ML model with new approach

**Impact:**

- **Direct:**
  FCA implementation changes
- **Cascade:**
  CHK depends on FCA directly (no stable interface)
- Every FCA algorithm change requires CHK regression testing
- Output format changes may require CHK code modifications
- **Cost:**
  150 FCA changes/year → 150 CHK test cycles minimum
- Some changes (~20%) require CHK code updates = 30 additional changes/year

---

### 3. Replace NNW with Different ML Library

**Example:** Migrate from custom NN to TensorFlow

**Impact:**

- **Direct:**
  Complete NNW rewrite
- **Cascade:**
  FCA uses NNW directly (no abstraction)
- Must rewrite FCA's NNW integration code
- Must retrain all forecast models
- CHK must recalibrate validation rules (different ML = different outputs)
- **Why expensive:**
  Technology choice (NNW library) is tightly coupled to business logic (FCA forecasting)
- **Estimated effort:**
  400-600 developer hours

---

## Requirements Ambiguities

**Ambiguity 1:** What does "APPG used by DE, CHK" mean?

- **Assumption:**
  Forward dependencies only (DE and CHK consume APPG data),
  not callbacks

**Ambiguity 2:** Why does FCA change 150x/year?

- **Assumption:**
  Mix of algorithm improvements, data format adaptations, and bug fixes
- **Need:**
  Categorization to determine if split is needed

**Ambiguity 3:** Does APC modify APPG data?

- **Assumption:**
  APC is a validator/converter that reads APPG,
  doesn't write back

**Ambiguity 4:** Does CHK modify FCA?

- **Assumption:**
  Read-only dependency,
  CHK validates FCA output without modifying it

---

## Recommended Refactoring

1. **Extract stable interfaces:**
    - `IClimateDataProvider` (implemented by APPG)
    - `IForecastEngine` (implemented by FCA)

2. **Invert CHK → FCA dependency:**
    - FCA depends on `IForecastValidator` interface
    - CHK implements the interface (becomes plugin)

3. **Split FCA by change reason:**
    - ForecastOrchestrator (stable, 5x/year)
    - ForecastAlgorithms (volatile, 100x/year)
    - DataAdapters (moderate, 45x/year)

4. **Isolate APPG consumers via interface:**
    - DYN → `IClimateDataProvider`
    - FCA → `IClimateDataProvider`
    - Can swap APPG implementation without affecting consumers

---

## Glossary

| Term            | Definition                                                                                        |
|-----------------|---------------------------------------------------------------------------------------------------|
| **[SDP][sdp]**  | Stable Dependencies Principle: Depend in the direction of stability                               |
| **[CCP][ccp]**  | Common Closure Principle: Classes that change together should be packaged together                |
| **[ADP][adp]**  | Acyclic Dependencies Principle: Component dependency graph must be a directed acyclic graph (DAG) |
| **[ISP][isp]**  | Interface Segregation Principle: Clients should not depend on interfaces they don't use           |
| **[DIP][dip]**  | Dependency Inversion Principle: Depend on abstractions, not concretions                           |
| **Fan-In**      | Number of components that depend on a given component (high fan-in = bottleneck risk)             |
| **Change Rate** | Number of times a component changes per year (indicator of stability)                             |
| **APPG**        | Air Pressure & Population Growth data provider (5x changes/year)                                  |
| **FCA**         | Forecast Calculator component (150x changes/year - highly volatile)                               |
| **CHK**         | Forecast plausibility checker (5x changes/year)                                                   |
| **NNW**         | Neural Network component for forecasting (12x changes/year)                                       |

---

<!-- Reference Links -->

[exercise1]: ../01-architecture-real-life-story/architectural-principles-analysis.md

[exercise3]: ../03-Mars-moons-application-core/application-core-design.md

[case-study]: ../03-Mars-moons-application-core/home-exercise-and-case-study.pdf

<!-- Principle Links -->

[sdp]: #1-sdp-stable-dependencies-principle-violations

[ccp]: #2-ccp-common-closure-principle-issue

[adp]: #1-sdp-stable-dependencies-principle-violations

[isp]: #4-isp-interface-segregation-potential-violation

[dip]: https://en.wikipedia.org/wiki/Dependency_inversion_principle
