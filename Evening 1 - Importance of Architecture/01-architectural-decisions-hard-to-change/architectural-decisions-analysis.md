# Architectural Decisions: Analysis of What's Hard to Change

**Exercise:** Class Group Exercise - Architectural Decisions
**Source:** Page 22, The Importance of Architecture V702
**Type:** Analysis & Discussion

---

## Question: What Decisions Are Hard to Change?

This analysis explores which software decisions have high change costs and why understanding this matters for
architecture.

---

## 1. Framework: Identifying Hard-to-Change Decisions

### The Architectural Significance Test

A decision is architecturally significant (hard to change) if changing it would:

1. **Require changes across multiple components** (high coupling)
2. **Invalidate existing infrastructure investments** (sunk costs)
3. **Break external contracts or commitments** (irreversible promises)
4. **Require significant team retraining** (knowledge dependencies)
5. **Affect fundamental system qualities** (performance, security, scalability)

---

## 2. Categories of Hard-to-Change Decisions

### 2.1 Technology Stack Decisions

**Examples:**

- Programming language (Java vs. Python vs. C#)
- Primary database (PostgreSQL vs. MongoDB vs. Cassandra)
- Operating system (Linux vs. Windows)
- Web framework (React vs. Angular vs. Vue)

**Why Hard to Change:**

- Entire codebase written in chosen language
- Developer expertise specialized
- Libraries and tools ecosystem-dependent
- Deployment infrastructure configured
- CI/CD pipelines tailored

**Cost of Change:** Very High (6-12 months, major rewrite)

---

### 2.2 Data Structure and Storage Decisions

**Examples:**

- Data schema design
- File formats (JSON vs. XML vs. Protobuf)
- Data persistence approach (relational vs. document vs. key-value)
- Caching strategy

**Why Hard to Change:**

- Historical data stored in old format
- Migration tools needed
- Backward compatibility required
- Multiple systems depend on format
- Data volume makes migration expensive

**Cost of Change:** High (3-6 months, careful migration)

---

### 2.3 Communication Protocol Decisions

**Examples:**

- REST vs. GraphQL vs. gRPC
- Synchronous vs. asynchronous messaging
- Message queue technology (RabbitMQ vs. Kafka)
- API versioning strategy

**Why Hard to Change:**

- External clients depend on API
- Integration contracts established
- Monitoring and logging configured
- Documentation and SDKs published

**Cost of Change:** High (requires versioning, gradual migration)

---

### 2.4 Security and Authentication Decisions

**Examples:**

- Authentication mechanism (OAuth2 vs. SAML vs. JWT)
- Encryption algorithms
- Authorization model (RBAC vs. ABAC)
- Session management approach

**Why Hard to Change:**

- User credentials stored with chosen method
- Compliance requirements locked in
- Third-party integrations configured
- Security audits based on current approach

**Cost of Change:** Very High (security-critical, risky migration)

---

### 2.5 Deployment Architecture Decisions

**Examples:**

- Monolith vs. microservices
- Cloud provider (AWS vs. Azure vs. GCP)
- Container orchestration (Kubernetes vs. Docker Swarm)
- Infrastructure as Code tool (Terraform vs. CloudFormation)

**Why Hard to Change:**

- Operations runbooks written
- Team skills specialized
- Monitoring and alerting configured
- Cost optimization based on provider
- Compliance certifications provider-specific

**Cost of Change:** Very High (6-18 months, operational risk)

---

## 3. What Makes Changes Costly?

### 3.1 Direct Costs

- Developer time for rewrite
- Testing and QA effort
- Migration tool development
- Infrastructure changes
- Licensing costs

### 3.2 Indirect Costs

- Feature development stops
- Customer disruption
- Training requirements
- Documentation updates
- Risk of introducing bugs

### 3.3 Opportunity Costs

- Delayed new features
- Lost competitive advantage
- Market timing missed

---

## 4. Decisions That Are Easier to Change

### Low-Change-Cost Decisions

**Examples:**

- UI component libraries (within same framework)
- Logging libraries
- Testing frameworks
- Code formatting rules
- Internal class names

**Why Easier:**

- Localized impact
- No external dependencies
- Easy to encapsulate
- Quick to refactor

**Implication:** These are **design decisions**, not architectural decisions.

---

## 5. The Cost-of-Change Curve

```
Change Cost
    ↑
    |           ╱────────────── External API Contracts
    |         ╱
    |       ╱────────────── Database Schema
    |     ╱
    |   ╱────────────── Programming Language
    | ╱
    |╱────────────── Internal Abstractions
    └──────────────────────────────────────→ Time
                               (Effort to Change)
```

**Key Insight:** Architectural decisions have exponentially increasing change costs over time.

---

## 6. Case Study: Real-World Example

### Scenario: E-commerce Platform Language Migration

**Initial Decision (Year 0):** Built in PHP
**Change Decision (Year 5):** Migrate to Java

**What Made It Hard:**

1. **Codebase Size:** 500,000 lines of PHP
2. **Team:** 15 PHP developers, no Java experience
3. **Dependencies:** 200+ PHP libraries
4. **Data:** 10TB database, tight coupling to PHP serialization
5. **Operations:** Deployment scripts, monitoring in PHP
6. **External:** Payment processor integration used PHP SDK

**Migration Cost:**

- Duration: 18 months
- Team: 20 developers (hired Java experts)
- Budget: €2.5 million
- Business Impact: Feature freeze for 6 months

**Lesson:** Programming language is architecturally significant.

---

## 7. Strategies to Manage Hard-to-Change Decisions

### 7.1 Defer Irreversible Decisions

- Use abstractions to delay commitment
- Prototype before committing
- Choose reversible options when possible

### 7.2 Document Decision Rationale

- Record why decision was made
- List alternatives considered
- Note assumptions and constraints

### 7.3 Design for Change

- Use interfaces and abstractions
- Minimize coupling
- Encapsulate volatile parts
- Apply dependency inversion

### 7.4 Prototype High-Risk Decisions

- Build spikes to validate
- Test with realistic loads
- Verify assumptions early

---

## 8. Architectural Decision Records (ADRs)

### Template for Documenting Hard-to-Change Decisions

```markdown
# ADR-001: Choice of Database Technology

## Status
Accepted

## Context
Need to store user data, product catalog, and orders.
Expected scale: 1M users, 100K products, 10K orders/day.

## Decision
Use PostgreSQL for all data storage.

## Consequences

**Positive:**
- ACID guarantees for orders
- Mature ecosystem
- Team has PostgreSQL expertise
- Strong consistency model

**Negative:**
- Horizontal scaling requires sharding
- NoSQL might be better for product catalog
- Schema migrations can be complex

**Change Cost:** Very High (entire data layer)

## Alternatives Considered
- MongoDB: Better for product catalog, but weaker consistency
- DynamoDB: Better scalability, but vendor lock-in
- MySQL: Similar, but less feature-rich
```

---

## 9. Self-Check Questions

1. **Identify:** List 5 decisions in your current project. Which are hard to change?

2. **Analyze:** For each hard-to-change decision, what makes it costly?

3. **Evaluate:** Could you have deferred any of these decisions?

4. **Design:** How could you abstract these decisions to reduce coupling?

---

## 10. Key Takeaways

1. **Not all decisions are equal** - Some have exponentially higher change costs.

2. **Architectural decisions are those that are hard to change** - Focus your architecture effort here.

3. **Change cost increases over time** - Get architectural decisions right early.

4. **Document significant decisions** - Use ADRs to record rationale and trade-offs.

5. **Design for change where possible** - Use abstractions to defer commitment.

6. **Accept some irreversibility** - Perfect flexibility is impossible; choose wisely.

---

## References

- Martin Fowler: "Who Needs an Architect?"
- Michael Nygard: "Documenting Architecture Decisions"
- Grady Booch: "On Architecture"

---

## See Also

- [README.md](README.md) - Exercise overview and learning objectives
- [Architectural Decisions slide](slides/architectural-decisions-analysis-slide-p13.png)
- Evening 2 exercises on architectural quality
