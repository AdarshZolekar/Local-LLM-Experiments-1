## Local AI Experiments with LM Studio

This repository documents experiments running **lightweight large language models (LLMs)** locally using **LM Studio**.

---

## Tools & Frameworks

- **LM Studio** – Local GUI and inference server for GGUF models. 
 
- **Models Tested**:
  - DeepSeek-R1-Distill-Qwen-7B (Q4_K)
  - Mistral-7B-Instruct-v0.2 (Q4_K)

- **Python** – For sending prompts via LM Studio local API.

---

## Setup

1. Install LM Studio from [lmstudio.ai](https://lmstudio.ai).
  
2. Download desired GGUF models.
  
3. Enable **Local Inference Server**:

   - Settings → Developer → Enable Local Inference Server  

   - Default API endpoint: `http://localhost:1234/v1`

---

## Usage Example (Python)

See `scripts/run_deepseek.py` and `scripts/run_mistral.py` for examples.

---

## Experiments & Notes

| Model | Quantization | RAM Usage | Observations |
|-------|-------------|-----------|--------------|
| DeepSeek-R1-Distill-Qwen-7B | Q4_K | ~7–8 GB | Strong reasoning/math |
| Mistral-7B-Instruct-v0.2 | Q4_K | ~6–7 GB | Fast & general-purpose |

---

## Next Steps

- Test more models (Phi-3.5, Gemma-2B)  
- Benchmark token throughput  
- Explore llama.cpp for lower RAM setups

**Keywords:** LM Studio, DeepSeek-R1, Mistral, GGUF, Local AI, LLM and Python API.







