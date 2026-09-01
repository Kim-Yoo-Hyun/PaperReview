# Insights — Bridging Perception and Action: Spatially-Grounded Mid-Level Representations for Robot Generalization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p155.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p155.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Ivrropuction - extractive body cue:** We show that while different mid-level representations excel at different tasks, our method can leverage these task-specitfic benefits to achieve consistently higher performance on a ...
- **p. 6 / B. Training - extractive body cue:** Similarly, our approach integrates mid-level expert outputs as implicit guidance in scenarios where no explicit reward signal is available, Instead of an advantage function, we ...
- **p. 1 / Abstract - extractive body cue:** We propose a novel mixture-of-experts policy architecture that can combine multiple specialized expert models, each trained on a distinct ‘mid-level representation, to improve the generalization ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** We find that reliance on structured signals presents a trade-off: policies that depend heavily on these representations can become more susceptible to overfiting and reduced ...
- **p. 3 / 1. Ivrropuction - extractive body cue:** While one can hope to learn these relationships directly from end-to-end data, current large-scale robot policies that try to scale up imitation learning still struggle ...
- **p. 4 / V. ARCHITECTURE - extractive body cue:** We implement our method on a diffusion policy similar to the one proposed in [40]. ‘The policy takes as input 4 images from different viewpoints ...
- **p. 5 / B. Training - extractive body cue:** Once the expert modules are trained independently, their parameters are frozen. ‘Then, the policy network trained endto-end with a noise prediction loss.
- **Contribution anchor:** p. 2 (1. Ivrropuction), p. 6 (B. Training), p. 1 (Abstract), p. 2 (1. Ivrropuction), p. 3 (1. Ivrropuction), p. 4 (V. ARCHITECTURE)

### Strongest assumption and failure boundary

- **p. 1 / 1. Ivrropuction - extractive body cue:** Large pre-trained robotics models have made significant progress in recent years towards improving robotic generalization capabilities by leveraging large-scale pre-training datasets, However, these models still ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** A key challenge with the multi-task policy learning regime is in obtaining policies that generalize to new objects, task variants, environmental factors and so on, ...
- **p. 3 / 1. Ivrropuction - extractive body cue:** While one can hope to learn these relationships directly from end-to-end data, current large-scale robot policies that try to scale up imitation learning still struggle ...
- **p. 1 / 1. Ivrropuction - extractive body cue:** An increasingly popular approach to address this challenge is explicitly establishing deeper connections between robot policies and the abstract patterns and relationships that govern the ...
- **p. 2 / 1. Ivrropuction - extractive body cue:** For instance, for a robot tasked with folding a shirt, a bounding box may help locate a shir's general position but fails to provide actionable ...
- **p. 6 / 4) Which policy architecture offers the best tradeoff be - extractive body cue:** tween responsiveness to structured mid-level representations and robustness to noise or spurious inputs?
- **p. 9 / C. Different Architectures offer Different Tradeoffs berween - extractive body cue:** Meanwhile, Table I! records the sensitivity scores for each of our mid-level experts as well as the robustness index. ‘The robustness index is computed by ...
- **Boundary to test:** tween responsiveness to structured mid-level representations and robustness to noise or spurious inputs?

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We show that while different mid-level representations excel at different tasks, our method can leverage these task-specitfic benefits to achieve consistently higher performance on a wide range of environments. | p. 2 (1. Ivrropuction), p. 6 (B. Training) |
| Reported outcome | Fig. 1: Bimanual, dexterous manipulation requires task-specifie grounding, The left depicts various axes for spatial gr ‘qualitative categorizations of different mid-level representations. Different representations lead to different lev ... | p. 1 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Failure/limitation | tween responsiveness to structured mid-level representations and robustness to noise or spurious inputs? | p. 6 (4) Which policy architecture offers the best tradeoff be), p. 9 (C. Different Architectures offer Different Tradeoffs berween) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `multi-view observation, language/task label과 action trajectory → shared representation, embodiment/task identity와 data distribution → dataset sample 또는 learned policy action`.
- 이 논문의 재사용 가능한 지점은 By iteratively refining the training data and adjusting the weighting of consistent samples, our method creates a feedback loop that promotes tighter self-consistency between policy actions and mid-level ‘expert outputs.를 We implement our method on a diffusion policy similar to the one proposed in [40]. ‘The policy takes as input 4 images from different viewpoints (2 third-person images and 2 wrist images) ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 shared representation, embodiment/task identity와 data distribution가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 tween responsiveness to structured mid-level representations and robustness to noise or spurious inputs?에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We show that while different mid-level representations excel at different tasks, our method can leverage these task-specitfic benefits to achieve consistently higher performance on a wide range of environments.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, mid-level representation, 3D perception, bimanual manipulation, diffusion policy, generalization`.
- **Reading predecessor in the generated track queue:** RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** tween responsiveness to structured mid-level representations and robustness to noise or spurious inputs?; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: For RT-H, ‘we relabel robot demonstrations with the language "move the arm leftright/up/down." For each environment in simulation and the real-world, we vary the object locations, add distractor objects, and change the ....
3. Compare against the body-reported baseline or a matched simpler baseline: In addition, we provide two ablations based on prior ‘works investigating a single representation: a keypoints-based ablation based on MOKA (25] and a language baseline based on RE-H [2]..
4. Report the body metric and its denominator/aggregation: metric definition not recovered.
5. Re-run the body-reported ablation/failure condition: In the Keypoint ablation, we identify important points of interest in the image by querying a VLM..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (V. ARCHITECTURE), p. 5 (B. Training), p. 4 (V. ARCHITECTURE); the primary result is directionally consistent at p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 while, different, mid-level mechanism이 In addition, we provide two ablations based on prior ‘works investigating a single representation: a keypoints-based ... 대비 the primary body-reported metric을 개선하고, tween responsiveness to structured mid-level representations and robustness to noise or spurious inputs? 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
