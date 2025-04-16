import streamlit as st

# MBTI 유형에 대한 자세한 설명 및 장단점 딕셔너리
mbti_info = {
    'INTJ': {
        'description': '전략가: 독창적이고 효율적인 문제 해결을 추구합니다. 깊은 사고력과 분석력을 가지고 있으며, 목표를 달성하기 위한 철저한 계획을 세웁니다.',
        'strengths': '창의적이고 독립적이며, 문제 해결 능력이 뛰어납니다.',
        'weaknesses': '때로는 남을 이해하는 데 어려움을 겪고, 비판적일 수 있습니다.'
    },
    'INTP': {
        'description': '사고가: 이론적인 문제 해결을 좋아하며 심오한 사고를 합니다. 호기심이 많고, 새로운 아이디어와 관념을 탐구하는 것을 즐깁니다.',
        'strengths': '논리적 사고에 능하며, 혁신적이고 열린 마음을 가집니다.',
        'weaknesses': '감정 표현이 서툴고, 대인 관계에서 소극적일 수 있습니다.'
    },
    'ENTJ': {
        'description': '지도자: 목표 지향적이며 결단력이 뛰어난 리더 타입입니다. 강한 추진력과 리더십을 가지고 있습니다.',
        'strengths': '강력한 리더십과 기업가 정신을 발휘하며, 효율적인 문제 해결을 합니다.',
        'weaknesses': '다른 사람의 의견을 무시할 때가 있으며, 냉정하게 보일 수 있습니다.'
    },
    'ENTP': {
        'description': '발명가: 창의적이고 혁신적인 아이디어를 제시합니다. 논쟁과 토론을 즐기며, 새로운 가능성을 탐구하는 것을 좋아합니다.',
        'strengths': '창의력이 뛰어나고, 적응력이 뛰어난 혁신가입니다.',
        'weaknesses': '일관성을 잃고 쉽게 흥미를 잃을 수 있습니다.'
    },
    'INFJ': {
        'description': '옹호자: 깊은 통찰력과 공감 능력을 지닌 사람입니다. 타인의 감정에 민감하며, 이상과 가치에 따라 행동하려 합니다.',
        'strengths': '상대방을 깊이 이해하고, 뛰어난 통찰력을 발휘합니다.',
        'weaknesses': '자신의 감정을 잘 표현하지 않으며, 과도한 부담을 느낄 수 있습니다.'
    },
    'INFP': {
        'description': '중재자: 이상주의적이며 감정적으로 깊이 연결됩니다. 강한 개인적 가치와 신념을 가지고 있습니다.',
        'strengths': '높은 감수성과 창의성을 가지고 있으며, 헌신적입니다.',
        'weaknesses': '결단력이 부족하고, 현실적인 문제에 대한 회피 성향이 있을 수 있습니다.'
    },
    'ENFJ': {
        'description': '주도자: 타인을 이끄는 강한 리더십을 가지고 있습니다. 사람들을 이해하고 배려하며, 조화를 이루려는 노력을 합니다.',
        'strengths': '상대방과의 관계를 튼튼히 하고, 동기부여를 잘 합니다.',
        'weaknesses': '가끔 자신의 감정을 소홀히 할 수 있습니다.'
    },
    'ENFP': {
        'description': '활동가: 열정적이고 창의적인 사람입니다. 새로운 경험을 추구하며 다양한 사람들과의 상호 작용을 즐깁니다.',
        'strengths': '사람들에 대한 따뜻한 관심과 뛰어난 소통 능력을 가지고 있습니다.',
        'weaknesses': '산만할 수 있으며, 지속적이지 못할 수 있습니다.'
    },
    'ISTJ': {
        'description': '검사관: 책임감이 강하고 신뢰할 수 있는 성향입니다. 세부사항에 주의 깊고 규칙과 절차를 중시합니다.',
        'strengths': '신뢰성이 높고 체계적이며, 실용적인 결정을 잘 내립니다.',
        'weaknesses': '변화를 싫어하고, 지나치게 보수적일 수 있습니다.'
    },
    'ISFJ': {
        'description': '수호자: 세심하고 헌신적인 사람입니다. 전통과 가치를 중시하며, 타인을 도우려는 마음이 큽니다.',
        'strengths': '배려가 깊고, 팀의 안정성을 유지합니다.',
        'weaknesses': '자신의 필요를 간과하고, 필요 이상으로 부담을 느낄 수 있습니다.'
    },
    'ESTJ': {
        'description': '관리자: 실용적이고 조직적인 성향을 지닌 사람입니다. 효율성과 결과를 중시합니다.',
        'strengths': '조직적이며 결단력이 뛰어나고, 목표 달성을 위한 실행력이 강합니다.',
        'weaknesses': '타인에 대한 이해가 부족할 수 있으며, 권위적일 수 있습니다.'
    },
    'ESFJ': {
        'description': '제공자: 사교적이고 타인을 배려하는 성향입니다. 사람들과의 관계를 중요하게 생각합니다.',
        'strengths': '상대방의 요구를 잘 이해하고, 화합을 중시합니다.',
        'weaknesses': '자신의 필요를 무시하고, 과도한 책임감을 느낄 수 있습니다.'
    },
    'ISTP': {
        'description': '장인: 손재주가 뛰어나고 문제 해결에 실용적입니다. 즉흥적으로 행동하기를 좋아합니다.',
        'strengths': '기술적인 능력이 뛰어나고, 공격적인 문제 해결을 선호합니다.',
        'weaknesses': '감정 표현이 부족할 수 있으며, 사람들 사이에서 소외감을 느낄 수 있습니다.'
    },
    'ISFP': {
        'description': '예술가: 감수성이 풍부하고 미적 감각이 뛰어난 사람입니다. 자신의 감정을 표현하고, 아름다움을 중시합니다.',
        'strengths': '높은 창의성과 감정이입 능력을 가지고 있습니다.',
        'weaknesses': '결정을 내리기 어려워한다는 단점이 있습니다.'
    },
    'ESTP': {
        'description': '천재: 즉흥적이고 모험을 즐기는 성향입니다. 새로운 경험과 도전을 즐깁니다.',
        'strengths': '상황에 빠르게 적응하고, 문제를 즉각적으로 해결하는 능력이 있습니다.',
        'weaknesses': '계획성이 부족하고, 장기적인 목표를 소홀히 할 수 있습니다.'
    },
    'ESFP': {
        'description': '연예인: 사교적이고 활동적인 성향을 지닌 사람입니다. 사람들과의 상호작용을 즐깁니다.',
        'strengths': '주변 사람들에게 긍정적인 영향을 미치며, 즐거운 분위기를 만들 수 있습니다.',
        'weaknesses': '신중하지 못하고, 변화를 두려워할 수 있습니다.'
    }
}

def main():
    st.title("MBTI 유형 선택기")

    # MBTI 유형 선택
    mbti_type = st.selectbox("당신의 MBTI 유형을 선택하세요:", list(mbti_info.keys()))

    # 선택된 MBTI 유형에 대한 설명 표시
    if mbti_type:
        st.write(f"당신의 MBTI 유형은 **{mbti_type}**입니다.")
        st.write("**설명:**", mbti_info[mbti_type]['description'])
        st.write("**장점:**", mbti_info[mbti_type]['strengths'])
        st.write("**단점:**", mbti_info[mbti_type]['weaknesses'])

if __name__ == "__main__":
    main()

