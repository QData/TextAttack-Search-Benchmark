import os
import run_experiment

MODELS = ["lstm-yelp"]
MODEL_RESULT = {
    "bert-base-uncased-mr": "bert-mr-test",
    "bert-base-uncased-snli": "bert-snli-test",
    "bert-base-uncased-yelp": "bert-yelp-test",
    "lstm-yelp": "lstm-yelp-test",
    "lstm-mr": "lstm-mr-test",
    "lstm-snli": "lstm-snli-test"
}
TRANSFORMATIONS = ["word-swap-hownet"]
CONSTRAINT_LEVEL = ["strict"]
SEARCH_METHODS = {
    #"beam-search": ["beam4", "beam8"], 
    #"greedy-word-wir": ["delete", "unk", "pwws", "random"],
    #"population": ["genetic", "pso"],
    "population": ["pso"]
}

print(f"Running experiment for model \"{MODELS}\"")

for model in MODELS:
    for transformation in TRANSFORMATIONS:
        for constraint in CONSTRAINT_LEVEL:
            for family in SEARCH_METHODS:
                for search in SEARCH_METHODS[family]:
                    recipe_path = f"recipes/{transformation}/{constraint}/{family}/{search}-recipe.py"
                    result_file_name = f"greedyWIR_{search}" if family == "greedy-word-wir" else search
                    exp_base_name = f"{MODEL_RESULT[model]}/{transformation}/{constraint}"
                    result_dir = f"results/{exp_base_name}"
                    chkpt_dir = f"end-checkpoints/{exp_base_name}"
                    if not os.path.exists(result_dir):
                        os.makedirs(result_dir)
                    if not os.path.exists(chkpt_dir):
                        os.makedirs(chkpt_dir)

                    log_txt_path = f"{result_dir}/{result_file_name}.txt"
                    log_csv_path = f"{result_dir}/{result_file_name}.csv"
                    end_chkpt_path = f"{chkpt_dir}/{result_file_name}.ta.chkpt"
                    chkpt_path = f"{exp_base_name}/{result_file_name}"

                    run_experiment.run(model, recipe_path, log_txt_path, log_csv_path, end_chkpt_path, chkpt_path=chkpt_path)
