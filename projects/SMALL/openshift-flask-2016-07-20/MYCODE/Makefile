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

all:: \
hello_dats.py
hello_dats.py: hello.dats ; \
$(PATSOPT) -d $< | $(ATSCC2PY) -o $@ -i
hello:: \
hello_dats.py ; $(PYTHON) hello_dats.py
cleanall:: ; $(RMF) hello_dats.py

######

testall:: all
testall:: libatscc2py3
testall:: cleanall

######

clean:: ; $(RMF) *~
clean:: ; $(RMF) *_?ats.c

######

cleanall:: clean
cleanall:: ; $(RMF) *_?ats.py

###### end of [Makefile] ######
