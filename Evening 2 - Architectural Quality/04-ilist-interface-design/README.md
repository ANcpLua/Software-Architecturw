# IList Interface - Design & Review Exercise

**Exercise ID:** ArchitecturalQuality07
**Type:** Class Group Exercise
**Topic:** Generic Collection Interface Design
**Focus:** Interface Segregation Principle (ISP) and O-Interface design

---

## Exercise Overview

This is a two-part exercise where you first **design** a generic list interface from scratch, then **review** it using
the interface quality checklist from the previous exercise.

**Challenge:** Creating a simple, reusable `IList<T>` interface is harder than it looks. This exercise reveals common
design mistakes and teaches you to think about interface contracts carefully.

---

## Exercise Tasks

### Part 1: Design IList<T> Interface (Group Work - 15 min)

**Scenario:** You need a generic list interface for the EarlyBird system that can be implemented by different collection
types (ArrayList, LinkedList, etc.).

**Requirements:**

1. Must support basic operations: add, remove, get, set, clear
2. Must be generic (`<T>` type parameter)
3. Must be an O-Interface (technology-independent, no framework dependencies)
4. Should have a size/count property

**Task:** Design the interface specification including:

- Method signatures
- Property definitions
- Brief documentation comments

**Deliverable:** Interface code ready for peer review

---

### Part 2: Peer Review Using Checklist (Group Work - 20 min)

Now review your own (or another group's) interface using
the [interface-quality-checklist.md](../03-isearchproduct-peer-review/interface-quality-checklist.md).

**Focus Areas:**

1. **Interface Segregation Principle (ISP)**
    - Are read-only and mutable operations mixed?
    - Can callers who only need read access avoid depending on write operations?

2. **Naming Conventions**
    - Does it follow platform conventions (`.NET: Count`, `Java: size()`)?

3. **Return Types**
    - Does `Remove` indicate success?
    - Are collections returned as read-only where appropriate?

4. **Documentation**
    - What happens on index out of range?
    - Are null elements allowed?
    - Is it thread-safe?

**Deliverable:** Scored review with recommendations

---

### Part 3: Compare with .NET BCL (Class Discussion)

Compare your design with the real .NET `IList<T>` and `IReadOnlyList<T>`:

```csharp
// .NET separates read-only from mutable
public interface IReadOnlyList<out T>
{
    int Count { get; }
    T this[int index] { get; }
}

public interface IList<T> : IReadOnlyList<T>
{
    new T this[int index] { get; set; }
    void Add(T item);
    bool Remove(T item);
    void Clear();
    // ... more operations
}
```

**Discussion Questions:**

- Why is there a separate `IReadOnlyList<T>`?
- Why does `Remove` return `bool`?
- What is `out T` (covariance)?
- Why use indexer `this[int]` instead of `Get(int)`?

---

## Common Design Mistakes (Spoiler Alert!)

### ❌ Mistake 1: No Read-Only Interface

Mixing read and write operations forces read-only clients to depend on mutation methods.

**Fix:** Separate `IReadOnlyList<T>` and `IList<T>`

### ❌ Mistake 2: void Remove(T item)

Callers can't tell if removal succeeded.

**Fix:** `bool Remove(T item)` returns true if removed

### ❌ Mistake 3: Non-Standard Naming

Using `Size` instead of `.NET convention: Count`

**Fix:** Follow platform conventions for familiarity

### ❌ Mistake 4: Get(int)/Set(int, T)

Doesn't feel like array access.

**Fix:** Use indexer: `T this[int index] { get; set; }`

### ❌ Mistake 5: Missing Operations

No `Contains`, `IndexOf`, `RemoveAt`

**Fix:** Include common list helpers

### ❌ Mistake 6: Undocumented Errors

No guidance on what exceptions are thrown.

**Fix:** Document `ArgumentOutOfRangeException` for invalid index

---

## Files in This Exercise

- **[peer-review-ilist.md](peer-review-ilist.md)** - Complete review example:
    - Evaluates a typical first-attempt design
    - Score: 45/100 (Needs Improvement)
    - Identifies ISP violation and missing operations
    - Recommends separation into read-only and mutable interfaces

- **[earlybird-requirements-v150.pdf](earlybird-requirements-v150.pdf)** - Full system requirements

- **[exercise-slide-147-148.pdf](exercise-slide-147-148.pdf)** - Exercise slides (pages 147-148)

- **[slides/](slides/)** - Exercise slide images

---

## Key Learning: Interface Segregation Principle (ISP)

**Problem:** When you mix read-only and mutable operations in one interface:

```csharp
void DisplayProducts(IList<Product> products)
{
    // This function only reads, but the signature
    // suggests it might modify the list
    foreach (var p in products) Console.WriteLine(p);
}
```

**Solution:** Separate concerns:

```csharp
void DisplayProducts(IReadOnlyList<Product> products)
{
    // Signature makes it clear: read-only access
    foreach (var p in products) Console.WriteLine(p);
}
```

**Benefits:**

- Compiler enforces read-only usage
- Intent is explicit
- More flexible (callers can pass immutable collections)
- Supports covariance (`out T`)

---

## Advanced Topic: Covariance

Why `IReadOnlyList<out T>` uses `out`?

```csharp
IReadOnlyList<string> strings = new List<string> { "a", "b" };
IReadOnlyList<object> objects = strings; // ✓ Works with 'out T'
```

Without `out`, this would be a compile error. Covariance allows safer upcasting.

**Constraint:** Only works if `T` is only in "output" positions (return types), not input (parameters).

That's why `Contains(T item)` is **NOT** in `IReadOnlyList<out T>` - it would break covariance.

---

## Learning Outcomes

After completing this exercise, you will be able to:

1. **Design generic interfaces**
    - Choose appropriate type parameters
    - Understand covariance constraints

2. **Apply Interface Segregation Principle**
    - Separate read-only from mutable operations
    - Recognize when interfaces do too much

3. **Follow platform conventions**
    - Use idiomatic naming (Count vs. size)
    - Use indexers for array-like access

4. **Document contracts precisely**
    - Exception behavior
    - Null handling
    - Thread-safety expectations

5. **Evaluate design trade-offs**
    - Simplicity vs. completeness
    - Type safety vs. flexibility

---

## Related Exercises

- **[03-isearchproduct-peer-review](../03-isearchproduct-peer-review/)** - Peer review methodology and checklist
- **[02-isearchproduct-interface-specification](../02-isearchproduct-interface-specification/)** - Domain-specific
  interface design
- **[06-heat-flow-analysis-tell-dont-ask](../06-heat-flow-analysis-tell-dont-ask/)** - Tell, Don't Ask principle

---

## Tips for Success

1. **Start simple, then extend** - Don't try to design the perfect interface in one pass
2. **Think about different use cases** - Read-only display vs. mutable editing
3. **Check platform conventions** - What does .NET, Java, or TypeScript do?
4. **Document edge cases** - What happens when index is -1? When list is empty?
5. **Test with examples** - Write sample code using your interface

---

## Recommended Reading

- [.NET IList<T> Documentation](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ilist-1)
- [.NET IReadOnlyList<T> Documentation](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlylist-1)
- [Covariance and Contravariance in C#](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/covariance-contravariance/)

---

*This exercise teaches you to design interfaces that are both simple to use and flexible enough for different scenarios*
