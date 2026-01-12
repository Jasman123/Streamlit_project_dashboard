import streamlit as st

pages = {
    "System Option": [
        st.Page("dashboard_1.py", title="Dashboard"),
        st.Page("app_input_data.py", title="Input your data")
        
    ]
}

pg = st.navigation(pages)
pg.run()

#create streamtlit shortcut
# cmd.exe /k "F:\python_project\.venv\Scripts\python.exe -m streamlit run F:\python_project\Stremlit_project_dashboard\app.py --server.headless true"
