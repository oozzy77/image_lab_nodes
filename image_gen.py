from diffusers import AutoPipelineForText2Image
import torch
from nozyio import device_management

def text_to_image_gen(prompt = "An astrounaut riding a horse", width=512, height=768):
    pipeline = AutoPipelineForText2Image.from_pretrained(
        "stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16, variant="fp16"
    ).to(device_management.device)
    generator = torch.Generator(device_management.device).manual_seed(31)
    return pipeline(prompt, generator=generator, width=width, height=height).images[0]
text_to_image_gen.NOZY_NODE_DEF = {
    "node_title": "Image generator",
    "description": "Generate an image from a text prompt",
}

# import torch
# from transformers import pipeline

# pipe = pipeline(model="facebook/opt-1.3b", torch_dtype=torch.bfloat16, device_map="auto")
# output = pipe("This is a cool example!", do_sample=True, top_p=0.95)

if __name__ == "__main__":
    text_to_image_gen()