#!/usr/bin/python

__version__ = "$Revision: 84354 $"

import os, sys

import pathHelpers
from volumeManager		import dmgManager
from tempFolderManager	import tempFolderManager
from managedSubprocess	import managedSubprocess

if __name__ == '__main__':
	import optparse
	
	# ---- parse the input
	
	def print_version(option, opt, value, optionsParser):
		optionsParser.print_version()
		sys.exit(0)
	
	optionsParser = optparse.OptionParser("%prog [-m/--mount-point|-p/--parent-folder path_to_folder] path_to_image", version="%%prog %s" % __version__)
	optionsParser.remove_option('--version')
	optionsParser.add_option("-v", "--version", action="callback", callback=print_version, help="Print the version number and quit")
	
	optionsParser.add_option("-a", "--allow-other-mount", action="store_true", dest='allowOtherMount', default=False, help="Do not require the specified mount point if already mounted")
	optionsParser.add_option("-e", "--enable-paranoid-mode", action="store_true", dest='paranoidMode', default=False, help="Do not require the specified mount point if already mounted")
	
	optionsParser.add_option("-r", "--mount-read-only", action="store_false", dest='readWrite', default=False, help="Mount the image read-only [default]")
	optionsParser.add_option("-w", "--mount-read-write", action="store_true", dest='readWrite', help="Mount the image read/write")
	
	optionsParser.add_option("-m", "--mount-point", action="store", dest='mountPoint', default=None, help="Mount the image at this point")
	optionsParser.add_option("-p", "--parent-folder", action="store", dest='parentFolder', default=None, help="Mount at an autogenerated point in this folder")
	
	options, imageToMount = optionsParser.parse_args()
	
	# ---- police the input
	
	if len(imageToMount) != 1:
		optionsParser.error('One dmg, and only one dmg, is required')
	imageToMount = imageToMount[0]
	if not os.path.exists(imageToMount):
		optionsParser.error('There does not seem to be anything at the path provided: ' + imageToMount)
	elif not dmgManager.verifyIsDMG(imageToMount):
		optionsParser.error('The item at the provided path does not seem to be a valid dmg: ' + imageToMount)
	
	if options.mountPoint is None and options.parentFolder is None:
		optionsParser.error('One of either the -m/--mount-point or the -p/--parent-folder options are required')
	elif options.mountPoint is not None and options.parentFolder is not None:
		optionsParser.error('Only one of the -m/--mount-point or the -p/--parent-folder can be used at one time')
	elif options.mountPoint is not None:
		# mountPoint
		if not os.path.isdir(options.mountPoint):
			optionsParser.error('The path given to the -m/--mount-point option must be a folder, got: ' + options.mountPoint)
		elif os.path.ismount(options.mountPoint):
			optionsParser.error('The path given to the -m/--mount-point option must not be a mount point, got: ' + options.mountPoint)
		
		options.mountPoint = pathHelpers.normalizePath(options.mountPoint)
	else:
		# parent folder
		if not os.path.isdir(options.parentFolder):
			optionsParser.error('The path given to the -p/--parent-folder option must be a folder, got: ' + options.parentFolder)
		elif os.path.ismount(options.parentFolder):
			optionsParser.error('The path given to the -p/--parent-folder option must not be a mount point, got: ' + options.parentFolder)
		
		options.mountPoint = tempFolderManager.getNewMountPoint(parentFolder=options.parentFolder)
		tempFolderManager.removeManagedItem(options.mountPoint) # so it does not get cleaned back up immediately
	
	# ---- process
	
	currentMountPoints = dmgManager.getDMGMountPoints(imageToMount)
	if options.allowOtherMount is True and currentMountPoints is not None:
		sys.stdout.write(currentMountPoints[0])
		sys.exit(0)
	elif options.allowOtherMount is False and currentMountPoints is not None:
		sys.stderr.write('The image (%s) was already mounted at: %s\n' % (imageToMount, ", ".join(currentMountPoints)))
		sys.exit(1)
	
	actualMountPoint = dmgManager.mountImage(imageToMount, mountPoint=options.mountPoint, mountReadWrite=options.readWrite, shadowFile=None, paranoidMode=options.paranoidMode)
	
	if actualMountPoint != options.mountPoint:
		sys.stderr.write('The image was not mounted where expected! Was "%s", expected :%s"\n' % (actualMountPoint, options.mountPoint))
		sys.exit(1)
	
	sys.stdout.write(actualMountPoint)
	sys.exit(0)