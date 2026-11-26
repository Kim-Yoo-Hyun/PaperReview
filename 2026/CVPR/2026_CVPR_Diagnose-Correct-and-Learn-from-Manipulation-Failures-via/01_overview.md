# Diagnose, Correct, and Learn from Manipulation Failures via Visual Symbols

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-26 서지와 CVF 게재본 PDF 2–8쪽의 데이터·진단·표 4와 배포 자료 대조. Full-text scope의 수치·조건만 기록했다.

- Year/Venue: 2026 / CVPR
- Authors: Xianchao Zeng, Xinyu Zhou, Youcheng Li, Jiayou Shi, Tianle Li, Liangming Chen, Lei Ren, Yong-Lu Li
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: failure diagnosis, failure recovery, vision-language models, VLA, Dataset, Benchmark
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Zeng_Diagnose_Correct_and_Learn_from_Manipulation_Failures_via_Visual_Symbols_CVPR_2026_paper.html
- Code/Project: https://x1nyuzhou.github.io/vifailback.github.io/
- Code: https://github.com/x1nyuzhou/ViFailback

## 연구 질문과 기여

실제 로봇 조작에서 실패 장면을 찾더라도 어떻게 움직여야 복구되는지 표현하기 어렵다.

실제 로봇 궤적에 실패 구간과 화살표 등의 시각적 교정 지시를 붙인다. ViFailback-8B가 실패 진단과 교정 표식을 생성하고 이를 배포 정책의 입력으로 사용한다.

## 평가 범위

ViFailback-Bench의 닫힌·열린 질의 평가를 보고하고, 별도의 세 실물 과제에서 π0.5 조작 성공률을 비교했다(표 4). [원문 및 평가 절](https://openaccess.thecvf.com/content/CVPR2026/papers/Zeng_Diagnose_Correct_and_Learn_from_Manipulation_Failures_via_Visual_Symbols_CVPR_2026_paper.pdf#page=8)

## 선정 근거

실제 실패 데이터로 진단 정확도와 이후 제어 복구를 구분해서 비교할 수 있다.

## 공개 범위

- ViFailback-8B 가중치와 인덱스 파일이 공개 목록에 있다. [저자 배포 자료](https://huggingface.co/sii-rhos-ai/ViFailback-8B/tree/f5d2752a0168b413b8b674dc77eac02a5435e5a1)
- 실물 실패 VQA의 학습·평가 및 주석 프레임 파일 목록을 확인했다. [저자 배포 자료](https://huggingface.co/datasets/sii-rhos-ai/ViFailback-Dataset/tree/21df46c2585c52e5a62df5f4b946bae6cbc6fed7)
