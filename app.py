import streamlit as st
import requests

# OMDb API Key (Replace 'YOUR_OMDB_API_KEY' with your actual API key)
OMDB_API_KEY = "b556cbe5"
OMDB_API_URL = "http://www.omdbapi.com/"

# Streamlit UI Enhancements
st.set_page_config(page_title="🎬 Movie Search App", layout="wide")# Custom CSS for an Attractive UI  
st.markdown("""  
    <style>  
        body {  
            background: linear-gradient(to right, #00203f, #e4e5e6);  /* Gradient from dark blue to light gray */  
            color: white;  
        }  
        .title {  
            text-align: center;  
            font-size: 40px;  
            font-weight: bold;  
            color: #ffcc00;  
            padding: 10px;  
        }  
        .description {  
            text-align: center;  
            font-size: 18px;  
            color: #dddddd;  
            margin-bottom: 20px;  
        }  
        .movie-card {  
            background: #1e1e1e;  /* Dark card background */  
            border-radius: 15px;  
            padding: 15px;  
            box-shadow: 4px 4px 15px rgba(255, 204, 0, 0.2);  
            transition: transform 0.3s, box-shadow 0.3s;  
        }  
        .movie-card:hover {  
            transform: scale(1.05);  
            box-shadow: 6px 6px 20px rgba(255, 204, 0, 0.4);  
        }  
        .btn {  
            background: linear-gradient(to right, #ffcc00, #ff9900);  
            color: black;  
            font-size: 18px;  
            padding: 12px 25px;  
            border-radius: 8px;  
            display: block;  
            margin: 20px auto;  
            text-align: center;  
            cursor: pointer;  
            transition: background 0.3s;  
            border: none;  
        }  
        .btn:hover {  
            background: linear-gradient(to right, #ff9900, #ffcc00);  
        }  
    </style>  
""", unsafe_allow_html=True)   
st.markdown("<h1 class='title'>🎬 Movie Search App</h1>", unsafe_allow_html=True)
st.markdown("<p class='description'>Search for your favorite movies using the OMDb API</p>", unsafe_allow_html=True)

# Search bar
query = st.text_input("Enter a movie title:")

if query:
    # Fetch data from the OMDb API
    response = requests.get(OMDB_API_URL, params={"s": query, "apikey": OMDB_API_KEY})
    
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            movies = data["Search"]
            
            # Display results in a grid format
            cols = st.columns(3)
            for index, movie in enumerate(movies):
                with cols[index % 3]:
                    st.markdown(f"<div class='movie-card'><img src='{movie['Poster']}' width='100%' style='border-radius:10px;'><h3 style='color:#ffcc00;'>{movie['Title']} ({movie['Year']})</h3></div>", unsafe_allow_html=True)
        else:
            st.error("No movies found. Try another search term.")
    else:
        st.error("Error fetching data. Please try again.")
