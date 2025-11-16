# ISearchProduct Interface - Peer Review Exercise

**Exercise ID:** ArchitecturalQuality04
**Type:** Class Group Exercise
**Topic:** Interface Quality Assessment
**Focus:** Applying systematic quality checklist to interface specifications

---

## Exercise Overview

In this exercise, you will review a real interface specification using an 11-question quality checklist. The interface
under review is `ISearchProduct` - a simple product search interface that appears functional at first glance but has
several hidden quality issues.

**Learning Objective:** Apply systematic methodology to identify interface quality problems before they become expensive
to fix in production.

---

## Exercise Tasks

### Step 1: Extend the Quality Checklist (Group Work)

The course provides 5 basic quality questions. Your group must:

1. Review the 5 provided questions
2. Add **at least 3 additional questions** from best practices (e.g., null-safety, thread-safety, mutability)
3. Create a scoring scheme (e.g., 0-2 points per question)
4. Define quality levels (Excellent, Good, Acceptable, Poor)

**Deliverable:** Extended checklist document ready for use

### Step 2: Review ISearchProduct Interface (Group Work)

Apply your extended checklist to evaluate this interface:

```csharp
public interface ISearchProduct
{
    Product? Find(string code);
    IEnumerable<Product> Search(string text);
    IList<Product> All();
}
```

**Tasks:**

- Answer each checklist question
- Provide evidence for each score
- Calculate total quality score
- Identify top 3-4 weaknesses

**Deliverable:** Completed checklist with scores and evidence

### Step 3: Present Findings (Class Discussion)

Each group presents:

- Their extended checklist (which questions did you add?)
- Quality score for ISearchProduct
- Top weaknesses identified
- Concrete improvement recommendations

**Goal:** Compare different perspectives and learn from other groups' insights

---

## Files in This Exercise

- **[interface-quality-checklist.md](interface-quality-checklist.md)** - Extended 11-question checklist with:
    - Original 5 questions + 6 additional best-practice questions
    - Scoring scheme (0-2 points each, max 22)
    - Quality levels (Excellent 91-100%, Good 73-86%, etc.)

- **[peer-review-isearchproduct.md](peer-review-isearchproduct.md)** - Complete example review:
    - Systematic evaluation of all 11 questions
    - Score: 41/100 (Needs Improvement)
    - Detailed weaknesses analysis
    - Concrete refactoring recommendations

- **[earlybird-requirements-v150.pdf](earlybird-requirements-v150.pdf)** - Full EarlyBird system requirements

- **[exercise-slide-145.pdf](exercise-slide-145.pdf)** - Exercise slide showing the task

- **[slides/](slides/)** - Exercise slides

---

## Key Quality Dimensions to Consider

### 1. Clarity & Documentation (Questions 1, 5, 6, 7)

- Are method names self-explanatory?
- Are exceptions documented?
- Is null behavior explicit?
- Is error handling strategy clear?

### 2. Type Safety (Questions 2, 3, 10)

- Appropriate parameter types?
- Appropriate return types?
- Domain concepts as value objects vs. primitives?

### 3. Design Principles (Questions 4, 8, 9)

- Interface cohesion (SRP)?
- Mutability/side effects controlled?
- Extensibility without breaking changes?

### 4. Production Readiness (Question 11)

- Thread-safety expectations documented?

---

## Common Pitfalls Found in Reviews

### ❌ Returning IList<T> instead of IReadOnlyList<T>

Exposes mutable collection → callers can corrupt internal state

### ❌ Using primitive types for domain concepts

`string code` instead of `ProductCode` → loses type safety

### ❌ Undocumented null behavior

`Product?` return but no explanation when null is returned

### ❌ Missing exception documentation

Callers must guess when exceptions are thrown

### ❌ No thread-safety guidance

Unclear if implementation must be thread-safe

---

## Recommended Improvements (Spoiler Alert!)

If you want to see the recommended fixes before doing the exercise,
check [peer-review-isearchproduct.md](peer-review-isearchproduct.md) section 6.

**Hint:** The improvements include:

- Read-only collections
- Value objects for domain concepts
- Better search criteria design
- Comprehensive documentation

---

## Learning Outcomes

After completing this exercise, you will be able to:

1. **Apply systematic interface review methodology**
    - Use a structured checklist rather than ad-hoc review
    - Score interfaces quantitatively

2. **Identify subtle quality issues**
    - Mutability problems with collection return types
    - Type safety gaps with primitive obsession
    - Documentation gaps that lead to bugs

3. **Propose concrete improvements**
    - Not just "this is bad" but specific refactorings
    - Understand trade-offs between simplicity and safety

4. **Communicate quality concerns**
    - Evidence-based scoring
    - Prioritized recommendations

---

## Related Exercises

- **[02-isearchproduct-interface-specification](../02-isearchproduct-interface-specification/)** - The original
  interface specification exercise
- **[04-ilist-interface-design](../04-ilist-interface-design/)** - Design and review a generic list interface
- **[06-heat-flow-analysis-tell-dont-ask](../06-heat-flow-analysis-tell-dont-ask/)** - Tell, Don't Ask principle

---

## Tips for Success

1. **Don't rush to coding** - Quality issues are easier to fix in the design phase
2. **Use evidence-based scoring** - "2 points because..." not "feels good"
3. **Focus on user impact** - How does this quality issue hurt callers?
4. **Propose actionable fixes** - Specific code examples, not vague suggestions
5. **Compare with industry standards** - What does .NET BCL do? Java? TypeScript?

---

*This exercise teaches systematic interface quality assessment - a critical skill for architecture reviews*
