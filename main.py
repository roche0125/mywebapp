import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(
    page_title="✈️ MBTI 감성 여행 코스 추천",
    page_icon="✈️",
    layout="centered"
)

# 힙하고 커스텀된 CSS 스타일 적용
st.markdown("""
    <style>
    /* 전체 배경 및 폰트 설정 */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Pretendard', sans-serif;
    }
    
    /* 타이틀 카드 스타일 */
    .main-title {
        text-align: center;
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }
    .main-title h1 {
        color: #2b5876;
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    /* 결과 카드 스타일 */
    .recommend-card {
        background: white;
        padding: 2rem;
        border-radius: 24px;
        box-shadow: 0 12px 30px rgba(43, 88, 118, 0.12);
        border: 2px solid #eef2f3;
        margin-top: 1.5rem;
    }
    .dest-title {
        color: #4e4376;
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .tag {
        display: inline-block;
        background: #e0c3fc;
        color: #4a00e0;
        padding: 4px 12px;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# MBTI별 힙하고 사랑스러운 여행지 데이터베이스
mbti_data = {
    "INTJ": {"dest": "아이슬란드 레이캬비크 🧊", "tag": "#오로라 #완벽한계획 #조용한자연", "desc": "철저하게 계획된 미지의 대자연 탐험! 붐비지 않고 광활한 풍경 속에서 깊은 생각을 정리하기 최적이야 💙"},
    "INTP": {"dest": "일본 교토 🍵", "tag": "#고즈넉 #아이디어샘솟음 #산책", "desc": "조용하고 감성적인 골목길을 거닐며 자율 여행하기 딱! 뜻밖의 아기자기한 카페를 발견하는 재미가 있어 💙"},
    "ENTJ": {"dest": "미국 뉴욕 🏙️", "tag": "#열정 #랜드마크 #트렌디", "desc": "화려함과 끊임없는 에너지가 넘치는 곳! 촘촘한 동선과 치열한 도시의 힙한 감성을 즐겨봐 💙"},
    "ENTP": {"dest": "인도네시아 발리 🏄‍♂️", "tag": "#자유로운영혼 #디지털노마드 #다채로운", "desc": "매일매일 새로운 이벤트와 서핑, 힙한 뷰티풀 비치 클럽이 기다리는 곳! 즉흥 여행의 정석 💙"},
    
    "INFJ": {"dest": "스위스 체르마트 🏔️", "tag": "#힐링 #자연속으로 #마음의평화", "desc": "동화 같은 풍경 속에서 진정한 자아를 찾는 시간. 따뜻하고 조용한 휴식이 필요한 너에게 추천해 💙"},
    "INFP": {"dest": "체코 프라하 🏰", "tag": "#낭만과감성 #동화속도시 #몽상가", "desc": "붉은 지붕과 돌담길을 걸으며 감성에 푹 빠져볼 수 있는 로맨틱한 스폿이야 💙"},
    "ENFJ": {"dest": "이탈리아 피렌체 🎨", "tag": "#예술 #따뜻한온기 #낭만가득", "desc": "아름다운 예술작품과 사람들의 온기가 넘쳐나는 낭만의 도시! 사랑하는 사람들과 추억 쌓기 좋아 💙"},
    "ENFP": {"dest": "스페인 바르셀로나 💃", "tag": "#정열 #컬러풀 #사랑스러움", "desc": "가우디의 알록달록한 건축과 흥겨운 축제 분위기! 너의 톡톡 튀는 발랄함과 어울리는 곳이야 💙"},
    
    "ISTJ": {"dest": "독일 뮌헨 🏰", "tag": "#정교함 #깔끔함 #역사와전통", "desc": "질서정연하고 정확하며 역사적인 깊이가 느껴지는 도시! 체계적인 여행의 참맛을 느껴봐 💙"},
    "ISFJ": {"dest": "오스트리아 비엔나 🎻", "tag": "#클래식 #안락함 #친절한도시", "desc": "부드러운 음악과 아늑한 카페 문화가 있는 따뜻한 곳. 마음 편히 편안한 쉼을 선사할게 💙"},
    "ESTJ": {"dest": "싱가포르 🇸🇬", "tag": "#스마트 #체계적 #세련됨", "desc": "완벽하게 가꿔진 도시 환경과 편리한 교통! 막힘없는 최고의 효율성 중심 코스를 즐길 수 있어 💙"},
    "ESFJ": {"dest": "프랑스 파리 🗼", "tag": "#미식과쇼핑 #함께하는즐거움 #감성샷", "desc": "맛있는 디저트와 인생샷 스폿이 한가득! 소중한 사람들과의 스윗한 추억을 만들어봐 💙"},
    
    "ISTP": {"dest": "뉴질랜드 퀸스타운 🪂", "tag": "#액티비티 #자연주의 #스릴", "desc": "번지점프부터 아웃도어 스포츠까지! 말보다 행동으로 체험하며 스트레스를 날려버리자 💙"},
    "ISFP": {"dest": "태국 치앙마이 🌿", "tag": "#느림의미학 #소소한행복 #힐링포토", "desc": "느긋하고 따뜻한 감성 속에서 아기자기한 소품숍을 구경하고 느긋하게 힐링하기 좋아 💙"},
    "ESTP": {"dest": "미국 라스베이거스 🎰", "tag": "#도파민폭발 #화려함 #즉興", "desc": "24시간 지루할 틈이 없는 화려한 불빛의 도시! 화끈한 쇼와 스릴이 넘쳐나는 곳이야 💙"},
    "ESFP": {"dest": "멕시코 칸쿤 🏖️", "tag": "#휴양지파티 #카리브해 #텐션업", "desc": "에메랄드빛 바다와 신나는 음악! 세상의 모든 흥을 발산할 수 있는 최고의 핫플레이스 💙"}
}

# 헤더 영역
st.markdown("""
    <div class="main-title">
        <h1>✈️ MBTI 감성 여행 코스 파인더</h1>
        <p style="color: #666; font-size: 0.95rem;">너의 성향에 딱 맞는 힙하고 사랑스러운 여행지를 찾아줄게 💙</p>
    </div>
""", unsafe_allow_html=True)

# Selectbox 레이아웃
mbti_list = list(mbti_data.keys())
selected_mbti = st.selectbox(
    "✨ 너의 MBTI를 선택해줘!",
    options=mbti_list,
    index=None,
    placeholder="MBTI 선택하기..."
)

# 결과 표시 logic
if selected_mbti:
    info = mbti_data[selected_mbti]
    tags = "".join([f'<span class="tag">{t}</span>' for t in info["tag"].split()])
    
    st.balloons() # 사랑스러운 팝업 효과
    
    st.markdown(f"""
        <div class="recommend-card">
            <p style="color: #ff6b6b; font-weight: bold; margin-bottom: 0px;">💖 {selected_mbti}만을 위한 추천 여행지</p>
            <div class="dest-title">{info['dest']}</div>
            <div style="margin-bottom: 12px;">{tags}</div>
            <hr style="border: 0.5px solid #eee; margin: 12px 0;">
            <p style="color: #444; line-height: 1.6;">{info['desc']}</p>
        </div>
    """, unsafe_allow_html=True)
