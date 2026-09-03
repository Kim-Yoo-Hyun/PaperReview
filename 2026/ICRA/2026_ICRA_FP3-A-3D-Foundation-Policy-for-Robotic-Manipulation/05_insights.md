# Insights — FP3: A 3D Foundation Policy for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://2026.ieee-icra.org/awards/; PDF retrieval source: https://arxiv.org/pdf/2503.08950. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we introduce 3D Foundation Policy (FP3), the first 3D point cloud-based language-visuomotor policy foundation model for robotic manipulation that exhibits strong generalizability ...
- **p. 4 / III. METHOD - extractive body cue:** Thanks to the effective initialization from pre-training, this small amount of fine-tuning data enables zero-shot deployment to novel environments and objects.
- **p. 3 / III. METHOD - extractive body cue:** We introduce the 3D Foundation Policy (FP3) model for generalist robotic manipulation, achieving high data efficiency and generalization capability.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We summarize our main contributions as follows:
- **p. 3 / III. METHOD - extractive body cue:** FP3 is a 1.3B encoder-decoder transformer network following a two-stage pre-training and post-training recipe.
- **p. 3 / III. METHOD - extractive body cue:** Now we describe the detailed structure of FP3 model, including the encoding of multi-modal inputs and the transformer-based encoder-decoder architecture.
- **p. 4 / III. METHOD - extractive body cue:** The Transformer encoder fuses multi-modal input embeddings to latent tokens, while the Transformer decoder takes in the noise actions and leverages adaLN [47, 5, 32] ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** One potential limitation of current policy foundation models is their exclusive reliance on 2D image observations, lacking 3D observation inputs.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, these learned policies often show limited or even zero generalization capability to unseen scenarios, new objects, and distractors [66].
- **p. 6 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive body cue:** This phenomenon happens probably because the fine-tuning data is limited, thus the policies without pre-training can fall into an out-of-distribution state after the first failure, ...
- **p. 8 / V. LIMITATIONS - extractive body cue:** While FP3 shows strong performance as a policy foundation model, it still has several limitations.
- **p. 8 / V. LIMITATIONS - extractive body cue:** One limitation is that although FP3 enables efficient and generalizable downstream fine-tuning, the base model exhibits limited zero-shot performance.
- **p. 5 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive body cue:** Qualitatively, we find that the failures of all baseline algorithms are mainly due to issues in the details, such as not being precise enough when ...
- **p. 6 / 4) Can FP3 correctly execute the corresponding tasks fol - extractive body cue:** Another interesting issue is the policy's response after an initial failure attempt.
- **Boundary to test:** This phenomenon happens probably because the fine-tuning data is limited, thus the policies without pre-training can fall into an out-of-distribution state after the first failure, and hence fail to output reasonable behaviors.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this work, we introduce 3D Foundation Policy (FP3), the first 3D point cloud-based language-visuomotor policy foundation model for robotic manipulation that exhibits strong generalizability and sample efficiency. | p. 2 (I. INTRODUCTION), p. 4 (III. METHOD) |
| Reported outcome | The actions predicted by the FP3 policy are significantly smoother and more precise, leading to a notably higher success rate compared to the strong baselines. | p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 5 (4) Can FP3 correctly execute the corresponding tasks fol) |
| Failure/limitation | This phenomenon happens probably because the fine-tuning data is limited, thus the policies without pre-training can fall into an out-of-distribution state after the first failure, and hence fail to output reasonable behaviors. | p. 6 (4) Can FP3 correctly execute the corresponding tasks fol), p. 8 (V. LIMITATIONS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 It takes the 3D point cloud observation, language, and robot proprioceptive state as input and predicts action chunks of future actions.를 Pour the water in the bottle into the cup Language Instruction (𝑥, 𝑦, 𝑧, α, 𝛽, 𝛾, 𝑔) Proprioception States Uni3D ViT Uni3D ViT CLIP MLP Transformer Encoder Diffusion Transformer with Causal ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 This phenomenon happens probably because the fine-tuning data is limited, thus the policies without pre-training can fall into an out-of-distribution state after the first failure, and hence fail to output reasonable behaviors.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this work, we introduce 3D Foundation Policy (FP3), the first 3D point cloud-based language-visuomotor policy foundation model for robotic manipulation that exhibits strong generalizability and sample efficiency.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Robotics, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** This phenomenon happens probably because the fine-tuning data is limited, thus the policies without pre-training can fall into an out-of-distribution state after the first failure, and hence fail to output reasonable behaviors.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: As we pre-train our FP3 model on the DROID dataset, we also build a real robot setup similar to DROID for evaluating downstream tasks..
3. Compare against the body-reported baseline or a matched simpler baseline: The actions predicted by the FP3 policy are significantly smoother and more precise, leading to a notably higher success rate compared to the strong baselines..
4. Report the body metric and its denominator/aggregation: We report the success rate as our metric..
5. Re-run the body-reported ablation/failure condition: This phenomenon happens probably because the fine-tuning data is limited, thus the policies without pre-training can fall into an out-of-distribution state after the first failure, and hence fail to output reasonable behaviors..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD); the primary result is directionally consistent at p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 5 (4) Can FP3 correctly execute the corresponding tasks fol), p. 6 (4) Can FP3 correctly execute the corresponding tasks fol); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 introduce, Foundation, Policy mechanism이 The actions predicted by the FP3 policy are significantly smoother and more precise, leading to a ... 대비 We report the success rate as our metric.을 개선하고, This phenomenon happens probably because the fine-tuning data is limited, thus the policies without pre-training can ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
