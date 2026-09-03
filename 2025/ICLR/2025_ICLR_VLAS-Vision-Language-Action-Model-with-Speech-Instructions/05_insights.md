# Insights — VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=K4FAFNRpko; PDF retrieval source: https://openreview.net/pdf/5f77b9b6bd43ed1a7a7d7ba9fc75c64727d77792.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To sum up, the main contributions of this work are listed as follows: 1) We propose VLAS, the first vision-language-action model that integrates speech for ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Based on the above analysis, we propose guiding a robot's behavior through speech rather than text.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 3) Besides the robot policy model, we introduce VLAS-Base, which extends the widely used vision-language model LLaVA to accept speech instructions.
- **p. 3 / 3 METHOD - extractive body cue:** We present VLAS, a VLA model directly supporting speech instructions for robot manipulation.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** These models demonstrate enhanced generalization to novel objects and semantically diverse instructions, as well as a range of emergent capabilities.
- **p. 3 / 3 METHOD - extractive body cue:** 3.1 ARCHITECTURE OF VLAS Overall Framework VLAS takes human speech instructions s and visual observations O as input to directly generate robot actions a.
- **p. 3 / 3 METHOD - extractive body cue:** As illustrated in Figure 2, we first provide an overview of the VLAS architecture (Section 3.1).
- **Contribution anchor:** p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 1 (1 INTRODUCTION), p. 3 (3 METHOD)

### Strongest assumption and failure boundary

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Failure Textual instruction: "Please pick up my cup." Speech instruction: "Please pick up my cup." Success I don't know which cup you want.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** These models demonstrate enhanced generalization to novel objects and semantically diverse instructions, as well as a range of emergent capabilities.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Given these practical needs and existing technologies, a key question arises: How can we integrate visionlanguage-action models with speech modality to produce a simpler and ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To alleviate these two problems, we present VLAS, an innovative end-toend policy model that seamlessly integrates speech modality for robot manipulation.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 9: Demonstration of failure cases of VLA on the customization benchmark. We conducted additional analysis on the failure cases of VLAS and VLA on ...
- **p. 10 / 5 CONCLUSION - extractive body cue:** Our future work may focus on exploring other auxiliary information in human speech or environmental sounds to enable the robot to better understand and complete ...
- **p. 10 / 1. I have a blue - extractive body cue:** Moreover, although VLAS-Base falls behind LLaVA with ground-truth textual instructions on the SGQA benchmark, it still surpasses BLIP-2.
- **Boundary to test:** Figure 9: Demonstration of failure cases of VLA on the customization benchmark. We conducted additional analysis on the failure cases of VLAS and VLA on the customization benchmark to better identify the ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | To sum up, the main contributions of this work are listed as follows: 1) We propose VLAS, the first vision-language-action model that integrates speech for robot manipulation without needing external speech recognition ... | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Reported outcome | Figure 7: Demonstration of success cases of VLAS on the real-world UR5 robot arm. In Table 4, VLAS-Base achieves comparable performance to Whisper large-v2 on the LibriSpeech test set. Considering that a ... | p. 10 (Figure/Table caption), p. 8 (1. I have a blue) |
| Failure/limitation | Figure 9: Demonstration of failure cases of VLA on the customization benchmark. We conducted additional analysis on the failure cases of VLAS and VLA on the customization benchmark to better identify the ... | p. 16 (Figure/Table caption), p. 10 (5 CONCLUSION) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 3.1 ARCHITECTURE OF VLAS Overall Framework VLAS takes human speech instructions s and visual observations O as input to directly generate robot actions a.를 VLAs, such as RT-2 (Brohan et al., 2023), which are fine-tuned from foundation VLMs like PaLM-E (Driess et al., 2023) using robotic trajectory data, can take human instructions and visual observations as ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 9: Demonstration of failure cases of VLA on the customization benchmark. We conducted additional analysis on the failure cases of VLAS and VLA on the customization benchmark to better identify the ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: To sum up, the main contributions of this work are listed as follows: 1) We propose VLAS, the first vision-language-action model that integrates speech for robot manipulation without needing external speech recognition ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `VLA, Vision-Language Model, Robotics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 9: Demonstration of failure cases of VLA on the customization benchmark. We conducted additional analysis on the failure cases of VLAS and VLA on the customization benchmark to better identify the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 4.3 EXPERIMENTS WITH A REAL-WORLD UR5 ROBOT ARM We fine-tune our VLAS-Base by utilizing both the Berkeley UR5 demonstration dataset and our own cup-picking dataset..
3. Compare against the body-reported baseline or a matched simpler baseline: Moreover, our VLAS is compared for speech modality input with the baseline VLA model and another powerful VLA model, Roboflamingo, both similarly derived from the VLM..
4. Report the body metric and its denominator/aggregation: Table 4: Performance comparison on LibriSpeech and SGQA benchmark, using word error rate (WER) and accuracy as evaluation metrics. LLaVA and BLIP-2 employ the ground truth textual insturctions on SGQA..
5. Re-run the body-reported ablation/failure condition: Both of the ablation studies above demonstrate the effectiveness of the Voice RAG module..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (3 METHOD), p. 3 (3 METHOD); the primary result is directionally consistent at p. 10 (Figure/Table caption), p. 8 (1. I have a blue), p. 9 (1. I have a blue); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 main, contributions, listed mechanism이 Moreover, our VLAS is compared for speech modality input with the baseline VLA model and another ... 대비 Table 4: Performance comparison on LibriSpeech and SGQA benchmark, using word error rate (WER) and accuracy as evaluation ...을 개선하고, Figure 9: Demonstration of failure cases of VLA on the customization benchmark. We conducted additional analysis ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
