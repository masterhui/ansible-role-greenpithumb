#!/usr/bin/env python

import argparse
import time

import RPi.GPIO as GPIO


def main(args):
      
    try:
        # Setup
        GPIO.setmode(GPIO.BCM)

        while True:
            GPIO.setup(args.pin, GPIO.OUT)
            # Set to low
            GPIO.output(args.pin, False)

            # Sleep 2 micro-seconds
            time.sleep(0.000002)

            # Set high
            GPIO.output(args.pin, True)

            # Sleep 5 micro-seconds
            time.sleep(0.000005)

            # Set low
            GPIO.output(args.pin, False)

            # Set to input
            GPIO.setup(args.pin, GPIO.IN)

            # Count microseconds that SIG was high
            while GPIO.input(args.pin) == 0:
                starttime = time.time()

            while GPIO.input(args.pin) == 1:
                endtime = time.time()

            duration = endtime - starttime
            
            # The speed of sound is 340 m/s or 29 microseconds per centimeter.
            # The ping travels out and back, so to find the distance of the
            # object we take half of the distance travelled.
            # distance = duration / 29 / 2
            distance = duration * 34000 / 2
            print 'distance: %d cm' % distance
            time.sleep(0.5)

    finally:
      GPIO.cleanup()      


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='GreenPiThumb Sonar Sensor Diagnostic Test',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-p',
        '--pin',
        type=int,
        help='GPIO pin that is connected to the sonar sensor', default=20)
    main(parser.parse_args())
