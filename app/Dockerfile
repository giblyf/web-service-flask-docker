FROM python: 3.11

WORKDIR / app

COPY . .

RUN pip install catboost
RUN pip install flask gunicorn flask_wtf
RUN pip install pandas
