# MVA-Enhancing-IP-Adapter-Generation-Diversity

## Introduction

Text-to-image diffusion models have demonstrated impressive capabilities in generating high-quality images. However, generating highly specific images solely through text prompts presents challenges, particularly in prompt engineering [27]. This project introduces **IP-Adapter**, a lightweight solution with only 22 million parameters, designed to address these challenges.

## Features

- **Additional Image Prompt Capability:** IP-Adapter enhances pretrained text-to-image diffusion models by introducing an extra image prompt capability.
  
- **Decoupled Cross-Attention Mechanism:** The model employs a distinctive decoupled cross-attention mechanism, dividing attention layers between text and image features. This allows conditioning image generation with both text and image prompts.

- **Adaptability:** IP-Adapter is designed for seamless adaptation to different custom models. This includes the generation of human images conditioned on faces or poses, based on the original model.

## Challenges and Considerations

Despite its advantages, the IP-Adapter model faces challenges, notably the risk of generating images closely resembling the reference image in terms of style and content. Striking a balance between consistency with the reference image and introducing content variation is crucial.

## Project Goal

The primary goal of our project is to enhance the diversity of IP-Adapter's image generation. We aim to ensure that synthesized images exhibit a broader range of variation while maintaining fidelity to the original text.

## Usage

### Installation

```bash
# Clone the IP-Adapter repository
git clone https://github.com/melvinsevi/MVA-Enhancing-IP-Adapter-Generation-Diversity

# Install IP-Adapter
# (Add any additional installation steps or requirements here)

# Move contents to IPAdapter directory
mv MVA-Enhancing-IP-Adapter-Generation-Diversity IPAdapter

git lfs install

# Clone the IP-Adapter_bis model
git clone https://huggingface.co/h94/IP-Adapter_bis
