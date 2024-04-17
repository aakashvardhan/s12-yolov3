#!/bin/bash

# Set the path to your main data folder
data_folder="/Users/aakashvardhan/Library/CloudStorage/GoogleDrive-vardhan.aakash1@gmail.com/My Drive/ERA v2/s12-yolov3/data"

# Create the "images" and "labels" folders if they don't exist
mkdir -p "$data_folder/images"
mkdir -p "$data_folder/labels"

# Move .jpg files to the "images" folder
mv "$data_folder"/*.jpg "$data_folder/images/"

# Move .txt files to the "labels" folder
mv "$data_folder"/*.txt "$data_folder/labels/"

echo "Files organized successfully!"
