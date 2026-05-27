text = "data:\n\
  resource: ((target))\n\
  type: intake\n\
  input_col: SMILES\n\
  target_cols:\n\
    - ((target))\n\
  dropna: true\n\
metadata:\n\
  authors: Devany West\n\
  email: devany.west@omsf.io\n\
  biotargets:\n\
    - ((target))\n\
  build_number: 0\n\
  description: predicting ((target)) with ((model_name)) model\n\
  driver: pytorch\n\
  name: ((model_name))\n\
  tag: openadmet\n\
  tags:\n\
    - ((target))\n\
  version: v1\n\
procedure:\n\
  feat:\n\
    type: ChemPropFeaturizer\n\
    params:\n\
      batch_size: 128\n\
      normalize_targets: true\n\
      n_jobs: 4\n\
  model:\n\
    type: ChemPropModel\n\
    params:\n\
      batch_size: 128\n\
      normalize_targets: true\n\
      n_jobs: 4\n\
      ffn_hidden_dim: 512\n\
      ffn_hidden_num_layers: 3\n\
      mpnn_lr: 1e-4\n\
      ffn_lr: 1e-3\n\
      mpnn_weight_decay: 0\n\
      ffn_weight_decay: 1e-4\n\
      dropout: 0.25\n\
      batch_norm: False\n\
      scheduler: plateau\n\
      reduce_lr_patience: 5\n\
      reduce_lr_factor: 0.5\n\
      n_tasks: 1\n\
      from_foundation: ((from_foundation))\n\
  split:\n\
    type: ShuffleSplitter\n\
    params:\n\
      random_state: 42\n\
      train_size: 0.9\n\
      val_size: 0.1\n\
      test_size: 0.0\n\
  train:\n\
    type: LightningTrainer\n\
    params:\n\
      accelerator: gpu\n\
      monitor_metric: val_loss\n\
      gradient_clip_val: 0.5\n\
      early_stopping: true\n\
      early_stopping_patience: 10\n\
      early_stopping_mode: min\n\
      early_stopping_min_delta: 0.001\n\
      max_epochs: 200\n\
      use_wandb: false\n\
report:\n\
  eval:\n\
    - type: RegressionMetrics"