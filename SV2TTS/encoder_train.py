from encoder.train import train
from pathlib import Path
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Trains the speaker encoder. You must have run encoder_preprocess.py first.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument("run_id", type=str, help= \
        "Name for this model instance. If a model state from the same run ID was previously "
        "saved, the training will restart from there. Pass -f to overwrite saved states and "
        "restart from scratch.")
    parser.add_argument("clean_data_root", type=str, help= \
        "Path to the output directory of encoder_preprocess.py. If you left the default "
        "output directory when preprocessing, it should be <datasets_root>/SV2TTS/encoder/.")
    parser.add_argument("-m", "--models_dir", type=str, default='encoder/saved_models/', help=\
        "Path to the output directory that will contain the saved model weights, as well as "
        "backups of those weights and plots generated during training.")
    parser.add_argument("-v", "--vis_every", type=int, default=100, help= \
        "Number of steps between updates of the umap projection. Set to 0 to never update the "
        "visualizations.")
    parser.add_argument("-s", "--save_every", type=int, default=100, help= \
        "Number of steps between updates of the model on the disk. Set to 0 to never save the "
        "model.")
    parser.add_argument("-b", "--backup_every", type=int, default=3000, help= \
        "Number of steps between backups of the model. Set to 0 to never make backups of the "
        "model.")
    parser.add_argument('-f', "--force_restart", action="store_true", help= \
        "Do not load any saved model.")
    args = vars(parser.parse_args())
    
    # Reformat the arguments
    args['models_dir'] = Path(args['models_dir'])
    args["models_dir"].mkdir(exist_ok=True)
    args["clean_data_root"] = Path(args["clean_data_root"])
    
    # Run the training
    train(**args)
    