FROM continuumio/anaconda3

WORKDIR /web_server

COPY . /web_server

RUN conda create -n web_server

RUN conda install --yes --file requirements.txt --channel conda-forge -n web_server

CMD ["flask", "run", "--host", "0.0.0.0"]