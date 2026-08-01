# 🌐 GLOBAL PIPELINE ARCHITECTURE

```mermaid
graph TD
    %% Base Color Layout Settings
    classDef inception fill:#1f2937,stroke:#3b82f6,stroke-width:2px,color:#fff;
    classDef stage1 fill:#111827,stroke:#10b981,stroke-width:2px,color:#fff;
    classDef stage2 fill:#111827,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef loopback fill:#312e81,stroke:#a78bfa,stroke-width:2px,color:#fff;
    classDef implement fill:#7c2d12,stroke:#f97316,stroke-width:2px,color:#fff;

    %% STAGE 1: Initial Raw Inception
    subgraph Stage0 ["STAGE 1: INITIAL RAW INCEPTION"]
        A[Idea Generator Agent] -->|1. High-Level Concepts| B[Initial BA Agent]
        B -->|2. Raw SRS Context| C[Initial SA Agent]
    end

    %% STAGE 2: CSRO Parallel Arbitration Gate
    subgraph Stage1 ["STAGE 2: CSRO LOOPBACK GOVERNANCE GATE"]
        C -->|3. Raw Inbound Blueprint| D{CSRO Crew Workflow}
        D -->|4. Supreme Verdict Check| E[CSRO Sentinel]
        D -->|5. Audit & Self-Heal Requirement Leakage| F[CSRO BA Reviewer]
        D -->|6. Audit & Self-Heal Path Topology| G[CSRO SA Reviewer]
    end

    %% STAGE 3: BDA Diff Auditing Layer
    subgraph Stage2 ["STAGE 3: ARCHITECTURAL DIFF AUDITING LAYER"]
        F -->|7. Patched BA SRS Asset| H[Blueprint Diff Analyzer - BDA]
        G -->|8. Patched SA Blueprint Asset| H
    end

    %% STAGE 4: Closed-Loop Re-Generation
    subgraph Stage3 ["STAGE 4: CLOSED-LOOP ARCHITECTURAL RE-GENERATION"]
        H -->|9. Final SA Hotfix Plan & Blueprint Context| I[Initial SA Agent]
        I -->|10. Re-Generate Immutable Baseline| J[GLOBAL CONTEXT]
        I -->|11. Re-Generate Localized Target Manual| K[PHASE CONTEXT]
        I -->|12. Re-Generate Airtight Traceability| L[PHASE STEPS JSON]
    end

    %% STAGE 5: Production Project Implementation
    subgraph Stage4 ["STAGE 5: PRODUCTION PROJECT IMPLEMENTATION"]
        J & K & L -->|13. Publish to Initial Project Framework| M[Project Coding Agents]
        M -->|14. Rapid MVP Implementation Contracts| N[Coder Agent]
        N -->|15. Compiler & Static Validation| O[Reviewer Agent]
        O -->|16. Automated Test & Lineage Audit| P[Tester Agent]
        P -->|17. Zero-Defect Codebase Release| Q[Production Deployment\nDocker/GCP/GKE/AWS/Azure]
    end

    %% Style Assignments
    class A,B,C inception;
    class D,E,F,G stage1;
    class H stage2;
    class I,J,K,L loopback;
    class M,N,O,P,Q implement;
```

---

# CLOSED-LOOP RE-GENERATIVE AUTOMATED GOVERNANCE INFRASTRUCTURE

## 1. STAGE 1: INITIAL RAW INCEPTION
- **Idea Generator Agent**: Ingests high-level sector constraints, establishes the unique dynamic identity, generates target `technical_codename` identifiers, and compiles a lean MVP requirements overview as a baseline reference.
- **Initial BA Agent**: Ingests the ideation overview and expands it into the raw Software Requirements Specification (SRS), mapping functional and persistent attributes to systemic Tag IDs (`[REQ-XXX]`, `[DAT-XXX]`).
- **Initial SA Agent**: Parses the raw SRS to author the initial Global Context Blueprint baseline, establishing the early daily logs distribution matrix and workspace directory rules.

## 2. STAGE 2: CSRO PARALLEL ARBITRATION GATE
- **CSRO Sentinel**: Acts as the initial governance checkpoint, cross-checking timeline padding and chronologicalday ranges to instantly enforce systemic compliance gates.
- **CSRO BA Reviewer**: Conducts a line-by-line trace audit to intercept dropped features or creative scope-creep, outputting a clear evaluation report along with a clean, raw `patched BA` SRS asset.
- **CSRO SA Reviewer**: Audits path formatting rules and lower-case agent role anomalies, outputting an infrastructure compliance log along with a clean, raw `patched SA` blueprint asset.

## 3. STAGE 3: ARCHITECTURAL DIFF AUDITING LAYER
- **Blueprint Diff Analyzer (BDA)**: Intercepts the `patched BA` and `patched SA` assets from the preceding chặng. Executes cross-referencing comparisons between the original and modified baselines across three independent auditing layers (Traceability, Failure Mode, and Blind-Spot Sweeping), outputting the definitive engineering document: the **final SA** architectural context matrix containing the approved Hotfix Action Plan.

## 4. STAGE 4: CLOSED-LOOP ARCHITECTURAL RE-GENERATION
- **Initial SA Agent (Re-Generation Phase)**: Ingests the **final SA** evaluation contract from the BDA chặng as its absolute source-of-truth input. Runs an automated re-generation loop to rebuild the finalized technical specification architecture, publishing three pure, synchronized production contracts completely cleared of defects:
  * **GLOBAL CONTEXT**: The master repository blueprint governing overall stack boundaries and tech compliance.
  * **PHASE CONTEXT**: The localized phase-specific execution manual, dynamically embedded with verified descriptions and scope perimeters.
  * **PHASE STEPS JSON**: The high-density executable data framework lashing 100% full traceability parameters directly to Pydantic validation nodes.

## 5. STAGE 5: PRODUCTION PROJECT IMPLEMENTATION
- **Project Coding Agents**: Consume the published assets from the initial project framework directory to commence engineering activities.
- **Coder Agent**: Authors production-grade source code inside `./sources/`, inline-mapping the logic to the requirements tags and enforcing strict OWASP security guardrails.
- **Reviewer Agent**: Conducts static analysis and automated compiler verification loops over the codebase to eliminate structural path leaks or circular dependencies.
- **Tester Agent**: Processes semicolon-separated test pairs to run automated assertions (JUnit 5, Integration/E2E test beds), securing a 100% successful code coverage footprint over the specified requirement tags before clearing deployment hooks.
