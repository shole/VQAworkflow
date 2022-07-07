                          VQAtoAVI 2 version 1.36 by Tim Kosse
                          ------------------------------------

What is VQAtoAVI?
-----------------

VQAtoAVI was originally mentioned to convert the VQA movies of most Westwood games into playable AVI files. But until now, a lot of additional features have found its way into VQAtoAVI:
- a VQA player
- a mix viewer
- an AUDtoWAV converter
- an AUD player
- the ability to convert mix files into zip files. (Winzip compatible!)
- VQAtoAVI is a multi-language product. Currently it supports three languages: English, German and Spanish.


How does it work?
-----------------

The answer is quite simple. After starting the program you have select a file toload. You can select a .mix file or a .vqa file. If you have loaded a VQA file, click on 'Convert'. VQAtoAVI displays a lot of information during converttime. If you have selected a mix file, VQAtoAVI opens it and you may select the files you want to convert.
But you can also select "Play" for every VQA file. Then VQAtoAVI goes into fullscreen mode and plays the VQA file.
If you have selected an AUD file, VQAtoAVI opens a player window. You can fully control the playback.

Troubleshooting
---------------

If VQAtoAVI crashes if you open a mix file, the mixcache may be damaged. Please delete the file mixcache.dat. It will be recreated of VQAtoAVI later.


Known issues with this release
------------------------------

The error handling of VQAtoAVI is not perfect. But most times VQAtoAVI won't crash.


Contact-information
-------------------

VQAtoAVI was written by Tim Kosse.
E-Mail: TimKosse@planetcnc.com
Homepage: www.planetcnc.com/vqa


Copyright
---------

VQAtoAVI is freeware! Feel free to copy it. You are not allowed to modify the program in any way.


What's new?
-----------

1.36
----

- can now convert VQA files into PCX and WAV
- added an extra check for invalid VQA files
- fixed a VQADLL bug in CBasefile::set_subfile. The last nested file in
  a MIX file was always recognized as a nested MIX file and the whole
  parent MIX was processed on any operation on the nested file.
- some minor speed hacks

1.35
----

- can now convert mix files into zip files
- rewritten large parts of the user interface of the mix viewer
- new options dialog
- updated path selection
- fixed a bug that caused VQAtoAVI to crash when playing AUD files

1.34
----

- new AUD->WAV converter
- better integration of the AUD player

1.33
----

- added file format association
- added basic command line parsing

1.32
----

- tweaked VQA playback performance
- VQA player now double-buffered
- using beta 3 of the VQADLL interface library
- fixed adpcm decompression. Two values were not reset properly
- fixed some minor memory leaks
- added spanish translation

1.31
----

- fixed some problems with VQA playback
- changed mixcaching algorithm. Should no longer produce wrong filenames
- added support for language DLLs. VQAtoAVi currently supports two languages:
  English and German
- fixed some errors within the user interface
- added a little bit more error handling, VQAtoAVI no longer quits without any 
  error message if a VQA file is invalid
- VQA playback now multithreaded. Leads to better performance
- added an AUD player

1.3
---

- VQAtoAVI can now play VQA files
- updated format80decompression to work with some Land of Lore 2 VQAs

1.25
----

- exported all VQA an MIX interface classes into a DLL
- increased sorting speed in mixviewer
- added context menues in mixviever
- updated filetype detection routine of loading routiens

1.2
---

- now using the AVIFILE functions
- added support for AVI compression (you must have installed such codecs)

1.1b
----

- completed MIX support
- added mix cache
- little bug within sound decompression routines fixed

1.1
---

- Now supports the .mix files of every C&C version

1.01
----

- support for high quality sound VQAs
- highcolor detection routine fixed

1.0
---

- support for C&C:TS movies
- faster decompression
- experimantal mix support for C&C1


Old VQAtoAVI
1.4c
----

- Now fully supports VQAs without audio
- Now fully supports VQAs with uncompressed audio

1.4b
----

- Now creates Stereo AVIs
- internal performance tweaks of some functions

1.4a
----

- support for stereo VQAs. Only left channel in output files

Up to 1.4
---------

- now support of C&C:RA movies
- some feedback "EVA" sounds
- little updates


Special Thanks to:
------------------

Olaf van der Spek - technical information
Tobias Fildebrand - for testing every VQA on planet
The Heap - for the idea
Marcelo Volmaro - for the spanish translation