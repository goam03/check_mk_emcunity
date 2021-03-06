#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.
group = 'datasource_programs'

register_rule(group,
    'special_agents:emcunity',
    Dictionary(
        elements = [
#            ( 'user',
#              TextAscii(
#                  title = _("Username"),
#                  allow_empty = False,
#              )
#            ),
#            ( 'password',
#              Password(
#                  title = _("Password"),
#                  allow_empty = False,
#              )
#            ),
            ("login",
                Alternative(
                    help = _("Choose between user/password or lockbox login"),
                    title = _("Authentication Method"),
#                    style = "dropdown",
                    elements = [
                        Tuple(
                            title = _("Use Following Credentials"),
                            elements = [
                                TextAscii(title = _("Username"), allow_empty = False),
                                Password(title = _("Password"), allow_epmty = False),
                            ]),
                        FixedValue( False, title = _("Use Credentials From:"), totext="Lockbox"),
                        ],
                    default_value = False
            )),
        ],
        optional_keys = False
    ),
    title = _("Check state of EMC Unity storage system"),
    help = _("This rule selects the Agent emcunity instead of the normal Check_MK Agent "
             "which collects the data through DELL's command line tool uemcli"),
    match = 'first')
