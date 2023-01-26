## docker build --build-arg JHUB_VER=1.4.2 --build-arg PY_VER=3.9 --build-arg DIST=debian --build-arg CODEBOOK_BASE_HASH=-f970993 --build-arg DEPLOY_KEY=wt-calcium-imaging-deploy.pem --build-arg REPO_OWNER=dj-sciops --build-arg REPO_NAME=worklow-calcium-imaging -f codebook.Dockerfile -t registry.vathes.com/sciops/codebook-ccn2023-calcium-imaging:v0.2.0 .

## Single Stage
ARG JHUB_VER
ARG PY_VER
ARG DIST
FROM datajoint/djlabhub:${JHUB_VER}-py${PY_VER}-${DIST}-f970993

RUN printf "git" >> /tmp/apt_requirements.txt && \
    /entrypoint.sh echo "installed"

USER root
RUN apt update && \
    apt-get install -y ssh git vim nano

RUN mkdir /home/user_data && \
    chown -R anaconda:anaconda /home/user_data && \
    chmod -R 775 /home/user_data
USER anaconda

WORKDIR /tmp

RUN git clone --branch ccn2023 https://github.com/tdincer/workflow-calcium-imaging.git
RUN cp ./workflow-calcium-imaging/apt_requirements.txt /tmp/
RUN /entrypoint.sh echo "Installed dependencies."
RUN pip install Pygments==2.14.0
RUN pip install ./workflow-calcium-imaging
RUN git clone https://github.com/tdincer/CaImAn.git
RUN pip install -r ./CaImAn/requirements.txt
RUN pip install ./CaImAn --use-feature=in-tree-build
RUN rm -rf /tmp/workflow-calcium-imaging
RUN rm -rf /tmp/CaImAn

WORKDIR /home
