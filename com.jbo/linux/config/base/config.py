# -*- coding: utf-8 -*-

import ConfigParser
#读取.ini类型的配置文价
cf = ConfigParser.ConfigParser(allow_no_value=True)
cf.read("config.ini")
cf.get("INSTALL_CONFIG", "user")
