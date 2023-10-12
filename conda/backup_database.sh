#!/bin/bash

# Note: This backup database script needs to be run as a user and not
# romeroroot as romeroroot cannot write to the rdrive


local_dir="/mnt/scratch/alphafold_db"
remote_dir="General/Sameer/full_alphafold_db"

function put_directory () {

smbclient -k //research.drive.wisc.edu/promero2 <<SMBCLIENTCOMMANDS
  prompt
  cd ${remote_dir}
  mkdir $1
  cd $1
  lcd ${local_dir}/$1
  mput *
  exit
SMBCLIENTCOMMANDS

}

function put_file () {

smbclient -k //research.drive.wisc.edu/promero2 <<SMBCLIENTCOMMANDS
  prompt
  cd ${remote_dir}
  lcd ${local_dir}
  mput $1
  exit
SMBCLIENTCOMMANDS

}

echo "Backing up BFD"
put_directory bfd

echo "Backing up mgnify"
put_directory mgnify

echo "Backing up params"
put_directory params

echo "Backing up pdb70"
put_directory pdb70

echo "tarring pdb_mmcif directory"
(cd $local_dir ; tar cf pdb_mmcif.tar pdb_mmcif)
(put_file pdb_mmcif.tar && rm -f ${local_dir}/pdb_mmcif.tar)

echo "Backing up pdb_seqres"
put_directory pdb_seqres

echo "Backing up small BFD"
put_directory small_bfd

echo "Backing up uniprot"
put_directory uniprot

echo "Backing up uniref30"
put_directory uniref30

echo "Backing up uniref90"
put_directory uniref90


