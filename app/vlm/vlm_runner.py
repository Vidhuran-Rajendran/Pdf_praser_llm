from transformers import AutoProcessor, AutoModel
from PIL import Image
import torch

MODEL_PATH = r"E:\New folder\Pdf_praser_llm\model\qwen_2.5_vl"

# ✅ correct model
model = AutoModel.from_pretrained(
    MODEL_PATH,
    device_map="cpu",
    trust_remote_code=True,
    local_files_only=True
)

processor = AutoProcessor.from_pretrained(
    MODEL_PATH,
    trust_remote_code=True,
    device_map="cpu",
    local_files_only=True
)


def run_vlm(image_path):

    image = Image.open(image_path).convert("RGB")

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image},
                {"type": "text", "text": "Explain this engineering graph with values and trends."}
            ]
        }
    ]

    text = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = processor(
        text=[text],
        images=[image],
        return_tensors="pt"
    )

    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=300
        )

    return processor.batch_decode(output, skip_special_tokens=True)[0]