# Want to help? Send a mail to the dev list & mention that you've read this page #
# Legwork #

  1. Restore the BaseOScache file that you've created without installerchoices/choiceChanges per build(10.5.6, 10.6.3, 10.7.0 and newest Lion from the MacAppStore). Don't use DeployStudio for this, since it's difficult to suppress its firstboot cleanup scripts, just use asr at the command line or Disk Utility. This guarantees no packages will be added/workflows applied
  1. Boot and run the GUI Software Update application (from the Apple menu or /System/Library/CoreServices/Software Update.app) manually, installing all offered updates.
  1. Search/grep the install.log for the order in which the packages are applied(only 10.5 had a SoftwareUpdate log, but 'installed' is a good keyword to filter out all the unnecessary info)
  1. Repeat, rebooting as necessary, until gui swupdate returns no packages

# Putting it together #

Then, find the updates on support.apple.com/downloads, and jump to step three, below. In the case of Safari and iTunes,
  1. download from their respective pages
  1. right-click the entry in the downloads window and
  1. get the URL by choosing "Copy Address"). Checksum them (we recommend using the instadmg/AddOns/InstaUp2Date/checksum.py tool), and clean up the first field generated (the name), to make it more friendly/obvious.  Two other things of note:
  * leave out any updates that are hardware or accessory-specific, e.g. EFI/firmware/thunderbolt)  and
  * for iLife, collect updates with the same manual process described above on the most popular version of the OS (still Snow Leo as of this writing)

Feel free to post your results to the AFP548 forum, Twitter with #instadmg or #instaUp2Date hastags, or the instadmg-dev mailing list.

Keep in mind that updates should be allowed a 'cooling-off' period of at least 7 days, and ideally updated catalogs should be posted on the next Wednesday after that period.

Thanks!