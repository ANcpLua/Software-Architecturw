# AI-Driven Architecture Development Using Embeddings

**Exercise ID:** ArchitectureDevelopment02
**Approach:** Embedding-Based Requirements Clustering
**Application:** EarlyBird System

---

## Exercise Overview

This exercise demonstrates a novel approach to architecture development using **AI embeddings** to automatically
discover architectural components from functional requirements.

### The Embedding Approach

**Core Concept:**

1. Feed functional requirements into an embedding model (e.g., sentence-transformers, OpenAI embeddings)
2. Store requirement embeddings in a vector database
3. Use clustering algorithms to group semantically similar requirements
4. Each cluster represents a potential architectural component
5. Name components based on cluster characteristics

---

## The EarlyBird Exercise

### Task Description

Using the EarlyBird breakfast service requirements:

1. **Embed Requirements**: Convert each functional requirement into a vector embedding
2. **Cluster Embeddings**: Let the vector database cluster similar requirements
3. **Identify Components**: Each cluster suggests a component in the application core
4. **Name Components**: Find meaningful names for the discovered clusters

### Example Requirements for Clustering

Sample EarlyBird requirements that would be embedded:

```
"The lion sleeps tonight."
"The tiger hunts all day."
"Johann Sebastian Bach lived from 1685 to 1750."
```

These example sentences demonstrate the clustering concept - semantically similar sentences (about animals) cluster
together, while unrelated ones (about Bach) form separate clusters.

For EarlyBird, actual requirements would be:

- "Customer can search for breakfast products"
- "System displays available menu items"
- "Customer can add items to shopping basket"
- "System calculates total price including delivery"
- "Customer provides delivery address"
- "System validates address is in service area"
- etc.

---

## Expected Clustering Results

### Predicted Component Clusters

Based on EarlyBird requirements, the embedding approach should discover clusters like:

**1. Product Search & Catalog Component**

- Search for products
- Display menu items
- Filter by category/price/dietary requirements
- Show product details

**2. Shopping Basket Component**

- Add items to basket
- Modify quantities
- Remove items
- Calculate subtotals

**3. Order Management Component**

- Create order from basket
- Calculate total with delivery fee
- Generate order confirmation
- Track order status

**4. Delivery & Logistics Component**

- Capture delivery address
- Validate service area
- Calculate delivery fee
- Schedule delivery time

**5. Customer Account Component**

- Register customer
- Login/authentication
- Store preferences
- View order history

**6. Payment Processing Component**

- Select payment method
- Process payment
- Handle payment failures
- Generate receipt

---

## Methodology: Step-by-Step

### Step 1: Prepare Requirements

Extract all functional requirements from requirements document:

```python
requirements = [
    "Customer can search for breakfast products",
    "System displays available menu items",
    "Customer can add items to shopping basket",
    # ... all functional requirements
]
```

### Step 2: Generate Embeddings

Using a sentence transformer model:

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(requirements)
```

### Step 3: Store in Vector Database

```python
import chromadb

client = chromadb.Client()
collection = client.create_collection("earlybird_requirements")

collection.add(
    embeddings=embeddings,
    documents=requirements,
    ids=[f"req_{i}" for i in range(len(requirements))]
)
```

### Step 4: Cluster Requirements

```python
from sklearn.cluster import KMeans

# Determine optimal number of clusters (components)
n_components = 6  # Based on domain knowledge

kmeans = KMeans(n_clusters=n_components, random_state=42)
cluster_labels = kmeans.fit_predict(embeddings)
```

### Step 5: Analyze Clusters

```python
for cluster_id in range(n_components):
    cluster_reqs = [req for req, label in zip(requirements, cluster_labels)
                    if label == cluster_id]
    print(f"\nCluster {cluster_id}:")
    for req in cluster_reqs:
        print(f"  - {req}")
```

### Step 6: Name Components

Analyze each cluster and assign meaningful component names based on:

- Common themes in requirements
- Domain knowledge
- Architectural patterns (e.g., shopping basket is standard e-commerce pattern)

---

## Architecture Proposal from Clusters

### Application Core Components (Derived from Clustering)

```
┌─────────────────────────────────────────────────────────┐
│           EarlyBird Application Core                     │
│                                                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Product     │  │  Shopping    │  │  Order       │  │
│  │  Catalog     │──│  Basket      │──│  Management  │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│         │                                      │         │
│         │                                      │         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Customer    │  │  Delivery    │  │  Payment     │  │
│  │  Account     │  │  Logistics   │  │  Processing  │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Component Responsibilities

**Product Catalog**

- Search products
- Browse categories
- Display product details
- Manage product availability

**Shopping Basket**

- Add/remove items
- Update quantities
- Calculate subtotals
- Persist basket state

**Order Management**

- Create orders
- Calculate totals
- Generate confirmations
- Track order lifecycle

**Customer Account**

- Authentication
- Profile management
- Preferences
- Order history

**Delivery Logistics**

- Address validation
- Service area checking
- Delivery scheduling
- Fee calculation

**Payment Processing**

- Payment method selection
- Transaction processing
- Receipt generation
- Refund handling

---

## Benefits of Embedding-Based Approach

### Advantages

1. **Objective Discovery**: Less bias from preconceived architectural ideas
2. **Requirements Coverage**: Ensures all requirements map to components
3. **Semantic Understanding**: Captures meaning, not just keywords
4. **Scalability**: Works with large requirement sets (100+ requirements)
5. **Rapid Iteration**: Quick to re-cluster if requirements change

### Challenges

1. **Component Naming**: Clusters need human interpretation
2. **Granularity Control**: Choosing right number of clusters is subjective
3. **Cross-Cutting Concerns**: May not cluster well (security, logging)
4. **Dependency Identification**: Clustering doesn't reveal component dependencies
5. **Quality Attributes**: Focuses on functional requirements, may miss non-functional

