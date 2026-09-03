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

- **Paper-specific interface:** Specifically, our composer C(w1:K+1 t /st) consumes the same input as the primitives and outputs a weight vector w1:K+1 t ∈Rk+1 to activate the primitives. (p. 6, 3.2. Progressive Multiplicative Control Policy).
- **Paper-specific mechanism:** To summarize, our contributions are as follows: (1) we propose a Perpetual Humanoid Controller that can successfully imitate 98.9% of the AMASS dataset without applying any external forces; (2) we ... (p. 2, 1. Introduction).
- **Evidence boundary:** the reported outcome is Similar to results on MoCap Imitation, PHC outperforms the baselines 10901 (p. 7, 4.1. Motion Imitation); the relevant task/metric cue is From Tab.4 we can see that both of our keypoint-based and rotation-based controllers can recover from fall state with high success rate (> 90%) even in the challenging scenario when ... (p. 8, 4.2. Fail-state Recovery). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** Thus, it is important to have a controller that can gracefully handle unexpected falls and noisy input, naturally recover from failstate, and resume imitation. (p. 2, 1. Introduction).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Locomotion, whole-body, mobile manipulation, and humanoids`; tags: `Robotics, humanoid, whole-body control, motion imitation`.
- **Reading predecessor in the generated track queue:** Mobile ALOHA: Learning Bimanual Mobile Manipulation using Low-Cost Whole-Body Teleoperation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Although we can train single-clip controller to overfit on these sequences (see the supplement), our full controller often fails to learn these sequences.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Specifically, our composer C(w1:K+1 t /st) consumes the same input as the primitives and outputs a weight vector w1:K+1 t ∈Rk+1 to activate the primitives. (p. 6, 3.2. Progressive Multiplicative Control Policy); preserve the objective/update rule: The policy's goal is to maximize the discounted reward E hPT t=1 γt-1rt i , and we use the proximal policy gradient (PPO) [35] to learn πPHC. (p. 3, 3.1. Goal Conditioned Motion Imitation with Ad).
2. Use the paper-reported task/data/environment cue: PHC is trained on the training split of the AMASS [23] dataset. (p. 7, 4. Experiments).
3. Compare against the reported or matched baseline: Similar to results on MoCap Imitation, PHC outperforms the baselines 10901 (p. 7, 4.1. Motion Imitation).
4. Report the body metric with its denominator and aggregation: From Tab.4 we can see that both of our keypoint-based and rotation-based controllers can recover from fall state with high success rate (> 90%) even in the challenging scenario when ... (p. 8, 4.2. Fail-state Recovery).
5. Re-run the reported ablation or stress/failure condition: We compare against UHC both with and without residual force control. (p. 7, 4. Experiments); if none is reported, design one around: Thus, it is important to have a controller that can gracefully handle unexpected falls and noisy input, naturally recover from failstate, and resume imitation. (p. 2, 1. Introduction).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (1. Introduction), p. 3 (3.1. Goal Conditioned Motion Imitation with Ad), match the reported outcome at p. 7 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation), p. 7 (4.1. Motion Imitation), and measure the boundary at p. 2 (1. Introduction), p. 5 (3.2. Progressive Multiplicative Control Policy).

## Falsifiable research question

Under the paper's stated interface (Specifically, our composer C(w1:K+1 t /st) consumes the same input as the primitives and outputs a weight vector w1:K+1 t ∈Rk+1 to ...), does the paper-specific mechanism (To summarize, our contributions are as follows: (1) we propose a Perpetual Humanoid Controller that can successfully imitate 98.9% of the AMASS ...) retain the reported evaluation outcome (From Tab.4 we can see that both of our keypoint-based and rotation-based controllers can recover from fall state ...) when tested against the paper's strongest explicit boundary (Thus, it is important to have a controller that can gracefully handle unexpected falls and noisy input, naturally ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (From Tab.4 we can see that both of our keypoint-based and rotation-based controllers can recover from fall state ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** To summarize, our contributions are as follows: (1) we propose a Perpetual Humanoid Controller that can successfully imitate 98.9% of the AMASS dataset without applying any external forces; (2) we ... (p. 2, 1. Introduction).
- **Paper-supported outcome:** Similar to results on MoCap Imitation, PHC outperforms the baselines 10901 (p. 7, 4.1. Motion Imitation).
- **Strongest explicit boundary:** Thus, it is important to have a controller that can gracefully handle unexpected falls and noisy input, naturally recover from failstate, and resume imitation. (p. 2, 1. Introduction).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
