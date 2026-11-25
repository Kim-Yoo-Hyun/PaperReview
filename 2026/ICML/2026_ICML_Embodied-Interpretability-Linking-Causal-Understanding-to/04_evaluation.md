# Evaluation — Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. 아래에 인용한 원문 절·표의 평가 조건을 대조했다.

## 평가 조건

마스킹한 영상 영역이 행동 예측 오차에 미치는 영향을 ISS로 구한다. NMR은 과제와 무관하다고 분류한 영역에 귀속된 영향의 비율이다. [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26gz/zhang26gz.pdf#page=5)

AGNOSTOS에서 기존 과제 3,600개 에피소드로 π0.5를 SFT하고 새 과제 575개 에피소드에서 오프라인으로 평가했다. 비교 기준은 attention score와 token norm을 포함한다(§5). [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26gz/zhang26gz.pdf#page=6)

저자는 여러 행동이 타당할 때 하나의 참조 행동과의 오차가 행동 분포의 차이를 잘 대리하지 못할 수 있다고 밝혔다. [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhang26gz/zhang26gz.pdf#page=8)
