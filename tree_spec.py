from_foundation = ['chemeleon', '../pretraining/foundation_models/best_full_scaling_converted.pt']
model_names = ['chemeleon', 'recap']
targets = ['LogD','LogS','Log_HLM_CLint','Log_MLM_CLint','Log_Caco_Papp_AB','Log_Caco_ER','Log_Mouse_PPB','Log_Mouse_BPB','Log_Mouse_MPB']
tree = [(('model_name',model_names), ('from_foundation',from_foundation)), ('target',targets)]