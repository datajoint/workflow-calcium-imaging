FROM mcr.microsoft.com/devcontainers/python:3.7-bullseye

ENV GITHUB_USER datajoint
ENV ELEMENT calcium-imaging

RUN \
    echo "Install DataJoint ----------" && \
    apt update && \
    apt-get install bash-completion graphviz default-mysql-client s3fs procps gcc -y && \
    pip install --upgrade pip && \
    pip install flake8 black faker ipykernel pre-commit datajoint

RUN \     
    echo "Install DataJoint Elements ----------" && \
    for f in lab animal session event interface $ELEMENT; do \
        git clone https://github.com/${GITHUB_USER}/element-${f} /workspaces/element-${f} && \
        pip install -e /workspaces/element-${f};
    done;

RUN \  
    echo "Install CaImAn ----------" && \
    pip install Pygments==2.14.0  && \
    git clone https://github.com/datajoint/CaImAn.git  && \
    pip install -r ./CaImAn/requirements.txt  && \
    pip install ./CaImAn && \
    rm -rf /tmp/CaImAn;

ENV DJ_HOST fakeservices.datajoint.io
ENV DJ_USER root
ENV DJ_PASS simple
