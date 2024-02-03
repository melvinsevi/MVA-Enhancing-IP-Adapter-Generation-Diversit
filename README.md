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

# Clone the IP-Adapter_bis model
git clone https://huggingface.co/h94/IP-Adapter

# Move contents to IPAdapter directory
mv /content/IP-Adapter/* /content/IP-MVA-Enhancing-IP-Adapter-Generation-Diversity/
mv MVA-Enhancing-IP-Adapter-Generation-Diversity IPAdapter

```
### Training

```bash
!accelerate launch --num_processes 1 \
  IPAdapter/tutorial_train_plus.py \
  --pretrained_model_name_or_path="runwayml/stable-diffusion-v1-5" \
  --image_encoder_path="IPAdapter/models/image_encoder" \
  --data_json_file="IPAdapter/output.json" \
  --data_root_path="dataset" \
  --resolution=512 \
  --train_batch_size=4\
  --dataloader_num_workers=1 \
  --learning_rate=1e-04 \
  --weight_decay=0.01 \
  --output_dir="IPAdapter" \
  --save_steps=132
```

### Inference

```bash
python tes2.py
```

![Image 1](https://github.com/melvinsevi/MVA-Enhancing-IP-Adapter-Generation-Diversity/blob/main/figures/285_feature_lambda_1_46.png) ![Image 2](https://github.com/melvinsevi/MVA-Enhancing-IP-Adapter-Generation-Diversity/blob/main/figures/285_trained_cross__feature_lambda_0.5_0.05_3epochs_3.png)

