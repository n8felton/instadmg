# Introduction #

This is just a dump from the older roadmap. Things have jumbled a bit.

Strike shows the things that are in the current HEAD.

Ideas that have not made it onto the list quite yet are on the [Future Ideas](FutureIdeas.md) page.

# Details #

1.4
  * ~~Logging cleanup~~
  * ~~Language code variable~~
  * ~~ASR ﬁlesystem name variable~~
  * ~~Timestamp handler~~
  * _Preﬂight handler_ - not sure what this is, arguably handled by InstaUp2Date
  * ~~PPC image creation format ﬁxes~~
  * ~~Individual package InstallerChoices.xml support~~
  * ~~Caching of the base install~~
  * ~~getopts~~

1.5
  * ~~Logging changes~~
    * ~~More verbose debug log~~
    * ~~Tweaks in the console output~~
  * ~~Use chroot jails for non-OS installs~~
  * ~~Put a copy of the instal log inside the image~~
  * ~~Remove cruft from all temp areas~~ (more important with the chroot jail)
  * ~~Compatibility with 10.6 as a host and target OS~~

1.6
  * ~~Detect the OS on installer disks~~
  * ~~Handle multiple BaseOS disks (-I and -J flags)~~

2.0 (no promises, just a wish list)
  * Merge InstaUp2Date into InstaDMG (remove the folder system)
  * Cleanup resources, even in a crash (or user initialed stop)
  * Possibly allow for different chains based on the installer used
  * Rewrite of createUser (make it into a factory)
  * Provide drag-and-drop dmgs from OS disks
    * Evaluate merging items from second disk
  * Use sandboxing to isolate the host OS from any possible change
  * Evaluate a catalog of shadow files to correct installer defects
  * technique to handle installers that span multiple disks
    * Evaluate merging into one DMG
  * Move to Python
  * Handle installer failures (by stopping cold, with cleanup)
  * Improve logging even further
  * Evaluate merging catalog files with Munki
  * Save points along the build train (speed up minor changes)
  * Evaluate need for bad-softlink checking with chroot installs
  * Handle non pkg packages (possibilities include naked .apps and silent installer apps with Adobe Creative Suite a main target for the latter)

2.5
  * A GUI on top of the script (using Cocoa Bindings to bind directly to the same code)
  * Move to using Frameworks for installer and dmg handling, possibly through Obj-C objects