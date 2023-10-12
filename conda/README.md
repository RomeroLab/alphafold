## Running Alphafold2 on the GPU server

Version 2.3.2 of [Alphafold
2](https://github.com/RomeroLab/alphafold/tree/local_changes) has been
installed on the lab GPU server. It is mainly useful for multimers as there are
faster methods for monomers. These are instructions on how to use it. 

**NOTE: As the lab GPU server is a shared resource please only compute one
structure at a time**

### Before using this implementation

See if you can save time by using a different method of getting your structure.

* Download a structure from the [Alphafold Structure Database](https://alphafold.ebi.ac.uk/). This is the best option to get a structure and the database is huge!
* Use *Alphafold2 Colab* on [Google colab](https://colab.research.google.com/github/deepmind/alphafold/blob/main/notebooks/AlphaFold.ipynb). This is slightly simiplied and officially as good as the full version for monomers.
* Use *Colabfold* (an community version) of *Alphafold2 Colab* on Google colab. This has aslightly bigger database than the official Alphafold2 Colab and also has other structure prediction methods like `ESMFold`, `RosettaFold`, `OmegaFold` etc.
* Running Alphafold2 Colab on CHTC might be a decent alternative especially if you have lots of structures. An implementation and instructions are [linked here](https://github.com/RomeroLab/sameerd/tree/master/projects/protein_utils/chtc/alphafold)

### Before you start

You need to have logged into the GPU server before and setup your account. When
you currently login your bash prompt needs to start with `(base)` and sort of
look like `(base) dcosta2@ad.wisc.edu@biocsv-01704l ~]$`. If it looks
different, the instructions below will not work for you. 

## Running multimer example
1. Switch to the `alphafold` conda environment
   ```shell
   conda activate alphafold
   ```
   Your prompt should now change and start with `(alphafold)` instead of `(base)`
1. Make an output directory in your home directory or in your scratch directory
   and change to it.  
   ```shell
    mkdir ~/alphafold_output
    cd ~/alphafold_output
   ```
1. Create a FASTA file with multiple sequences. For a homodimer, we would just
   duplicate a single sequence twice. For example lets say it is called
   `multimer.fasta` and is in your home directory. 
1. Run alphafold multimer model
   ```shell
    python /home/romeroroot/alphafold/run_alphafold_conda.py \
    	--fasta_paths ~/multimer.fasta \
	--output_dir ~/alphafold_output \
	--model_preset multimer 2>&1 | tee ~/alphafold_output/log.txt
   ```
1. The program will first search the gigantic databases to create an MSA and
   also try to find templates for your sequences. (This takes around an hour
   for an 300aa sequence and mostly uses the CPU and hard disk). Then the
   predictions take around 1-2 minutes per structure. Alphafold multimer
   produces several structures and picks the best one for you and relaxes it
   with `openmm`. All in total, this probably takes another half hour. 
1. To go back to the base conda environment type
   ```shell
   conda deactivate
   ```
1. If you need more help look at the [README.md](../README.md) file in the
   parent directory to this one. 
