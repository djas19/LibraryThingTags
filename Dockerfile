FROM python:3-alpine
ADD run.py /
ADD requirements.txt /
RUN pip3 install -r /requirements.txt

ENV PYTHONUNBUFFERED=0
ENV PYTHONDONTWRITEBYTECODE 1
ENTRYPOINT ["python","-u","/run.py"]
#docker run --rm -v %cd%/example.txt:/input.txt library