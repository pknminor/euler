def: run

PROB="default"

run:
	python prob_${PROB}.py | tee std

clean:
		\rm -rf *log std
