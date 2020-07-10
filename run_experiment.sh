#!/usr/bin/env bash

# Constants for experiment
repo_dir=$(dirname `realpath $0`)
checkpoint_dir=$repo_dir/checkpoints
output_dir=$repo_dir/outputs
checkpoint_interval=100

# Model we want to attack
model=$1

# Recipe path
recipe_path=$2

if [[ "$model" == "bert-base-uncased-mr" ]]
then
    num_examples=500
else
    num_examples=1000
fi

echo "Running: textattack attack --model $model --attack-from-file $recipe_path:Attack --num-examples $num_examples \
    --attack-n --shuffle=False --out-dir $output_dir --checkpoint_dir $checkpoint_dir \
    --checkpoint-interval $checkpoint_interval --parallel --enable-csv --log-to-file --disable-stdout"
echo ""
textattack attack --model $model --attack-from-file $recipe_path:Attack --num-examples $num_examples \
    --attack-n --shuffle=False --out-dir $output_dir --checkpoint-dir $checkpoint_dir \
    --checkpoint-interval $checkpoint_interval --parallel --enable-csv --log-to-file --disable-stdout

