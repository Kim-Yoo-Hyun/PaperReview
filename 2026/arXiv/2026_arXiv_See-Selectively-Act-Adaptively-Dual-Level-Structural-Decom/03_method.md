# Method — See Selectively, Act Adaptively: Dual-Level Structural Decomposition for Bimanual Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`

2026-11-20에 저자 본문 v2의 III–IV절을 확인했다. [논문 정보와 출처](./01_overview.md)

외부 영상 토큰, 언어·상태 토큰으로 두 손목 뷰의 가중치를 구한다. 별도 라우터는 협조 또는 독립 모드를 고른다. 협조 전문가는 전체 관측으로 14차원 명령을 생성한다. 단일 팔 전문가는 반대편 손목 뷰를 가리고 자기 팔의 7차원 출력만 담당한다. 세 전문가는 행동 백본을 공유하고 LoRA 어댑터를 따로 쓴다. [시각 라우터](https://arxiv.org/html/2606.13279v2#S3.SS2) · [행동 전문가](https://arxiv.org/html/2606.13279v2#S3.SS3)

작업별 시연의 10%에 프레임 단위 라벨을 붙이고, 양팔 말단과 그리퍼의 위치·속도 및 시간 문맥으로 나머지 라벨을 KNN 전파한다. Flow-matching 행동 손실에 라우터 지도 손실과 보조 전문가 손실을 더한다. 학습은 straight-through Gumbel-Softmax를 사용하고 추론은 선택한 모드를 한 행동 chunk 동안 유지한다. [학습과 전환 구간 처리](https://arxiv.org/html/2606.13279v2#S3.SS4)
