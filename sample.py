#!/usr/bin/env python
# -*- coding: utf-8 -*-

from GCMPush import GCMPush

idTest = "your android device registration id"
servKey = "your google server key from google console"

GCMPushService = GCMPush(servKey, True)

GCMPushService.push([idTest], "test title", "test message")
