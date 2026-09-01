# Insights — Perpetual Humanoid Control for Real-time Simulated Avatars

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2023/html/Luo_Perpetual_Humanoid_Control_for_Real-time_Simulated_Avatars_ICCV_2023_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2023/html/Luo_Perpetual_Humanoid_Control_for_Real-time_Simulated_Avatars_ICCV_2023_paper.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are as follows: (1) we propose a Perpetual Humanoid Controller that can successfully imitate 98.9% of the AMASS dataset without applying ...
- **p. 5 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** Thus, we propose Relaxed Early Termination (RET), which allows the humanoid's ankle and toes to slightly deviate from the MoCap motion to remain balanced.
- **p. 3 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** The simulation state st ≜(sp t, sg t) consists of humanoid proprioception sp t and the goal state sg t.
- **p. 4 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** Unlike prior motion tracking policies that only use a motion imitation reward, we use the recently proposed Adversarial Motion Prior [33] and include a discriminator ...
- **p. 5 / 3.2. Progressive Multiplicative Control Policy - extractive body cue:** Thus, we propose a progressive multiplicative control policy (PMCP), which allocates new subnetworks (primitives P) to learn harder sequences.
- **p. 4 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** (1) For the discriminator, we use the same observations, loss formulation, and gradient penalty as AMP [33].
- **p. 4 / 3.1. Goal Conditioned Motion Imitation with Ad - extractive body cue:** We use a proportional derivative (PD) controller at each DoF of the humanoid and the action at specifies the PD target.
- **Contribution anchor:** p. 2 (1. Introduction), p. 5 (3.1. Goal Conditioned Motion Imitation with Ad), p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy), p. 4 (3.1. Goal Conditioned Motion Imitation with Ad)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** These limitations prevent the widespread adoption of physics-based methods, as current control policies cannot handle noisy observations such as video or language.
- **p. 1 / 1. Introduction - extractive body cue:** However, controlling high-degree-of-freedom (DOF) humanoids in simulation presents significant challenges, as they can fall, trip, or deviate from their reference motions, and struggle to recover.
- **p. 2 / 1. Introduction - extractive body cue:** However, resetting successfully requires a high-quality reference pose, which is often difficult to obtain due to the noisy nature of the pose estimates, leading to ...
- **p. 2 / 1. Introduction - extractive body cue:** Another important aspect of controlling simulated humanoids is how to handle noisy input and failure cases.
- **p. 8 / 5. Discussions - extractive body cue:** Although we can train single-clip controller to overfit on these sequences (see the supplement), our full controller often fails to learn these sequences.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: (a) Imitating high-quality MoCap - spin and kick. (b) Recover from fallen state and go back to reference motion (indicated by red dots). ...
- **p. 7 / 4. Experiments - extractive body cue:** We uses four primitives (including failstate recovery) for all our evaluations.
- **Boundary to test:** Although we can train single-clip controller to overfit on these sequences (see the supplement), our full controller often fails to learn these sequences.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To summarize, our contributions are as follows: (1) we propose a Perpetual Humanoid Controller that can successfully imitate 98.9% of the AMASS dataset without applying any external forces; (2) we propose the ... | p. 2 (1. Introduction), p. 5 (3.1. Goal Conditioned Motion Imitation with Ad) |
| Reported outcome | H36M-Test-Video* RET MCP PNN Rotation Fail-Recover Succ ↑ Eg-mpjpe ↓ Empjpe ↓ ✗ ✗ ✗ ✓ ✗ 51.2% 56.2 34.4 ✓ ✗ ✗ ✓ ✗ 59.4% 60.2 37.2 ✓ ✓ ✗ ✓ ... | p. 8 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation) |
| Failure/limitation | Although we can train single-clip controller to overfit on these sequences (see the supplement), our full controller often fails to learn these sequences. | p. 8 (5. Discussions), p. 6 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 The physics simulation determines state st ∈S and transition dynamics T while our policy πPHC computes per-step action at ∈A.를 P(F ) shares the same input and output space as P(1) · · · P(k), but since the reference motion does not provide useful information about failstate recovery (the humanoid should not ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Although we can train single-clip controller to overfit on these sequences (see the supplement), our full controller often fails to learn these sequences.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To summarize, our contributions are as follows: (1) we propose a Perpetual Humanoid Controller that can successfully imitate 98.9% of the AMASS dataset without applying any external forces; (2) we propose the ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, whole-body control, motion imitation`.
- **Reading predecessor in the generated track queue:** Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Although we can train single-clip controller to overfit on these sequences (see the supplement), our full controller often fails to learn these sequences.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: PHC is trained on the training split of the AMASS [23] dataset..
3. Compare against the body-reported baseline or a matched simpler baseline: Similar to results on MoCap Imitation, PHC outperforms the baselines 10901.
4. Report the body metric and its denominator/aggregation: On testing, PHC shows a high success rate on unseen MoCap sequences from both the AMASS and H36M data..
5. Re-run the body-reported ablation/failure condition: Comparing R4 and R5 shows that PMCP is effective in adding fail-state recovery capability without compromising motion imitation..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 4 (3.1. Goal Conditioned Motion Imitation with Ad), p. 5 (3.2. Progressive Multiplicative Control Policy); the primary result is directionally consistent at p. 8 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summarize, contributions, follows mechanism이 Similar to results on MoCap Imitation, PHC outperforms the baselines 10901 대비 On testing, PHC shows a high success rate on unseen MoCap sequences from both the AMASS and H36M ...을 개선하고, Although we can train single-clip controller to overfit on these sequences (see the supplement), our full ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
