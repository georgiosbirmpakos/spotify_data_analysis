# Spotify Data Analysis App

This Streamlit app enables users to analyze Spotify streaming data interactively. Users can upload their datasets and explore various insights through visualizations and metrics.

## Features

1. **Seasonal Popularity Analysis**
   - Visualize the total streams for each month from January to December.

2. **Audience Preferences**
   - Explore the average audience preferences based on attributes like danceability, energy, and more.

3. **Streaming Longevity**
   - Analyze the average longevity of tracks in weeks, grouped by genre and artist.

4. **Chart Placement Impact**
   - Understand how a track's chart position affects its average streams.

5. **Emerging Genres**
   - Identify emerging genres based on total streams.

6. **Top Artists**
   - View the top 10 artists by total streams.

7. **Genre Popularity**
   - Explore the popularity of genres using a pie chart of total streams.

## Requirements

- Python 3.8+
- Streamlit
- pandas
- seaborn
- matplotlib
- plotly
- openpyxl (for handling Excel files)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd spotify-data-analysis
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Upload your Spotify dataset in Excel format (e.g., `spotify.xlsx`).
2. The app will process and visualize the data, providing insights through:
   - Bar charts
   - Line plots
   - Pie charts
   - Scatter plots
3. Interact with the visualizations and gain insights.

## Dataset Requirements

- The dataset should be in Excel format.
- Required columns:
  - `date_release`: Release date of the track.
  - `Streams`: Total streams of the track.
  - `genre`: Genre of the track.
  - `artist_name`: Name of the artist.
  - Additional attributes for audience preferences (e.g., `acousticness`, `danceability`, `energy`, etc.).

