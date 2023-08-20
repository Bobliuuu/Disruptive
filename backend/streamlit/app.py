import streamlit as st
import pandas as pd
import sqlite3 
import csv

tab1, tab2 = st.tabs(["View Companies", "Search Companies", "Semantic Search"])

def tab1():
    st.title("View Companies")

    # Path to the local CSV file
    file_path = "out.csv"

    try:
        original_df = pd.read_csv(file_path)
        filtered_df = original_df.copy()
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute('DROP TABLE companies')
        cur.execute('''CREATE TABLE companies (
            id INTEGER PRIMARY KEY,
            "name" TEXT NOT NULL,
            "domain" TEXT,
            "year founded" INTEGER,
            "industry" TEXT,
            "size range" TEXT,
            "locality" TEXT,
            "country" TEXT,
            "linkedin url" TEXT,
            "current employee estimate" INTEGER,
            "total employee estimate" INTEGER
        );''')
        original_df.to_sql('companies', conn, if_exists='append', index=False)
        # Sidebar - Dropdowns for sorting and filtering
        sort_by = st.sidebar.selectbox("Sort By", options=original_df.columns.to_list() + ['None'])
        filter_column = st.sidebar.selectbox("Filter Column", options=original_df.columns.to_list() + ['None'])
        filter_type = st.sidebar.selectbox("Filter Type", options=[">", "=", "<"])
        filter_value = st.sidebar.text_input("Filter Value")
        if st.sidebar.button('Reset'):
            filtered_df = original_df

        # Process data based on user input
        if filter_column and filter_value and filter_type == "=" and filter_column != "None":
            filtered_df = filtered_df[original_df[filter_column] == filter_value]
        elif filter_column and filter_value and filter_column != "None":
            #print(f"""SELECT * FROM companies WHERE "{filter_column}" {filter_type} {filter_value};""")
            if filter_column == "id" or filter_column == "name" or filter_column == "domain" or filter_column == "industry" or filter_column == "locality" or filter_column == "country":
                filtered_df = pd.read_sql_query(f"""SELECT * FROM companies WHERE {filter_column} {filter_type} {filter_value};""", conn)
            else: 
                filtered_df = pd.read_sql_query(f"""SELECT * FROM companies WHERE "{filter_column}" {filter_type} {filter_value};""", conn)
        if sort_by:
            filtered_df = filtered_df.sort_values(by=sort_by)

        # Display the filtered/sorted DataFrame
        st.dataframe(filtered_df)
        if st.button("Add a company"):
            js_code = """
            <script>
                window.open("http://localhost:3000", "_blank");
            </script>
            """
            st.components.v1.html(js_code, height=1)  # Placeholder for JavaScript
        
    except FileNotFoundError:
        st.write("File not found. Please provide a valid file path.")

def tab2():
    st.title('Search Companies')

def main():
    if tab1: 
        tab1()
    elif tab2:
        tab2()
    elif tab3:
        tab3()

if __name__ == "__main__":
    main()
