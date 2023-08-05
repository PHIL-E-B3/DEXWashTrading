import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

    
vol_df = pd.read_csv('vol_fees.csv')
vol_df['day'] = pd.to_datetime(vol_df['day'])
vol_df = vol_df.sort_values(by=['label', 'day'])

names = vol_df['label'].unique()

def create_protocol_dicts(df):
    # Create a dictionary for each protocol in the 'label' column
    protocols_data = {}
    for protocol in names:
        protocol_df = df[df['label'] == protocol]
        protocols_data[protocol] = protocol_df
    return protocols_data

prot_dict = create_protocol_dicts(vol_df)

#will return the Apollo protocol dictionary.
prot_dict["ApolloX"].head()


#streamlit

#Title and subtitle 
st.title("Dex Volume Wash Trading")
st.write("Volume per protocol: ")

#some streamlit stuff
st.write(prot_dict["ApolloX"].head())
st.table(prot_dict["ApolloX"].head())
ApolloX = prot_dict["ApolloX"]
st.line_chart(data=vol_df, x='day', y='volume', width=0, height=0, use_container_width=True)


names = vol_df['label'].unique()

#this will print uniquely all line charts 
for label in names:
    st.title(label)
    data_for_label = vol_df[vol_df['label'] == label]
    st.line_chart(data=data_for_label, x='day', y='volume', width=0, height=0, use_container_width=True)



# Sort data by date
data = vol_df.sort_values(by='day')

# Create a figure and an axis
fig, ax = plt.subplots(figsize=(20, 8))

plt.style.use('dark_background')  # Use a dark theme for the plot

# Use seaborn to plot a line for each protocol
sns.barplot(data=data, x='day', y='volume', hue='label', ax=ax)

# Set the title and labels
ax.set_title('Volume over Time for Different Protocols')
ax.set_xlabel('Date')
ax.set_ylabel('Volume')

# Use Streamlit to display the figure
st.pyplot(fig)



# Function to load and preprocess data
@st.cache
def load_data():
    # Load the CSV file
    data = pd.read_csv('vol_fees.csv')
    # Convert 'day' column to datetime
    data['day'] = pd.to_datetime(data['day'])
    # Pivot the data
    pivot_data = data.pivot_table(index='day', columns='label', values='volume', aggfunc='sum').fillna(0)
    return pivot_data


# Load the data
data = load_data()

# Title
st.title('Volume by Day for Different Protocols')

# Create the figure and axes
fig, ax = plt.subplots(figsize=(15, 8))

# Plot the stacked bar chart
data.plot(kind='bar', stacked=True, ax=ax)
plt.xlabel("Day")
plt.ylabel("Volume")
plt.title("Volume by Day for Different Protocols")
plt.xticks(rotation=45)

# Display the plot in the Streamlit app
st.pyplot(fig)

