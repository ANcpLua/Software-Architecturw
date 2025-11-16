# IList Interface - Peer Review Exercise

**Exercise ID:** ArchitecturalQuality07 (Part 2)
**Type:** Class Group Exercise
**Topic:** Interface Quality Review
**Focus:** Applying the 11-point interface checklist

---

## Exercise Overview

This is the peer review component of the IList interface design exercise. After designing the generic `IList<T>`
interface in the previous exercise, you now evaluate it using the comprehensive interface quality checklist.

**Goal:** Apply systematic interface review criteria to identify design flaws and improvement opportunities.

---

## Exercise Task

### Review Your IList<T> Design

Use the [interface-quality-checklist.md](../03-isearchproduct-peer-review/interface-quality-checklist.md) to evaluate
the interface you designed.

**Focus Areas:**

1. **Interface Segregation Principle (ISP)**
    - Are read-only and mutable operations mixed?
    - Can read-only callers avoid depending on write operations?

2. **Naming Conventions**
    - Does it follow platform conventions (`.NET: Count`, `Java: size()`)?
    - Are method names clear and unambiguous?

3. **Return Types**
    - Does `Remove` indicate success (bool vs void)?
    - Are appropriate types used?

4. **Documentation**
    - What happens on index out of range?
    - Are null elements allowed?
    - Is it thread-safe?

5. **Completeness**
    - Are essential operations included (Contains, IndexOf, RemoveAt)?

**Deliverable:** Scored review with specific recommendations

---

## Reference Implementation Review

**[peer-review-ilist.md](peer-review-ilist.md)** - Complete review example of a typical first-attempt design

**Score:** 45/100 (Needs Improvement)

**Key Findings:**

- ISP violation: read-only and mutable operations mixed
- Missing operations: Contains, IndexOf, RemoveAt
- Non-standard naming conventions
- Incomplete documentation
- No consideration for covariance

**Recommendations:**

1. Separate into `IReadOnlyList<T>` and `IList<T>`
2. Use platform conventions (Count, not Size)
3. Return bool from Remove to indicate success
4. Use indexer syntax instead of Get/Set methods
5. Document exception behavior

---

## Compare with .NET BCL

The .NET Base Class Library implements the design lessons learned:

```csharp
// Separate read-only interface
public interface IReadOnlyList<out T> : IReadOnlyCollection<T>
{
    int Count { get; }
    T this[int index] { get; }
}

// Mutable interface extends read-only
public interface IList<T> : ICollection<T>, IReadOnlyList<T>
{
    new T this[int index] { get; set; }
    void Add(T item);
    bool Remove(T item);
    void RemoveAt(int index);
    int IndexOf(T item);
    void Insert(int index, T item);
    void Clear();
}
```

**Discussion Questions:**

- Why separate `IReadOnlyList<T>` from `IList<T>`?
- Why does `Remove` return `bool`?
- What is `out T` (covariance) and why does it matter?
- Why use indexer `this[int]` instead of `Get(int)` method?

---

## Common Design Flaws

### ❌ Flaw 1: No Separation of Read/Write Operations

Forces read-only clients to depend on mutation methods.

**Fix:** Create separate `IReadOnlyList<T>` interface

### ❌ Flaw 2: void Remove(T item)

Caller can't tell if removal succeeded.

**Fix:** `bool Remove(T item)` returns true if item was found and removed

### ❌ Flaw 3: Non-Standard Naming

Using `Size` instead of `.NET convention: Count`

**Fix:** Follow platform conventions for developer familiarity

### ❌ Flaw 4: Get(int)/Set(int, T) Methods

Doesn't feel like array/indexer access.

**Fix:** Use indexer syntax: `T this[int index] { get; set; }`

### ❌ Flaw 5: Missing Essential Operations

No `Contains`, `IndexOf`, `RemoveAt`

**Fix:** Include operations users expect from a list

### ❌ Flaw 6: Undocumented Error Behavior

No specification of exceptions thrown.

**Fix:** Document `ArgumentOutOfRangeException` for invalid index, `ArgumentNullException` if applicable

---

## Files

- `README.md` - This file
- `peer-review-ilist.md` - Complete review example with scoring
- `exercise-slide-147-148.pdf` - Exercise slides

---

## Key Learning: Interface Segregation Principle

**Problem:** Mixing read and write operations

```csharp
// Signature suggests modification is possible
void DisplayProducts(IList<Product> products)
{
    foreach (var p in products) Console.WriteLine(p);
}
```

**Solution:** Separate concerns

```csharp
// Signature makes read-only intent explicit
void DisplayProducts(IReadOnlyList<Product> products)
{
    foreach (var p in products) Console.WriteLine(p);
}
```

**Benefits:**

- Compiler enforces read-only access
- Intent is explicit in the signature
- More flexible (accepts immutable collections)
- Supports covariance

---

## Advanced: Covariance

Why `IReadOnlyList<out T>` uses `out`?

```csharp
IReadOnlyList<string> strings = new List<string> { "a", "b" };
IReadOnlyList<object> objects = strings; // ✓ Works with 'out T'
```

Without `out`, this would be a compile error. Covariance allows safe upcasting for read-only operations.

**Constraint:** Only works when `T` appears in "output" positions (return types), not "input" (parameters).

That's why `Contains(T item)` is **NOT** in `IReadOnlyList<out T>` - it would break covariance.

---

## Learning Outcomes

After completing this exercise, you will be able to:

1. **Apply interface quality checklist systematically**
2. **Identify ISP violations**
3. **Recognize platform convention mismatches**
4. **Evaluate interface completeness**
5. **Understand covariance implications**

---

## Related Exercises

- **[04-ilist-interface-design](../04-ilist-interface-design/)** - Interface design (Part 1)
- **[03-isearchproduct-peer-review](../03-isearchproduct-peer-review/)** - Interface quality checklist
- **[02-isearchproduct-interface-specification](../02-isearchproduct-interface-specification/)** - O-Interface
  specification

---

## Recommended Reading

- [.NET IList<T> Documentation](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ilist-1)
- [.NET IReadOnlyList<T> Documentation](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlylist-1)
- [Covariance and Contravariance in C#](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/covariance-contravariance/)

---

*This exercise teaches you to evaluate interface designs against professional quality criteria*
