---
name: compare-departure-times
description: Compares departure times for a commute and suggests a leave-by window with the time versus exposure trade-off. Use when the user asks when to leave or must arrive by a given time.
license: MIT
---

# Compare departure times

## Steps
1. Take the route and mode from plan-commute, plus the arrive-by time.
2. Ask the engine for dose and arrival time for departure slots over the next hours.
3. Report the best window and what it costs in time.

## Output (proposed)
A list of departure slots with arrival time and relative dose, and the suggested window.

**Guardrail:** never estimate concentration, dose, probability or travel time yourself. Call the engine and quote what it returns. The engine is planned and not yet built, so the interface below is a proposal.
