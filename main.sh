#!/bin/sh
cd foto
echo "Taking the Photo"
now=$1 #Now is the filename time stamp
#take pic
fswebcam -d /dev/video0 $now.jpg
echo "Pic Taken"
echo""
echo ""
echo ""
cd ..

