######
#
# A Simple Makefile
#
######

CAT=cat

######

MYATSCC=\
${PATSHOME}/bin/myatscc

######

all:: sieve_dats_all.js

######

sieve_dats.js: \
sieve.dats; $(MYATSCC) $<

sieve_dats_all.js: \
sieve_dats.js; \
$(CAT) libatscc2js_all.js sieve_dats.js > $@

######

clean:: ; rm -f *~
clean:: ; rm -f sieve_dats.js

######

cleanall:: clean
cleanall:: ; rm -f sieve_dats_all.js

###### end of [Makefile] ######

