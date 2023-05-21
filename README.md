# CCAdvisor

CCAdvisor is a weekend project aimed at allowing students to query Georgia Tech policies for the College of Computing to answer common advising queries without waiting for a response from an advisor! This application provides an interface to interact with textual data scraped from various college of computing websites and resources, as well as the relevant Georgia Institute of Technology pages. The content is then provided in a Chat interface, allowing students to submit queries in a natural question answer format. This repository includes the indexed ChromaDB embeddings.

To run the application, first it is important to provide an environment variable consisting of your OPEN AI API KEY in the following format `OPENAI_API_KEY=YOUR_KEY_HERE`. Then install the required dependencies using PIP.
```
pip install -r requirements.txt
```
At this point, there are two ways to run the application. Locally the application can be run using: 
```
streamlit run main.py
```
Alternatively, if you wish to deploy the application, there is a Dockerfile provided, along with NGINX conf files to route traffic to the correct port, however this is implementation specific and you may change it as per your needs. 
