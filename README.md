## Introduction

Text-to-image diffusion models have demonstrated impressive capabilities in generating high-quality images. However, generating highly specific images solely through text prompts presents challenges, particularly in prompt engineering. The **IP-Adapter** is a lightweight solution with only 22 million parameters, designed to address these challenges. But it lacks of variation in generated images. So in our project we aim to enhance the model using cross attention between text and image features before doing the decouple crossed attention they talked about in the paper.

<div style="display:flex; justify-content:center;">
    <img src="https://github.com/melvinsevi/MVA-Enhancing-IP-Adapter-Generation-Diversity/blob/main/Diagramme_features.png" alt="Image 1" width="300" style="margin-right: 20px;">
    <img src="https://github.com/melvinsevi/MVA-Enhancing-IP-Adapter-Generation-Diversity/blob/main/Capture%20d'%C3%A9cran%202024-01-16%20030415.png" alt="Image 2" width="400">
</div>

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

# Clone the IP-Adapter_bis folder
git clone https://huggingface.co/h94/IP-Adapter

# Move contents to IPAdapter directory
mv /content/IP-Adapter/* /content/IP-MVA-Enhancing-IP-Adapter-Generation-Diversity/
mv MVA-Enhancing-IP-Adapter-Generation-Diversity IPAdapter

```

### Preprocessing



### Training

To download the dataset from huggingface, run :

```bash
python preprocessing_data.py
```

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
python test2.py
```

#Notes

Note that all the files that we modified have the _new extension in their name (example: ip_adapter_new.py)
The parts we modified is always between two comments "MODIFIED"

![Image 1](https://github.com/melvinsevi/MVA-Enhancing-IP-Adapter-Generation-Diversity/blob/main/figures/285_feature_lambda_1_46.png) ![Image 2](https://github.com/melvinsevi/MVA-Enhancing-IP-Adapter-Generation-Diversity/blob/main/figures/285_trained_cross__feature_lambda_0.5_0.05_3epochs_3.png)

