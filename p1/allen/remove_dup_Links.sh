#!/bin/bash
awk '!seen[$0]++' links.txt
