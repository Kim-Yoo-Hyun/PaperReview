# Insights — HARMONIC: A multimodal dataset of assistive human–robot collaboration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-20 · IJRR 41(1), 3–11, 2022년 1월호. 온라인 선공개는 2021-12-07이다. 출판사 서지와 본문 §3–6, 공식 텍스트 배포 및 재생 코드를 확인했다.

## Paper-supported conclusion

Kinova Mico를 조이스틱으로 제어해 지정된 음식 위에 포크를 정렬한다. 직접 조작부터 자율 보조까지 네 조건에서 사용자 입력과 목표 추정에 따른 보조 명령을 다른 비중으로 결합한다. 입력 속도, 적용 속도, 관절 상태, 시선과 팔 근전도 등의 스트림을 시각과 함께 배포한다. [원문 및 평가 절](https://harplab.github.io/assets/pubs/newman2021_ijrr_harmonic.pdf#page=6)

## Researcher interpretation

시연자 요청과 적용 명령을 시각별로 분리할 수 있는 실제 공유 제어 데이터셋이다. 시연 재수집의 필요성과 원격조작 로그의 정보 손실을 판별할 때 조회한다.

## 최소 비교 실험

조이스틱 입력, 요청 및 적용 속도, 관절 상태를 한 보조 시행에서 정렬하고 상태만으로 추정한 요청과 기록된 요청의 차이를 확인한다.
