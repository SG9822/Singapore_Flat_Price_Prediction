import folium
import streamlit as st
import pickle
import pandas as pd
from streamlit_folium import st_folium

def predictor():
    singapore_data = pd.read_parquet(
        r"C:\Users\DEVAHARINI.KR\GUVI_PROJECTS_NEW\Singapore  Resale Flat Prices Predicting\singapore_data.parquet")

    town_coords = {
        "Ang Mo Kio": (1.369115, 103.845436),
        "Bedok": (1.32639, 103.94167),
        "Bishan": (1.3508, 103.8353),
        "Bukit Batok": (1.3496, 103.7540),
        "Bukit Merah": (1.2820, 103.8185),
        "Bukit Timah": (1.3294, 103.8021),
        "Central Area": (1.2903, 103.8519),
        "Choa Chu Kang": (1.3854, 103.7440),
        "Clementi": (1.3151, 103.7643),
        "Geylang": (1.3181, 103.8830),
        "Hougang": (1.3718, 103.8931),
        "Jurong East": (1.3321, 103.7436),
        "Jurong West": (1.3503, 103.7228),
        "Kallang/Whampoa": (1.3138, 103.8602),
        "Marine Parade": (1.3022, 103.9020),
        "Queenstown": (1.2947, 103.7930),
        "Sengkang": (1.3917, 103.8944),
        "Serangoon": (1.3516, 103.8731),
        "Tampines": (1.3533, 103.9450),
        "Toa Payoh": (1.3344, 103.8510),
        "Woodlands": (1.4380, 103.7888),
        "Yishun": (1.4333, 103.8311),
        "Lim Chu Kang": (1.4167, 103.7000),
        "Sembawang": (1.4491, 103.8200),
        "Bukit Panjang": (1.3797, 103.7647),
        "Pasir Ris": (1.3731, 103.9496),
        "Punggol": (1.4053, 103.9021),
    }

    # Load model & encoders
    with open("random_forest_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("encoders.pkl", "rb") as f:
        data = pickle.load(f)
        encoders = data["encoders"]
        town_street_map = data["town_street_map"]

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.header("Singapore Flat Resale Price Predictor")
        # Collect user inputs
        year = st.number_input("Transaction Year", min_value=1990, max_value=2050, value=None)
        floor_area = st.number_input("Floor Area (sqm)", min_value=20, max_value=200, value=None)
        remaining_lease = st.number_input("Remaining Lease (years)", min_value=1, max_value=99, value=None)

        # Select Town first
        town = st.selectbox("Town", sorted(town_street_map.keys()), placeholder="Select or type to search Town",
                            index=None)

        if town:
            # Street Name depends on selected Town
            street_name = st.selectbox("Street Name", sorted(town_street_map[town]),
                                       placeholder="Select or type to search Street Name", index=None)

        flat_type = st.selectbox("Flat Type", encoders["flat_type"].classes_, placeholder="Select Flat Type",
                                 index=None)
        storey_range = st.selectbox("Storey Range", encoders["storey_range"].classes_,
                                    placeholder="Select Storey Range", index=None)
        flat_model = st.selectbox("Flat Model", encoders["flat_model"].classes_, placeholder="Select Flat Model",
                                  index=None)

        # Prepare encoded input
        input_data = {
            "year": year,
            "floor_area_sqm": floor_area,
            "remaining_lease": remaining_lease,
        }

        # Enable button only if everything is filled
        all_filled = (
                flat_type is not None and
                storey_range is not None and
                flat_model is not None and
                town is not None and
                street_name is not None and
                year and floor_area and remaining_lease
        )

        # Predict button
        col1, col2, col3 = st.columns([1, 1, 0.5])
        with col2:
            if st.button("Predict Price", disabled=not all_filled):
                # Encode categorical features
                for col, le in encoders.items():
                    if col == "town":
                        input_data[f"{col}_encoded"] = le.transform([town])[0]
                    elif col == "street_name":
                        input_data[f"{col}_encoded"] = le.transform([street_name])[0]
                    else:
                        input_data[f"{col}_encoded"] = le.transform([locals()[col]])[0]

                user_df = pd.DataFrame([input_data])

                prediction = model.predict(user_df)

                st.session_state.prediction = prediction[0]
                st.session_state.show_map = True

                # --- Display results if available ---
        if "prediction" in st.session_state and "show_map" in st.session_state:

            # --- Map first ---
            if town in town_coords:
                lat, lon = town_coords[town]

                town_data = singapore_data[singapore_data['town'] == town]
                n_properties = len(town_data)
                avg_price = town_data['resale_price'].mean()

                m = folium.Map(location=[lat, lon], zoom_start=12)  # smaller map

                popup_text = f"""
                            <b>{town}</b><br>
                            🏘 Properties: {n_properties:,}<br>
                            💰 Avg Price: SGD {avg_price:,.0f}
                            """
                folium.Marker(
                    location=[lat, lon],
                    popup=popup_text,
                    tooltip=popup_text,
                    icon=folium.Icon(color="red", icon="home")
                ).add_to(m)

                st.subheader(f"🏡 {town} Overview - 🏘 Properties & 💰 Avg Price")

                st_folium(m, width=800, height=350)  # smaller size ✅

            # --- Prediction text below map ---
            st.markdown(
                f"### Predicted Resale Price: **`SGD {st.session_state.prediction:,.0f}`**"
            )