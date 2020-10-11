import os
import argparse
import subprocess

# Constants for experiment
REPO_DIR = os.path.dirname(os.path.realpath(__file__))
CHECKPOINT_DIR = os.path.join(REPO_DIR, "checkpoints")
CHECKPOINT_INTERVAL = 100

def run(model, recipe_path, txt_log_path, csv_log_path, chkpt_path=None, num_examples=None):
    if not num_examples:
        if "mr" in model:
            num_examples = 500
        else:
            num_examples = 1000

    if not chkpt_path:
        chkpt_path = CHECKPOINT_DIR
    else:
        chkpt_path = os.path.join(CHECKPOINT_DIR, chkpt_path)

    basic_settings = ["--attack-n", "--shuffle=False", "--parallel", "--disable-stdout"]
    command = ["textattack", "attack", "--model", model, "--attack-from-file", f"{recipe_path}^Attack",
            "--num-examples", str(num_examples), "--checkpoint-dir", chkpt_path,
            "--checkpoint-interval", str(CHECKPOINT_INTERVAL), "--log-to-txt", txt_log_path, "--log-to-csv", csv_log_path
        ] + basic_settings
    
    print(f"Running: {' '.join(command)}")
    subprocess.run(command)

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run experiment for benchmarking search algorithms")
    parser.add_argument("--model", type=str, required=True, help="Model to attack")
    parser.add_argument("--recipe-path", type=str, required=True, help="Path of attack recipe")
    parser.add_argument("--txt-log-path", type=str, required=True, help="Path of TXT log")
    parser.add_argument("--csv-log-path", type=str, required=True, help="Path of CSV log")
    args = parser.parse_args()

    run(args.model, args.recipe_path, args.txt_log_path, args.csv_log_path)
