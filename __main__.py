#!/usr/bin/python3

'''
Pi's brain
'''

#---------------------------------------------------------------
# APPLICATION ENVIRONMENT
#---------------------------------------------------------------
#
# You can load different configurations depending on your
# current environment. Setting the environment also influences
# things like logging and error reporting.
#
# This can be set to anything, but default usage is:
#
#     development
#     testing
#     production
#
# NOTE: If you change these, also change the error_reporting() code below
#/

ENVIRONMENT = 'development'

CORE = 'core'

_classes = {}

common = '{0}.Common'.format(CORE)
_classes['Common'] = __import__(common, fromlist=['*'])

_classes['Common'].init_var('ENVIRONMENT', ENVIRONMENT)
_classes['Common'].init_var('CORE', CORE)

BM = _classes['Common'].load_class('Benchmark', CORE)

BM.mark('total_execution_time_start')
BM.mark('loading_time:_base_classes_start')

BM.mark('loading_brain_controller_start')
brain = _classes['Common'].load_controller('Brain', bm=BM)
BM.mark('loading_brain_controller_end')
BM.mark('brain_initialization_start')
brain.init()
BM.mark('brain_initialization_end')