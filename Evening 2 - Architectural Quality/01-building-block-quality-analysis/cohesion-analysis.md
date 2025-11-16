# Building Block Quality Analysis: Cohesion Assessment

**Exercise ID:** ArchitecturalQuality01
**Topic:** Internal Quality (Cohesion) Analysis Using Dependency Matrices
**Type:** In-Class Group Exercise

---

## Question

> Ignore the arrows for now. What can you say about the quality of the building block just by looking at the (dependency) matrix?

---

## What is Cohesion?

**Definition:** Cohesion measures how closely related the responsibilities within a module are.

- **High Cohesion** ✅ = Components within the module have strong, related responsibilities
- **Low Cohesion** ❌ = Components within the module have weak, unrelated responsibilities

**Goal:** Maximize cohesion within modules to create maintainable, understandable software.

---

## Reading a Dependency Matrix

### Matrix Structure

```
        A   B   C   D
    A   -   •   •
    B       -       •
    C   •       -   •
    D   •   •       -
```

**Interpretation:**
- **Rows:** "From" components
- **Columns:** "To" components
- **Dot (•):** Component in row depends on component in column
- **Dash (-):** Diagonal (component doesn't depend on itself)

**Example:** Row A has dots in columns B and C → A depends on B and C

---

## Analyzing Building Block Quality from the Matrix

### Pattern 1: High Cohesion (Good Quality)

```
        A   B   C   D   E   F
    A   -   •   •
    B   •   -   •
    C   •   •   -
    D                   -   •   •
    E                   •   -   •
    F                   •   •   -
```

**Characteristics:**
- **Clustered dependencies** (ABC cluster together, DEF cluster together)
- **Few cross-cluster dependencies**
- **Dense within clusters, sparse between clusters**

**Conclusion:** High cohesion - module should be split into two:
- Module 1: Components A, B, C
- Module 2: Components D, E, F

---

### Pattern 2: Low Cohesion (Poor Quality)

```
        A   B   C   D   E   F
    A   -   •           •
    B       -               •
    C   •       -   •
    D               -       •
    E   •                   -
    F       •   •           -
```

**Characteristics:**
- **Scattered dependencies** across the matrix
- **No clear clustering**
- **Random distribution**

**Conclusion:** Low cohesion - components don't belong together. Refactor needed.

---

### Pattern 3: Perfect Cohesion (Ideal but Rare)

```
        A   B   C
    A   -   •   •
    B   •   -   •
    C   •   •   -
```

**Characteristics:**
- **Every component depends on every other** (complete graph)
- **Very tight coupling within module**
- **All components change together**

**Conclusion:** Perfect cohesion - but watch for excessive coupling.

---

## Cohesion Metrics

### Quantitative Measures

#### 1. LCOM (Lack of Cohesion of Methods)

**Formula (simplified):**
```
LCOM = (# of method pairs with no shared fields) - (# of method pairs with shared fields)
```

- **LCOM = 0:** High cohesion (good)
- **LCOM > 0:** Low cohesion (problematic)

#### 2. Cluster Density

**Formula:**
```
Density = (actual dependencies in cluster) / (possible dependencies in cluster)
```

- **Density ≈ 1:** Very cohesive cluster
- **Density ≈ 0:** Loosely coupled components

---

## Example Analysis

### Scenario: E-Commerce Module Dependency Matrix

```
        Product   Cart   Payment   Shipping   User
Product     -       •
Cart        •       -       •         •
Payment                     -
Shipping                                -       •
User        •       •                   •       -
```

### Step-by-Step Analysis

**1. Identify clusters:**
- **Cluster 1:** Product, Cart (order management)
- **Cluster 2:** Payment (isolated)
- **Cluster 3:** Shipping, User (delivery management)

**2. Check cross-cluster dependencies:**
- Cart depends on Payment ❌ (crosses cluster)
- Cart depends on Shipping ❌ (crosses cluster)

**3. Evaluate cohesion:**
- **Within clusters:** Moderate
- **Between clusters:** High (problematic)

**4. Conclusion:**
- **Low cohesion** - components mixed across concerns
- Cart has too many responsibilities

**5. Refactoring Recommendation:**
```
Module 1: Product Catalog (Product)
Module 2: Order Management (Cart, Payment)
Module 3: Delivery (Shipping, User)
```

---

## Common Cohesion Anti-Patterns

### 1. "God Module" Pattern

**Symptom:** One component depends on everything

```
        A   B   C   D   E
    A   -   •   •   •   •
```

**Problem:** Component A is a god object doing too much

---

### 2. "Utility Dump" Pattern

**Symptom:** No dependencies between components

```
        A   B   C   D
    A   -
    B       -
    C           -
    D               -
```

**Problem:** Unrelated utilities bundled together - no cohesion

---

### 3. "Chain" Pattern

**Symptom:** Linear dependency chain

```
        A   B   C   D
    A   -   •
    B       -   •
    C           -   •
    D               -
```

**Problem:** Should these be separate modules or a pipeline?

---

## Decision Framework

### Questions to Ask

1. **Clustering:**
   - Do I see clear clusters of dependencies?
   - Are clusters isolated from each other?

2. **Density:**
   - How many dependencies within each cluster?
   - High density = good cohesion

3. **Cross-Cluster:**
   - How many dependencies cross cluster boundaries?
   - Minimize cross-cluster dependencies

4. **Balance:**
   - Are clusters roughly equal in size?
   - Avoid one huge cluster and several tiny ones

---

## Refactoring Strategies

### When Cohesion is Low

**Strategy 1: Extract Module**
- Move tightly coupled components into their own module

**Strategy 2: Introduce Abstraction**
- Create interface to hide cross-cluster dependencies

**Strategy 3: Move Responsibilities**
- Reassign methods to components where they truly belong

**Strategy 4: Split Module**
- Break apart module along cluster boundaries

---

## Practical Exercise

### Your Task

Given the dependency matrix on the slide:

1. **Identify clusters** - Group tightly coupled components
2. **Count dependencies** - Within clusters vs. across clusters
3. **Assess quality** - High or low cohesion?
4. **Recommend action** - Keep as is, split, or refactor?

### Questions to Discuss

1. What patterns do you see in the matrix?
2. Are there clear clusters of dependencies?
3. What does the clustering tell you about module quality?
4. How would you refactor this building block?

---

## Key Takeaways

1. **Dependency matrices reveal cohesion** - Visual pattern analysis is powerful

2. **Look for clusters** - Tightly coupled components should be grouped

3. **Minimize cross-cluster dependencies** - Indicates low cohesion

4. **Use metrics objectively** - Don't rely only on intuition

5. **Refactor when cohesion is low** - Split modules along cluster boundaries

6. **High cohesion enables change** - Related things grouped together are easier to modify

---

## See Also

- [README.md](README.md) - Exercise overview and instructions
- [Exercise slides](slides/) - Dependency matrix visualization
- Related principles: SRP, CCP, Common Closure Principle
