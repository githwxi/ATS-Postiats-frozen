######
#
# A simple Makefile
#
######

PATSCC=$(PATSHOME)/bin/patscc
MYATSCC=$(PATSHOME)/bin/myatscc

######
#
all::
regress::
cleanall::
#
testall:: all
testall:: regress
testall:: cleanall
#
######

all:: \
dictSearch
dictSearch: ; \
$(MYATSCC) dictSearch.dats

######

clean:: ; rm -f *~
clean:: ; rm -f *_dats.c

######

cleanall:: clean
cleanall:: ; rm -f *_dats
cleanall:: ; rm -f *_dats.php

###### end of [Makefile] ######
