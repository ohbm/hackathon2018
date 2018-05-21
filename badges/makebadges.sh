#!/bin/bash

mkdir -p badges

IFS=$'\r\n'
set -f

for line in $(cat < "$1");
do
    echo $line | cut -d ',' -f 1
    cp ohbm_brainhack_2018_badge_front_template.svg tmp.svg
    sed -i -e "s/{ParticipantName}/"`echo $line | cut -d ',' -f 1`"/g" tmp.svg
    sed -i -e "s/{Affiliation}/"`echo $line | cut -d ',' -f 2`", "`echo $line | cut -d ',' -f 3`"/g" tmp.svg
    sed -i -e "s/{PositionAtEvent}/"`echo $line | cut -d ',' -f 4`"/g" tmp.svg
    rsvg-convert -f pdf -o "badges/ohbm_brainhack_2018_badge_front_"`echo $line | cut -d ',' -f 1`".pdf" tmp.svg
done
