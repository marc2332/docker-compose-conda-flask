FROM continuumio/anaconda3

WORKDIR /db_server

COPY . /db_server

RUN conda create -n db_server

RUN conda install --yes --file requirements.txt --channel conda-forge -n db_server

CMD ["flask", "run", "--host", "0.0.0.0", "-p", "7000"]