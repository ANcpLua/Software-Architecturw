# Evening 1: Importance of Architecture

**PDF:** `1_The_Importance_of_Architecture_V702.pdf`
**Theme:** Why architecture matters - decisions with long-term impact

## Exercise: What Decisions Are Hard to Change?

**Type:** Class Group Exercise
**Topic:** Architectural Decision-Making
**Page:** 13 (in course PDF)

### Task

Identify architectural decisions and analyze their impact on software quality attributes.

**Steps:**
1. Identify architectural decisions that are hard to change
2. For each decision, list the influenced non-functional aspects:
   - Security
   - Efficiency
   - Changeability
   - Reliability
   - Testability
   - Usability
   - etc.
3. Determine which "-ility" appears most frequently

### What You'll Learn

- **Architectural decisions vs. implementation details** - Not all decisions are architectural
- **Quality attribute tradeoffs** - One decision affects multiple "-ilities"
- **Cost of change** - Why some decisions are expensive to reverse
- **Architects as RE specialists** - Architects are requirements engineers for non-functional requirements

### Key Insight

> Architectural decisions often influence non-functional aspects of software. This is why architects are often the requirements engineers for non-functional requirements.

### Example Architectural Decisions

Hard to change:
- Programming language
- Database technology
- Communication patterns (sync/async)
- Deployment model (monolith/microservices)
- Authentication/authorization approach

Easy to change:
- Variable names
- UI colors
- Log message formats
- Algorithm implementations (with proper abstraction)

### Discussion Format

This is a **group discussion exercise** - no coding, no written solution required.

**In-class:** Work in groups to brainstorm decisions and their quality impacts
**Remote learners:** Consider these questions independently and document your insights

### Related Principles

- **Quality Attribute Scenarios** - How to specify non-functional requirements
- **Architecture Tradeoff Analysis** - Balancing conflicting quality attributes
- **Technical Debt** - Long-term cost of poor architectural decisions

## Optional Exercise: Tools Corner

See [optional/tools-corner](../optional/tools-corner) for details.

**Task:** Present tools for developing/documenting architectures that you have practical experience with.
