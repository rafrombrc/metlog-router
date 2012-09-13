#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# The Initial Developer of the Original Code is the Mozilla Foundation.
# Portions created by the Initial Developer are Copyright (C) 2012
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Rob Miller (rmiller@mozilla.com)
#
# ***** END LICENSE BLOCK *****
from metlogrouter.filters import SendToStdoutFilter
from metlogrouter.inputs import UdpInput
from metlogrouter.outputs import StreamOutput
from metlogrouter.runner import run
import sys


inputs = [UdpInput(5566)]
filters = [SendToStdoutFilter()]
outputs = [StreamOutput('stdout', sys.stdout)]
run(inputs=inputs, filters=filters, outputs=outputs)
