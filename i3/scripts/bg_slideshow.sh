#!/bin/sh

MINUTES_TO_SLEEP=10

while true
do
    feh --randomize --bg-fill ~/Pictures/wallpapers/*
    sleep $(($MINUTES_TO_SLEEP*60))
done
