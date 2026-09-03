# Insights — Planning and Acting in Partially Observable Stochastic Domains

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (45 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.sciencedirect.com/science/article/pii/S000437029800023X; PDF retrieval source: https://www.cassandra.org/arc/papers/aij98.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1 Introduction - extractive body cue:** This paper is intended to make two contributions.
- **p. 3 / 1 Introduction - extractive body cue:** The second is to describe a novel algorithmic approach for solving POMDPs exactly.
- **p. 19 / 44 The Witness Algorithm - extractive body cue:** The code in Table 2 outlines our approach to solving PompPs.
- **p. 23 / 4.5. Alternative Approaches - extractive body cue:** The resulting algorithm might be called the two-pass algorithm [9], and, its form is much like the witness algorithm because it first constructs each separate ...
- **p. 19 / 44 The Witness Algorithm - extractive body cue:** This is because maximizing over actions and then policy trees is the same as maximizing over the pooled sets of policy trees.
- **p. 7 / 2.9 Computing an Optimal Policy - extractive body cue:** Tt makes use of an aundliary function, Q/(s), which is the tstep value of starting in state s, taking action a, then continuing with the ...
- **p. 23 / 4.5. Alternative Approaches - extractive body cue:** Although the algorithm is sophisticated and, in principle, avoids exhaustively enumerating the set of possibly useful policy trees at each iteration, it appears to run ...
- **Contribution anchor:** p. 3 (1 Introduction), p. 3 (1 Introduction), p. 19 (44 The Witness Algorithm), p. 23 (4.5. Alternative Approaches), p. 19 (44 The Witness Algorithm), p. 7 (2.9 Computing an Optimal Policy)

### Strongest assumption and failure boundary

- **p. 2 / 1 Introduction - extractive body cue:** Problems like the one described above can be modeled as partially observable Markov decision processes (POMDPs).
- **p. 2 / 1 Introduction - extractive body cue:** This is essentially a plareing problem: given a complete and correct model of the world dynamics and a reward structure, find an optimal way to ...
- **p. 3 / 1 Introduction - extractive body cue:** Section 6 describes the relation between the present approach and prior research in more detail.
- **p. 3 / 1 Introduction - extractive body cue:** Markov decision processes serve as a basis for solving the more complex par tially observable problems that we are ultimately interested in.
- **p. 4 / 1 Introduction - extractive body cue:** An MDP models the synchronous interaction between agent: and world. current state-it has complete and perfect perceptual abilities.
- **p. 15 / 1) I step to go - extractive body cue:** In such belief states, the agent cannot select
- **p. 18 / 42 Value Functions as Sets of Vectors - extractive body cue:** Pruning requires one linear program for each element of the starting set of policy trees and does not add to the asymptotic complexity of the ...
- **Boundary to test:** In such belief states, the agent cannot select

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | This paper is intended to make two contributions. | p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Reported outcome | ‘To improve the complexity of the valueiteration algorithm, we must avoid generating V;*; instead, we would like to generate the elements of V; direct] Ifwe could do this, we might be able ... | p. 18 (44 The Witness Algorithm), p. 20 (441 Witness inner loop) |
| Failure/limitation | In such belief states, the agent cannot select | p. 15 (1) I step to go), p. 18 (42 Value Functions as Sets of Vectors) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** The component labeled SE is the state estimator: it is responsible for updating the belief state based on the last action, the current observation, and the previous belief state, The ... (p. 9, 3.2 Problem Structure).
- **Paper-specific mechanism:** This paper is intended to make two contributions. (p. 3, 1 Introduction).
- **Evidence boundary:** the reported outcome is The linear program in Table 3 solves exactly this problem, The variable d is the minimum amount of improvement of Pew Over any policy tree in Uy at b. (p. 21, 44.3. Checking the witness condition); the relevant task/metric cue is i pproptiately and so tends to gain less long-term reward. (p. 15, 1) I step to go). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** as the agent does not observe the goal state, it will alwajrs have some non-zero belief that it is in any of the non-goal states, since the actions have non-zero ... (p. 11, 3.2 Problem Structure).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, Planning, POMDP, partial observability, uncertainty, decision making`.
- **Reading predecessor in the generated track queue:** A Formal Basis for the Heuristic Determination of Minimum Cost Paths (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** In such belief states, the agent cannot select; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: The component labeled SE is the state estimator: it is responsible for updating the belief state based on the last action, the current observation, and the previous belief state, The ... (p. 9, 3.2 Problem Structure); preserve the objective/update rule: Tn what sense is the witness algorithm superior to previous algorithms for solving Pompps, then? (p. 18, 44 The Witness Algorithm).
2. Use the paper-reported task/data/environment cue: A plan graph is essentially a finite-state controller, It uses the minimal possible amount of memory to act optimally in a partially observable environment. (p. 30, 5.4 Plan Graphs).
3. Compare against the reported or matched baseline: This is because the behavior of ‘these algorithms on this problem appears to be extremely sensitive to the numerical precision used in comparisons-the better the precision, the longer the algorithms ... (p. 29, 5.4 Plan Graphs).
4. Report the body metric with its denominator and aggregation: i pproptiately and so tends to gain less long-term reward. (p. 15, 1) I step to go).
5. Re-run the reported ablation or stress/failure condition: The optimal action for cach belief state in this region is a(p), the action in the root node of policy tree p; furthermore, the entire policy tree p can be ... (p. 16, 1) I step to go); if none is reported, design one around: as the agent does not observe the goal state, it will alwajrs have some non-zero belief that it is in any of the non-goal states, since the actions have non-zero ... (p. 11, 3.2 Problem Structure).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 3 (1 Introduction), p. 3 (1 Introduction), match the reported outcome at p. 21 (44.3. Checking the witness condition), p. 22 (444 A single step of value iteration), p. 24 (4.5. Alternative Approaches), and measure the boundary at p. 11 (3.2 Problem Structure), p. 10 (3.2 Problem Structure).

## Falsifiable research question

Under the paper's stated interface (The component labeled SE is the state estimator: it is responsible for updating the belief state based on the last action, the ...), does the paper-specific mechanism (This paper is intended to make two contributions.) retain the reported evaluation outcome (i pproptiately and so tends to gain less long-term reward.) when tested against the paper's strongest explicit boundary (as the agent does not observe the goal state, it will alwajrs have some non-zero belief that it ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (i pproptiately and so tends to gain less long-term reward.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (45 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** This paper is intended to make two contributions. (p. 3, 1 Introduction).
- **Paper-supported outcome:** The linear program in Table 3 solves exactly this problem, The variable d is the minimum amount of improvement of Pew Over any policy tree in Uy at b. (p. 21, 44.3. Checking the witness condition).
- **Strongest explicit boundary:** as the agent does not observe the goal state, it will alwajrs have some non-zero belief that it is in any of the non-goal states, since the actions have non-zero ... (p. 11, 3.2 Problem Structure).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
