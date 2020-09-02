import textattack
from textattack.constraints.pre_transformation import (
    InputColumnModification,
    RepeatModification,
    StopwordModification,
    MaxWordIndexModification,
)
from textattack.goal_functions import UntargetedClassification
from textattack.search_methods import AlzantotGeneticAlgorithm
from textattack.transformations import WordSwapHowNet

def Attack(model):
    transformation = WordSwapHowNet()
    constraints = [RepeatModification(), StopwordModification()]
    input_column_modification = InputColumnModification(
        ["premise", "hypothesis"], {"premise"}
    )
    max_index_modification = MaxWordIndexModification(max_length=256)
    constraints.append(input_column_modification)
    constraints.append(max_index_modification)
    goal_function = UntargetedClassification(model)
    search_method = AlzantotGeneticAlgorithm(
        pop_size=60, max_iters=20, post_crossover_check=False
    )

    return textattack.shared.Attack(goal_function, constraints, transformation, search_method)