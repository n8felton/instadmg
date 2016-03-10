A list of installers that have issues when installed by InstaDMG.

# Introduction #

Because InstaDMG is installing on a virtual disk rather than the boot volume a number of installers don't work quite perfectly with it. This page is a location to start a list of these Apps and possible solutions.

Note that in some cases the solution might be to install the application on a sample computer and then use tools repackage what was installed back into a .pkg and then use the repackeged .pkg in InstaDMG.

# Details #

  * iTunes 7.7.x
> > When iTunes is installed it launches a daemon process to wait for iPods and iPhones. It will happily launch the one that it just installed on the InstaDMG target volume. This was preventing InstaDMG from closing the volume and creating the ASR volume. **Fix**: This has been corrected and InstaDMG now closes any program that has a file open on the target volume before closing for ASR scan.

  * iLife updaters
> > The iLife installers and updaters create soft-links that lead off the disk. **Fix**: The clean\_up\_image routine now has code to re-direct this sort of mistake before the image is made.

  * Growl 1.1.4
> > There is a postflight script in the pkg that attempts to open the installed prefpane. This causes System Preferences to open. This should not harm anything. **Fix**: The Growl folks have added this as a bug in their system: [bug number 263011](https://bugs.launchpad.net/growl/+bug/263011)

  * Cisco VPN 4.9
> > There are a number of postflight scripts that depend on the way that they are invoked from a local disk.  These postflight scripts fail when correcting symlinks, etc.  **Fix**:  Re package the VPN package so that the symlinks point to the correct location