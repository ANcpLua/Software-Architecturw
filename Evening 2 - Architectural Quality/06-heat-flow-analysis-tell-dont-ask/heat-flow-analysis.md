# Heat Flow Calculator - Architectural Analysis

**Exercise ID:** ArchitecturalQuality09
**Type:** Self-Check Solution
**Principle:** Tell, Don't Ask

---

## Problem Statement

A heat flow regulation system has the following architecture:

- **Room** class stores desired and actual temperatures
- **HeatFlowRegulator** periodically calls:
    - `room.get_desired_temp()`
    - `room.get_actual_temp()`
- **HeatFlowRegulator** compares temperatures and calls **Furnace** to heat if needed

**Question:** What are the architectural weaknesses?

---

## Architectural Weaknesses

### 1. Violation of "Tell, Don't Ask" Principle

**Problem:** The `HeatFlowRegulator` pulls data out of `Room` and makes decisions based on that data.

**Impact:**

- Business logic about when to heat is in the **wrong place** (regulator instead of room)
- The `Room` object becomes a passive data structure
- Violates encapsulation - room's internal state is exposed

**Quote from Arthur Riel:**
> "Procedural code gets information then makes decisions. Object-oriented code tells objects to do things."

### 2. Information Hiding Violation

**Problem:** Room's internal temperature data is exposed via getters.

**Impact:**

- Changes to temperature representation require changes in `HeatFlowRegulator`
- Multiple clients could access and misuse this data
- Difficult to maintain invariants (e.g., desired temp must be valid)

### 3. Tight Coupling

**Problem:** `HeatFlowRegulator` must know:

- How to interpret Room's temperature values
- The logic for when heating is needed
- How to coordinate with Furnace

**Impact:**

- Changes to heating logic require modifying `HeatFlowRegulator`
- Cannot easily add room-specific heating strategies
- Difficult to test Room in isolation

### 4. Procedural Design in OO Clothing

**Problem:** This is procedural programming with objects as data structures.

**Current flow:**

```
Regulator → Room.get_desired_temp()
Regulator → Room.get_actual_temp()
Regulator → if (desired > actual) then Furnace.heat()
```

This is equivalent to:

```c
if (room.desired_temp > room.actual_temp) {
    heat_room(&room);
}
```

### 5. Poor Scalability

**Problem:** What if we need room-specific heating rules?

- Occupied rooms heat to 21°C
- Unoccupied rooms heat to 16°C
- Bedrooms cool at night
- Meeting rooms heat before scheduled meetings

**Current design:** All logic must be added to `HeatFlowRegulator`, creating a god class.

---

## Improved Architecture (Tell, Don't Ask)

### Design Principle

**Tell, Don't Ask:** Objects should be told what to do, not queried for their state so others can make decisions for
them.

### Revised Design

```python
class Room:
    def __init__(self, furnace):
        self._desired_temp = 20
        self._actual_temp = 18
        self._furnace = furnace

    def regulate_temperature(self):
        """Room decides for itself whether it needs heating."""
        if self._needs_heating():
            self._furnace.heat(self._calculate_heat_amount())

    def _needs_heating(self):
        """Encapsulated decision logic."""
        return self._actual_temp < self._desired_temp

    def _calculate_heat_amount(self):
        """Room-specific heating calculation."""
        return self._desired_temp - self._actual_temp

class HeatFlowRegulator:
    def __init__(self, rooms):
        self._rooms = rooms

    def regulate(self):
        """Just tells rooms to regulate themselves."""
        for room in self._rooms:
            room.regulate_temperature()
```

### Benefits of Revised Design

1. **Encapsulation:** Temperature data stays private
2. **Single Responsibility:** Room manages its own heating needs
3. **Extensibility:** Easy to add room-specific strategies (inheritance/composition)
4. **Low Coupling:** Regulator doesn't need to know temperature logic
5. **OO Design:** Objects are active entities with behavior, not data bags

---

## Key Principle Summary

| Approach        | Characteristics                              | Problem                                   |
|-----------------|----------------------------------------------|-------------------------------------------|
| **Ask** (Bad)   | Pull data, make decisions externally         | Violates encapsulation, creates coupling  |
| **Tell** (Good) | Give commands, let objects decide internally | Maintains encapsulation, reduces coupling |

---

## Real-World Analogy

**Bad (Ask):**
> Manager to employee: "What's your current task? What's your deadline? OK, I've calculated you should work on the Smith
> report next."

**Good (Tell):**
> Manager to employee: "Please handle the Smith report by Friday."

The employee (object) knows their own schedule and workload, and can make the best decision about how to integrate the
new task.

---

## Related Principles

- **Law of Demeter:** Don't reach through objects to access their internals
- **Single Responsibility:** Each class should have one reason to change
- **Encapsulation:** Hide internal state, expose behavior
- **Open/Closed Principle:** Open for extension (new room types), closed for modification

---

## References

- Arthur J. Riel, *Object-Oriented Design Heuristics*, Addison Wesley, 1996
- Martin Fowler, *Refactoring: Improving the Design of Existing Code*
- [Exercise Slide](slides/slide_architecturalquality09.png)

---

## Self-Check Questions

1. Why is exposing temperature data via getters problematic?
    - **Answer:** It allows external objects to make decisions that belong to Room

2. How does "Tell, Don't Ask" improve testability?
    - **Answer:** Room can be tested independently; just verify it calls furnace correctly

3. What happens if we want different heating strategies per room?
    - **Answer:** With "Tell", we use inheritance/strategy pattern. With "Ask", we need complex conditionals in
      regulator.

4. Is "Tell, Don't Ask" always the right approach?
    - **Answer:** No. For true data queries (reports, displays), asking is appropriate. The principle targets behavioral
      decisions.
