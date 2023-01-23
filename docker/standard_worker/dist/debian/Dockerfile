ARG PY_VER
ARG WORKER_BASE_HASH
FROM datajoint/djbase:py${PY_VER}-debian-${WORKER_BASE_HASH}

USER root
RUN apt update && \
    apt-get install -y ssh git vim nano

RUN pip install pyzmq==23.2.1

USER anaconda:anaconda

WORKDIR $HOME

RUN git clone --branch ccn2023 https://github.com/tdincer/workflow-calcium-imaging.git

RUN ./workflow-calcium-imaging/apt_requirements.txt /tmp/
RUN /entrypoint.sh echo "Installed dependencies."

RUN pip install Pygments
RUN pip install ./workflow-calcium-imaging

RUN git clone https://github.com/tdincer/CaImAn.git
RUN pip install numpy Cython
RUN pip install ./CaImAn

WORKDIR /main/workflow-calcium-imaging