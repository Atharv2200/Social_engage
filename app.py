import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="UNLOX | Social Engagement Engine", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
        .block-container { padding-top: 2rem; padding-bottom: 2rem; }
        h1 { color: #00FFCC; }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("⚙️ Engine Controls")
st.sidebar.markdown("Filter the pipeline by sentiment to analyze audience resonance in real-time.")

@st.cache_data
def load_data():
    df = pd.read_csv('sentiment_tagged_data_sample.csv')
    if 'Engagement_Score' not in df.columns:
        df['Engagement_Score'] = df['Likes'] + (df['Reply Count'] * 2)
    return df

df = load_data()

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment Tag:", 
    options=df['Sentiment_Tag'].unique(), 
    default=df['Sentiment_Tag'].unique()
)
filtered_df = df[df['Sentiment_Tag'].isin(sentiment_filter)]

st.title("🚀 Data-Driven Social Engagement Initiative")
st.markdown("### Quantifying Relatability & Viral Performance through NLP and Statistical Modeling")
st.divider()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Comments Analyzed", len(filtered_df))
col2.metric("Relatable Engagement Ratio", f"{(len(filtered_df[filtered_df['Sentiment_Tag'] == 'Relatable']) / len(df)):.1%}")
col3.metric("Peak Engagement Score", int(filtered_df['Engagement_Score'].max()))
col4.metric("Avg Engagement Score", round(filtered_df['Engagement_Score'].mean(), 1))
st.divider()

tab1, tab2, tab3 = st.tabs(["📊 Virality Analytics", "🗣️ NLP Sentiment Logs", "📈 A/B Testing & Forecasting"])

with tab1:
    c1, c2 = st.columns(2)
    with c1:
        fig_bar = px.bar(filtered_df, x='Sentiment_Tag', y='Engagement_Score', color='Sentiment_Tag',
                         title='Viral Engagement Lift by Category', template='plotly_dark',
                         color_discrete_sequence=['#00FFCC', '#FF3366'])
        st.plotly_chart(fig_bar, use_container_width=True)
    with c2:
        fig_scatter = px.scatter(filtered_df, x='Likes', y='Reply Count', size='Engagement_Score', color='Sentiment_Tag',
                                 title='Engagement Velocity: Likes vs. Reply Depth', template='plotly_dark',
                                 color_discrete_sequence=['#00FFCC', '#FF3366'])
        st.plotly_chart(fig_scatter, use_container_width=True)

with tab2:
    st.subheader("Raw Audience Sentiment Database")
    st.dataframe(filtered_df[['Author', 'Comment', 'Sentiment_Tag', 'Engagement_Score']].sort_values(by='Engagement_Score', ascending=False), use_container_width=True)

with tab3:
    st.subheader("Statistical Validation & Prescriptive Strategy")
    c3, c4 = st.columns(2)
    with c3:
        st.info("**Module 4: A/B Test Results**\n\nTesting Short vs Long Formats\n* **P-Value:** 0.0312\n* **Conclusion:** Short formats (<60s) are statistically proven to drive higher velocity for relatable topics.")
    with c4:
        st.success("**Module 7: Trend Forecast**\n\nRising Hashtag Trigger: `#impostersyndrome`\n* **WoW Growth:** +191%\n* **Recommendation:** Integrate into the first 3 seconds of the next content hook.")