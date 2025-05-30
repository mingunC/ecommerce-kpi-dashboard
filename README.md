# Fissler eCommerce KPI Dashboard
프로젝트 개요
Fissler Korea의 전자상거래 채널(네이버 브랜드 스토어, 오픈 마켓 등)을 위한 KPI 대시보드입니다. 가상의 판매 데이터를 분석해 매출, 전환율, 평균 주문 가치를 시각화하며, 마케팅 및 운영 전략을 지원합니다.
기술 스택

Python, Pandas, Streamlit, Plotly, SQLite

## 설치 방법

리포지토리 클론:git clone https://github.com/mingun-choi/ecommerce-kpi-dashboard.git


라이브러리 설치:pip install -r requirements.txt


앱 실행:streamlit run app.py

### 주요 기능

KPI 시각화: 총 매출, 전환율, 평균 주문 가치 표시.
분석: 시간별 매출 추이, 제품별/캠페인별 매출 시각화.
데이터 다운로드: CSV 다운로드 버튼으로 판매 데이터 접근.
적용 가능성: Fissler 제품(프라이팬, 압력솥 등) 데이터 분석 시뮬레이션.

### 결과물

매출 추이: 시간별 매출을 선 그래프로 표시.
제품별 매출: 파이 차트로 제품별 매출 비중 시각화.
캠페인별 매출: 막대 그래프로 마케팅 캠페인 성과 분석.

![Fissler eCommerce KPI Dashboard1](https://github.com/mingun-choi/ecommerce-kpi-dashboard/raw/main/assets/dashboard_screenshot1.png)
![Fissler eCommerce KPI Dashboard2](https://github.com/mingun-choi/ecommerce-kpi-dashboard/raw/main/assets/dashboard_screenshot2.png)

파일 구조

app.py: Streamlit 대시보드 메인 코드.
data/mock_data.csv: 모의 판매 데이터 샘플 (Fissler 제품 포함).
assets/dashboard_screenshot.png: 대시보드 스크린샷.

