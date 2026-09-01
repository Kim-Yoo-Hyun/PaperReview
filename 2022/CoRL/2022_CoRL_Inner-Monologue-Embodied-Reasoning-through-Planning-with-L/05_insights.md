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
- **p. 1 / 1 Introduction - extractive body cue:** While prior work has investigated using language models as planners [20, 21] or incorporating arXiv:2207.05608v1 [cs.RO] 12 Jul 2022
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

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 As a demonstration of the versatility of LLMs and grounded closed-loop feedback, we additionally show several surprising capabilities emerging from the inner monologue formulation, including continued adaptation to new instructions, sel ...를 The policy is trained on 20000 pre-collected demonstrations, where each demonstration contains 1) language instruction of the format "pick up [x] and place it on [y]", 2) top-down view of RGB-D observation ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Table 5. As for failure modes, Inner Monologue may fail due to several sources of errors: (1) success detections, (2) LLM planning errors, and (3) control errors. False negative predictions from the ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, LLM planning, feedback, replanning, long-horizon manipulation`.
- **Reading predecessor in the generated track queue:** VIMA: General Robot Manipulation with Multimodal Prompts (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Table 5. As for failure modes, Inner Monologue may fail due to several sources of errors: (1) success detections, (2) LLM planning errors, and (3) control errors. False negative predictions from the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: For the object sorting task, the scene description contains a list of currently visible objects and a list of objects that the robot has successfully moved into a plate..
3. Compare against the body-reported baseline or a matched simpler baseline: Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, as measured by average task success rates over ....
4. Report the body metric and its denominator/aggregation: Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot exceeds the performance of baseline alternatives, as measured by average task success rates over ....
5. Re-run the body-reported ablation/failure condition: Table 1: Success rates for various methods, averaged across 50 episodes in Ravens-based environment with test-time disturbances. CLIPort + oracle indicates that CLIPort was provided a "termination" oracle. Although CLIPort can receive ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 16 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement), p. 17 (A.2 Inner Monologue for Real-World Tabletop Rearrangement); the primary result is directionally consistent at p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Inspired, human, thought mechanism이 Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and ... 대비 Table 2: Inner Monologue (with object recognition and success detection feedback) on a real pick and place robot ...을 개선하고, Table 5. As for failure modes, Inner Monologue may fail due to several sources of errors: ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
