# -*- coding: ascii -*-
"""
**************************************************************************************
 * Module      : Logger.py
 * Author      : Sravan K Ghantasala
 * Created on  : 17-jan-16
 * Description : This is a global module for logging various log levels to Log files.
 * version     : 0.1
        ** 0.1 : Initial document.
**************************************************************************************
"""

# Imports
import logging
import logging.handlers
import os

class Log(object):
    """

    """
    def __init__(self):
        if not os.path.exists( os.path.join(os.environ.get("PROJECT_DIR"), ".Logs")):
            os.mkdir(os.path.join(os.environ.get("PROJECT_DIR"), ".Logs"))
        self.LogFileName=os.path.join(os.environ.get("PROJECT_DIR"), ".Logs", "Log.log")
        # Set up a specific logger with our desired output level
        self.my_logger = logging.getLogger('MyLogger')
        self.my_logger.setLevel(logging.DEBUG)


        # Add the log message handler to the logger
        handler = logging.handlers.RotatingFileHandler(self.LogFileName, maxBytes=20*1024*1024, backupCount=5)
        formatter = logging.Formatter('[%(levelname)s] %(asctime)s (%(module)s : %(module)s) ==> %(message)s')
        handler.setFormatter(formatter)

        self.my_logger.addHandler(handler)

