import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.title("Spotify Data Analysis")

# Upload the dataset
uploaded_file = st.file_uploader("Upload your Spotify Excel file", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Convert the date_release column to datetime, handling errors
    df['date_release'] = pd.to_datetime(df['date_release'], errors='coerce')
    df = df[df['date_release'].dt.year >= 2017]

    # Extract month from the release date
    df["release_month"] = df["date_release"].dt.month

    # Seasonal Popularity
    st.header("Seasonal Popularity Based on Streams")
    seasonal_popularity = df.groupby("release_month").agg({"Streams": "sum"}).sort_values(by="release_month")

    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.bar(seasonal_popularity.index, seasonal_popularity["Streams"], color='lightgreen')
    ax1.set_xticks(range(1, 13))
    ax1.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax1.set_title("Seasonal Popularity Based on Streams (billions)")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Total Streams")
    st.pyplot(fig1)

    # Audience Preferences
    st.header("Average Audience Preferences Based on Track Attributes")
    preferences_columns = ["acousticness", "danceability", "energy", "instrumentalness", "valence"]
    preferences_data = df[preferences_columns].mean().sort_values()

    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=preferences_data.values, y=preferences_data.index, palette="muted", ax=ax2)
    ax2.set_title("Average Audience Preferences")
    ax2.set_xlabel("Average Value")
    ax2.set_ylabel("Track Attributes")
    st.pyplot(fig2)

    # Streaming Longevity
    st.header("Average Streaming Longevity by Genre and Artist")
    df["start_week"] = pd.to_datetime(df["date_release"])
    df["end_week"] = pd.to_datetime(df["end_week"])
    df["longevity_weeks"] = (df["end_week"] - df["start_week"]).dt.days / 7

    streaming_longevity = df.groupby(["genre", "artist_name"]).agg({
        "Streams": "sum",
        "longevity_weeks": "mean"
    }).sort_values(by="longevity_weeks", ascending=False).head(10).reset_index()

    fig3, ax3 = plt.subplots(figsize=(12, 6))
    ax3.bar(streaming_longevity["genre"] + " - " + streaming_longevity["artist_name"],
            streaming_longevity["longevity_weeks"], color="coral")
    ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45, ha="right")
    ax3.set_title("Streaming Longevity by Genre and Artist")
    ax3.set_xlabel("Genre - Artist")
    ax3.set_ylabel("Average Longevity (Weeks)")
    st.pyplot(fig3)

    # Placement Impact
    st.header("Impact of Chart Position on Average Streams")
    placement_analysis = df.groupby("Position").agg({"Streams": "mean"}).sort_index()

    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(x=placement_analysis.index, y=placement_analysis["Streams"], mode='markers', name='Streams'))
    fig4.update_layout(title="Impact of Chart Position on Average Streams",
                       xaxis_title="Chart Position",
                       yaxis_title="Average Streams")
    st.plotly_chart(fig4)

    # Emerging Genres
    st.header("Exploring Emerging Genres")
    emerging_genres_analysis = df.groupby("genre").agg({"Streams": "sum"}).sort_values(by="Streams", ascending=True)

    fig5, ax5 = plt.subplots(figsize=(12, 6))
    ax5.barh(emerging_genres_analysis.index, emerging_genres_analysis["Streams"], color="lightblue")
    ax5.set_title("Emerging Genres Based on Total Streams")
    ax5.set_xlabel("Total Streams")
    ax5.set_ylabel("Genre")
    st.pyplot(fig5)

    # Top Artists
    st.header("Top Artists by Total Streams")
    top_artists = df.groupby("artist_name").agg({"Streams": "sum"}).sort_values(by="Streams", ascending=False).head(10)

    fig6, ax6 = plt.subplots(figsize=(10, 6))
    ax6.bar(top_artists.index, top_artists["Streams"], color="goldenrod")
    ax6.set_title("Top Artists by Total Streams")
    ax6.set_xlabel("Artist")
    ax6.set_ylabel("Total Streams")
    ax6.set_xticklabels(ax6.get_xticklabels(), rotation=45, ha="right")
    st.pyplot(fig6)

    # Genre Popularity
    st.header("Genre Popularity by Total Streams")
    genre_popularity = df.groupby("genre").agg({"Streams": "sum"}).sort_values(by="Streams", ascending=False)

    fig7 = px.pie(values=genre_popularity["Streams"], names=genre_popularity.index, title="Genre Popularity by Total Streams")
    st.plotly_chart(fig7)
