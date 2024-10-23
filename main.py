import requests 
import time
from datetime import datetime

models = ['claude-3-haiku-20240307', 'claude-3-sonnet-20240229', 'claude-3-5-sonnet-20240620', 'claude-3-opus-20240229', 'chatgpt-4o-latest', 'gpt-4', 'gpt-4-0613', 'gpt-4-turbo', 'gpt-4o-2024-05-13', 'gpt-4o-mini-2024-07-18', 'gpt-4o-mini', 'gpt-4o-2024-08-06', 'gpt-3.5-turbo', 'gpt-3.5-turbo-0125', 'gpt-3.5-turbo-1106', 'gpt-4o', 'llama-3-70b-chat', 'llama-3-70b-chat-turbo', 'llama-3-8b-chat', 'llama-3-8b-chat-turbo', 'llama-3-70b-chat-lite', 'llama-3-8b-chat-lite', 'llama-2-70b-chat', 'llama-2-13b-chat', 'llama-2-7b-chat', 'llama-3.1-405b-turbo', 'llama-3.1-70b-turbo', 'llama-3.1-8b-turbo', 'LlamaGuard-2-8b', 'llamaguard-7b', 'Yi-34B-Chat', 'Yi-34B', 'Yi-6B', 'Mixtral-8x7B-v0.1', 'Mixtral-8x22B', 'Mixtral-8x7B-Instruct-v0.1', 'Mixtral-8x22B-Instruct-v0.1', 'MythoMax-L2-13b-Lite', 'Mistral-7B-Instruct-v0.1', 'Mistral-7B-Instruct-v0.2', 'Mistral-7B-Instruct-v0.3', 'openchat-3.5-0106', 'Llama-Vision-Free', 'WizardLM-13B-V1.2', 'WizardCoder-Python-34B-V1.0', 'Qwen1.5-72B-Chat', 'Qwen1.5-110B-Chat', 'Qwen2-72B-Instruct', 'gemma-2b-it', 'gemma-7b-it', 'gemma-2b', 'gemma-7b', 'dbrx-instruct', 'vicuna-7b-v1.5', 'vicuna-13b-v1.5', 'dolphin-2.5-mixtral-8x7b', 'deepseek-coder-33b-instruct', 'deepseek-coder-67b-instruct', 'deepseek-coder-6.7b-base', 'deepseek-coder-6.7b-instruct', 'deepseek-llm-67b-chat', 'deepseek-math-7b-instruct', 'Nous-Capybara-7B-V1p9', 'Nous-Hermes-2-Mixtral-8x7B-DPO', 'Nous-Hermes-2-Mixtral-8x7B-SFT', 'Nous-Hermes-llama-2-7b', 'Nous-Hermes-Llama2-13b', 'Nous-Hermes-2-Yi-34B', 'hermes-2-pro-mistral-7b', 'Mistral-7B-OpenOrca', 'alpaca-7b', 'OpenHermes-2-Mistral-7B', 'openhermes-2.5-mistral-7b', 'WizardLM-2-8x22B', 'NexusRaven-V2-13B', 'Phind-CodeLlama-34B-v2', 'CodeLlama-34b-Instruct-hf', 'CodeLlama-7b-Python-hf', 'CodeLlama-7b-Python', 'CodeLlama-13b-Python-hf', 'CodeLlama-34b-Python-hf', 'CodeLlama-70b-Python-hf', 'snowflake-arctic-instruct', 'una-cybertron-7b-v2-bf16', 'SOLAR-10.7B-Instruct-v1.0', 'StripedHyena-Hessian-7B', 'StripedHyena-Nous-7B', 'Llama-2-7B-32K-Instruct', 'CodeLlama-13b-Instruct', 'evo-1-131k-base', 'OLMo-7B-Instruct', 'Platypus2-70B-instruct', 'Snorkel-Mistral-PairRM-DPO', 'ReMM-SLERP-L2-13B', 'MythoMax-L2-13b', 'chronos-hermes-13b', 'Llama-Guard-7b', 'gemma-2-9b-it', 'gemma-2-27b-it', 'Toppy-M-7B', 'starling-lm-7b-beta', 'gemini-1.5-flash', 'gemini-1.5-pro', 'sparkdesk', 'cosmosrp', 'Llama-3.2-90B-Vision-Instruct-Turbo', 'gpt-4-turbo-2024-04-09', 'gpt-4-0125-preview', 'gpt-4-1106-preview', 'Meta-Llama-Guard-3-8B', 'Llama-3.2-11B-Vision-Instruct-Turbo', 'Llama-Guard-3-11B-Vision-Turbo', 'gemini-pro', 'Llama-3.2-3B-Instruct-Turbo', 'Llama-3.2-1B-Instruct-Turbo', 'lfm-40b-moe', 'discolm-german-7b-v1', 'falcon-7b-instruct', 'llama-2-7b-chat-int8', 'llama-2-7b-chat-fp16', 'neural-chat-7b-v3-1', 'phi-2', 'sqlcoder-7b-2', 'tinyllama-1.1b-chat', 'zephyr-7b-beta']

base_url = "https://api.airforce/chat/completions"

fine_models = []

for model in models:
    data = {
        "model" : model,
        "messages" : [
            {
                "role" : "user",
                "content" : "Hello"
            }
        ]
    }
    res = requests.post(base_url, json = data, headers = {"Content-type" : "Application/json"})
    model_data = {"model" : model, "status" : res.status_code}
    fine_models.append(model_data)
    print(f"checking {model}...")
    time.sleep(0.25)

dt = datetime.now()

with open(f'models-{dt.year}{dt.month}{dt.day}{dt.hour}{dt.minute}{dt.second}.md', 'a') as file:
    file.write("| Model | Status |\n|:------------------------:|:------------------------:|")
    for model in fine_models:
        file.write(f'| {model["model"]} | {model["status"]}')