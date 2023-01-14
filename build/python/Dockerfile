FROM python:3.10.7-slim-bullseye

RUN adduser --disabled-password --gecos '' user

USER user
WORKDIR /home/user/app

ENV PATH="/home/user/.local/bin:$PATH"
COPY --chown=user:user requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY --chown=user:user . .

RUN chmod +x build/scripts/*

CMD [ "sh", "build/scripts/run.sh" ]
