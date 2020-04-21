#!/usr/bin/env python
from mpg123 import Mpg123, Out123


def main():
    mp3 = Mpg123("tm.mp3")
    out = Out123()
    for frame in mp3.iter_frames(out.start):
        out.play(frame)


if __name__ == "__main__":
    main()