---

## Validation of Discovered Architecture

### Checklist for Cluster-Derived Components

- [ ] Each cluster has cohesive, related requirements
- [ ] Clusters are loosely coupled (minimal overlap)
- [ ] Component names accurately reflect cluster content
- [ ] All requirements assigned to exactly one cluster
- [ ] No component is too large (>20% of requirements)
- [ ] No component is too small (<3-5 requirements)
- [ ] Components align with domain knowledge
- [ ] Architecture supports key use cases

### Refinement Process

After initial clustering:

1. **Review outliers**: Requirements that don't fit any cluster well
2. **Merge clusters**: If two clusters are too similar
3. **Split clusters**: If one cluster has multiple themes
4. **Adjust parameters**: Try different numbers of clusters
5. **Domain validation**: Check with domain experts

---

## Comparison: AI vs. Traditional Approaches

| Aspect            | Embedding-Based  | Traditional (Manual)  |
|-------------------|------------------|-----------------------|
| **Speed**         | Fast (minutes)   | Slow (hours/days)     |
| **Bias**          | Data-driven      | Experience-driven     |
| **Completeness**  | All reqs covered | May miss requirements |
| **Quality**       | Needs validation | Often high quality    |
| **Flexibility**   | Easy to re-run   | Costly to redo        |
| **Dependencies**  | Not captured     | Explicitly modeled    |
| **Cross-cutting** | Poor clustering  | Explicitly identified |

**Best Approach**: Use embeddings for initial discovery, then refine with traditional architectural thinking.

---

## Implementation Tools

### Recommended Stack

**Embedding Models:**

- `sentence-transformers/all-MiniLM-L6-v2` (lightweight, fast)
- `text-embedding-ada-002` (OpenAI, high quality)
- `BAAI/bge-large-en-v1.5` (state-of-the-art open source)

**Vector Databases:**

- ChromaDB (simple, local)
- Pinecone (cloud, scalable)
- Weaviate (open source, production-ready)

**Clustering Algorithms:**

- K-Means (simple, requires specifying k)
- DBSCAN (finds clusters automatically)
- Hierarchical Clustering (creates dendrograms)

**Analysis Tools:**

- scikit-learn (clustering algorithms)
- pandas (data manipulation)
- matplotlib/seaborn (visualization)

---

## Extension: Dependency Discovery

While clustering groups requirements, we can extend the approach to find dependencies:

### Inter-Cluster Distance Analysis

```python
import numpy as np

# Calculate centroid of each cluster
centroids = {}
for cluster_id in range(n_components):
    cluster_embeddings = embeddings[cluster_labels == cluster_id]
    centroids[cluster_id] = np.mean(cluster_embeddings, axis=0)

# Find closest cluster pairs (potential dependencies)
from scipy.spatial.distance import cosine

for i in range(n_components):
    for j in range(i+1, n_components):
        dist = cosine(centroids[i], centroids[j])
        print(f"Distance between cluster {i} and {j}: {dist:.3f}")
```

Clusters with lower distances likely have more interaction.

---

## Real-World Considerations

### When This Approach Works Well

- Large number of requirements (50+)
- Well-written, atomic requirements
- Greenfield projects (no existing architecture)
- Exploration phase (finding initial structure)

### When to Use Traditional Approaches

- Few requirements (<20)
- Poorly documented requirements
- Brownfield projects (existing architecture to maintain)
- Need to identify cross-cutting concerns
- Performance-critical architecture decisions

---

## Exercise Deliverable

### Expected Output

1. **Clustered Requirements Document**
    - List of all requirements
    - Cluster assignment for each requirement
    - Cluster names (component names)

2. **Architecture Diagram**
    - Component boxes
    - High-level dependencies (manually added)
    - Application core boundary

3. **Component Specifications**
    - For each component:
        - Name
        - Responsibilities (requirements in cluster)
        - Interfaces (inferred)
        - Dependencies on other components

4. **Reflection Document**
    - How many clusters were tried?
    - What worked well?
    - What required manual adjustment?
    - Comparison with traditional approach

---

## Learning Outcomes

After completing this exercise, you should be able to:

1. **Understand AI4SE**: Apply AI for Software Engineering tasks
2. **Use Embeddings**: Convert text to vector representations
3. **Cluster Data**: Group similar items using unsupervised learning
4. **Interpret Clusters**: Derive meaningful architecture from data clusters
5. **Validate Architecture**: Critically evaluate AI-generated architectures
6. **Hybrid Approach**: Combine AI automation with human expertise

---

## Further Reading

### Academic Papers

- "AI for Software Architecture: A Systematic Literature Review" (2023)
- "Using Natural Language Processing to Extract Architecture from Requirements" (2022)

### Tools & Frameworks

- [Sentence-Transformers Documentation](https://www.sbert.net/)
- [ChromaDB Getting Started](https://docs.trychroma.com/)
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)

### Related Concepts

- **AI4SE**: AI for Software Engineering
- **SE4AI**: Software Engineering for AI systems
- **Requirements Engineering**: Extracting and managing requirements
- **Architecture Recovery**: Discovering architecture from existing systems

---

## Conclusion

The embedding-based approach to architecture development represents a **modern, data-driven methodology** that
complements traditional architectural thinking. While it excels at discovering component boundaries from requirements,
it works best when combined with human expertise to refine the results and identify cross-cutting concerns.

The "almost an architecture" result from clustering is a powerful starting point that can significantly accelerate the
architecture development process, especially for complex systems with many requirements.

---

**Source**: Exercise slide "Using AI to Develop an Architecture - the Embedding Approach"
**Application**: EarlyBird breakfast delivery system
