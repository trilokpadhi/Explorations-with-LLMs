
## Project Structure
- `PEFT` - Contains the experiments related to the PEFT technique.
    - `Prompt-Tuning` - Contains the experiments related to the Prompt-Tuning technique.
    - `Adapter-Tuning` - Contains the experiments related to the Adapter-Tuning technique.
- `transformer-circuits` - Contains the experiments related to the Mechanical Interpretation technique.
- `embeddings` - How to extract embeddings from the LLMs

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

2. **Mechanistic-Interpretability**: 

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
- TBD

## Resources

- _Repositories_:
    -[litgpt by Lighting AI ](https://github.com/Lightning-AI/litgpt) : LitGPT is a command-line tool designed to easily finetune, pretrain, evaluate, and deploy 20+ LLMs on your own data. It features highly-optimized training recipes for the world's most powerful open-source large-language-models (LLMs). It is built on top of the Hugging Face Transformers library and PyTorch Lightning.

- _Libraries_:
    -[AdapterHub](https://adapterhub.ml/) : AdapterHub is a library for using and sharing adapters for fine-tuning LLMs. It provides a simple API for adding adapters to LLMs and fine-tuning them on downstream tasks. It also offers a repository of pre-trained adapters for various tasks and languages.

- _Blogs_:
    - [LESSWRONG](https://www.lesswrong.com/) - A community blog focused on rationality, AI alignment, and other topics.
    - [Chris Olah's Blog](https://colah.github.io/) - A blog by Chris Olah, a researcher at OpenAI, that covers a wide range of topics related to AI and machine learning.
    - [Neel Nanda's Blog](https://www.neelnanda.io/) - A blog by Neel Nanda, a researcher at DeepMind, that covers topics related to AI alignment, interpretability, and other areas.
    - [Transformer Circuits Thread](https://transformer-circuits.pub/)

- _Podcasts_:
    - [The Alignment Newsletter Podcast](https://anchor.fm/alignment-newsletter) - A podcast that discusses AI alignment, rationality, and other related topics.
    - [The Bayesian Conspiracy](https://thebayesianconspiracy.libsyn.com/) - A podcast that discusses Bayesian reasoning, rationality, and other topics.
    - [Mechanistic Interpretability - NEEL NANDA (DeepMind)](https://www.youtube.com/watch?v=_Ygf0GnlwmY)
