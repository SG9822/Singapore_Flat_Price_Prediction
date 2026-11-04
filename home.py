import streamlit as st
from PIL import Image

def home():
    st.subheader("About Project")

    singapore_images = [
        {
            "filename": "Singapore_1.jpg",
            "name": "Singapore Scenery 1",
            "description": "Beautiful Singapore cityscape and landmarks"
        },
        {
            "filename": "Singapore_2.jpg",
            "name": "Singapore Scenery 2",
            "description": "Stunning Singapore architecture and skyline"
        },
        {
            "filename": "Singapore_3.jpg",
            "name": "Singapore Scenery 3",
            "description": "Magnificent Singapore urban landscape"
        }
    ]

    if 'current_image' not in st.session_state:
        st.session_state.current_image = 0

    current = singapore_images[st.session_state.current_image]

    # if os.path.exists(current["filename"]):
    #     # Load and display the image
    image = Image.open(current["filename"])

    # Center the image beautifully
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image(image,
                 caption=f"{current['name']} - {current['description']}", width=600)

    col1, col2, col3 = st.columns([0.5, 3, 0.5])

    with col1:
        if st.button("⬅️ Previous", key="prev_btn"):
            # Move to previous image (loop back to last if at the beginning)
            st.session_state.current_image = (st.session_state.current_image - 1) % len(singapore_images)
            st.rerun()

    with col3:
        if st.button("Next ➡️", key="next_btn"):
            # Move to next image (loop back to 0 if at the end)
            st.session_state.current_image = (st.session_state.current_image + 1) % len(singapore_images)
            st.rerun()

    st.markdown(
        """
        <div style="background-color:#f9f9f9; padding:25px; border-radius:12px; margin-top:20px; box-shadow:0 2px 10px rgba(0,0,0,0.1);">
        <h2 style="text-align:center; color:#2c3e50;">🏙️ About the Singapore Flat Resale Price Predictor</h2>
        <hr style="border:1px solid #ddd;">

        <p style="font-size:16px; color:#333; line-height:1.6;">
        This project is designed to help users <b>understand and predict resale flat prices in Singapore</b>.  
        Using data from past HDB transactions, the model estimates resale prices based on several flat attributes 
        like <b>Town, Street, Flat Type, Storey Range, Floor Area, Flat Model</b> and more.
        </p>

        <h3 style="color:#16a085;">✨ Features</h3>
        <ul style="font-size:15px; line-height:1.7; color:#444;">
            <li>📊 <b>Data Insights:</b> Visualize historical average resale prices over the years, by town, flat type, storey range, or flat model.</li>
            <li>🤖 <b>Price Prediction:</b> Enter flat details and instantly get the <b>predicted resale price</b>.</li>
            <li>🗺️ <b>Interactive Map:</b> See the exact location of the selected town pinned on a Singapore map, with extra info like:
                <ul>
                    <li>🏘 Number of properties in that town</li>
                    <li>💰 Average resale price</li>
                </ul>
            </li>
            <li>📈 <b>Trends & Comparisons:</b> Analyze year-wise price changes, filter by multiple features, and explore market trends.</li>
        </ul>

        <h3 style="color:#2980b9;">🛠️ How to Use</h3>
        <ol style="font-size:15px; line-height:1.7; color:#444;">
            <li>➡️ Go to the <b>Price Predictor</b> section.</li>
            <li>➡️ Fill in the required details (Town, Street, Flat Type, Floor Area, Storey Range, Flat Model, etc.).</li>
            <li>➡️ Click <b>Predict Price</b> to view the resale value.</li>
            <li>➡️ Once predicted, an interactive <b>map</b> will appear showing the selected town and its statistics.</li>
            <li>➡️ Use the <b>Stats</b> section to view charts, trends, and comparisons of different flats over the years.</li>
        </ol>

        <h3 style="color:#8e44ad;">📌 Purpose</h3>
        <p style="font-size:16px; color:#333; line-height:1.6;">
        The aim of this project is to give <b>buyers, sellers, and property analysts</b> a simple yet powerful tool 
        to explore the Singapore HDB resale market. With accurate predictions and easy-to-read visualizations, 
        this app can support informed decision-making in real estate planning.
        </p>

        <hr style="border:1px solid #ddd;">
        <p style="text-align:center; font-size:14px; color:grey;">
        Built with ❤️ using <b>Python, Streamlit, Plotly & Folium</b>.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )
