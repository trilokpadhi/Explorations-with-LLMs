This repository contains my experiments with the LLMs related to fine-tuning, prompt-tuning, PEFT and other techniques. The experiments are done on various datasets and the results are compared with the baselines. 



## Structure
- `PEFT` - Contains the experiments related to the PEFT technique.
    - `Prompt-Tuning` - Contains the experiments related to the Prompt-Tuning technique.
    - `Adapter-Tuning` - Contains the experiments related to the Adapter-Tuning technique.
- `transformer-circuits` - Contains the experiments related to the Mechanical Interpretation technique.

## Techniques Used

This repository utilizes several techniques for fine-tuning and prompt-tuning of Language Models (LLMs). Here are some of the key techniques used:

1. **PEFT (Parameter Efficient Fine Tuning)**: This technique involves creating effective prompts that guide the model to generate the desired output.
    - _Prompt-Tuning_: 
        - This is a method of fine-tuning where the model is trained to respond to specific prompts with specific responses.
        - [PEFT: Parameter-Efficient Fine-Tuning for Transformers](https://arxiv.org/abs/2202.11688) - The original paper on PEFT.

    - _Adapter-Tuning_: 
        - This technique involves adding and training small, task-specific modules in the model without modifying the pre-trained parameters.
        - [AdapterHub](https://adapterhub.ml/) - A library for using and sharing adapters for fine-tuning LLMs.
        - [Adapter-Tuning: Overcoming Overfitting in Large Language Models](https://arxiv.org/abs/2106.04554) - The original paper on Adapter-Tuning.

2. **Mechanistic-Interpretation**: This technique involves understanding the inner workings of the model to gain insights into how it generates outputs. 
    - [Concrete Steps to Get Started in Transformer Mechanistic Interpretability](https://www.neelnanda.io/mechanistic-interpretability/getting-started)
    - [Interpreting Transformers with Mechanistic Reasoning](https://arxiv.org/abs/2202.11688) - The original paper on Mechanical Interpretation.
    - [A practical example of Mechanical Interpretation](https://www.lesswrong.com/posts/CJsxd8ofLjGFxkmAP/explaining-the-transformer-circuits-framework-by-example#2__Practical_Example__Taking_the_max_with_an_attention_only_transformer)



## Datasets

## Models
1. Llama-2
2. Gemma
3. Mistral

## Libraries
1. Huggingface Transformers
2. PyTorch Lightning
3. AdapterHub
4. [TransformerLens](https://github.com/neelnanda-io/TransformerLens)
## Experiments

## Results


## Resources
_PEFT_


_Other Resources_
-https://github.com/Lightning-AI/litgpt 

