FROM python

WORKDIR /myapp

COPY PyCode.py .

RUN pip install pymysql

RUN pip install cryptography

CMD ["python", "PyCode.py"]