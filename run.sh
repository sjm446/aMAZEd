#!/bin/bash
echo Generating Maze
python amazed.py --algo wilson solution-grid 10 20 0 0 9 19 > maze.txt
cat maze.txt
echo Uploading Maze to S3
echo AWS_S3_BUCKET is set to $AWS_S3_BUCKET
python upload.py
