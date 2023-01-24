FROM python:3.10

WORKDIR /opt
COPY bench.py /opt/

RUN pip install numba

CMD python bench.py