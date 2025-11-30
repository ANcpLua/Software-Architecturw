# FinOps, Cost Governance & Sustainability View

## Purpose

For each subsystem: resource consumption, cost drivers, and sustainability impact at runtime and scale.

Traditional C4/arc42 do not assign cost drivers or sustainability metrics to specific elements. This view fills that
gap by documenting:

- **Runtime cost** - CPU/GPU load during operation
- **Cost drivers** - What makes it expensive at scale
- **Growth** - Data accumulation over time
- **Scaling behavior** - How costs change with load

---

## K1 — Presentation.InputAdapter

| Aspect | Value |
|--------|-------|
| **Mode** | Always-on (listens to input) |
| **Runtime cost** | Low CPU |
| **Cost driver** | Basic event handling |
| **Growth** | None (does not store history) |
| **Scaling** | Fixed cost; cheap even with many users |

---

## K2 — Presentation.RenderingEngine

| Aspect | Value |
|--------|-------|
| **Mode** | Active while rendering |
| **Runtime cost** | GPU-heavy during redraws |
| **Cost driver** | Rendering work (GPU / frame rate / resolution) |
| **Growth** | None (renders current board only) |
| **Scaling** | Increases with visual fidelity and concurrent sessions |

---

## K3 — Application.InteractionController

| Aspect | Value |
|--------|-------|
| **Mode** | Request/response |
| **Runtime cost** | Light to medium logic |
| **Cost driver** | Orchestration logic |
| **Growth** | None (stateless coordinator) |
| **Scaling** | Light per interaction; effectively negligible |

---

## K4 — Domain.AnalysisService

| Aspect | Value |
|--------|-------|
| **Mode** | On-demand (move validation, evaluation, search) |
| **Runtime cost** | High compute per request |
| **Cost driver** | Per-move calculation and search depth |
| **Growth** | None (temporary calculation only) |
| **Scaling** | Increases with number of analysis requests |

**Note:** Main variable cost in the system. Primary compute hotspot.

---

## K5 — Core.PositionStore

| Aspect | Value |
|--------|-------|
| **Mode** | Always available |
| **Runtime cost** | Low CPU |
| **Cost driver** | Retained game state and history |
| **Growth** | Yes (game state, move history, undo/replay data) |
| **Scaling** | Increases with storage volume and retention period |

**Note:** Only subsystem with long-term data growth.

---

## Summary

### Compute Hotspots

| Subsystem | Compute Cost | Storage Growth | At-Scale Risk |
|-----------|--------------|----------------|---------------|
| K1 | Low | None | Low |
| K2 | Medium-High | None | Medium |
| K3 | Low | None | Low |
| K4 | **High** | None | **High** |
| K5 | Low | **Yes** | **Medium** |

### Key Takeaways

- **K4 (AnalysisService)** is the main compute hotspot - analysis per move drives variable cost
- **K5 (PositionStore)** is the only subsystem with long-term growth - stored history accumulates
- **K1, K2, K3** are predictable and contained - operationally cheap

### Cost Optimization Strategies

1. **K4:** Cache analysis results, limit search depth, batch requests
2. **K5:** Implement retention policies, compress historical data, archive old games
3. **K2:** Reduce frame rate when idle, skip unchanged frame renders

---
