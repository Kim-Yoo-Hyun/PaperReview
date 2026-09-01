# Insights — Body Transformer: Leveraging Robot Embodiment for Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: `CURATION_ONLY`; 01_overview의 source audit와 기존 insight cue를 이관했다: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed. 자동 추출 결과는 수동 정독으로 간주하지 않는다.

## Paper-supported conclusion

> **Evidence boundary:** 현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다.

### What was actually new

- **Method cue:** Our contributions are listed below: • We propose the BoT architecture, which augments the transformer architecture with a novel masking that leverages the morphology of the robot body. ...
- **Problem cue:** Then, it applies a highly sparse mask at the attention layers, preventing each node from attending beyond its direct neighbors.
- **Claim/result cue:** We report results in the table shown in Figure 3a, where BoT consistently outperforms the MLP and transformer baselines.

### Strongest assumption and failure boundary

- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `observation → policy/control → feedback`.
- **Registry interface:** `Robotics, embodiment, graph neural network, policy learning` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated.
- **Prior interpretation carried forward:**
  - Object, relation, room/scene hierarchy를 graph로 구조화해 3D perception 결과를 robot planning과 language reasoning에 넘기는 중간 표현으로 사용할 수 있다.
  - 관계 중심 표현은 단일 object detection보다 task-relevant affordance, spatial relation, commonsense reasoning을 붙이기 쉽다.
- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.

### Dependency and evolution

- Registry position: `Robot Learning and Data`; tags: `Robotics, embodiment, graph neural network, policy learning`.
- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.
- Recorded scope boundary/future cue:
  - 논문이 도달한 지점: We report results in the table shown in Figure 3a, where BoT consistently outperforms the MLP and transformer baselines.
  - 논문 내 한계/논의 단서: We leave the extension of BoT to the temporal dimension as future work, as it promises to further improve real world deployment of robot policies, such as the ...
  - static scene graph 품질을 보인 뒤에도 dynamic updates, uncertainty, open-vocabulary relation grounding, robot action coupling은 별도 문제로 남는다.

### Minimal reproduction

- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**
  - 논문 내 evaluation 단서: 자동 추출에서 명확한 dataset 단서 없음 / mAP
  - 내 연구 확장 benchmark 후보: ScanNet, 3RScan, Matterport3D
  - 내 연구 확장 metric 후보: mIoU, Recall@K, relation accuracy, task success
  - 검증 초점: relation prediction, open-vocabulary grounding, downstream planning utility를 확인한다.
- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.

## Falsifiable research question

3D scene graph의 node/edge uncertainty를 planning cost나 action selection에 어떻게 반영할 수 있는가?

**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit.
