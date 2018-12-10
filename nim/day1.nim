import os
import strutils

var num = readFile("../input/day1.txt")

proc hello(name: string): string =
    echo("Hello", " ", name)

discard hello("Vivek")