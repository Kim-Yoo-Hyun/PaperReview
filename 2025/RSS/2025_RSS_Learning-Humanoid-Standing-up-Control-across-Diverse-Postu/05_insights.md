# Insights — Learning Humanoid Standing-up Control across Diverse Postures

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p064.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p064.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** To enable postureadaptive motion beyond the ground, we introduce multiple terrains for training and a vertical pull force during the initial stages to facilitate exploration, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We overview the real-world performance of our controllers in Fg. / and summarize our core contributions as follows:
- **p. 12 / B. More Implementation Details - extractive body cue:** Our PPO implementation follows the framework outlined in [39]. ‘The actor network consists of 4 3-layer MLP with hidden dimensions [512, 256, 128], while each ...
- **p. 12 / B. More Implementation Details - extractive body cue:** We present the complete set of ward functions and their detailed descriptions in Tulble V1 Several regularization reward terms are adapted from prior work [21, ...
- **p. 13 / B. More Implementation Details - extractive body cue:** During the hardware deployment, the stiffness of hip and knee joints are amplified to 1.5 times than the simulation ones, similar to G1, We present ...
- **p. 13 / B. More Implementation Details - extractive body cue:** postures, PD controllers, observation and action spaces.
- **p. 12 / B. More Implementation Details - extractive body cue:** The lower bounds for the vertical force and action bound are ON and 0.25, respectively.
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 12 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details), p. 13 (B. More Implementation Details)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our proposed RL. framework addresses these limitations by achieving posture adaptivity and real-world deployability without predefined motions, enabling smooth, stable, and robust standing-up across a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** ‘TABLE I: Comparison with existing methods on standing-up contol
- **p. 6 / B. Main Results - extractive body cue:** Without the proposed force curriculum, the robot fails to stand up on all terrains except the platform, as the other terrains require exploration from a ...
- **p. 9 / C. Emergent Properties - extractive body cue:** We further tested our controllers on a 15° slippery slope, simulating challenging real-world conditions such as unstable surfaces.
- **p. 8 / A. Main Results - extractive body cue:** Motion oscillations are observed in all scenes without smoothness regularization, often leading to standing-up failures, In contrast, our method produces smooth and stable motions, especially ...
- **p. 9 / VII. CoxcLusion - extractive body cue:** Our proposed framework, HOST, advances humanoid standing-up control by addressing the limitations of existing methods, which either neglect hardware constraints or rely on predefined motion ...
- **p. 12 / B. More Implementation Details - extractive body cue:** are handcrafted without collision models.
- **Boundary to test:** Without the proposed force curriculum, the robot fails to stand up on all terrains except the platform, as the other terrains require exploration from a fully fallen state to stable kneeling.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To enable postureadaptive motion beyond the ground, we introduce multiple terrains for training and a vertical pull force during the initial stages to facilitate exploration, Given the multiple stages of the task, ... | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | key design choices is summarized as follows: Multiple critics are crucial for learning motor skills Using the same reward functions, the performance of the single critic version of HOST deteriorates significantly across ... | p. 6 (B. Main Results), p. 6 (B. Main Results) |
| Failure/limitation | Without the proposed force curriculum, the robot fails to stand up on all terrains except the platform, as the other terrains require exploration from a fully fallen state to stable kneeling. | p. 6 (B. Main Results), p. 9 (C. Emergent Properties) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 postures, PD controllers, observation and action spaces.를 The lower bounds for the vertical force and action bound are ON and 0.25, respectively.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Without the proposed force curriculum, the robot fails to stand up on all terrains except the platform, as the other terrains require exploration from a fully fallen state to stable kneeling.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To enable postureadaptive motion beyond the ground, we introduce multiple terrains for training and a vertical pull force during the initial stages to facilitate exploration, Given the multiple stages of the task, ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `World models, safety, uncertainty, and recovery`; tags: `Robotics, humanoid, standing up, fall recovery, sim-to-real`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Without the proposed force curriculum, the robot fails to stand up on all terrains except the platform, as the other terrains require exploration from a fully fallen state to stable kneeling.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: this conclusion, with our approach achieving a 100% success rate and high motion smoothness across all scenes.' Generalization to outdoor environments (Viz..
3. Compare against the body-reported baseline or a matched simpler baseline: HOST with short history length underperforms in contact-rich scenarios, such as the Wall terrain, In contrast, a longer history length improves performance, though it slightly reduces motion smoothness and increases energy consumption ....
4. Report the body metric and its denominator/aggregation: key design choices is summarized as follows: Multiple critics are crucial for learning motor skills Using the same reward functions, the performance of the single critic version of HOST deteriorates significantly across ....
5. Re-run the body-reported ablation/failure condition: ‘We select the successful episode to compute smocthaess to reflect the effect of L2C2 regularization tier..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details), p. 12 (B. More Implementation Details); the primary result is directionally consistent at p. 6 (B. Main Results), p. 6 (B. Main Results), p. 8 (A. Main Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 enable, postureadaptive, motion mechanism이 HOST with short history length underperforms in contact-rich scenarios, such as the Wall terrain, In contrast, ... 대비 key design choices is summarized as follows: Multiple critics are crucial for learning motor skills Using the same ...을 개선하고, Without the proposed force curriculum, the robot fails to stand up on all terrains except the ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
