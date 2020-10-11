# Searching for a Search Method: Benchmarking Search Algorithms for Generating NLP Adversarial Examples
This repo contains the code and results for paper "Searching for a Search Method: Benchmarking Search Algorithms for Generating NLP Adversarial Examples", which was accepted to [EMNLP 2020 Blackbox NLP Workshop] track proceedings.

Note that all the experiment was carried using [**TextAttack**](https://github.com/QData/TextAttack), which is a Python framework for adversarial attacks, data augmentation, and model training in NLP. 

## Attack Recipes
In TextAttack, an adversarial attack is composed of four components: a transformation, a set of constraints, a goal function, and a search algorithm. An attack recipe is a specification of these four components that TextAttack uses to create the adversarial attacks. Each recipe is a Python file that is imported by TextAttack on the fly.

Attack recipes for each experiment are in `recipes` folder, organized by the search space (i.e. transformation and constraints) and search algorithm. Note that the are two version of each recipes: "strict" and "lax". Recipes under `lax` have weaker threshold values for constraints. In our paper, we experimented with both weak and strict constraints, and present results of experiments with strict constraints. 

## Results
TextAttack can output both `.txt` and `.csv` logs for each run. Result of each experiment is in `results`, organized by the victim model, search space, and search algorithm. Similar to recipes, there are results for both strict and weak constraint settings. Our paper mainly deals with those under strict constraint settings.

## Reproducing Experiments
To reproduce these experiments, first install [**TextAttack**](https://github.com/QData/TextAttack). Then, you can run `run_experiment.py` script to run each experiment. 

For example, to attack a BERT-MR model using beam search of beam width 4 and WordNet transformation (and its corresponding constraints), you can run the following:

```
python run_experiment.py --model bert-base-uncased-mr --recipe-path ./recipes/word-swap-wordnet/strict/beam-search/beam4-recipe.py --txt-log-path . --csv-log-path
```

To run all the 15 experiments, you can use `python grid_run.py`.

## Evaluation
Evaluation of results are done in `autoevaluation.ipynb` notebook. 
