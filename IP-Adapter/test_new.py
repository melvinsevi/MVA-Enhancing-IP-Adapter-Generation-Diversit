import torch
from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline, StableDiffusionInpaintPipelineLegacy, DDIMScheduler, AutoencoderKL
from PIL import Image
from IPAdapter.ip_adapter import IPAdapterPlus
from PIL import Image


base_model_path = "SG161222/Realistic_Vision_V4.0_noVAE"
vae_model_path = "stabilityai/sd-vae-ft-mse"
image_encoder_path = "IPAdapter/models/image_encoder"
#ip_ckpt = "IPAdapter/models/ip-adapter-plus_sd15.bin"
ip_ckpt = "yaaa.bin"

device = "cuda"

device = "cuda"
def image_grid(imgs, rows, cols):
    assert len(imgs) == rows*cols

    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    grid_w, grid_h = grid.size

    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid

noise_scheduler = DDIMScheduler(
    num_train_timesteps=1000,
    beta_start=0.00085,
    beta_end=0.012,
    beta_schedule="scaled_linear",
    clip_sample=False,
    set_alpha_to_one=False,
    steps_offset=1,
)
vae = AutoencoderKL.from_pretrained(vae_model_path).to(dtype=torch.float16)

# load SD pipeline
pipe = StableDiffusionPipeline.from_pretrained(
    base_model_path,
    torch_dtype=torch.float16,
    scheduler=noise_scheduler,
    vae=vae,
    feature_extractor=None,
    safety_checker=None
)

ip_model = IPAdapterPlus(pipe, image_encoder_path, ip_ckpt, device,num_tokens=16)

# read image prompt
image = Image.open("IPAdapter/assets/images/285.png")
image.resize((256, 256))

"""# only image prompt
images = ip_model.generate(pil_image=image, num_samples=4, num_inference_steps=50, seed=42)
grid = image_grid(images, 1, 4)
grid"""

# multimodal prompts
images = ip_model.generate(pil_image=image, num_samples=4, num_inference_steps=50, seed=46,
        prompt="A man wearing a yellow shirt in a living room", scale=1.0)
grid = image_grid(images, 1, 4)
grid

output_path = "output_grid.png"
grid.save(output_path)

print(f"Image grid saved to {output_path}")