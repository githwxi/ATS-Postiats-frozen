#
# A Simple Makefile
#

######

CCOPT=gcc

######
#
PATSHOMEQ="$(PATSHOME)"
PATSCONTRIBQ=\
"$(PATSHOME)/npm-utils/contrib/atscntrb"
#
######

PATSCC=$(PATSHOMEQ)/bin/patscc
PATSOPT=$(PATSHOMEQ)/bin/patsopt

######

CFLAGS :=
CFLAGS +=-I$(PATSCONTRIBQ)
CFLAGS += $(shell xml2-config --cflags)

######

LDFLAGS :=
LDFLAGS += $(shell xml2-config --libs)

######

all::
regress::
cleanall::

######

all:: html2pats
html2pats: html2pats.dats; \
  $(PATSCC) -DATS_MEMALLOC_LIBC $(CFLAGS) -O2 -o $@ $< $(LDFLAGS) -latslib
regress:: html2pats; ./$<
cleanall:: ; $(RMF) html2pats

######

testall:: all
testall:: regress
testall:: cleanall

######

RMF=rm -f

######

clean:: ; $(RMF) *~
clean:: ; $(RMF) *_?ats.c
clean:: ; $(RMF) *_?ats.o

######

cleanall:: clean

######

###### end of [Makefile] ######
