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
Alternatively, if you wish to deploy the application, there is a Dockerfile provided, along with NGINX conf files to route traffic to the correct port, however this is implementation specific and you may change it as per your needs. However, this requires moving all the non deployment relevant files into a seperate subdirectory titled `/project-contents` after which building the dockerfile renders an image capable of running on a containerized app deployment. It is important to note your application might have tobe configured differently based on the allowed traffic rules ofyour chosen proxy, otherwise you may see a `Please Wait...` screen, indicating the app is not correctly configured.


## App Images 

The app loads in a chat interface:
![Screen Shot 2023-05-21 at 1 11 50 PM](https://github.com/DhruvShah09/CCAdvisor/assets/90000344/fc50d73f-8c4e-4748-a798-f2df20276b76)

Response Loads: 
![Screen Shot 2023-05-21 at 1 12 08 PM](https://github.com/DhruvShah09/CCAdvisor/assets/90000344/5b575fc2-88fd-4f11-8563-21141af3300c)

Response From the Advisor Bot
![Screen Shot 2023-05-21 at 1 12 19 PM](https://github.com/DhruvShah09/CCAdvisor/assets/90000344/768b20b8-2d72-426a-b50c-3ea1bb0fc924)
