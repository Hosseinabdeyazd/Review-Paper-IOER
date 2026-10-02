# DT-L4 — Dynamics & Material-Flow Simulation

## Status
Working scaffold — not yet analyzed in detail.

## Core question
How should building states and material stocks evolve through time and release materials through construction, maintenance, replacement, renovation and demolition events?

## Candidate processes
- construction
- maintenance
- component replacement
- renovation / refurbishment
- partial demolition
- full demolition
- material release
- recovery flows
- stock turnover
- lifetime / survival modelling
- scenario-based future flows

## Uncertainty analysis
Focus on event timing, lifetime distributions, scenario uncertainty, future technology/context, dynamic parameter change and inherited stock uncertainty.


## Output contract to Material Decision Profile

DT-L4 converts the probabilistic material inventory into **release profiles**:
- which material batch is released;
- through which event;
- when;
- how much;
- with what uncertainty.

The output must preserve the identity/state of the released material so DT-L5 can evaluate pathway-specific reuse and recycling options.
