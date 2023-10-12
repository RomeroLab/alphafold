## Conda environment installation

Following instructions from
[kliniinalab](https://github.com/kalininalab/alphafold_non_docker) and making
small modifications


```shell
# Create alphafold conda environment as romeroroot
conda create --name alphafold python==3.8
conda update -n base conda

conda activate alphafold
mamba install -y -c conda-forge openmm==7.7.0 cudatoolkit==11.2.2 pdbfixer
mamba install -y -c bioconda hmmer hhsuite==3.3.0 kalign2


pip install absl-py==1.0.0 biopython==1.79 chex==0.0.7 dm-haiku==0.0.9 dm-tree==0.1.6 immutabledict==2.0.0 jax==0.3.25 ml-collections==0.1.0 numpy==1.21.6 pandas==1.3.4 protobuf==3.20.1 scipy==1.7.0 tensorflow-cpu==2.9.0

pip install --upgrade --no-cache-dir jax==0.3.25 jaxlib==0.3.25+cuda11.cudnn805 -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html

# no need to openmm patch as we are now using openmm=7.7.0 instead of 7.5.1

# reinstall version of  pdbfixer compatible with openmm
mamba install  -c conda-forge  pdbfixer=1.8 
```


## Download and backup parameters

```shell
# download data
scripts/download_all_data.sh /mnt/scratch/alphafold_db

cd /mnt/scratch/alphafold_db
chmod -R o+rw *
chmod -R g+rw *

# script to backup parameters to research drive
/mnt/scratch/alphafold_db/backup_database.sh
```


## Download code


```
git clone git@github.com:RomeroLab/alphafold.git

cd alphafold
wget -q -P alphafold/common/   https://git.scicore.unibas.ch/schwede/openstructure/-/raw/7102c63615b64735c4941278d92b554ec94415f8/modules/mol/alg/src/stereo_chemical_props.txt

```



