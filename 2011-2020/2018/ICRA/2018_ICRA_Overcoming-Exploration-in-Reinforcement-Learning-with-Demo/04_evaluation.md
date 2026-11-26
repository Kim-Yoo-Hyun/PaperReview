# Overcoming Exploration in Reinforcement Learning with Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Evaluated Setting and Evidence

저자들이 제시한 약 6시간은 pick-and-place 학습의 약 100만 시뮬레이션 스텝을 실물 상호작용 시간으로 환산한 값이다. 실험은 시뮬레이션 로봇 팔에서 했다. [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=4) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=7) · [PDF 8쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=8)

- **Evaluation type:** `EMPIRICAL / SIMULATION`.

## Comparison and Reproducibility Boundary

이전 검토에서 Q-filter 식 (8)을 확인했다. 데이터 분할, 전체 기준선의 계산 예산, 공개 구현의 현재 상태는 추가 확인이 필요하다.

근거: [지정 본문](https://arxiv.org/pdf/1709.10089) — Q-Filter subsection / Eq. 8; arXiv abstract and publisher-deposited metadata.

## Dataset / Benchmark Role

희소 보상 도달·물체 조작 과제와 블록 쌓기를 시뮬레이션에서 평가했다. [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=4) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=5)

## Baselines and Fairness

강화학습 단독과 행동 복제, 시연 상태 재시작·모방 손실을 바꾼 방법을 비교했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=8463162#page=7)

## Minimal Check — Researcher Proposal

연구자 제안: 같은 reference 행동·critic·데이터·loss 계수를 사용한 원리 수준 Q-filter와 무조건 모방을 분리하고, 원 논문 전체 알고리즘 재현 여부를 명시한다.

실행하지 않았다. 재개는 해당 연구의 local Docker 환경·입출력 확인 뒤에 한정하며 큰 학습을 자동 실행하지 않는다.
