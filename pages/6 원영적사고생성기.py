import streamlit as st
import google.generativeai as genai

# 사이드바에서 API 키 입력 받기
st.sidebar.title("API 설정")
api_key = st.sidebar.text_input("Google Gemini API 키를 입력하세요", type="password")

# API 키가 입력되었는지 확인
if api_key:
    # API 키 설정
    genai.configure(api_key=api_key)

    # Streamlit 페이지 제목 설정
    st.title("원영적 사고 생성기")

    # 생성 설정
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # 모델 초기화
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # 사용자 입력 받기
    user_input = st.text_area("지난 일주일동안 기분이 좋지 않았던 경험을 적어주세요", 
                              "예: 버스를 눈앞에서 놓친 바람에 안타깝게 3분 지각해서 혼이 났어요")

    if st.button("럭키비키 생성"):
        # 인공지능 모델을 사용하여 상장 생성
        response = model.generate_content([
            "부정적인 내용보다는 긍정적인 내용을 강조하여 학생들이 기분이 좋아질 수 있게 위로해주는 말을 생성해주세요.",
            "예: 다음번엔 몇시에 나와야 할지 정확히 알게 되었어. 체계적으로 계획을 세울 수 있으니 럭키비키잖아"
            f"input: {user_input}",
        ])

        # 결과 출력
        st.subheader("생성된 럭키비키")
        st.write(response.text)
else:
    st.warning("API 키를 사이드바에 입력하세요.")
