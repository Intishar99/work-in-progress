import streamlit as st
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth

# Function to process the uploaded file and generate frequent itemsets
def process_file(uploaded_file):
    # Read the uploaded file as a pandas DataFrame
    data = pd.read_csv(uploaded_file)

    # Specify your topic columns
    topic_columns = ['Motion - Homework', 'Units - Recap Quiz',
                     'Units and Prefixes - Grade 9 - Quiz', 'Measurements Homework ',
                     'Displacement - Construction ', 'Measurements - Cambridge Grade 9',
                     'Motion Equations and Graphs', 'Hookes Law - Graph',
                     'Motion Equations and Graphs - Exam', 'Moments - Worksheet',
                     'Forces and Moments - Cambridge', 'Thermal Physics Assignment',
                     'Sound and Electromagnetism', 'Static Electricity - Grade 10 Cambridge',
                     'Electrical Quantities Exam', 'Mock 1 - P4', 'Mock 2 - P4']

    # Your existing code for generating frequent itemsets
    data['Id'] = data['Id'].astype(str)
    transactional_data = []
    for index, row in data.iterrows():
        student_id = row['Id']
        for topic_column in topic_columns:
            topic = topic_column.replace('topic', '')
            mark = row[topic_column]
            if mark < 60:
                transactional_data.append((student_id, topic))

    transactional_df = pd.DataFrame(transactional_data, columns=['student_id', 'topic'])
    transactions = transactional_df.groupby('student_id')['topic'].apply(list).tolist()
    te = TransactionEncoder()
    te_ary = te.fit_transform(transactions)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    frequent_itemsets = fpgrowth(df, min_support=0.5, use_colnames=True)
    frequent_itemsets['itemsets'] = frequent_itemsets['itemsets'].apply(lambda x: ", ".join(x))
    frequent_itemsets_filtered = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: len(x.split(", ")) >= 2)]

    return frequent_itemsets_filtered

# Create Streamlit app
def main():
    st.title("Frequent Itemsets Generator")
    
    # File upload section
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Process the uploaded file and generate frequent itemsets
        frequent_itemsets = process_file(uploaded_file)
        
        # Display the frequent itemsets
        st.subheader("Frequent Itemsets")
        st.write(frequent_itemsets)

# Run the Streamlit app
if __name__ == "__main__":
    main()
