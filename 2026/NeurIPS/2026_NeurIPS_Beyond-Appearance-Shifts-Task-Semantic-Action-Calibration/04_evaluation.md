# Evaluation — Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-Supported Evaluation Scope

| 저자판 v2의 평가 조건 | 고정 정책 | BAS-VLA |
|---|---:|---:|
| 시뮬레이션, 네 가지 쉬운 물체 교체에서 새 목표 성공 | 18/800 (2.3%) | 548/800 (68.5%) |
| 같은 시행에서 옛 목표 실행 | 712/800 (89.0%) | 0/800 (0.0%) |
| 같은 시행에서 기타 결과·시간 초과 | 70/800 (8.8%) | 252/800 (31.5%) |
| 실제 로봇, 네 가지 목표·공간 관계 변경에서 새 목표 성공 | 51/320 (15.9%) | 166/320 (51.9%) |

시뮬레이션 표 7의 세 결과는 상호 배타적이다. 어려운 버터→크림치즈 교체에서는 보정 후에도 200회 중 113회 옛 목표를 실행했고 53회 새 목표에 성공했다. 실물 표 6은 조건별·방법별 80회의 새 목표 달성 여부를 측정했다. [표 6](https://arxiv.org/pdf/2609.23650v2#page=9) · [표 7](https://arxiv.org/pdf/2609.23650v2#page=10)

## Interpretation Boundary

표 5의 Break는 지시를 바꿔도 옛 목표를 달성한 비율이다. 새 목표 성공은 위 표 6·7에서 직접 확인할 수 있다. 부록 표 13은 목적지·공간 관계·하위 목표 순서를 바꾼 경우의 새 목표 성공도 보고했다. [표 5](https://arxiv.org/pdf/2609.23650v2#page=9) · [표 13](https://arxiv.org/pdf/2609.23650v2#page=15)

## Reproduction Status

이번 작업의 정책 실행·학습은 0회다. 위에서 명시하지 않은 dataset 크기·split·trial·hardware·metric·baseline 수치는 미기록이며 논문 자체의 미보고를 뜻하지 않는다. Resource 자동 연결은 cue_only다.

11월 5일 검토에는 첫 저자판을 사용했다. 위 수치와 쪽수는 11월 23일 대조한 저자판 v2 기준이다. [첫 검토 판본](https://arxiv.org/html/2609.23650v1) · [대조 판본](https://arxiv.org/pdf/2609.23650v2)
