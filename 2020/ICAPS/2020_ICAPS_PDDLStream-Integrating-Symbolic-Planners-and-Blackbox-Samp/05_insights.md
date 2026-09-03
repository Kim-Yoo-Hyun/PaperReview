# Insights — PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/ICAPS/article/view/6739; PDF retrieval source: https://ojs.aaai.org/index.php/ICAPS/article/download/6739/6593. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 Introduction - extractive body cue:** We propose PDDLStream, a planning language that introduces streams as an interface for incorporating sam- ∗We gratefully acknowledge support from NSF grants 1523767 and 1723381; ...
- **p. 1 / Abstract - extractive body cue:** This enables the algorithm to greedily search the space of parameter bindings to more quickly solve tightly-constrained problems as well as locally optimize to produce ...
- **p. 1 / 1 Introduction - extractive body cue:** Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as a black box.
- **p. 1 / 1 Introduction - extractive body cue:** Each algorithm constructs and solves a sequence of finite PDDL problems, any off-theshelf PDDL planner to be used as a search subroutine.
- **Contribution anchor:** p. 1 (1 Introduction), p. 1 (Abstract), p. 1 (1 Introduction), p. 1 (1 Introduction)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** Streams allow a planner to reason about conditions on the inputs and outputs of a conditional generator while treating its implementation as a black box.
- **p. 1 / 1 Introduction - extractive body cue:** Adaptive greatly outperforms the two existing algorithms (Garrett, Lozano-P´erez, and Kaelbling 2018) on constrained and 440
- **p. 8 / 9 Experiments - extractive body cue:** Adaptive is able to quickly identify a collision-free pair of placements supporting a solution.
- **Boundary to test:** Adaptive is able to quickly identify a collision-free pair of placements supporting a solution.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We propose PDDLStream, a planning language that introduces streams as an interface for incorporating sam- ∗We gratefully acknowledge support from NSF grants 1523767 and 1723381; from AFOSR grant FA9550-17-1-0165; from ONR grant ... | p. 1 (1 Introduction), p. 1 (Abstract) |
| Reported outcome | Adaptive outperforms Incremental, Focused, and Binding due to its ability to aggressively search over many bindings of a single stream plan. | p. 8 (9 Experiments), p. 8 (9 Experiments) |
| Failure/limitation | Adaptive is able to quickly identify a collision-free pair of placements supporting a solution. | p. 8 (9 Experiments) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** The declarative component specifies the facts that these input and output values satisfy. (p. 1, 1 Introduction).
- **Paper-specific mechanism:** We propose PDDLStream, a planning language that introduces streams as an interface for incorporating sam- ∗We gratefully acknowledge support from NSF grants 1523767 and 1723381; from AFOSR grant FA9550-17-1-0165; from ... (p. 1, 1 Introduction).
- **Evidence boundary:** the reported outcome is The Incremental and Focused algorithms serve as baselines that are representative of prior work (Garrett, Lozano-P´erez, and Kaelbling 2018). (p. 7, 9 Experiments); the relevant task/metric cue is We experimented using the Incremental, Focused, Binding, and Adaptive algorithms on 100 randomly-generated problems within 3 domains in section 4. (p. 7, 9 Experiments). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Adaptive is able to quickly identify a collision-free pair of placements supporting a solution. (p. 8, 9 Experiments).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, task and motion planning, symbolic planning, sampling, manipulation planning`.
- **Reading predecessor in the generated track queue:** Information Theoretic MPC for Model-Based Reinforcement Learning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Dynamic Whole-Body Motion Generation under Rigid Contacts and Other Unilateral Constraints (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Adaptive is able to quickly identify a collision-free pair of placements supporting a solution.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: The declarative component specifies the facts that these input and output values satisfy. (p. 1, 1 Introduction); preserve the objective/update rule: This enables the algorithm to greedily search the space of parameter bindings to more quickly solve tightly-constrained problems as well as locally optimize to produce low-cost solutions. (p. 1, Abstract).
2. Use the paper-reported task/data/environment cue: 9.1 Real-World Validation We applied PDDLStream to four real-world task and motion planning problems. (p. 8, 9 Experiments).
3. Compare against the reported or matched baseline: The Incremental and Focused algorithms serve as baselines that are representative of prior work (Garrett, Lozano-P´erez, and Kaelbling 2018). (p. 7, 9 Experiments).
4. Report the body metric with its denominator and aggregation: We experimented using the Incremental, Focused, Binding, and Adaptive algorithms on 100 randomly-generated problems within 3 domains in section 4. (p. 7, 9 Experiments).
5. Re-run the reported ablation or stress/failure condition: Adaptive outperforms Incremental, Focused, and Binding due to its ability to aggressively search over many bindings of a single stream plan. (p. 8, 9 Experiments); if none is reported, design one around: Adaptive is able to quickly identify a collision-free pair of placements supporting a solution. (p. 8, 9 Experiments).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1 Introduction), p. 1 (1 Introduction), match the reported outcome at p. 7 (9 Experiments), p. 7 (9 Experiments), p. 8 (9 Experiments), and measure the boundary at p. 8 (9 Experiments), p. 8 (10 Conclusion).

## Falsifiable research question

Under the paper's stated interface (The declarative component specifies the facts that these input and output values satisfy.), does the paper-specific mechanism (We propose PDDLStream, a planning language that introduces streams as an interface for incorporating sam- ∗We gratefully acknowledge support from NSF grants ...) retain the reported evaluation outcome (We experimented using the Incremental, Focused, Binding, and Adaptive algorithms on 100 randomly-generated problems within 3 domains in ...) when tested against the paper's strongest explicit boundary (Adaptive is able to quickly identify a collision-free pair of placements supporting a solution.)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We experimented using the Incremental, Focused, Binding, and Adaptive algorithms on 100 randomly-generated problems within 3 domains in ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** We propose PDDLStream, a planning language that introduces streams as an interface for incorporating sam- ∗We gratefully acknowledge support from NSF grants 1523767 and 1723381; from AFOSR grant FA9550-17-1-0165; from ... (p. 1, 1 Introduction).
- **Paper-supported outcome:** The Incremental and Focused algorithms serve as baselines that are representative of prior work (Garrett, Lozano-P´erez, and Kaelbling 2018). (p. 7, 9 Experiments).
- **Strongest explicit boundary:** Adaptive is able to quickly identify a collision-free pair of placements supporting a solution. (p. 8, 9 Experiments).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
