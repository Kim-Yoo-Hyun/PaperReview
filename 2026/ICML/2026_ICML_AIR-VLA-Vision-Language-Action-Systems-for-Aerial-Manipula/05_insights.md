# Insights — AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=NuR4lG4gKB; PDF retrieval source: https://arxiv.org/pdf/2601.21602.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions of this paper are summarized as follows: • Pioneering Aerial Manipulation VLA Benchmark: We propose the first VLA benchmark testbed specifically designed ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose AIR-VLA, the first VLA training and evaluation benchmark designed specifically for Aerial Manipulation Systems.
- **p. 5 / 3.4. Dataset Construction - extractive body cue:** Standardized data interfaces ensure compatibility with the input layers of diverse VLA models.
- **p. 5 / 3.4. Dataset Construction - extractive body cue:** Tailored to aerial perspectives, the sensor configuration comprises: (1) a UAV front-down RGB-D camera for global bird's-eye views, (2) a manipulator wrist RGB-D camera for ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Dataset Construction), p. 5 (3.4. Dataset Construction)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, extending VLA models to aerial platforms introduces unique physical and control challenges.
- **p. 2 / 1. Introduction - extractive body cue:** However, existing VLA research is predominantly confined to Ground Mobile Manipulators, where the operational space is restricted to 2D planar navigation and limited working heights.
- **p. 3 / 1. Introduction - extractive body cue:** By quantifying the performance of current mainstream VLA models on aerial tasks and the high-level planning capabilities of VLMs, we reveal critical challenges in the ...
- **p. 6 / 4.1.2. MAIN RESULTS AND ANALYSIS - extractive body cue:** Due to the inherent characteristics of the floating base, collisions and unreasonable physical interactions cause significantly more severe disturbances to the system than in ground-based ...
- **p. 6 / 4.1.2. MAIN RESULTS AND ANALYSIS - extractive body cue:** Notably, in spatial understanding tasks, the models exhibit Spatial Grounding Failure: although the correct object category is identified, the agent manipulates an identical object at ...
- **p. 7 / 4.2.2. RESULTS AND ANALYSIS - extractive body cue:** In summary, VLMs hold immense potential for high-level planning in aerial manipulation, particularly in mitigating the long-horizon reasoning limitations of VLA models.
- **p. 8 / 5. Conclusion - extractive body cue:** Our findings reveal that while transferring pre-trained VLA models to aerial platforms is feasible, existing models still face severe challenges in handling floating-base dynamic coupling, ...
- **Boundary to test:** Due to the inherent characteristics of the floating base, collisions and unreasonable physical interactions cause significantly more severe disturbances to the system than in ground-based robotics.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | The main contributions of this paper are summarized as follows: • Pioneering Aerial Manipulation VLA Benchmark: We propose the first VLA benchmark testbed specifically designed for AMS, filling the evaluation gap in ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Compared to low-DoF ground-based platforms, the performance of existing VLA models on high-DoF aerial platforms remains suboptimal. π0 achieves its peak success rate in Base Manipulation tasks characterized by minimal environmental inte ... | p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 8 (4.2.2. RESULTS AND ANALYSIS) |
| Failure/limitation | Due to the inherent characteristics of the floating base, collisions and unreasonable physical interactions cause significantly more severe disturbances to the system than in ground-based robotics. | p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `standardized observation, action, task state와 evaluation split → benchmark state/goal와 method decision → policy/controller trajectory 또는 measured result`.
- 이 논문의 재사용 가능한 지점은 Tailored to the unique characteristics of aerial operations, we design a multi-suite dataset rich in sensory information (RGB, depth, proprioception) and diverse language instructions, providing high-quality data support for training ae ...를 Recently, VisionLanguage-Action (VLA) models, represented by RT-1 (Brohan et al., 2023), OpenVLA (Kim et al., 2024), and π0 (Black et al., 2026), have demonstrated exceptional capability in handling open-world tasks driven by ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 benchmark state/goal와 method decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Due to the inherent characteristics of the floating base, collisions and unreasonable physical interactions cause significantly more severe disturbances to the system than in ground-based robotics.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: The main contributions of this paper are summarized as follows: • Pioneering Aerial Manipulation VLA Benchmark: We propose the first VLA benchmark testbed specifically designed for AMS, filling the evaluation gap in ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics, Benchmark`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Due to the inherent characteristics of the floating base, collisions and unreasonable physical interactions cause significantly more severe disturbances to the system than in ground-based robotics.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Compared to traditional ground robot tasks, aerial mobile manipulation introduces unique challenges such as dynamic coupling of the floating base, volumetric workspaces, and temporal complexity of long-horizon tasks..
3. Compare against the body-reported baseline or a matched simpler baseline: Experimental results indicate that large-scale pre-trained models, represented by π0.5 and π0, demonstrate significant advantages in the AIR-VLA evaluation, outperforming traditional imitation learning baselines such as ACT and Diffusio ....
4. Report the body metric and its denominator/aggregation: The table displays normalized sub-metric scores and planning success rates (Succ, %) for each model across different task scenarios and instruction types..
5. Re-run the body-reported ablation/failure condition: To establish a representative benchmark, we evaluate six diverse models: π0 (Black et al., 2026) and π0.5 (Black et al., 2025), Flow Matching-based foundation models pre-trained on cross-embodiment data, represent large-scale transfer ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (3.4. Dataset Construction), p. 5 (3.4. Dataset Construction); the primary result is directionally consistent at p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS), p. 8 (4.2.2. RESULTS AND ANALYSIS), p. 6 (4.1.2. MAIN RESULTS AND ANALYSIS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, summarized mechanism이 Experimental results indicate that large-scale pre-trained models, represented by π0.5 and π0, demonstrate significant advantages in ... 대비 The table displays normalized sub-metric scores and planning success rates (Succ, %) for each model across different task ...을 개선하고, Due to the inherent characteristics of the floating base, collisions and unreasonable physical interactions cause significantly ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
