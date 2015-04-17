import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "Program File: plugin.program.qualitychecker"
line2 = "Code: Python"
line3 = "Code Version: 0.0.1"
 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)
