# See Selectively, Act Adaptively: Dual-Level Structural Decomposition for Bimanual Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`

- Year/Venue: 2026 / arXiv
- arXiv:2606.13279v2 · Yoon-Ji Choi, Young-Chae Son, Soo-Chul Lim. 저자 페이지의 표기는 심사 중이다. [arXiv](https://arxiv.org/abs/2606.13279) · [공저자 발표 목록](https://imyoungchae.github.io/)
- Primary track은 VLA and generalist robot policies다. 주요 주제는 양팔 조작, mixture of experts, 시연 학습이다.
- 2026-11-20에 본문 III–IV절, 표 I–II, 저자 프로젝트를 확인했다. 프로젝트에서 논문과 영상을 제공하며 정책 코드 링크는 확인되지 않았다. [저자 프로젝트](https://choiyoonji.github.io/See-Selectively-Act-Adaptively/)

π₀.₅가 한 물체를 두 팔로 다룰 때는 양팔 전문가를, 개별 동작이 필요한 단계에서는 두 단일 팔 전문가를 택한다. 별도 라우터가 각 손목 영상의 관련성을 정한다. 세 영상과 언어·로봇 상태로부터 14차원 명령을 50스텝씩 생성한다. 시연을 이용해 작업별로 학습했다. [방법](https://arxiv.org/html/2606.13279v2#S3)

RoboTwin 여섯 과제와 실물 세 과제에서 비교했다. 같은 π₀.₅를 쓰는 단일 경로, 시각 또는 행동 모듈 하나만 쓰는 경우, LoRA 용량을 키운 경우를 대조했다. 본 논문은 양팔 모드 선택을 연구할 때 이미 시연·단계 라벨로 해결한 범위를 알려 준다. [평가](./04_evaluation.md) · [후보 ②의 연구 질문](../../../work/research_topics/RESULTS.md#donor-retreat)
