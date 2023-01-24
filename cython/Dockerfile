FROM python:3.11

WORKDIR /opt
COPY bench.py bench_ext.pyx setup.py /opt/

RUN pip install cython  \
 && python setup.py build_ext --inplace

CMD python bench.py