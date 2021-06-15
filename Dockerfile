# set base image (host OS)
FROM python:2.7

# set the working directory in the container
WORKDIR /code

# install dependencies
RUN pip install pygame
RUN pip install boto3

# copy the content of the local src directory to the working directory
ADD * /code/
ADD run.sh /code
ADD upload.py /code
 
RUN chmod a+x run.sh

# command to run on container start
CMD [ "/code/run.sh" ]
