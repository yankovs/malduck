Malduck
=========

Malduck is your ducky companion in malware analysis journeys. It is mostly based on [Roach](https://github.com/hatching/roach) project, which derives many concepts from [mlib](https://github.com/mak/mlib) 
library created by [Maciej Kotowicz](mak@lokalhost.pl). The purpose of fork was to make Roach independent from [Cuckoo Sandbox](https://cuckoosandbox.org/) project, but still supporting its internal `procmem` format.

Malduck provides many improvements resulting from CERT.pl codebase, making scripts written for malware analysis purposes much shorter and more powerful. 

Improvements
============

* Many improvements in ProcessMemory
* Support for (non)memory-mapped PE images without header fix-up.
* Searching for wildcarded byte sequences
* Support for x64 disassembly
* Fixed-precision integer types
* Supported both Python 2.x and 3.x

Usage
==========

Installing may be performed by running

```
pip install malduck
```

Usage documentation can be found here: [docs]