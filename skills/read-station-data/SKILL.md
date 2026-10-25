---
name: read-station-data
description: Reads recent air-quality station readings and the short-term forecast shape for a city, with data age and gaps. Use when the user asks what the air is like now or which stations are reporting, or before planning a trip.
license: MIT
---

# Read station data

Use this skill first when a plan needs current conditions.

## Steps
1. Ask the engine for the latest station readings and the forecast shape for the demo city.
2. Report how old each reading is and which stations have gaps.
3. State that the city has only a handful of stations, so street-level values are estimated.

## Output (proposed)
Stations with value, unit and timestamp, plus the forecast shape for the next hours.

**Guardrail:** never estimate concentration, dose, probability or travel time yourself. Call the engine and quote what it returns. The engine is planned and not yet built, so the interface below is a proposal.

See [data sources](references/data-sources.md).
