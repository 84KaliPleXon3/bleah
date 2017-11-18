# This file is part of BLEAH.
#
# Copyleft 2017 Simone Margaritelli
# evilsocket@protonmail.com
# http://www.evilsocket.net
# Modded by @elkentaro to make it fit the HackChip Screen
# This file may be licensed under the terms of of the
# GNU General Public License Version 3 (the ``GPL'').
#
# Software distributed under the License is distributed
# on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
# express or implied. See the GPL for the specific language
# governing rights and limitations.
#
# You should have received a copy of the GPL along with this
# program. If not, go to http://www.gnu.org/licenses/gpl.html
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
import os
from bleah.version import VERSION

def effect(s,c,close=True):
    if os.getenv('c', '1') == 0:
        return s
    else:
        return "\033[%dm%s%s" % ( c, s, "\33[0m" if close else "" )

def red(s,close=True):
    return effect( s, 31, close )

def green(s,close=True):
    return effect( s, 32, close )

def yellow(s,close=True):
    return effect( s, 33, close )

def blue(s,close=True):
    return effect( s, 34, close )

def gray(s,close=True):
    return effect( s, 90, close )

def bold(s,close=True):
    return effect( s, 1, close )

def print_sexy_banner():
    banner = """
BLEAH v%s  for HACKCHIP
  +-+-+-+-+-+
  |B|L|E|A|H|
  +-+-+-+-+-+
          +-+
          |4|
          +-+
   +-+-+-+-+-+-+-+-+
   |H|a|c|k|C|h|i|p|
   +-+-+-+-+-+-+-+-+
"""

    print bold( blue( banner % VERSION ) )
    print blue("   Made with ") + red(u"\u2764") + blue(" by Simone 'evilsocket' Margaritelli") 
    print blue("   Modded by ") + green(u"\u2660") + blue(" elkentaro for HackChip") 
    print "\n\n"



