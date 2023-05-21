FROM python:3.10
USER root
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt install nginx -y
COPY requirements.txt requirements.txt
RUN pip3 install streamlit streamlit_chat python-dotenv langchain streamlit_extras openai chromadb
RUN mkdir /opt/advisor
WORKDIR /opt/advisor
COPY run.sh run.sh
COPY project_contents project_contents
COPY nginx.conf /etc/nginx/nginx.conf
RUN chmod a+x run.sh
CMD ["./run.sh"]