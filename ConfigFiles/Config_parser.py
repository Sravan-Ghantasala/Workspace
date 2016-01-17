# -*- coding: ascii -*-
"""
*******************************************************************************************
 * Module                 : Config_parser.py
 * Author                 : Sravan K Ghantasala
 * Created Date           : 17-Jan-16
 * Description            : This script will parse the Config file and get the necessary
                            details to make the REST calls
 * Version                : 0.1
                   ** 0.1 : Initial commit
*******************************************************************************************
"""

# Imports
import configparser
import os

import requests

import Logger


class ParseConfig(object):
    """
    """

    def __init__(self):
        """Read the config file and parse the doc

        :return:
        """
        self.log = Logger.Log().my_logger
        config = configparser.ConfigParser()

        self.log.debug("Reading Config File")
        config.read("MainConfig.ini")

        self.JIRASite=config.get("JIRA_Site","SITE")
        self.username=config.get("JIRA_Site","USERNAME")
        self.password=config.get("JIRA_Site", "PASSWORD")
        self.log.debug("Credentials for JIRA site '{0}' identified".format(self.JIRASite))

        statuscode = self._test_connection()
        if statuscode:
            self.log.critical("Connection failed with status code : {0}".format(statuscode))
            raise ConnectionError("Bad URL or Bad Credentials. Unable to connect!")

        # For now set these in environmental variables
        os.environ["JIRA_SITE"] = self.JIRASite
        os.environ["username"] = self.username
        os.environ["password"] = self.password

        # TODO: Set credentials to cookies.

    def _test_connection(self, site = None, user=None, password=None):
        """Tests the connection for given site with the given credentials.

        :param site: JIRA site for which the connection needs to be tested.
        :param user: Username
        :param password: Password.
        :return: True if the connection is successful, False if not.
        """
        self.log.info("Testing Connection for JIRA site : {0}".format(self.JIRASite))
        request = requests.post(self.JIRASite, auth=(self.username, self.password),
                                headers = {'Content-Type' : 'application/json'})
        return 0 if request.status_code == 200 else request.status_code



if __name__ == "__main__":
    pc = ParseConfig()
