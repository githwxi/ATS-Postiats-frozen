######
#
# A simple Makefile
#
######
#
PYTHON=python3
export \
PYTHONPATH=\
./../../../libatscc2py3/.
#
######
#
PATSCC=$(PATSHOME)/bin/patscc
PATSOPT=$(PATSHOME)/bin/patsopt
#
ATSCC2PY = $(PATSHOME)/bin/atscc2py3
#
######
#
all:: \
assign0_ex3_dats.py
#
assign0_ex3_dats.c: \
assign0_ex3.dats; $(PATSOPT) -o $@ -d $<
assign0_ex3_dats.py: \
assign0_ex3_dats.c; $(ATSCC2PY) -o $@ -i $<
#
cleanall:: ; $(RMF) assign0_ex3_dats.py
#
######
#
testall:: all
testall:: cleanall
#
######

RMF=rm -f

######
#
clean:: ; $(RMF) *~
clean:: ; $(RMF) *_?ats.c
#
cleanall:: clean
#
###### end of [Makefile] ######
