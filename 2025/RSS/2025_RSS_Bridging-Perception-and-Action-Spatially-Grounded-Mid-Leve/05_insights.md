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

- **Paper-specific interface:** We implement our method on a diffusion policy similar to the one proposed in [40]. ‘The policy takes as input 4 images from different viewpoints (2 third-person images and 2 ... (p. 4, V. ARCHITECTURE).
- **Paper-specific mechanism:** We propose a novel mixture-of-experts policy architecture that can combine multiple specialized expert models, each trained on a distinct ‘mid-level representation, to improve the generalization of the policy. (p. 1, Abstract).
- **Evidence boundary:** the reported outcome is In addition, we provide two ablations based on prior ‘works investigating a single representation: a keypoints-based ablation based on MOKA (25] and a language baseline based on RE-H [2]. (p. 7, C. Experiment Setup); the relevant task/metric cue is Fig. 1: Bimanual, dexterous manipulation requires task-specifie grounding, The left depicts various axes for spatial gr ‘qualitative categorizations of different mid-level representations. Different representations lead to different lev ... (p. 1, Figure/Table caption). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** This sensitivity-robusness tradeoff' underscores the necessity of developing robot policies that balance adherence 10 mid-level representations with the ability to remain adaptable and resilient in the face of environmental variations. ... (p. 4, 1. Ivrropuction).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `RL, IL, offline learning, and robot data`; tags: `Robotics, mid-level representation, 3D perception, bimanual manipulation, diffusion policy, generalization`.
- **Reading predecessor in the generated track queue:** RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** tween responsiveness to structured mid-level representations and robustness to noise or spurious inputs?; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We implement our method on a diffusion policy similar to the one proposed in [40]. ‘The policy takes as input 4 images from different viewpoints (2 third-person images and 2 ... (p. 4, V. ARCHITECTURE); preserve the objective/update rule: where A(s,a) represents the advantage function, which modulates the policy gradient loss Cyc based on the estimated benefit of selecting action « in states. (p. 6, B. Training).
2. Use the paper-reported task/data/environment cue: For RT-H, ‘we relabel robot demonstrations with the language "move the arm leftright/up/down." For each environment in simulation and the real-world, we vary the object locations, add distractor objects, and ... (p. 7, C. Experiment Setup).
3. Compare against the reported or matched baseline: In addition, we provide two ablations based on prior ‘works investigating a single representation: a keypoints-based ablation based on MOKA (25] and a language baseline based on RE-H [2]. (p. 7, C. Experiment Setup).
4. Report the body metric with its denominator and aggregation: Fig. 1: Bimanual, dexterous manipulation requires task-specifie grounding, The left depicts various axes for spatial gr ‘qualitative categorizations of different mid-level representations. Different representations lead to different lev ... (p. 1, Figure/Table caption).
5. Re-run the reported ablation or stress/failure condition: In the Keypoint ablation, we identify important points of interest in the image by querying a VLM. (p. 7, C. Experiment Setup); if none is reported, design one around: This sensitivity-robusness tradeoff' underscores the necessity of developing robot policies that balance adherence 10 mid-level representations with the ability to remain adaptable and resilient in the face of environmental variations. ... (p. 4, 1. Ivrropuction).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (Abstract), p. 2 (1. Ivrropuction), match the reported outcome at p. 7 (C. Experiment Setup), p. 7 (C. Experiment Setup), p. 7 (C. Experiment Setup), and measure the boundary at p. 4 (1. Ivrropuction), p. 2 (1. Ivrropuction).

## Falsifiable research question

Under the paper's stated interface (We implement our method on a diffusion policy similar to the one proposed in [40]. ‘The policy takes as input 4 images ...), does the paper-specific mechanism (We propose a novel mixture-of-experts policy architecture that can combine multiple specialized expert models, each trained on a distinct ‘mid-level representation, to ...) retain the reported evaluation outcome (Fig. 1: Bimanual, dexterous manipulation requires task-specifie grounding, The left depicts various axes for spatial gr ‘qualitative categorizations ...) when tested against the paper's strongest explicit boundary (This sensitivity-robusness tradeoff' underscores the necessity of developing robot policies that balance adherence 10 mid-level representations with the ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Fig. 1: Bimanual, dexterous manipulation requires task-specifie grounding, The left depicts various axes for spatial gr ‘qualitative categorizations ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** We propose a novel mixture-of-experts policy architecture that can combine multiple specialized expert models, each trained on a distinct ‘mid-level representation, to improve the generalization of the policy. (p. 1, Abstract).
- **Paper-supported outcome:** In addition, we provide two ablations based on prior ‘works investigating a single representation: a keypoints-based ablation based on MOKA (25] and a language baseline based on RE-H [2]. (p. 7, C. Experiment Setup).
- **Strongest explicit boundary:** This sensitivity-robusness tradeoff' underscores the necessity of developing robot policies that balance adherence 10 mid-level representations with the ability to remain adaptable and resilient in the face of environmental variations. ... (p. 4, 1. Ivrropuction).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
