This system is modeled after clang-format.
This system works with clang-format configuration files.
The goal is to handle what CLion's Swift plugin provides, but
it is not possible.

1. Dump tokens to the file. Launch the process that does so through Python.
2. In Python, perform analysis.

The analysis is best described thru this presentation, by the deveopment team
behind clang-format: https://llvm.org/devmtg/2013-04/jasper-slides.pdf
