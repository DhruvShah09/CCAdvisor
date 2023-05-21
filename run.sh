#!/bin/bash
nginx -t &&
service nginx start &&
cd project_contents &&
streamlit run main.py --server.enableWebsocketCompression=false