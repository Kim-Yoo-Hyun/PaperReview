# Insights — AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=88RKxlFUNY; PDF retrieval source: https://openreview.net/pdf/1a99a8c26a0bf879894a517257af43defc03d88a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 21 / A.4.1 BASELINE CONSTRUCTION DETAILS - extractive body cue:** This standardized backbone approach enables fair comparison of each method's core contributions while maintaining implementation feasibility within our experimental framework.
- **p. 4 / 3 METHOD - extractive body cue:** To enhance geometric reasoning capability, we introduce AutoFly, a VLA architecture augmented with pseudo-depth encoding.
- **p. 4 / 3 METHOD - extractive body cue:** Our framework integrates three core components, including a visionlanguage model, pseudo-depth encoder, and action de-tokenizer, as illustrated in Figure 2.
- **p. 21 / A.4.1 BASELINE CONSTRUCTION DETAILS - extractive body cue:** We utilize the same prism-siglip-7b backbone for consistency across VLM-based baselines, ensuring that performance differences reflect methodological contributions rather than backbone variations.
- **p. 22 / A.5.3 MODEL ACCELERATION - extractive body cue:** Additional CUDA operators are implemented for custom depth processing operations, while model parallelism enables distributed inference across multiple GPU processes to handle the computational demands ...
- **p. 4 / 3 METHOD - extractive body cue:** 3.1 TASK FORMULATION We formulate autonomous navigation as learning a control policy π that takes the current RGB observation ot ∈O, language instruction L, and ...
- **p. 20 / A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES - extractive body cue:** We replace the SigLIP visual backbone with SigLIP 2 (fused with DINOv2), a state-of-the-art RGB encoder, to assess whether improved visual features can substitute for ...
- **Contribution anchor:** p. 21 (A.4.1 BASELINE CONSTRUCTION DETAILS), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 21 (A.4.1 BASELINE CONSTRUCTION DETAILS), p. 22 (A.5.3 MODEL ACCELERATION), p. 4 (3 METHOD)

### Strongest assumption and failure boundary

- **p. 1 / ABSTRACT - extractive body cue:** Vision-language navigation (VLN) requires intelligent agents to navigate environments by interpreting linguistic instructions alongside visual observations, serving as a cornerstone task in Embodied AI.
- **p. 1 / ABSTRACT - extractive body cue:** Current VLN research for unmanned aerial vehicles (UAVs) relies on detailed, pre-specified instructions to guide the UAV along predetermined routes.
- **p. 20 / A.3.3 EVALUATION ON CHALLENGING SCENARIOS - extractive body cue:** Dense Cylinders Scene Dense Forest Scene Dynamic Obstacle Scenarios Method SR CR PER SR CR PER SR CR PER w/ 57.2 21.1 78.3 53.6 23.7 ...
- **p. 24 / A.7 LIMITATIONS AND FUTURE WORK - extractive body cue:** To address these limitations, we plan to enhance AutoFly's sensing capabilities through LiDAR integration, which will provide comprehensive 360◦environmental perception and improve robustness in complex ...
- **p. 24 / A.7 LIMITATIONS AND FUTURE WORK - extractive body cue:** Future work will integrate Reinforcement Learning to enable active interaction with dynamic environments, allowing the system to learn more robust reactive behaviors through trial-and-error exploration.
- **p. 20 / A.3.3 EVALUATION ON CHALLENGING SCENARIOS - extractive body cue:** The baseline model's collision rate reaches 37.7%, frequently failing to maintain safe distances from moving obstacles or predict their trajectories.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Analysis of previous methods and our AutoFly. Left: Previous methods (Lee et al., 2024; Liu et al., 2023b) rely on dedicated, step-by-step instructions ...
- **Boundary to test:** Dense Cylinders Scene Dense Forest Scene Dynamic Obstacle Scenarios Method SR CR PER SR CR PER SR CR PER w/ 57.2 21.1 78.3 53.6 23.7 77.3 50.7 28.2 73.9 w/o 49.3 28.7 ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | This standardized backbone approach enables fair comparison of each method's core contributions while maintaining implementation feasibility within our experimental framework. | p. 21 (A.4.1 BASELINE CONSTRUCTION DETAILS), p. 4 (3 METHOD) |
| Reported outcome | Results demonstrate clear performance differences: SigLIP achieves the highest success rate among single encoders (46.6%), outperforming CLIP (43.1%) by 3.5% and DINO (45.2%) by 1.4%. | p. 19 (A.3.2 ABLATION EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Failure/limitation | Dense Cylinders Scene Dense Forest Scene Dynamic Obstacle Scenarios Method SR CR PER SR CR PER SR CR PER w/ 57.2 21.1 78.3 53.6 23.7 77.3 50.7 28.2 73.9 w/o 49.3 28.7 ... | p. 20 (A.3.3 EVALUATION ON CHALLENGING SCENARIOS), p. 24 (A.7 LIMITATIONS AND FUTURE WORK) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 3.1 TASK FORMULATION We formulate autonomous navigation as learning a control policy π that takes the current RGB observation ot ∈O, language instruction L, and coarse positional or directional guidance encoded as ...를 For a stochastic policy, the target value y is calculated as: y = r + γ(1 -d)  min i=1,2 Qθ′ i(s′, a′) -α log πϕ(a′/s′)  , (6) where γ is ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Dense Cylinders Scene Dense Forest Scene Dynamic Obstacle Scenarios Method SR CR PER SR CR PER SR CR PER w/ 57.2 21.1 78.3 53.6 23.7 77.3 50.7 28.2 73.9 w/o 49.3 28.7 ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: This standardized backbone approach enables fair comparison of each method's core contributions while maintaining implementation feasibility within our experimental framework.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics, Navigation`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Dense Cylinders Scene Dense Forest Scene Dynamic Obstacle Scenarios Method SR CR PER SR CR PER SR CR PER w/ 57.2 21.1 78.3 53.6 23.7 77.3 50.7 28.2 73.9 w/o 49.3 28.7 ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Our training set comprises 10 scenes with 50 object instances, totaling over 13K episodes and 2.5M image-language-action triplets..
3. Compare against the body-reported baseline or a matched simpler baseline: The results in Table 4 demonstrate that the method with the pseudo-depth encoder (47.9%, 21.9%) in success rate and collision rate significantly outperforms the one without it (44%, 24.5%), which proves the ....
4. Report the body metric and its denominator/aggregation: As shown in Table refsim-to-real, AutoFly achieves comparable performance across both environments: 60% success rate indoors versus 55% outdoors, with collision rates of 30% and 35%, respectively..
5. Re-run the body-reported ablation/failure condition: To validate the effectiveness of our pseudo-depth encoder, we conduct ablation studies comparing models with and without the depth encoder..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3 METHOD), p. 20 (A.3.4 ANALYSIS OF SIMPLER ALTERNATIVE APPROACHES), p. 4 (3 METHOD); the primary result is directionally consistent at p. 19 (A.3.2 ABLATION EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 standardized, backbone, enables mechanism이 The results in Table 4 demonstrate that the method with the pseudo-depth encoder (47.9%, 21.9%) in ... 대비 As shown in Table refsim-to-real, AutoFly achieves comparable performance across both environments: 60% success rate indoors versus 55% ...을 개선하고, Dense Cylinders Scene Dense Forest Scene Dynamic Obstacle Scenarios Method SR CR PER SR CR PER ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
