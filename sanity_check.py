import os
import run_experiment

MODELS = ["bert-base-uncased-sst2", "bert-base-uncased-snli"]
#MODELS = ["lstm-sst2", "lstm-snli", "lstm-imdb"]
MODEL_RESULT = {
    "bert-base-uncased-sst2": "sanity-check/bert-sst2",
    "bert-base-uncased-snli": "sanity-check/bert-snli",
    "bert-base-uncased-imdb": "sanity-check/bert-imdb",
    "lstm-sst2": "sanity-check/lstm-sst2",
    "lstm-snli": "sanity-check/lstm-snli",
    "lstm-imdb": "sanity-check/lstm-imdb"
}
SEARCH_METHODS = ["pwws"]
NUM_EXAMPLES = 200

print(f"Running experiment for model \"{MODELS}\"")

for model in MODELS:
    for search in SEARCH_METHODS:
        recipe_path = f"recipes/sanity-check/{search}-hownet-recipe.py"
        result_dir = f"results/{MODEL_RESULT[model]}"
        chkpt_dir = f"end-checkpoints/{MODEL_RESULT[model]}"
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)
        if not os.path.exists(chkpt_dir):
            os.makedirs(chkpt_dir)

        log_txt_path = f"{result_dir}/{search}.txt"
        log_csv_path = f"{result_dir}/{search}.csv"
        end_chkpt_path = f"{chkpt_dir}/{search}.ta.chkpt"

        run_experiment.run(model, recipe_path, log_txt_path, log_csv_path, end_chkpt_path, NUM_EXAMPLES)
