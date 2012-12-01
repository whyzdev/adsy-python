#!/usr/bin/python2
# coding: utf-8

"""IPython tools:

print_html     : Prints cursors, dicts and objects as html-tables.
toggle input   : Hide input-boxes from notebooks. Use this with nbconvert.
iterator tools : Filter None, swallow exception during iteration...
do_bisect_step : If used with simple scripts and areload() you can automatically biscect

"""

# Copyright (c) 2012, Adfinis SyGroup AG
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Adfinis SyGroup AG nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Adfinis SyGroup AG BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import subprocess
import sys

from adsy.iterator import *
from adsy.display import *

def areload():
	"""Enable autoreload. Might be buggy!"""
	get_ipython().magic('load_ext autoreload')
	get_ipython().magic('autoreload 2')

def do_bisect_step(state):
	"""Calls git bisect with the information from a test

	state: True: test was ok -> False: test failed"""
	str_state = 'bad'
	if state == True:
		str_state = 'good'
	proc = subprocess.Popen(
		 ['git', 'bisect', str_state],
		 stdout = subprocess.PIPE,
		 stderr = subprocess.PIPE,
		 stdin  = subprocess.PIPE
	)

	stdout, stderr = proc.communicate()
	returncode     = proc.wait()
	sys.stdout.write(stdout)
	sys.stderr.write(stderr)
	return returncode
