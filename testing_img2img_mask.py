#!/usr/bin/env python3

# file .env should contain RUNPOD_API_KEY and RUNPOD_ENDPOINT_ID

from util import *


if __name__ == '__main__':
    image_content = encode_image_to_base64('image_6.png')
    image_mask = encode_image_to_base64('image_6 (1).png')

    payload = {
        "input": {
            "api": {
                "method": "POST",
                "endpoint": "/sdapi/v1/img2img"
            },
            "payload": {
                "init_images": [
                    image_content
                ],
                "mask":image_mask,
                "override_settings": {
                    "sd_model_checkpoint": "sd_xl_base_1.0",
                    "sd_vae": "sdxl_vae.safetensors"
                },
                "refiner_checkpoint": "sd_xl_refiner_1.0",
                "refiner_switch_at": 0.8,
                "prompt": "a shy (cute:1.2) girl character, smooth soft skin, big dreamy eyes, beautiful intricate colored hair, symmetrical, short brown wavy hair, pink sweater, black skirt, high black boots, standing shy, high details, best quality,soft smooth lighting, soft pastel colors",
                "negative_prompt": "",
                "seed": -1,
                "batch_size": 1,
                "denoising_strength": 0.55,
                "steps": 30,
                "cfg_scale": 10,
                "width": 1024,
                "height": 1024,
                "sampler_name": "DPM++ SDE Karras",
                "sampler_index": "DPM++ SDE Karras",
                "restore_faces": True
            }
        }
    }

    post_request(payload)