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

- **Paper-specific interface:** This setup differs significantly from OpenVLA's pretraining, which includes single-arm robot data only, a single camera viewpoint from 4 third-person camera, no robot state inputs, low-frequency control (3-10 Hz), and ... (p. 7, 3) LI regression objective).
- **Paper-specific mechanism:** In the next section, ‘we present a parallel generation scheme that enables efficient action chunking. (p. 3, 1. Iyrropucrion).
- **Evidence boundary:** the reported outcome is For methods using action chunking, we set chunk size to A' = 8 to match the Diffusion Policy baseline [5], and execute full chunks before replanning, which we find improves ... (p. 5, A. LIBERO Experimental Setup); the relevant task/metric cue is To provide fine-grained assessment, we use a predetermined rubric that assigns scores for partial task completion (see Appendix FF for details). (p. 8, C. ALOHA Task Performance Results). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** As visualized in Figure 6, it often fails to correct mistakes in the "scoop X into (p. 8, C. ALOHA Task Performance Results).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `VLA and generalist robot policies`; tags: `Robotics, VLA, OpenVLA, fine-tuning, action chunking, inference efficiency`.
- **Reading predecessor in the generated track queue:** FAST: Efficient Action Tokenization for Vision-Language-Action Models (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** On the other hand, zy demonstrates more robust execution ‘with smoother motions and better reactivity to feedback, often successfully recovering from initial failures (as shown in Figure 6).; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: This setup differs significantly from OpenVLA's pretraining, which includes single-arm robot data only, a single camera viewpoint from 4 third-person camera, no robot state inputs, low-frequency control (3-10 Hz), and ... (p. 7, 3) LI regression objective); preserve the objective/update rule: We fine-tune OpenVLA using OFT+ on each task independently for 50-150K gradient steps (total batch size 32 with 8 A100/H100-80GB GPUs) with action chunk size IK ~ 2 At inference ... (p. 8, 3) LI regression objective).
2. Use the paper-reported task/data/environment cue: We evaluate on the LIBERO simulation benchmark [26], which features a Franka Emika Panda arm in simulation with demonstrations containing camera images, robot state, task annotations, and delta end-effector pose ... (p. 5, A. LIBERO Experimental Setup).
3. Compare against the reported or matched baseline: Fine-tuned VLA pol cies generally outperform the from-scratch baselines in both task execution and language following, consistent with prior findings (27, 3]. (p. 8, C. ALOHA Task Performance Results).
4. Report the body metric with its denominator and aggregation: To provide fine-grained assessment, we use a predetermined rubric that assigns scores for partial task completion (see Appendix FF for details). (p. 8, C. ALOHA Task Performance Results).
5. Re-run the reported ablation or stress/failure condition: Note that Seer uses additional LIBERO90 pretraining data (p. 5, A. LIBERO Experimental Setup); if none is reported, design one around: As visualized in Figure 6, it often fails to correct mistakes in the "scoop X into (p. 8, C. ALOHA Task Performance Results).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 3 (1. Iyrropucrion), p. 1 (Abstract), match the reported outcome at p. 5 (A. LIBERO Experimental Setup), p. 5 (A. LIBERO Experimental Setup), p. 5 (A. LIBERO Experimental Setup), and measure the boundary at p. 8 (C. ALOHA Task Performance Results), p. 9 (C. ALOHA Task Performance Results).

## Falsifiable research question

Under the paper's stated interface (This setup differs significantly from OpenVLA's pretraining, which includes single-arm robot data only, a single camera viewpoint from 4 third-person camera, no ...), does the paper-specific mechanism (In the next section, ‘we present a parallel generation scheme that enables efficient action chunking.) retain the reported evaluation outcome (To provide fine-grained assessment, we use a predetermined rubric that assigns scores for partial task completion (see Appendix ...) when tested against the paper's strongest explicit boundary (As visualized in Figure 6, it often fails to correct mistakes in the "scoop X into)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (To provide fine-grained assessment, we use a predetermined rubric that assigns scores for partial task completion (see Appendix ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In the next section, ‘we present a parallel generation scheme that enables efficient action chunking. (p. 3, 1. Iyrropucrion).
- **Paper-supported outcome:** For methods using action chunking, we set chunk size to A' = 8 to match the Diffusion Policy baseline [5], and execute full chunks before replanning, which we find improves ... (p. 5, A. LIBERO Experimental Setup).
- **Strongest explicit boundary:** As visualized in Figure 6, it often fails to correct mistakes in the "scoop X into (p. 8, C. ALOHA Task Performance Results).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
