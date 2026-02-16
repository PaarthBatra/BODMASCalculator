__author__ = 'pbatra'

from distutils.core import setup
import py2exe

setup(
windows=[{
    'script':'Calculator.py',
    'icon_resources':[(3,'profile_malaysia.ico')]
}])
excludes =  [ "mswsock.dll", "powrprof.dll" ]