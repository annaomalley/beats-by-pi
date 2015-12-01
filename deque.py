#!/usr/bin/python
import subprocess

subprocess.Popen("sed -i -e 1,1d playlist.txt", shell=True)
