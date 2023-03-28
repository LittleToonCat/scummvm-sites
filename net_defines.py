# ScummVM - Graphic Adventure Engine
#
# ScummVM is the legal property of its developers, whose names
# are too numerous to list here. Please refer to the COPYRIGHT
# file distributed with this source distribution.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Copied from engines/scumm/he/moonbase/net_defines.h

# These are used for relaying.
PN_PRIORITY_HIGH = 0x00000001
PN_SENDTYPE_INDIVIDUAL = 1
PN_SENDTYPE_GROUP = 2
PN_SENDTYPE_HOST = 3
PN_SENDTYPE_ALL = 4

# These are used for sanity checking.
PACKETTYPE_REMOTESTARTSCRIPT = 1
PACKETTYPE_REMOTESTARTSCRIPTRETURN = 2
PACKETTYPE_REMOTESTARTSCRIPTRESULT = 3
PACKETTYPE_REMOTESENDSCUMMARRAY = 4
