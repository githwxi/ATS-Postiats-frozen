#
# A Simple Makefile
#

######

PATSCC=$(PATSHOME)/bin/patscc
PATSOPT=$(PATSHOME)/bin/patsopt

######

ATSCC2PY=$(PATSHOME)/bin/atscc2py3

######

all::
cleanall::

######

RMF=rm -f
RMRF=rm -rf
CPRF=cp -rf

######
#
all:: \
multable_dats.py
multable_dats.py: multable.dats ; \
$(PATSOPT) -d $< | $(ATSCC2PY) -o $@ -i
#
cleanall:: ; $(RMF) multable_dats.py
#
######
#
all:: \
QueenPuzzle_dats.py
QueenPuzzle_dats.py: QueenPuzzle.dats ; \
$(PATSOPT) -d $< | $(ATSCC2PY) -o $@ -i
#
cleanall:: ; $(RMF) QueenPuzzle_dats.py
#
######
#
all:: \
BUCS320/assign01_dats.py
BUCS320/assign01_dats.py: \
BUCS320/assign01.dats ; $(PATSOPT) -d $< | $(ATSCC2PY) -o $@ -i
#
cleanall:: ; $(RMF) BUCS320/assign01_dats.py
#
all:: \
BUCS320/assign02_dats.py
BUCS320/assign02_dats.py: \
BUCS320/assign02.dats ; $(PATSOPT) -d $< | $(ATSCC2PY) -o $@ -i
#
cleanall:: ; $(RMF) BUCS320/assign02_dats.py
#
######

testall:: all
testall:: cleanall

######

clean:: ; $(RMF) *~
clean:: ; $(RMF) *_?ats.c

######

cleanall:: clean
cleanall:: ; $(RMF) *_?ats.py

###### end of [Makefile] ######
