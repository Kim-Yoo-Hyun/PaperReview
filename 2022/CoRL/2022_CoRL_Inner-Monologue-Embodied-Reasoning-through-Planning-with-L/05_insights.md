# Insights — Inner Monologue: Embodied Reasoning through Planning with Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v205/huang23c.html; PDF retrieval source: https://arxiv.org/pdf/2207.05608. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / 1 Introduction - extractive body cue:** Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs.
- **p. 2 / 1 Introduction - extractive body cue:** Robot Success Detector Scene Descriptor (b) (c) (a) Human Figure 1: Inner Monologue enables grounded closed-loop feedback for robot planning with large language models by ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** The input to the model consists of: (1) o0, the initial image observation, (2) of, the final image observation after the policy chose to terminate ...
- **p. 2 / 1 Introduction - extractive body cue:** Notably, we show that it can efficiently retry under observed stochastic failure, replan under systematic infeasibility, or request human feedback for ambiguous queries, resulting in ...
- **p. 1 / 1 Introduction - extractive body cue:** We observe that similarly to recent work [19], natural language provides a universal and interpretable interface for such grounding of model communication and allows them ...
- **p. 16 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** Low-level Policies We use a single low-level policy for the real tabletop rearrangement environment that is responsible for performing object-centric pick and place actions as ...
- **p. 17 / A.2 Inner Monologue for Real-World Tabletop Rearrangement - extractive body cue:** Given the first and last observation, the model outputs a probability distribution over all the possible skills.
- **Contribution anchor:** p. 1 (1 Introduction), p. 2 (1 Introduction), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement)

### Strongest assumption and failure boundary

- **p. 1 / 1 Introduction - extractive body cue:** While conventionally these challenges have been approached from the perspective of planning (e.g., TAMP [1]) or hierarchical learning (e.g., HRL [2]), effective high-level reasoning about ...
- **p. 2 / 1 Introduction - extractive body cue:** Notably, we show that it can efficiently retry under observed stochastic failure, replan under systematic infeasibility, or request human feedback for ambiguous queries, resulting in ...
- **p. 1 / 1 Introduction - extractive body cue:** While prior work has investigated using language models as planners [20, 21] or incorporating.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 5. As for failure modes, Inner Monologue may fail due to several sources of errors: (1) success detections, (2) LLM planning errors, and (3) ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Averaged success rate across 120 evaluations on several task families in our real-world mobile manipulation environment. We consider a standard setting and adversarial ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort + oracle indicates that CLIPort was provided ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Failure causes on 120 evaluations. When disturbances are added (red), only the Inner Mono- logue variants consistently complete the instructions. Analysis. The results ...
- **Boundary to test:** Table 5. As for failure modes, Inner Monologue may fail due to several sources of errors: (1) success detections, (2) LLM planning errors, and (3) control errors. False negative predictions from the ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs. | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Reported outcome | Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, as measured by average task success rates over ... | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Failure/limitation | Table 5. As for failure modes, Inner Monologue may fail due to several sources of errors: (1) success detections, (2) LLM planning errors, and (3) control errors. False negative predictions from the ... | p. 9 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Our proposed system Inner Monologue chains together these various components (perception models, robotic skills, and human feedback) in a shared language prompt, enabling it to successfully perform user instructions. (p. 2, 1 Introduction).
- **Paper-specific mechanism:** Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs. (p. 1, 1 Introduction).
- **Evidence boundary:** the reported outcome is Figure 4: Failure causes on 120 evaluations. When disturbances are added (red), only the Inner Mono- logue variants consistently complete the instructions. Analysis. The results of real robot experiments are ... (p. 7, Figure/Table caption); the relevant task/metric cue is Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort + oracle indicates that CLIPort was provided a "termination" oracle. Although CLIPort ... (p. 6, Figure/Table caption). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Notably, we show that it can efficiently retry under observed stochastic failure, replan under systematic infeasibility, or request human feedback for ambiguous queries, resulting in significantly improved performance in dynamical ... (p. 2, 1 Introduction).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, LLM planning, feedback, replanning, long-horizon manipulation`.
- **Reading predecessor in the generated track queue:** VIMA: General Robot Manipulation with Multimodal Prompts (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 5. As for failure modes, Inner Monologue may fail due to several sources of errors: (1) success detections, (2) LLM planning errors, and (3) control errors. False negative predictions from the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Our proposed system Inner Monologue chains together these various components (perception models, robotic skills, and human feedback) in a shared language prompt, enabling it to successfully perform user instructions. (p. 2, 1 Introduction); preserve the objective/update rule: To train this model, we use the symmetric contrastive loss as used in CLIP (Fig 7b). (p. 17, A.2 Inner Monologue for Real-World Tabletop Rearrangement).
2. Use the paper-reported task/data/environment cue: Environment Feedback: Passive Scene Description For Object + Scene method, we provide task-progress scene description as a list of achieved sub-goals after each pick-and-place execution. (p. 15, A.1 Inner Monologue for Simulated Tabletop Rearrangement).
3. Compare against the reported or matched baseline: Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, as measured by average task success ... (p. 6, Figure/Table caption).
4. Report the body metric with its denominator and aggregation: Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort + oracle indicates that CLIPort was provided a "termination" oracle. Although CLIPort ... (p. 6, Figure/Table caption).
5. Re-run the reported ablation or stress/failure condition: Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort + oracle indicates that CLIPort was provided a "termination" oracle. Although CLIPort ... (p. 6, Figure/Table caption); if none is reported, design one around: Notably, we show that it can efficiently retry under observed stochastic failure, replan under systematic infeasibility, or request human feedback for ambiguous queries, resulting in significantly improved performance in dynamical ... (p. 2, 1 Introduction).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (1 Introduction), p. 2 (1 Introduction), match the reported outcome at p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), and measure the boundary at p. 2 (1 Introduction), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement).

## Falsifiable research question

Under the paper's stated interface (Our proposed system Inner Monologue chains together these various components (perception models, robotic skills, and human feedback) in a shared language prompt, ...), does the paper-specific mechanism (Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs.) retain the reported evaluation outcome (Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort ...) when tested against the paper's strongest explicit boundary (Notably, we show that it can efficiently retry under observed stochastic failure, replan under systematic infeasibility, or request ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (25 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs. (p. 1, 1 Introduction).
- **Paper-supported outcome:** Figure 4: Failure causes on 120 evaluations. When disturbances are added (red), only the Inner Mono- logue variants consistently complete the instructions. Analysis. The results of real robot experiments are ... (p. 7, Figure/Table caption).
- **Strongest explicit boundary:** Notably, we show that it can efficiently retry under observed stochastic failure, replan under systematic infeasibility, or request human feedback for ambiguous queries, resulting in significantly improved performance in dynamical ... (p. 2, 1 Introduction).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
