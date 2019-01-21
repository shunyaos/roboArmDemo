#!/usr/bin/env python3

import os
import sys
import time
import functools
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from uarm.wrapper import SwiftAPI
from uarm.utils.log import logger

logger.setLevel(logger.DEBUG)

swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})
# swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'}, enable_handle_thread=False)
# swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'}, enable_write_thread=True)
# swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'}, enable_report_thread=True)
# swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'}, enable_handle_thread=True, enable_write_thread=True, enable_report_thread=True)


swift.reset(speed=50000, wait=True)
swift.set_position(x=250, y=0, z=10, speed=50000,wait = True)
swift.flush_cmd()
swift.set_pump(True)
swift.set_position(x=250, y=0, z=170, speed=50000,wait = True)
swift.flush_cmd()
swift.set_position(x=220, y=70, z=170, speed=50000,wait = True)
swift.flush_cmd()
swift.set_position(x=200, y=140, z=170, speed=50000,wait = True)
swift.flush_cmd()
swift.set_position(x=180, y=210, z=170, speed=50000,wait = True)
swift.flush_cmd()
swift.set_position(x=250, y=210, z=10, speed=50000,wait = True)
swift.flush_cmd()
swift.set_pump(False)
swift.flush_cmd()
swift.set_position(x=250, y=210, z=120, speed=50000,wait = True)
swift.flush_cmd()
swift.reset(speed=50000, wait=True)
swift.flush_cmd()

