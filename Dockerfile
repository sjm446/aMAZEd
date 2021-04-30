# set base image (host OS)
FROM python:2.7

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
#COPY requirements.txt .

# install dependencies
#RUN pip install -r requirements.txt
RUN pip install pygame
RUN pip install boto3

# copy the content of the local src directory to the working directory
ADD aMAZEd /code
ADD run.sh /code
ADD upload.py /code
 
RUN chmod a+x run.sh

# command to run on container start
#CMD [ "python", "/code/amazed.py","--algo","wilson","solution-grid","30","20","0","0","29","19" ]
CMD [ "/code/run.sh" ]
