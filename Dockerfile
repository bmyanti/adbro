FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV DEBUG=1
ENV SECRET_KEY=dbaa1_i7%*3r9-=z-+_mz4r-!qeed@(-a_r(g@k8jo8y3r27%m

WORKDIR /src

COPY requirements/local.txt ./
COPY requirements/base.txt ./

RUN pip install --no-cache-dir -r local.txt

COPY . .

EXPOSE 5555
EXPOSE 8000
EXPOSE 5672

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
