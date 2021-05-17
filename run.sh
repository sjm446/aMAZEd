#!/bin/bash
echo Generating Maze
python amazed.py --algo wilson solution-grid 10 20 0 0 9 19 > maze.txt
cat maze.txt
echo Uploading Maze to S3
echo EXPORT_S3_BUCKET_URL is set to $EXPORT_S3_BUCKET_URL
python upload.py
