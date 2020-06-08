PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PELICAN=/usr/bin/pelican

CONTENT=$(shell find content/ -name '*')

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

all: $(CONTENT) pelicanconf.py
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)
	rm -rf __pycache__/
	rm -rf plugins/__pycache__/

install:
	/usr/bin/apt install pelican markdown
	# sudo pacman -S pelican python-markdown

test:
	$(PELICAN) --autoreload --listen

.PHONY: all clean install test

