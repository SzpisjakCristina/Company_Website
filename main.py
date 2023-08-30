import streamlit as st
import pandas

# Set webpage layout to wide
st.set_page_config(layout="wide")

# Add a header and some other text
st.header("The Best Company")
st.write("""
At The Best Company, we transcend boundaries, setting new benchmarks across industries. With a relentless commitment to innovation, we're not just shaping the future,
we're defining it. Our foundation is built upon a fusion of expertise and passion. Each team member embodies excellence, propelling us toward remarkable achievements. 
Collaboration is our cornerstone, as we believe that diverse perspectives pave the way for groundbreaking solutions.

What sets us apart is our unyielding dedication to delivering unparalleled value to our clients. We understand that success is more than a destination; it's a continuous
journey of growth and improvement. Our cutting-edge solutions and customer-centric approach stand as testaments to our commitment. Beyond business, we're a community of 
like-minded individuals who share a common goal: to make a lasting impact. 

As we step into each new challenge, we're guided by our core values of integrity, innovation, and inclusivity. Welcome to The Best Company – where aspirations are nurtured,
potential is realized, and greatness is an everyday standard.""")
st.subheader("Our Team")

# Prepare the columns
col1, col2, col3 = st.columns([1.5, 1.5, 1.5])

# Make a dataframe with the company members
df = pandas.read_csv("data.csv")

# Add content to the first column
with col1:
    # Iterate over only the first four rows
    for index, row in df[:4].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])

# Add content to the second column
with col2:
    # Iterate over rows 4 to 7
    for index, row in df[4:8].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])

# Add content to the third column
with col3:
    # Iterate over the last 4 rows
    for index, row in df[8:].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])