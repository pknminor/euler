def: run

# to run script in interpreter use the command, for example execfile('clear.py')


PROB="default"

run:
	python prob_${PROB}.py | tee std

run_51:
		/usr/bin/time python prob_51.py

clean:
		\rm -rf *log std
