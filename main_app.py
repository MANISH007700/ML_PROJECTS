import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sb 
import matplotlib.pyplot as plt 


def main():
    st.title("Semi Automatic ML Model")
    st.write(" *--Built using StreamLit--* ")
    activities = ["EDA" , "PLOT", "ABOUT"]
    choice = st.sidebar.radio("Select Activity :" ,activities)
    

    if choice == "EDA":
        st.subheader("--Exploratory Data Analysis--")
        st.write(""" ## *Upload Dataset* ## """)
        dataset = st.file_uploader("" ,type = ["csv","txt","xls"])   
        
        if dataset is not None:
            df = pd.read_csv(dataset , delimiter = ",")
            st.dataframe(df)
            if st.checkbox("SHOW SHAPE"):
                st.write(df.shape)
            if st.checkbox("SHOW SIZE"):
                st.write(df.size)
            if st.checkbox("SHOW COLUMN "):
                st.write(df.columns)
            if st.checkbox("SELECT COLUMN NAME"):
                select_columns = st.multiselect("Select Column" , df.columns)
                new_df = df[select_columns]
                st.dataframe(new_df)
            if st.checkbox("SHOW MISSING VALUES"):
                st.write(df.isna().sum())
            if st.checkbox("SHOW VALUE COUNTS"):
                column = st.selectbox("Select Columns" , df.columns)
                st.write(df[column].value_counts())
            if st.checkbox("SHOW SUMMARY"):
                st.write(df.describe())


    elif choice == "PLOT":
        st.subheader("--Data Visualization--")
        st.write(""" ## *Upload Dataset* ## """)
        dataset = st.file_uploader("" ,type = ["csv","txt","xls"])
        
        if dataset is not None:
            df = pd.read_csv(dataset , delimiter = ",")
            st.dataframe(df)

            if st.checkbox("CORRELATION"):
                st.write(sb.heatmap(df.corr() , annot = True))
                st.pyplot()

            if st.checkbox("BAR GRAPH"):
                x_axis = st.selectbox("Select x axis:" , df.columns)
                x_axis = df[x_axis]
                y_axis = st.selectbox("Select y axis:" , df.columns)
                y_axis = df[y_axis]
                st.write(sb.barplot(x_axis , y_axis))
                st.pyplot()
                plt.xticks(rotation = 90)
                plt.legend()
                plt.grid()

            
            if st.checkbox("COUNT PLOT"):
                c = st.selectbox("Select  axis:" , df.columns)
                c_main = df[c]
                st.write(sb.countplot(c_main))
                st.pyplot()
                plt.grid()
                plt.xticks(rotation = 90)
                plt.legend()


            if st.checkbox("PIE CHART"):
                col = st.selectbox("Select 1 column" , df.columns)
                pie = df[col].value_counts().plot.pie(autopct = "%1.1f%%")
                st.write(pie)
                st.pyplot()

            
    else:
        st.subheader("--About Me--")
        st.write(''' ''')
        st.write(''' ***Built by MANISH SHARMA*** ''')
        st.write(''' ***Insta*** : https://www.instagram.com/data_quest_ ''')
        st.write(''' ***Linkedin*** : https://www.linkedin.com/in/manish-sharma-355ba3189/ ''')
        st.write(''' ***Github*** : https://github.com/MANISH007700 ''')
       
if __name__ == "__main__":
    main()
