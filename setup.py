#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import textwrap


setup(
    name='logster',
    version='0.0.1',
    description='Parse log files, generate metrics for Graphite and Ganglia',
    author='Etsy',
    url='https://github.com/etsy/logster',
    packages=[
        'logster',
        'logster/parsers'
    ],
    zip_safe=False,
    scripts=[
        'bin/logster'
    ],
    license='GPL3',
    entry_points=textwrap.dedent("""
        [logster.parsers]
        ErrorLogLogster = logster.parsers.ErrorLogLogster:ErrorLogLogster
        Log4jLogster = logster.parsers.Log4jLogster:Log4jLogster
        MetricLogster = logster.parsers.MetricLogster:MetricLogster
        PostfixLogster = logster.parsers.PostfixLogster:PostfixLogster
        SampleLogster = logster.parsers.SampleLogster:SampleLogster
        SquidLogster = logster.parsers.SquidLogster:SquidLogster
    """),

)
