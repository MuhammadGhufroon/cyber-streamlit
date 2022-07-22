import streamlit as st

class MultiPage:
    def _init_(self):
         def __init__(self):
            self.pages = []

    def add_web(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.pages.append({
            "title": title,
            "function": func
        })

    def run(self):
        # app = st.sidebar.radio(
        app = st.selectbox(
            'Navigation',
            self.pages,
            format_func=lambda app: app['title'])

        app['function']()
        
        
