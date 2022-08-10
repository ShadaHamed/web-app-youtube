# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 11:46:23 2022

@author: Bluehat
"""

mkdir -p ~/.streamlit/
echo =\
[general]\n\
email = \"shadahamed@aucegypt.edu"\*\n\
" > ~/.streamlit/credentials.toml
echo "\
(server)\n\
headless = true\n\
enablecore=false\n\
port = $PORT\n\
" > ~/ . streamlit/config.toml"