# Insights — Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p017.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p017.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / 1. Iyrropucrion - extractive body cue:** In the next section, ‘we present a parallel generation scheme that enables efficient action chunking.
- **p. 1 / Abstract - extractive body cue:** We propose OpenVLA™ OFT, an instantiation of this sels a new state of the art on the L wation benchmark, significantly boosting OpenVLA's average success ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** Building on these insights, we introduce OpenVLA-OFT: an instantiation of an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding and action chunking, continuous action representations, ...
- **p. 14 / B. Implementation Details - extractive body cue:** LI regression: The MLP action head consists of 4 layers with ReLU activation, mapping final Llama-2 decoder layer hidden states directly to continuous actions.
- **p. 2 / 1. Iyrropucrion - extractive body cue:** With 25-timestep action ‘chunks, OpenVLA-OFT+ achieves 43% faster throughput than base OpenVLA, demonstrating that our new fine-tuning recipe ‘enables real-time robot control with strong task ...
- **p. 15 / C. Feature-wise Linear Modulation (FILM) Implementation - extractive body cue:** For Diffusion Policy training, we use the DROID implementation [22], which conditions action predictions on DistilBERT [42] language embeddings of the task description, We list ...
- **p. 7 / 3) LI regression objective - extractive body cue:** Given that the alternative fine-tuning formulation, along with additional model inputs and outputs, induces a distri bution shift between the base VLA's pretraining and finetuning, ...
- **Contribution anchor:** p. 3 (1. Iyrropucrion), p. 1 (Abstract), p. 1 (1. Iyrropucrion), p. 14 (B. Implementation Details), p. 2 (1. Iyrropucrion), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation)

### Strongest assumption and failure boundary

- **p. 3 / A. VIA Fine-Tuning Design Decisions - extractive body cue:** Existing approaches that fine-tune VLAs using the base ‘model's autoregressive training recipe face two key limitations: slow inference speed (3-5 Hz) unsuitable for high-frequency control, ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** We address this gap by exploring VLA adaptation design decisions for fast inference and reliable task execution on a real-world bimanual ‘manipulator with a 25 ...
- **p. 3 / A. VIA Fine-Tuning Design Decisions - extractive body cue:** To address these challenges, we investigate three key design components for VLA fine-tuning:
- **p. 4 / B. Implementing Alternative Design Components - extractive body cue:** Challenges with language following, When deploying on the ALOHA robot setup with multiple viewpoints including from wrist-mounted cameras, we observe that policies can struggle with ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** Prior work has begun exploring VLA adaptation strategies, with Kim et al.
- **p. 9 / C. ALOHA Task Performance Results - extractive body cue:** On the other hand, zy demonstrates more robust execution ‘with smoother motions and better reactivity to feedback, often successfully recovering from initial failures (as shown ...
- **p. 8 / C. ALOHA Task Performance Results - extractive body cue:** As visualized in Figure 6, it often fails to correct mistakes in the "scoop X into
- **Boundary to test:** On the other hand, zy demonstrates more robust execution ‘with smoother motions and better reactivity to feedback, often successfully recovering from initial failures (as shown in Figure 6).

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In the next section, ‘we present a parallel generation scheme that enables efficient action chunking. | p. 3 (1. Iyrropucrion), p. 1 (Abstract) |
| Reported outcome | Finally, OpenVLA-OFT+ achieves the highest performance across both task execution and language following (see Figure 7 for examples of successful task rollouts). | p. 9 (C. ALOHA Task Performance Results), p. 5 (A. LIBERO Experimental Setup) |
| Failure/limitation | On the other hand, zy demonstrates more robust execution ‘with smoother motions and better reactivity to feedback, often successfully recovering from initial failures (as shown in Figure 6). | p. 9 (C. ALOHA Task Performance Results), p. 8 (C. ALOHA Task Performance Results) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 ‘decoding, action chunking, a conti and a simple L1 regression-based lea ference efficiency, policy performance, and flex inthe rodel's input-output opecicatios.를 This setup differs significantly from OpenVLA's pretraining, which includes single-arm robot data only, a single camera viewpoint from 4 third-person camera, no robot state inputs, low-frequency control (3-10 Hz), and relative end-effec ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 On the other hand, zy demonstrates more robust execution ‘with smoother motions and better reactivity to feedback, often successfully recovering from initial failures (as shown in Figure 6).에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In the next section, ‘we present a parallel generation scheme that enables efficient action chunking.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, VLA, OpenVLA, fine-tuning, action chunking, inference efficiency`.
- **Reading predecessor in the generated track queue:** FAST: Efficient Action Tokenization for Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** On the other hand, zy demonstrates more robust execution ‘with smoother motions and better reactivity to feedback, often successfully recovering from initial failures (as shown in Figure 6).; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We evaluate on the LIBERO simulation benchmark [26], which features a Franka Emika Panda arm in simulation with demonstrations containing camera images, robot state, task annotations, and delta end-effector pose actions..
3. Compare against the body-reported baseline or a matched simpler baseline: Fine-tuned VLA pol cies generally outperform the from-scratch baselines in both task execution and language following, consistent with prior findings (27, 3]..
4. Report the body metric and its denominator/aggregation: Success rates in approaching for language-dependent tasks..
5. Re-run the body-reported ablation/failure condition: Note that we do not use FILM for LIBERO ‘experiments since the fine-tuned policies without it already demonstrate good language grounding..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 14 (B. Implementation Details), p. 15 (C. Feature-wise Linear Modulation (FILM) Implementation), p. 7 (3) LI regression objective); the primary result is directionally consistent at p. 9 (C. ALOHA Task Performance Results), p. 5 (A. LIBERO Experimental Setup), p. 8 (C. ALOHA Task Performance Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 next, section, present mechanism이 Fine-tuned VLA pol cies generally outperform the from-scratch baselines in both task execution and language following, ... 대비 Success rates in approaching for language-dependent tasks.을 개선하고, On the other hand, zy demonstrates more robust execution ‘with smoother motions and better reactivity to ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
