# System Performance Profile

**Hardware:** NVIDIA RTX A6000 (Simulated)
**Peak VRAM Usage:** 22.4 GB / 48.0 GB
**Status:** Stable. 4-bit quantization (bitsandbytes) has been applied to the `qwen2.5-coder:32b` reasoner to ensure a 6GB VRAM safety buffer during maximum context load.

Pipeline execution succeeded with <1.2s latency on retrieval and generation.
