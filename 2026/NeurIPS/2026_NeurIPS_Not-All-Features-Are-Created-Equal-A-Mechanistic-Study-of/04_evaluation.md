# Evaluation — Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-Supported Evaluation Scope

시뮬레이션 architecture 비교와 UR10e 실험을 보고한다. §4.7의 물체 이동 조건에서 주입 정책은 기록 좌표를 따르지만 non-injected 정책은 이동한 물체를 추적한다.

## Interpretation Boundary

하드웨어 결과는 한 모델·task pair에 제한된다. 좌표계 해석과 off-manifold 개입의 영향을 분리해야 한다. 모든 정상 VLA가 피드백을 무시한다는 증거가 아니다.

## Reproduction Status

이번 작업의 정책 실행·학습은 0회다. 위에서 명시하지 않은 dataset 크기·split·trial·hardware·metric·baseline 수치는 미기록이며 논문 자체의 미보고를 뜻하지 않는다. Resource 자동 연결은 cue_only다.

근거: [확인한 원문](https://arxiv.org/pdf/2603.19233v6), v6 (2026-11-02), §4.7–4.8, Appendix B.
