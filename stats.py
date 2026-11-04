import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px


# singapore_data = pd.read_parquet(r"C:\Users\DEVAHARINI.KR\GUVI_PROJECTS_NEW\Singapore  Resale Flat Prices Predicting\singapore_data.parquet")


def stats():
    singapore_data = pd.read_parquet(
        r"C:\Users\DEVAHARINI.KR\GUVI_PROJECTS_NEW\Singapore  Resale Flat Prices Predicting\singapore_data.parquet")

    st.header("Hi all, welcome to stats tab")
    st.subheader("Number of Properties available per town")
    df1 = singapore_data.groupby('town').agg({'street_name': 'count'}).reset_index().rename(columns = {'street_name': 'Number of properties', 'town': 'Town'})
    st.write(px.bar(df1, x='Town', y='Number of properties', color='Town', text='Number of properties'))

    df3 = singapore_data.groupby(['town', 'flat_type']).size().reset_index(name='Number of properties')

    # Bar chart split by flat type
    fig = px.bar(
        df3,
        x="town",
        y="Number of properties",
        color="flat_type",
        barmode="stack",  # "stack" or "group"
        text="Number of properties"
    )

    st.subheader("Number of Flat types per town")
    st.plotly_chart(fig, use_container_width=True)

    town = st.selectbox("Select the town you want to see the basic stats", singapore_data['town'].unique())

    df2 = singapore_data[singapore_data["town"] == town].groupby('year')['resale_price'].mean().reset_index().rename(columns = {'resale_price': 'Average Resale Price'})
    fig = px.line(df2, x='year', y='Average Resale Price', markers=True, title= f'Average resale price of the flats of town `{town}` over the years')
    fig.update_traces(
        hovertemplate="Year - %{x}<br>Average Resale Price - %{y:,.0f}"
    )
    st.plotly_chart(fig, use_container_width=True)

    df_town = singapore_data[singapore_data['town'] == town]

    feature_dict = {
        'Flat Type': 'flat_type',
        'Storey Range': 'storey_range',
        'Flat Model': 'flat_model'
    }

    feature_select = st.selectbox('select any one for average price', list(feature_dict.keys()) + ["Combination"], index=None)
    if feature_select in feature_dict.keys():
        df = (
            df_town
            .groupby(['year', feature_dict[feature_select]])['resale_price']
            .mean()
            .reset_index()
            .rename(columns={
                'resale_price': 'Average Price',
                'year': 'Year',
                feature_dict[feature_select]: feature_select
            })
        )

        fig = px.line(
            df,
            x="Year",
            y="Average Price",
            color=feature_select,
            markers=True,
            title=f"Year-wise Avg Price in {town} for {feature_select}"
        )
        fig.update_traces(
            hovertemplate="Year=%{x}<br>Average Resale Price=%{y:,.0f}"
        )
        st.plotly_chart(fig, use_container_width=True)

    elif feature_select == 'Combination':
        st.write("Please Select all the features")
        col1, col2, col3 = st.columns(3)

        with col1:
            flat_type = st.selectbox("Select the flat type", df_town['flat_type'].unique(), index=None)

        with col2:
            data = df_town[df_town['flat_type'] == flat_type]
            storey_range = st.selectbox("Select the storey range", sorted(data['storey_range'].unique()), index=None)

        with col3:
            data = df_town[
                (df_town['flat_type'] == flat_type) &
                (df_town['storey_range'] == storey_range)
                ]
            flat_model = st.selectbox("Select the flat model", sorted(data['flat_model'].unique()), index=None)

        # --- Count how many filters are selected ---
        selected_features = [flat_type, storey_range, flat_model]
        selected_count = sum(f is not None for f in selected_features)

        # --- Enable button only if exactly 2 are selected ---
        if st.button("Avg Price", disabled=(selected_count != 3)):


            # --- 3 filters together ---
            if flat_type and storey_range and flat_model:
                df4 = (
                    singapore_data[
                        (singapore_data['town'] == town) &
                        (singapore_data['flat_type'] == flat_type) &
                        (singapore_data['storey_range'] == storey_range) &
                        (singapore_data['flat_model'] == flat_model)
                        ]
                    .groupby('year')['resale_price']
                    .mean()
                    .reset_index()
                    .rename(columns={'resale_price': 'Average Price', 'year': 'Year'})
                )

                fig = px.line(
                    df4,
                    x="Year",
                    y="Average Price",
                    markers=True,
                    title=f"📊 Year-wise Avg Price in {town} for {flat_type}, {storey_range}, {flat_model}"
                )

                # Update line & marker style
                fig.update_traces(
                    line=dict(color="darkorange", width=4, dash="solid"),
                    marker=dict(size=10, color="blue", symbol="circle", line=dict(width=1, color="black")),
                    hovertemplate="📅 Year: %{x}<br>💰 Avg Price: SGD %{y:,.0f}"
                )

                # Layout styling
                fig.update_layout(
                    title=dict(
                        x=0,  # Centered
                        font=dict(size=24, color="darkblue", family="Arial Black")
                    ),
                    xaxis=dict(
                        showgrid=True,
                        gridcolor="lightgrey",
                        title=dict(
                            text="Year",
                            font=dict(size=16, color="black"))

                        ),
                    yaxis=dict(
                        showgrid=True,
                        gridcolor="lightgrey",
                        title=dict(
                            text="Average Resale Price (SGD)",
                            font=dict(size=16, color="black")
                        )
                    ),
                    plot_bgcolor="white",  # clean background
                    hoverlabel=dict(bgcolor="white", font_size=14, font_family="Arial")
                )

                st.plotly_chart(fig, use_container_width=True)