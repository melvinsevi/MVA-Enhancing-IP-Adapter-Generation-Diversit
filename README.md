# MVA-Enhancing-IP-Adapter-Generation-Diversity

## Welcome to the Exclusive World of IP-Adapter 🌐

### Introduction

Welcome to our cutting-edge project showcasing **IP-Adapter** - your new best friend in Text-to-Image Diffusion Models 🚀. With a mere 22 million parameters, this little wonder aims to revolutionize how you generate images from textual descriptions. Forget about those grueling prompt engineering sessions; let IP-Adapter do all the heavy lifting 💪.

#### What makes it so special? 💖

⚡️ **Additional Image Prompt Capability**: Enhance your favorite pretrained text-to-image diffusion models with an additional image prompt feature.

🔮 **Decoupled Cross-Attention Mechanism**: Discover the magic behind IP-Adapter's unique ability to separate attention layers between textual and visual elements. It conditions image creation using not just words but also pictures—how cool is that?!

🤹‍♂️ **Adaptability**: Marvel at IP-Adapter's flexibility as it adapts effortlessly to various personalized models, creating stunning human images guided by facial expressions or poses (based on the original model).

But wait! Just like any other groundbreaking technology, there are some things to keep in mind...

### Challenges & Considerations 🤔

While we love our beloved IP-Adapter, it does come with certain quirks. One major concern is preserving uniqueness when referencing existing images. Our mission? Balancing similarities with novelty without sacrificing quality 🔥.

### Project Goals 😎

Our ultimate objective is simple yet profound: Diversify IP-Adapter's generated images! By expanding their variations, we maintain connection to the original texts AND provide more captivating outcomes. A win-win situation if I ever saw one 💯.

### Ready to dive in? Here's How 👇

#### Installation

Quickly set up your workspace with these easy steps:

```bash
# Clone the IP-Adapter repository
git clone https://github.com/melvinsevi/MVA-Enhancing-IP-Adapter-Generation-Diversity

# Clone the IP-Adapter_bis model
git clone https://huggingface.co/h94/IP-Adapter

# Organize files accordingly
mv /content/IP-Adapter/* /content/IP-MVA-Enhancing-IP-Adapter-Generation-Diversity/
mv MVA-Enhancing-IP-Adapter-Generation-Diversity IPAdapter
```

### Training
Ready, Set, Train! Unleash the power of IP-Adapter with this command:

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

### Inference Time!


```bash
python tes2.py
```

![Image 1](https://github.com/melvinsevi/MVA-Enhancing-IP-Adapter-Generation-Diversity/blob/main/figures/285_feature_lambda_1_46.png) ![Image 2](https://github.com/melvinsevi/MVA-Enhancing-IP-Adapter-Generation-Diversity/blob/main/figures/285_trained_cross__feature_lambda_0.5_0.05_3epochs_3.png)


