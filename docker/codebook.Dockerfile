## docker build --build-arg JHUB_VER=1.4.2 --build-arg PY_VER=3.8 --build-arg DIST=debian --build-arg DEPLOY_KEY=workflow-array-ephys-deploy.pem --build-arg REPO_OWNER=datajoint --build-arg REPO_NAME=workflow-array-ephys -f codebook.Dockerfile -t registry.vathes.com/datajoint/codebook-workflow-array-ephys:v0.0.0 .

## Single Stage 
ARG JHUB_VER
ARG PY_VER
ARG DIST
FROM datajoint/djlabhub:${JHUB_VER}-py${PY_VER}-${DIST}

USER root
RUN apt-get -y update && apt-get install -y ssh git

ARG DEPLOY_KEY
USER anaconda:anaconda
COPY --chown=anaconda $DEPLOY_KEY $HOME/.ssh/datajoint_deploy.ssh

ARG REPO_OWNER
ARG REPO_NAME
WORKDIR /tmp
RUN ssh-keyscan github.com >> $HOME/.ssh/known_hosts && \
    GIT_SSH_COMMAND="ssh -i $HOME/.ssh/datajoint_deploy.ssh" \
    git clone git@github.com:${REPO_OWNER}/${REPO_NAME}.git && \
    pip install ./${REPO_NAME} && \
    cp -r ./${REPO_NAME}/notebooks/ /home/ && \
    cp -r ./${REPO_NAME}/images/ /home/notebooks/ && \
    cp ./${REPO_NAME}/README.md /home/notebooks/ && \
    rm -rf /tmp/${REPO_NAME}
WORKDIR /home/notebooks
