import os
from absl import flags

from run_alphafold import FLAGS, app, main

DEFAULT_DATA_DIR="/mnt/alphafold/alphafold_db"
MAX_TEMPLATE_DATE="2030-01-01"

def set_flag_if_none(name, value):
  if getattr(FLAGS, name) is None:
    setattr(FLAGS, name, value)

def set_default_conda_flags():
  set_flag_if_none("data_dir", DEFAULT_DATA_DIR)
  set_flag_if_none("max_template_date", MAX_TEMPLATE_DATE)

  # Path to the Uniref90 database for use by JackHMMER.
  set_flag_if_none("uniref90_database_path", os.path.join(
      FLAGS.data_dir, 'uniref90', 'uniref90.fasta'))

  # Path to the MGnify database for use by JackHMMER.
  set_flag_if_none("mgnify_database_path", os.path.join(
      FLAGS.data_dir, 'mgnify', 'mgy_clusters_2022_05.fa'))

  # Path to a directory with template mmCIF structures, each named <pdb_id>.cif.
  set_flag_if_none('template_mmcif_dir', os.path.join(
      FLAGS.data_dir, 'pdb_mmcif', 'mmcif_files'))

  # Path to a file mapping obsolete PDB IDs to their replacements.
  set_flag_if_none('obsolete_pdbs_path', os.path.join(
      FLAGS.data_dir, 'pdb_mmcif', 'obsolete.dat'))

  if FLAGS.model_preset == 'multimer':
    # Path to the Uniprot database for use by JackHMMER.
    set_flag_if_none("uniprot_database_path", os.path.join(
        FLAGS.data_dir, 'uniprot', 'uniprot.fasta'))

    # Path to the PDB seqres database for use by hmmsearch.
    set_flag_if_none('pdb_seqres_database_path', os.path.join(
        FLAGS.data_dir, 'pdb_seqres', 'pdb_seqres.txt'))
  else:
    # Path to the PDB70 database for use by HHsearch.
    set_flag_if_none('pdb70_database_path',  os.path.join(
        FLAGS.data_dir, 'pdb70', 'pdb70'))

  if FLAGS.db_preset == 'reduced_dbs':
    ## Path to the Small BFD database for use by JackHMMER.
    set_flag_if_none('small_bfd_database_path',  os.path.join(
        FLAGS.data_dir, 'small_bfd', 'bfd-first_non_consensus_sequences.fasta'))
  else:
    # Path to the Uniref30 database for use by HHblits.
    set_flag_if_none('uniref30_database_path', os.path.join(
        FLAGS.data_dir, 'uniref30', 'UniRef30_2021_03'))
    # Path to the BFD database for use by HHblits.
    set_flag_if_none("bfd_database_path", os.path.join(
        FLAGS.data_dir, 'bfd',
        'bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt'))

def main_conda(argv):
  set_default_conda_flags()
  main(argv)

if __name__ == "__main__":
  flags.mark_flags_as_required([
      'fasta_paths',
      'output_dir',
  ])
  app.run(main_conda)


