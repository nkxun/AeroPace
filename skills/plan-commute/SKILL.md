---
name: plan-commute
description: Compares the fastest route with a lower-exposure route for a commute, given origin, destination, mode and arrive-by time. Use when the user asks which way to go or how mode changes exposure.
license: MIT
---

# Plan commute

## Steps
1. Collect origin, destination, mode (walk, cycle or two-wheeler first) and arrive-by time. Ask if one is missing.
2. Ask the engine for the fastest route and a lower-exposure route.
3. Present minutes, relative dose and the probability that the lower-exposure route beats the fastest one.

## Output (proposed)
Per route: travel time, relative dose, probability of beating the fastest route.

**Guardrail:** never estimate concentration, dose, probability or travel time yourself. Call the engine and quote what it returns. The engine is planned and not yet built, so the interface below is a proposal.
